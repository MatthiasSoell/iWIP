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
VOID_TAGS = set("area base br col embed hr img input link meta param source track wbr".split())
SHARED_CLASSES = {"header", "footer", "post-header", "post-footer", "reveal-branding"}


class Navigation(HTMLParser):
    def __init__(self, *, content_class=None, shared=False, collect_links=True):
        super().__init__()
        self.content_class = content_class
        self.shared = shared
        self.collect_links = collect_links
        self.regions = []
        self.content_found = False
        self.ids = set()
        self.canonical = None
        self.targets = []
        self.links = []
        self.pdf_downloads = []

    def handle_endtag(self, tag):
        for index in range(len(self.regions) - 1, -1, -1):
            if self.regions[index][0] == tag:
                del self.regions[index:]
                break

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID_TAGS:
            self.handle_endtag(tag)

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        classes = set((attributes.get("class") or "").split())
        element_id = attributes.get("id")
        if element_id:
            self.ids.add(element_id)
        if tag == "link" and attributes.get("rel") == "canonical":
            self.canonical = attributes.get("href")
        if self.content_class in classes:
            self.content_found = True
        selected = self.regions[-1][1] if self.regions else not (self.content_class or self.shared)
        if self.content_class in classes or (self.shared and classes & SHARED_CLASSES):
            selected = True
        if tag not in VOID_TAGS:
            self.regions.append((tag, selected))
        if self.collect_links and selected and tag != "base" and attributes.get("href"):
            self.links.append(attributes["href"].strip())
        if tag == "a" and "download" in attributes and attributes.get("title") == "PDF herunterladen":
            self.pdf_downloads.append(attributes.get("href") or "")
        if tag != "button" or not self.collect_links or not selected:
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


def configured_site_url(repo_root):
    config = (repo_root / "config.toml").read_text(encoding="utf-8")
    match = re.search(r"""^baseURL\s*=\s*(["'])(.+?)\1""", config, re.MULTILINE)
    if not match:
        raise ValueError("Missing baseURL in config.toml")
    return match[2]


def read_navigation(html, **options):
    navigation = Navigation(**options)
    navigation.feed(html.read_text(encoding="utf-8"))
    navigation.close()
    return navigation


def check_links(navigation, html, root, site, document_url, pending_pdf=None, *, literature=False):
    for destination in navigation.targets:
        built = built_target(root, site, document_url, destination, button=True)
        if not (built.is_file() or (built / "index.html").is_file()):
            raise ValueError(f"Missing built button target: {destination}")

    checked_links = 0
    for destination in dict.fromkeys(navigation.links):
        built = built_target(root, site, document_url, destination)
        if built is None or built == pending_pdf:
            continue
        target = built if built.is_file() else built / "index.html"
        if not target.is_file():
            raise ValueError(f"Missing built link target: {destination}")
        if literature and unquote(urlsplit(destination).fragment) == "literatur":
            ids = navigation.ids if target == html else read_navigation(target, collect_links=False).ids
            if "literatur" not in ids:
                raise ValueError(f"Missing built literature anchor: {destination}")
        checked_links += 1
    return checked_links


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path)
    parser.add_argument("build_root", type=Path)
    parser.add_argument("site_url", nargs="?", help="Defaults to baseURL from config.toml.")
    parser.add_argument("--shared", action="store_true", help="Check shared header and footer links only.")
    parser.add_argument(
        "--pending-pdf", type=Path, help="Build-relative path of the one PDF generated in deployment."
    )
    args = parser.parse_args()

    try:
        root = args.build_root.resolve()
        html = args.html.resolve()
        site_url = args.site_url or configured_site_url(Path(__file__).resolve().parents[1])
        site = urlsplit(site_url.rstrip("/") + "/")
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

        navigation = read_navigation(html, shared=args.shared)
        checked_links = check_links(navigation, html, root, site, document_url, pending_pdf)
    except (OSError, ValueError) as error:
        parser.exit(1, f"{args.html}: {error}\n")

    print(f"Checked {len(navigation.targets)} JavaScript navigation buttons.")
    print(f"Checked {checked_links} distinct local href targets.")


if __name__ == "__main__":
    main()
