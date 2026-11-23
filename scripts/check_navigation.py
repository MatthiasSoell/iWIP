"""Check local button destinations that HTML link checkers do not extract."""

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


class Navigation(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        if tag != "button":
            return
        attributes = dict(attrs)
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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path)
    parser.add_argument("build_root", type=Path)
    parser.add_argument("site_url")
    args = parser.parse_args()

    try:
        root = args.build_root.resolve()
        html = args.html.resolve()
        site = urlsplit(args.site_url.rstrip("/") + "/")
        if site.scheme not in ("http", "https") or not site.netloc or site.query or site.fragment:
            raise ValueError("Expected an absolute HTTP(S) site URL without query or fragment")
        document = quote(html.relative_to(root).as_posix())
        navigation = Navigation()
        navigation.feed(html.read_text(encoding="utf-8"))
        navigation.close()
        prefix = unquote(site.path)
        for destination in navigation.targets:
            target = urlsplit(urljoin(urljoin(site.geturl(), document), destination))
            path = unquote(target.path)
            if (target.scheme, target.netloc) != (site.scheme, site.netloc) or not path.startswith(prefix):
                raise ValueError(f"Button target is outside the site: {destination}")
            built = (root / path[len(prefix):]).resolve()
            if not built.is_relative_to(root) or not (built.is_file() or (built / "index.html").is_file()):
                raise ValueError(f"Missing built button target: {destination}")
    except (OSError, ValueError) as error:
        parser.exit(1, f"{args.html}: {error}\n")

    print(f"Checked {len(navigation.targets)} JavaScript navigation buttons.")


if __name__ == "__main__":
    main()
