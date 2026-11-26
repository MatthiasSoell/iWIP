"""Regression tests for local HTML fragments in FINAL."""

import tempfile
import unittest
from pathlib import Path
from urllib.parse import urlsplit

from check_navigation import check_links, read_navigation


class NavigationFragmentTest(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.site = urlsplit("https://example.org/iWIP/")
        self.url = self.site.geturl()
        self.html = self.root / "index.html"

    def check(self, href, body=""):
        self.html.write_text(f'<a href="{href}">Link</a>{body}', encoding="utf-8")
        navigation = read_navigation(self.html)
        return check_links(navigation, self.html, self.root, self.site, self.url, fragments=True)

    def test_missing_ordinary_and_literature_anchors(self):
        for href in ("#fehlender-abschnitt", "#literatur"):
            with self.subTest(href=href):
                with self.assertRaisesRegex(ValueError, f"Missing built HTML anchor: {href}"):
                    self.check(href)

    def test_valid_html_fragments(self):
        for href, body in (
            ("#f%C3%B6rdern", '<h2 id="fördern">Fördern</h2>'),
            ("#literatur", '<span id="literatur"></span>'),
            ("#alt", '<a name="alt"></a>'),
            ("#TOP", ""),
            ("#:~:text=Link", ""),
            ("#alt:~:text=Link", '<a name="alt"></a>'),
        ):
            with self.subTest(href=href):
                self.assertEqual(self.check(href, body), 1)

    def test_other_html_page_has_its_own_targets(self):
        page = self.root / "andere"
        page.mkdir()
        (page / "index.html").write_text('<h2 id="dort">Abschnitt</h2>', encoding="utf-8")
        self.assertEqual(self.check("andere/#dort"), 1)
        with self.assertRaisesRegex(ValueError, "Missing built HTML anchor: andere/#hier"):
            self.check("andere/#hier", '<h2 id="hier">Abschnitt</h2>')

    def test_reveal_hash_is_scoped_to_the_target_presentation(self):
        page = self.root / "folien.html"
        page.write_text('<div class="reveal"><div class="slides"></div></div>', encoding="utf-8")
        for href in ("folien.html#/", "folien.html#/2/1", "folien.html#/diskussion"):
            with self.subTest(href=href):
                self.assertEqual(self.check(href), 1)
        with self.assertRaisesRegex(ValueError, "Missing built HTML anchor: #/2/1"):
            self.check("#/2/1")
        with self.assertRaisesRegex(ValueError, "Missing built HTML anchor: folien.html#fehlt"):
            self.check("folien.html#fehlt")

    def test_pdf_fragment_is_left_to_the_pdf_viewer(self):
        (self.root / "handout.pdf").touch()
        self.assertEqual(self.check("handout.pdf#page=3"), 1)


if __name__ == "__main__":
    unittest.main()
