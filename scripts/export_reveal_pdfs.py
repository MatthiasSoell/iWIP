#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
ROOT_FIELD_RE = re.compile(r"^([A-Za-z0-9_]+):\s*(.*?)\s*$", re.MULTILINE)


@dataclass(frozen=True)
class ExportSpec:
    source_path: Path
    reveal_url: str
    pdf_output: Path


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
    return parser.parse_args()


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
    if len(cleaned) >= 2 and cleaned[0] == cleaned[-1] and cleaned[0] in {'"', "'"}:
        return cleaned[1:-1]
    return cleaned


def parse_bool(value: str | None) -> bool:
    if value is None:
        return False
    normalized = strip_yaml_scalar(value).strip().lower()
    return normalized == "true"


def resolve_pdf_filename(front_matter: dict[str, str], markdown_path: Path) -> str:
    filename = front_matter.get("pdf_filename") or f"{markdown_path.parent.name}.pdf"
    candidate = Path(filename)
    if candidate.name != filename or candidate.suffix.lower() != ".pdf":
        raise ValueError(
            f"Invalid pdf_filename in {markdown_path}: {filename!r}. Expected a PDF file name without directories."
        )
    return filename


def discover_exports(repo_root: Path, served_base_url: str) -> list[ExportSpec]:
    content_root = repo_root / "content" / "praesentation"
    public_root = repo_root / "public"
    exports: list[ExportSpec] = []

    for markdown_path in sorted(content_root.glob("**/_index.md")):
        front_matter = parse_front_matter(markdown_path)
        if not parse_bool(front_matter.get("pdf_export")):
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
            )
        )

    return exports


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
        "decktape",
        "--pause",
        str(pause_ms),
        "--chrome-arg=--no-sandbox",
        "--chrome-arg=--disable-dev-shm-usage",
        "reveal",
        spec.reveal_url,
        str(spec.pdf_output),
    ]
    subprocess.run(command, check=True)


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    exports = discover_exports(repo_root, args.served_base_url)

    if not exports:
        print("No Reveal presentations with pdf_export: true found.")
        return 0

    for spec in exports:
        print(f"Exporting {spec.source_path.relative_to(repo_root)} -> {spec.pdf_output.relative_to(repo_root)}")
        if args.dry_run:
            continue
        export_pdf(spec, args.pause_ms, args.readiness_retries, args.readiness_delay)

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"PDF export failed: {exc}", file=sys.stderr)
        raise SystemExit(1)