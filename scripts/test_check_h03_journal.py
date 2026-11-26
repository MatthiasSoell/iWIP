"""Regression tests for H03 evaluation using synthetic journal snapshots."""

import subprocess
import tempfile
import unittest
from pathlib import Path

from test_journal import A6, B3


CHECKER = Path(__file__).with_name("check_h03_journal.rb")


class H03CheckTest(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        a2 = A6.split(b"- id: J-002")[0] + b"```\n"
        a3 = A6.split(b"- id: J-003")[0] + b"```\n"
        journals = {"A1": None, "A2": a2, "A3": a3, "A4": a3, "A5": a3,
                    "A6": A6, "B1": A6, "B2": A6, "B3": B3}
        for turn, journal in journals.items():
            directory = self.root / turn
            directory.mkdir()
            if journal is not None:
                (directory / "planning_journal.md").write_bytes(journal)
        for turn in ("A6", "B1", "B2", "B3"):
            (self.root / turn / "journal_history").mkdir()
        self.archive("B3").write_bytes(A6)

    def archive(self, turn):
        return self.root / turn / "journal_history" / "session_001.md"

    def check(self):
        return subprocess.run(["ruby", str(CHECKER), str(self.root)],
                              capture_output=True, text=True)

    def assert_rejected(self, message):
        result = self.check()
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn(message, result.stderr)

    def test_allowed_fields_and_archive(self):
        # The synthetic revisions carry dialogue_ref and omit an unrecorded rationale.
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_invalid_fields(self):
        journal = self.root / "A2" / "planning_journal.md"
        original = journal.read_bytes()
        for field, message in (
            (b"  rationale: null\n", "ungültiger Text in rationale"),
            (b"  dialogue_ref: ''\n", "ungültiger Text in dialogue_ref"),
            (b"  unknown: value\n", "Ungültige Historienfelder"),
            (b"  refers_to: J-002\n", "Nur frühere IDs"),
        ):
            with self.subTest(field=field):
                journal.write_bytes(original[:-4] + field + original[-4:])
                self.assert_rejected(message)

    def test_revision_cannot_omit_required_reference(self):
        journal = self.root / "B3" / "planning_journal.md"
        extra_revision = (
            b"- id: J-005\n  date: 2026-11-25\n  type: revision\n"
            b"  content: Die Sicherung auf den Vergleich der Strategien begrenzen.\n"
        )
        for event_id, candidate in (
            ("J-004", B3.replace(b"  refers_to: [J-003]\n", b"")),
            ("J-005", B3[:-4] + extra_revision + B3[-4:]),
        ):
            with self.subTest(event_id=event_id):
                journal.write_bytes(candidate)
                self.assert_rejected(f"B3: Fehlender Revisionsbezug für {event_id}")

    def test_a6_revisions_cover_both_prior_decision_checkpoints(self):
        for turn in ("A6", "B1", "B2", "B3"):
            journal = self.root / turn / "planning_journal.md"
            journal.write_bytes(journal.read_bytes().replace(b"[J-001, J-002]", b"[J-001]"))
        self.archive("B3").write_bytes(A6.replace(b"[J-001, J-002]", b"[J-001]"))
        self.assert_rejected("A6: Revisionsbezug auf A3 fehlt")

    def test_early_archive(self):
        for turn in ("B1", "B2"):
            with self.subTest(turn=turn):
                self.archive(turn).write_bytes(A6)
                self.assert_rejected(f"{turn}: Sitzungsarchiv")
                self.archive(turn).unlink()

    def test_missing_or_wrong_final_snapshot(self):
        self.archive("B3").unlink()
        self.assert_rejected("B3: Erwartet genau einen")
        self.archive("B3").write_bytes(B3)
        self.assert_rejected("B3: Erwartet genau einen")

    def test_missing_archive_evidence(self):
        self.archive("B2").parent.rmdir()
        self.assert_rejected("B2: Archivbeleg fehlt")


if __name__ == "__main__":
    unittest.main()
