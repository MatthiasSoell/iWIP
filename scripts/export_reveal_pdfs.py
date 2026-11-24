#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import fnmatch
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from html.parser import HTMLParser
from http.client import HTTPException
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urljoin, urlsplit
from urllib.request import urlopen

from check_navigation import built_target, read_navigation

FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
ROOT_FIELD_RE = re.compile(r"^([A-Za-z0-9_]+):[ \t]*(.*)$", re.MULTILINE)
GLOBAL_RENDER_REBUILD_PATTERNS = (
    ".github/workflows/hugo.yml",
    "config.toml",
    "go.mod",
    "go.sum",
    "layouts/**",
    "scripts/export_reveal_pdfs.py",
    "static/css/custom_reveal.css",
)


@dataclass(frozen=True)
class ExportSpec:
    source_path: Path
    reveal_url: str
    pdf_output: Path
    published_rel_dir: Path

    @property
    def published_pdf_rel_path(self) -> Path:
        return self.published_rel_dir / self.pdf_output.name


class MediaReferences(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.urls: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if not value:
                continue
            if name in {"src", "data-src", "poster"}:
                self.urls.add(value)
            elif name in {"srcset", "data-srcset", "data-background",
                          "data-background-image", "data-background-video"}:
                self.urls.update(candidate.split()[0] for candidate in value.split(",")
                                 if candidate.strip())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export all Reveal presentations with pdf_export: true to PDF."
    )
    parser.add_argument(
        "--repo-root",
        default=Path(__file__).resolve().parents[1],
        type=Path,
        help="Repository root containing content/ and public/.",
    )
    parser.add_argument(
        "--only",
        type=Path,
        help="Export only this repository-relative Reveal _index.md.",
    )
    parser.add_argument(
        "--public-root",
        type=Path,
        help="Temporary Hugo output directory for --only.",
    )
    parser.add_argument(
        "--served-base-url",
        default="http://127.0.0.1:8080/iWIP",
        help="Base URL of the locally served Hugo site.",
    )
    parser.add_argument(
        "--pause-ms",
        default=2000,
        type=int,
        help="DeckTape pause in milliseconds.",
    )
    parser.add_argument(
        "--readiness-retries",
        default=10,
        type=int,
        help="Number of readiness checks before failing a Reveal URL.",
    )
    parser.add_argument(
        "--readiness-delay",
        default=1.0,
        type=float,
        help="Delay in seconds between readiness checks.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the planned exports without calling DeckTape.",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="With --only, validate the built download link and print its build-relative PDF path.",
    )
    parser.add_argument(
        "--changed-paths-file",
        type=Path,
        help="Optional file containing repo-relative changed paths, NUL- or newline-separated.",
    )
    parser.add_argument(
        "--published-base-url",
        help="Published site base URL used to restore previously generated PDFs for selective rebuilds.",
    )
    parser.add_argument(
        "--force-full-rebuild",
        action="store_true",
        help="Force a full PDF rebuild regardless of changed files.",
    )
    args = parser.parse_args()
    if (args.only is None) != (args.public_root is None):
        parser.error("--only and --public-root must be used together")
    if args.check_only and (args.only is None or args.dry_run):
        parser.error("--check-only requires --only and cannot be combined with --dry-run")
    if args.only is not None and (
        args.changed_paths_file or args.published_base_url or args.force_full_rebuild
    ):
        parser.error("--only cannot be combined with deployment selection options")
    return args


def parse_front_matter(markdown_path: Path) -> dict[str, str]:
    content = markdown_path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(content)
    if not match:
        return {}

    values: dict[str, str] = {}
    for key, raw_value in ROOT_FIELD_RE.findall(match.group(1)):
        values[key] = strip_yaml_scalar(raw_value)
    return values


def strip_yaml_scalar(value: str) -> str:
    cleaned = value.strip()
    if not cleaned.startswith(('"', "'")):
        cleaned = re.split(r"[ \t]+#", cleaned, maxsplit=1)[0].rstrip()
    if len(cleaned) >= 2 and cleaned[0] == cleaned[-1] and cleaned[0] in {'"', "'"}:
        return cleaned[1:-1]
    return cleaned


def parse_bool(value: str | None) -> bool:
    if value is None:
        return False
    scalar = re.split(r"\s+#", value, maxsplit=1)[0]
    normalized = strip_yaml_scalar(scalar).strip().lower()
    return normalized == "true"


def resolve_pdf_filename(front_matter: dict[str, str], markdown_path: Path) -> str:
    filename = front_matter.get("pdf_filename") or f"{markdown_path.parent.name}.pdf"
    candidate = Path(filename)
    if candidate.name != filename or candidate.suffix.lower() != ".pdf":
        raise ValueError(
            f"Invalid pdf_filename in {markdown_path}: {filename!r}. Expected a PDF file name without directories."
        )
    return filename


def discover_exports(
    repo_root: Path, served_base_url: str, public_root: Path, only: Path | None
) -> list[ExportSpec]:
    content_root = repo_root / "content" / "praesentation"
    sources = sorted(content_root.glob("**/_index.md"))
    if only is not None:
        source = (repo_root / only).resolve()
        if only.is_absolute() or source not in sources:
            raise ValueError(f"Expected a repository-relative Reveal _index.md: {only}")
        sources = [source]

    exports: list[ExportSpec] = []
    for markdown_path in sources:
        front_matter = parse_front_matter(markdown_path)
        if parse_bool(front_matter.get("draft")) or not parse_bool(
            front_matter.get("pdf_export")
        ):
            continue

        pdf_filename = resolve_pdf_filename(front_matter, markdown_path)
        published_rel_dir = markdown_path.parent.relative_to(repo_root / "content")
        reveal_url = f"{served_base_url.rstrip('/')}/{published_rel_dir.as_posix()}/#/"
        pdf_output = public_root / published_rel_dir / pdf_filename
        exports.append(
            ExportSpec(
                source_path=markdown_path,
                reveal_url=reveal_url,
                pdf_output=pdf_output,
                published_rel_dir=published_rel_dir,
            )
        )

    return exports


def load_changed_paths(changed_paths_file: Path | None) -> tuple[list[str], bool]:
    if changed_paths_file is None:
        return [], False
    if not changed_paths_file.exists():
        raise FileNotFoundError(f"Changed paths file not found: {changed_paths_file}")

    contents = changed_paths_file.read_text(encoding="utf-8")
    if "\0" in contents:
        return [path for path in contents.split("\0") if path], True
    changed_paths = [line.strip().replace("\\", "/") for line in contents.splitlines() if line.strip()]
    return changed_paths, True


def path_matches_pattern(path: str, pattern: str) -> bool:
    return fnmatch.fnmatch(path, pattern)


def is_global_render_change(path: str) -> bool:
    return any(path_matches_pattern(path, pattern) for pattern in GLOBAL_RENDER_REBUILD_PATTERNS)


def spec_is_affected(spec: ExportSpec, repo_root: Path, changed_paths: list[str]) -> bool:
    source_path = spec.source_path.relative_to(repo_root).as_posix()
    source_dir = spec.source_path.parent.relative_to(repo_root).as_posix()
    source_dir_prefix = f"{source_dir}/"
    return any(path == source_path or path.startswith(source_dir_prefix) for path in changed_paths)


def changed_media_targets(
    changed_paths: list[str], repo_root: Path, public_root: Path, site: str
) -> set[Path]:
    static_media = [path.removeprefix("static/") for path in changed_paths
                    if path.startswith("static/")]
    content_media = [Path(path) for path in changed_paths
                     if path.startswith("content/") and Path(path).suffix.lower() != ".md"]
    targets = {(public_root / path).resolve() for path in static_media}
    if not content_media:
        return targets

    # Resolve bundle resources using Hugo's own routes, including custom slugs.
    pages = subprocess.check_output(
        ["hugo", "list", "all"], cwd=repo_root, text=True,
        env={**os.environ, "HUGO_BASEURL": site, "HUGO_ENVIRONMENT": "production"},
    )
    bundles = {
        Path(page["path"]).parent: page["permalink"]
        for page in csv.DictReader(StringIO(pages)) if Path(page["path"]).name == "index.md"
    }
    site_url = urlsplit(site)
    for path in content_media:
        # Keep the default route as well, including when the bundle was removed.
        targets.add((public_root / path.relative_to("content")).resolve())
        for parent in path.parents:
            if parent in bundles:
                resource = quote(path.relative_to(parent).as_posix())
                target = built_target(public_root, site_url, bundles[parent], resource)
                if target is not None:
                    targets.add(target)
                break
    return targets


def uses_changed_media(spec: ExportSpec, public_root: Path, site: str, targets: set[Path]) -> bool:
    html = spec.pdf_output.parent / "index.html"
    references = MediaReferences()
    references.feed(html.read_text(encoding="utf-8"))
    references.close()
    document_url = urljoin(site, quote(html.relative_to(public_root).as_posix()))
    site_url = urlsplit(site)
    return any(
        built_target(public_root, site_url, document_url, urljoin(document_url, reference)) in targets
        for reference in references.urls
    )


def select_exports_to_build(
    exports: list[ExportSpec],
    repo_root: Path,
    changed_paths: list[str],
    changed_paths_known: bool,
    force_full_rebuild: bool,
    public_root: Path,
    site_url: str,
) -> tuple[list[ExportSpec], bool, str]:
    if force_full_rebuild:
        return exports, True, "forced full rebuild"

    if not changed_paths_known:
        return exports, True, "changed paths unavailable"

    for path in changed_paths:
        if is_global_render_change(path):
            return exports, True, f"global render change: {path}"

    site = site_url.rstrip("/") + "/"
    targets = changed_media_targets(changed_paths, repo_root, public_root, site)
    selected = [
        spec for spec in exports
        if spec_is_affected(spec, repo_root, changed_paths)
        or (targets and uses_changed_media(spec, public_root, site, targets))
    ]
    return selected, False, "selective rebuild"


def build_published_pdf_url(spec: ExportSpec, published_base_url: str) -> str:
    encoded_parts = [quote(part) for part in spec.published_pdf_rel_path.parts]
    return f"{published_base_url.rstrip('/')}/{'/'.join(encoded_parts)}"


def check_pdf_download(spec: ExportSpec, public_root: Path, site_url: str) -> None:
    html = spec.pdf_output.parent / "index.html"
    navigation = read_navigation(html, collect_links=False)
    site = urlsplit(site_url.rstrip("/") + "/")
    document_url = urljoin(site.geturl(), quote(html.relative_to(public_root).as_posix()))
    links = navigation.pdf_downloads
    if len(links) != 1 or built_target(
        public_root.resolve(), site, document_url, links[0]
    ) != spec.pdf_output.resolve():
        raise ValueError(f"{html}: expected one PDF download for {spec.published_pdf_rel_path}")


def is_complete_pdf(path: Path) -> bool:
    if not path.is_file():
        return False
    with path.open("rb") as pdf:
        if pdf.read(5) != b"%PDF-":
            return False
        pdf.seek(max(5, path.stat().st_size - 1024))
        return pdf.read().rstrip().endswith(b"%%EOF")


def restore_published_pdfs(
    exports: list[ExportSpec], published_base_url: str, dry_run: bool
) -> list[ExportSpec]:
    missing = []
    for spec in exports:
        source_url = build_published_pdf_url(spec, published_base_url)
        print(f"Restoring {spec.published_pdf_rel_path.as_posix()} from {source_url}")
        if dry_run:
            continue

        try:
            with urlopen(source_url, timeout=15) as response:
                spec.pdf_output.parent.mkdir(parents=True, exist_ok=True)
                spec.pdf_output.write_bytes(response.read())
        except (URLError, TimeoutError, HTTPException) as exc:
            print(f"Could not restore {source_url}: {exc}. Will export again.")
            missing.append(spec)
            continue
        if not is_complete_pdf(spec.pdf_output):
            print(f"Invalid PDF at {source_url}. Will export again.")
            missing.append(spec)
    return missing


def wait_for_url(url: str, retries: int, delay: float) -> None:
    for attempt in range(1, retries + 1):
        try:
            with urlopen(url) as response:
                if 200 <= response.status < 400:
                    return
        except (HTTPError, URLError):
            if attempt == retries:
                raise RuntimeError(f"Reveal URL not ready after {retries} attempts: {url}")
            time.sleep(delay)


def export_pdf(spec: ExportSpec, pause_ms: int, retries: int, delay: float) -> None:
    wait_for_url(spec.reveal_url, retries, delay)
    spec.pdf_output.parent.mkdir(parents=True, exist_ok=True)

    command = [
        "npx",
        "-y",
        "decktape@3.12.0",
        "--pause",
        str(pause_ms),
        "--chrome-arg=--no-sandbox",
        "--chrome-arg=--disable-dev-shm-usage",
        "reveal",
        spec.reveal_url,
    ]
    with TemporaryDirectory(dir=spec.pdf_output.parent) as staging:
        generated = Path(staging) / spec.pdf_output.name
        subprocess.run([*command, str(generated)], check=True)
        if not is_complete_pdf(generated):
            raise RuntimeError(f"Incomplete PDF generated for {spec.source_path}")
        generated.replace(spec.pdf_output)


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    public_root = repo_root / "public"
    if args.public_root is not None:
        audit_output = args.public_root.resolve()
        if audit_output == repo_root or audit_output.is_relative_to(repo_root):
            raise ValueError("--public-root must be outside the repository")
        public_root = audit_output

    exports = discover_exports(repo_root, args.served_base_url, public_root, args.only)
    if args.only is not None:
        if not exports:
            raise ValueError(f"No PDF export configured for {args.only}")
        spec = exports[0]
        if args.check_only:
            check_pdf_download(spec, public_root, args.served_base_url)
            print(spec.published_pdf_rel_path.as_posix())
            return 0
        if spec.pdf_output.exists():
            raise FileExistsError(f"Temporary PDF already exists: {spec.pdf_output}")
        if not (spec.pdf_output.parent / "index.html").is_file():
            raise FileNotFoundError(f"Built Reveal HTML missing for {args.only}")
        print(f"Exporting {args.only} -> {spec.pdf_output}")
        if not args.dry_run:
            export_pdf(spec, args.pause_ms, args.readiness_retries, args.readiness_delay)
            check_pdf_download(spec, public_root, args.served_base_url)
        return 0

    changed_paths, changed_paths_known = load_changed_paths(args.changed_paths_file)

    if not exports:
        print("No Reveal presentations with pdf_export: true found.")
        return 0

    site_url = args.published_base_url or args.served_base_url
    exports_to_build, full_rebuild, selection_reason = select_exports_to_build(
        exports,
        repo_root,
        changed_paths,
        changed_paths_known,
        args.force_full_rebuild,
        public_root,
        site_url,
    )

    print(f"PDF export scope: {selection_reason}")

    if full_rebuild:
        print(f"Rebuilding all {len(exports_to_build)} PDFs.")
    else:
        if not args.published_base_url:
            raise RuntimeError("Selective PDF rebuild requires --published-base-url so unchanged PDFs can be restored.")
        unchanged = [spec for spec in exports if spec not in exports_to_build]
        missing = restore_published_pdfs(unchanged, args.published_base_url, args.dry_run)
        exports_to_build.extend(missing)
        print(f"Rebuilding {len(exports_to_build)} changed or missing PDFs.")

    for spec in exports_to_build:
        print(f"Exporting {spec.source_path.relative_to(repo_root)} -> {spec.pdf_output.relative_to(repo_root)}")
        if args.dry_run:
            continue
        export_pdf(spec, args.pause_ms, args.readiness_retries, args.readiness_delay)

    if not args.dry_run:
        for spec in exports:
            if not is_complete_pdf(spec.pdf_output):
                raise RuntimeError(f"Missing or incomplete PDF in deployment: {spec.published_pdf_rel_path}")
            check_pdf_download(spec, public_root, site_url)
        print(f"Verified {len(exports)} PDF downloads in the deployment artifact.")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"PDF export failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
