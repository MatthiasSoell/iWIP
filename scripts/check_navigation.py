"""Check HTML links and JavaScript navigation against a local Hugo build."""

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote, unquote, urljoin, urlsplit


LOCATION = re.compile(r"\b(?:window\.)?location\s*\.\s*href\s*=")
DESTINATION = re.compile(
    r"""\s*(['"])((?:[^'"\\\r\n]|\\[/'"]|\\u[0-9a-fA-F]{4})+)\1\s*;?\s*"""
)
JS_ESCAPE = re.compile(r"""\\([/'"]|u[0-9a-fA-F]{4})""")
NAVIGATION_TITLES = {"Zur Blogansicht", "Zur Präsentationsansicht"}
DEFAULT_PORTS = {"http": 80, "https": 443}


class Navigation(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []
        self.links = []
        self.pdf_downloads = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag != "base" and attributes.get("href"):
            self.links.append(attributes["href"].strip())
        if tag == "a" and "download" in attributes and attributes.get("title") == "PDF herunterladen":
            self.pdf_downloads.append(attributes.get("href") or "")
        if tag != "button":
            return
        action = (attributes.get("onclick") or "").strip()
        assignment = LOCATION.match(action)
        if assignment:
            match = DESTINATION.fullmatch(action[assignment.end():])
            if match:
                self.targets.append(JS_ESCAPE.sub(unescape_js, match[2]))
                return
        if assignment or LOCATION.search(action) or attributes.get("title") in NAVIGATION_TITLES:
            raise ValueError(f"Unsupported navigation button at line {self.getpos()[0]}")


def unescape_js(match):
    escape = match[1]
    return chr(int(escape[1:], 16)) if escape.startswith("u") else escape


def built_target(root, site, document_url, destination, *, button=False):
    target = urlsplit(urljoin(document_url, destination))
    path = unquote(target.path)
    prefix = unquote(site.path)
    site_port = None if site.port == DEFAULT_PORTS.get(site.scheme) else site.port
    target_port = None if target.port == DEFAULT_PORTS.get(target.scheme) else target.port
    same_site = (target.hostname, target_port) == (site.hostname, site_port)
    in_prefix = path.startswith(prefix) or path == prefix.rstrip("/")
    if target.scheme not in DEFAULT_PORTS or not same_site or not in_prefix:
        if button:
            raise ValueError(f"Button target is outside the site: {destination}")
        if same_site and not in_prefix and not urlsplit(destination).netloc:
            raise ValueError(f"Local link target is outside the site: {destination}")
        return None
    built = (root / path[len(prefix):]).resolve()
    if not built.is_relative_to(root):
        raise ValueError(f"Target is outside the build: {destination}")
    return built


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path)
    parser.add_argument("build_root", type=Path)
    parser.add_argument("site_url")
    parser.add_argument(
        "--pending-pdf", type=Path, help="Build-relative path of the one PDF generated in deployment."
    )
    args = parser.parse_args()

    try:
        root = args.build_root.resolve()
        html = args.html.resolve()
        site = urlsplit(args.site_url.rstrip("/") + "/")
        if site.scheme not in ("http", "https") or not site.netloc or site.query or site.fragment:
            raise ValueError("Expected an absolute HTTP(S) site URL without query or fragment")
        document = quote(html.relative_to(root).as_posix())
        document_url = urljoin(site.geturl(), document)
        pending_pdf = None
        if args.pending_pdf is not None:
            pending_pdf = (root / args.pending_pdf).resolve()
            if (args.pending_pdf.is_absolute() or not pending_pdf.is_relative_to(root)
                    or pending_pdf.suffix.lower() != ".pdf" or pending_pdf.parent != html.parent):
                raise ValueError("Expected a build-relative PDF path next to the HTML being checked")

        navigation = Navigation()
        navigation.feed(html.read_text(encoding="utf-8"))
        navigation.close()
        for destination in navigation.targets:
            built = built_target(root, site, document_url, destination, button=True)
            if not (built.is_file() or (built / "index.html").is_file()):
                raise ValueError(f"Missing built button target: {destination}")

        checked_links = 0
        for destination in dict.fromkeys(navigation.links):
            built = built_target(root, site, document_url, destination)
            if built is None or built == pending_pdf:
                continue
            if not (built.is_file() or (built / "index.html").is_file()):
                raise ValueError(f"Missing built link target: {destination}")
            checked_links += 1
    except (OSError, ValueError) as error:
        parser.exit(1, f"{args.html}: {error}\n")

    print(f"Checked {len(navigation.targets)} JavaScript navigation buttons.")
    print(f"Checked {checked_links} distinct local href targets.")


if __name__ == "__main__":
    main()
