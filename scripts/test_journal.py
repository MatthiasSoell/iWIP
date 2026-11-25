"""Regression tests for the Skill's journal transaction, using synthetic H03 states."""

from concurrent.futures import ThreadPoolExecutor
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


SKILL_SCRIPTS = Path(__file__).resolve().parents[1] / ".agents/skills/iwip-planungsagent/scripts"
sys.path.insert(0, str(SKILL_SCRIPTS))
import write_journal as journal


COMMON = """## Current State

```yaml
planning_focus: Feedback in einer betrieblichen Ausbildungssituation
main_line: Gemeinsame Fallanalyse mit Perspektivvergleich und Wirkungsanalyse
commitments:
  - {product}
constraints:
  - 90 Minuten
  - Keine externe Recherche
open_item: null
```

## Decision History

```yaml
- id: J-001
  date: 2026-11-25
  type: decision
  content: Drei Feedbackfälle vergleichen.
- id: J-002
  date: 2026-11-25
  type: decision
  content: Vergleichsmatrix zur Ergebnissicherung.
- id: J-003
  date: 2026-11-25
  type: revision
  dialogue_ref: H03.A6
  refers_to: [J-001, J-002]
  content: Einen gemeinsamen Fall analysieren und einen Gesprächsentwurf kommentieren.
"""
A6 = (COMMON.format(product="Gemeinsam kommentierter Gesprächsentwurf") + "```\n").encode()
B3 = (
    COMMON.format(product="Zwei Feedbackstrategien in einer Entscheidungstabelle abwägen")
    + """- id: J-004
  date: 2026-11-25
  type: revision
  dialogue_ref: H03.B3
  refers_to: [J-003]
  content: Bedingte Wahl zwischen zwei Feedbackstrategien in einer Entscheidungstabelle begründen.
```
"""
).encode()


class JournalTest(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.case = Path(folder.name)
        self.live = self.case / journal.JOURNAL
        self.history = self.case / "journal_history"

    def cli(self, command, *args, candidate=None):
        return subprocess.run(
            [sys.executable, str(SKILL_SCRIPTS / "write_journal.py"), command, str(self.case), *args],
            input=candidate,
            capture_output=True,
        )

    def read(self):
        result = self.cli("read")
        self.assertEqual(result.returncode, 0, result.stderr)
        digest, data = result.stdout.split(b"\n", 1)
        return digest.decode(), data

    def write(self, expected, candidate, *modes):
        return self.cli("write", "--expected", expected, *modes, candidate=candidate)

    def test_existing_journal_rejects_missing_or_conflicting_modes(self):
        self.live.write_bytes(A6)
        expected = self.read()[0]
        for modes in ((), ("--archive", "--continue")):
            with self.subTest(modes=modes):
                result = self.write(expected, B3, *modes)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(b"--archive", result.stderr)
                self.assertIn(b"--continue", result.stderr)
                self.assertFalse(result.stdout)
                self.assertEqual(self.live.read_bytes(), A6)
                self.assertFalse(self.history.exists())

    def test_h03_restart_and_revision(self):
        self.assertEqual(self.read(), ("missing", b""))
        result = self.write("missing", A6)
        self.assertEqual(result.returncode, 0, result.stderr)
        # B1 reads the state. B2 is a wording change with no journal-worthy event.
        a6_digest, loaded = self.read()
        self.assertEqual(loaded, A6)
        self.assertFalse(self.history.exists())
        # An accidental no-op write or explicit reconciliation also stays read-only.
        self.assertEqual(self.write(a6_digest, A6, "--archive").stdout, b"unchanged\n")
        self.assertFalse(self.history.exists())
        self.assertEqual(self.read(), (a6_digest, A6))

        result = self.write(a6_digest, B3, "--archive")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.live.read_bytes(), B3)
        self.assertEqual((self.history / "session_001.md").read_bytes(), A6)
        self.assertFalse((self.case / "planning_state.md").exists())
        # Retrying the identical transaction doesn't create a second snapshot or event.
        self.assertEqual(self.write(a6_digest, B3, "--archive").stdout, b"unchanged\n")
        # A further change in the same session uses --continue.
        later = B3.replace(b"90 Minuten", b"120 Minuten")
        self.assertEqual(self.write(self.read()[0], later, "--continue").returncode, 0)
        self.assertEqual(self.live.read_bytes(), later)
        self.assertEqual(list(self.history.iterdir()), [self.history / "session_001.md"])
        self.assertEqual((self.history / "session_001.md").read_bytes(), A6)

    def test_appends_after_existing_snapshot_without_overwriting(self):
        # CRLF and non-ASCII must survive byte-for-byte in the snapshot.
        original = A6.replace(b"\n", b"\r\n")
        self.live.write_bytes(original)
        self.history.mkdir()
        first = self.history / "session_009.md"
        first.write_bytes(b"older")
        result = self.write(self.read()[0], B3, "--archive")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(first.read_bytes(), b"older")
        self.assertEqual((self.history / "session_010.md").read_bytes(), original)

    def test_failed_staging_leaves_current_journal_untouched(self):
        self.live.write_bytes(A6)
        with patch.object(journal.os, "fsync", side_effect=OSError("stage interrupted")):
            with self.assertRaisesRegex(OSError, "stage interrupted"):
                journal.write_journal(self.case, journal.fingerprint(A6), B3, "archive")
        self.assertEqual(list(self.case.iterdir()), [self.live])
        self.assertEqual(self.live.read_bytes(), A6)

    def test_failed_snapshot_leaves_current_journal_untouched(self):
        self.live.write_bytes(A6)
        with patch.object(journal.os, "link", side_effect=OSError("archive interrupted")):
            with self.assertRaisesRegex(OSError, "archive interrupted"):
                journal.write_journal(self.case, journal.fingerprint(A6), B3, "archive")
        self.assertEqual(list(self.history.iterdir()), [])
        self.assertEqual(self.live.read_bytes(), A6)

    def test_failed_replace_reuses_existing_snapshot_on_retry(self):
        self.live.write_bytes(A6)
        expected = journal.fingerprint(A6)
        with patch.object(journal.os, "replace", side_effect=OSError("replace interrupted")):
            with self.assertRaisesRegex(OSError, "replace interrupted"):
                journal.write_journal(self.case, expected, B3, "archive")
        self.assertEqual(self.live.read_bytes(), A6)
        snapshot = self.history / "session_001.md"
        self.assertEqual(snapshot.read_bytes(), A6)
        before = snapshot.stat()

        result = self.write(expected, B3, "--archive")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.live.read_bytes(), B3)
        self.assertEqual(snapshot.stat().st_ino, before.st_ino)
        self.assertEqual(snapshot.stat().st_mtime_ns, before.st_mtime_ns)
        self.assertEqual(list(self.history.iterdir()), [snapshot])

    def test_retry_after_replace_but_before_confirmation(self):
        self.live.write_bytes(A6)
        expected = journal.fingerprint(A6)
        fsync = os.fsync

        def fail_after_replace(fd):
            if self.live.read_bytes() == B3:
                raise OSError("confirmation interrupted")
            fsync(fd)

        with patch.object(journal.os, "fsync", side_effect=fail_after_replace):
            with self.assertRaisesRegex(OSError, "confirmation interrupted"):
                journal.write_journal(self.case, expected, B3, "archive")
        self.assertEqual(self.live.read_bytes(), B3)
        self.assertEqual((self.history / "session_001.md").read_bytes(), A6)
        result = self.write(expected, B3, "--archive")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, b"unchanged\n")
        self.assertEqual(len(list(self.history.iterdir())), 1)

    def test_stale_base_is_rejected_before_archiving(self):
        self.live.write_bytes(A6)
        digest, _ = self.read()
        intervening = A6.replace(b"90 Minuten", b"120 Minuten")
        self.live.write_bytes(intervening)
        result = self.write(digest, B3, "--archive")
        self.assertEqual(result.returncode, 1)
        self.assertFalse(result.stdout)
        self.assertEqual(self.live.read_bytes(), intervening)
        self.assertFalse(self.history.exists())

    def test_parallel_writers_get_one_commit_and_one_conflict(self):
        self.live.write_bytes(A6)
        expected = self.read()[0]
        candidates = [B3, B3.replace(b"90 Minuten", b"120 Minuten")]
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(lambda candidate: self.write(expected, candidate, "--archive"), candidates))
        self.assertEqual(sorted(result.returncode for result in results), [0, 1])
        winner = next(data for data, result in zip(candidates, results) if result.returncode == 0)
        self.assertEqual(self.live.read_bytes(), winner)
        self.assertEqual((self.history / "session_001.md").read_bytes(), A6)
        self.assertEqual(len(list(self.history.iterdir())), 1)

    def test_symlink_targets_are_rejected(self):
        with tempfile.TemporaryDirectory() as outside:
            elsewhere = Path(outside) / journal.JOURNAL
            elsewhere.write_bytes(A6)
            self.live.symlink_to(elsewhere)
            self.assertEqual(self.cli("read").returncode, 1)
            self.assertEqual(self.write(journal.fingerprint(A6), B3, "--archive").returncode, 1)
            self.assertEqual(elsewhere.read_bytes(), A6)
            self.live.unlink()
            self.live.write_bytes(A6)
            self.history.symlink_to(outside)
            result = self.write(self.read()[0], B3, "--archive")
            self.assertEqual(result.returncode, 1)
            self.assertFalse(result.stdout)
            self.assertEqual(self.live.read_bytes(), A6)
            self.assertEqual(os.listdir(outside), [journal.JOURNAL])


if __name__ == "__main__":
    unittest.main()
