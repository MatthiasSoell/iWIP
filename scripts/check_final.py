"""Build and check one prepared iWIP publication candidate in isolation."""

import argparse
import csv
import hashlib
import shutil
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.parse import urlsplit

from check_navigation import built_target, check_links, configured_site_url, read_navigation
from export_reveal_pdfs import check_pdf_download, discover_exports, parse_front_matter


BUILD_DIRS = ("archetypes", "assets", "config", "content", "data", "i18n", "layouts", "static", "themes", "_vendor")
BUILD_FILES = ("config.toml", "go.mod", "go.sum")


def copy_build_sources(repo, source):
    for name in BUILD_DIRS:
        if (repo / name).is_dir():
            shutil.copytree(
                repo / name, source / name,
                ignore=shutil.ignore_patterns("planning_journal.md", "planning_state.md"),
            )
    for name in BUILD_FILES:
        if (repo / name).is_file():
            shutil.copy2(repo / name, source / name)


def artifact_type(path):
    if ".." not in path.parts and len(path.parts) >= 4:
        if path.parts[:2] == ("content", "blog") and path.name == "index.md":
            return "blog"
        if path.parts[:2] == ("content", "praesentation") and path.name == "_index.md":
            return "reveal"
    raise ValueError(f"Expected a repository-relative blog index.md or Reveal _index.md: {path}")


def publication_url(source, target):
    # Let Hugo resolve slugs and route overrides without rendering the site.
    listing = subprocess.run(
        ["hugo", "list", "all"], cwd=source, check=True, capture_output=True, text=True,
    )
    for row in csv.DictReader(listing.stdout.splitlines()):
        if row["path"] == target.as_posix() and row["draft"] == "false":
            return row["permalink"]
    raise ValueError(f"Candidate missing from Hugo's published routes: {target}")


def check_candidate(repo, target, candidate, base_blog):
    kind = artifact_type(target)
    if (kind == "reveal") != (base_blog is not None):
        raise ValueError("Pass --base-blog PATH SHA256 for Reveal candidates only")

    with TemporaryDirectory(prefix="iwip-final-") as temporary:
        workspace = Path(temporary).resolve()
        source = workspace / "source"
        output = workspace / "public"
        source.mkdir()
        copy_build_sources(repo, source)

        if base_blog:
            blog_path, approved_hash = base_blog
            blog = Path(blog_path)
            if artifact_type(blog) != "blog":
                raise ValueError(f"Expected the approved blog source: {blog}")
            if hashlib.sha256((source / blog).read_bytes()).hexdigest() != approved_hash:
                raise ValueError(f"Staged blog differs from the approved version: {blog}")

        staged = source / target
        staged.parent.mkdir(parents=True, exist_ok=True)
        staged.write_bytes(candidate)
        site_url = configured_site_url(source).rstrip("/") + "/"
        site = urlsplit(site_url)
        page_url = publication_url(source, target)
        built = built_target(output, site, site_url, page_url, button=True)
        page_path = urlsplit(page_url).path
        html = built / "index.html" if page_path.endswith("/") else built
        subprocess.run(["hugo", "--minify", "--destination", str(output)], cwd=source, check=True)

        navigation = read_navigation(html, content_class="slides" if kind == "reveal" else "post-content")
        if not navigation.content_found:
            raise ValueError(f"Expected rendered {kind} content at {page_url}")

        frontmatter = parse_front_matter(staged)
        if kind == "blog" and "md-oer-meta" in navigation.ids:
            expected_permalink = page_path[len(site.path.rstrip("/")):]
            if navigation.canonical != page_url or frontmatter.get("permalink") != expected_permalink:
                raise ValueError(f"OER permalink must match the built canonical route: {expected_permalink}")

        pending_pdf = None
        if kind == "reveal":
            exports = discover_exports(source, site_url, output, target)
            if not exports:
                raise ValueError(f"No PDF export configured for {target}")
            spec = exports[0]
            if spec.pdf_output.parent / "index.html" != html:
                raise ValueError(f"PDF must be published next to the Reveal HTML: {page_url}")
            check_pdf_download(spec, output, site_url)
            pending_pdf = spec.pdf_output.resolve()

        check_links(navigation, html, output, site, page_url, pending_pdf, fragments=True)
        return page_url


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path, help="Repository-relative content path.")
    parser.add_argument("candidate", type=Path, help="Prepared Markdown file with draft: false.")
    parser.add_argument("--base-blog", nargs=2, metavar=("PATH", "SHA256"), help="Approved blog for Reveal.")
    args = parser.parse_args()
    try:
        candidate = args.candidate.read_bytes()
        page_url = check_candidate(Path(__file__).resolve().parents[1], args.target, candidate, args.base_blog)
    except subprocess.CalledProcessError as error:
        parser.exit(1, f"{error.stderr or error}\n")
    except (OSError, ValueError) as error:
        parser.exit(1, f"{args.target}: {error}\n")
    print(f"Checked {page_url} (SHA-256: {hashlib.sha256(candidate).hexdigest()})")


if __name__ == "__main__":
    main()
