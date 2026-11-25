"""Read or atomically replace the journal in an already approved case folder."""

import argparse
from contextlib import contextmanager
import fcntl
import hashlib
import os
from pathlib import Path
import re
import stat
import sys
import tempfile


JOURNAL = "planning_journal.md"
SNAPSHOT_NAME = re.compile(r"session_(\d{3,})\.md")


@contextmanager
def open_directory(path):
    fd = os.open(path, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        yield fd
    finally:
        os.close(fd)


def read_file(path):
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(fd, "rb") as source:
        if not stat.S_ISREG(os.fstat(source.fileno()).st_mode):
            raise ValueError(f"Keine regulaere Datei: {path}")
        return source.read()


def read_journal(folder):
    try:
        return read_file(folder / JOURNAL)
    except FileNotFoundError:
        return None


def fingerprint(data):
    return "missing" if data is None else hashlib.sha256(data).hexdigest()


@contextmanager
def staged_file(folder, data):
    fd, name = tempfile.mkstemp(prefix=".planning_journal_", dir=folder)
    path = Path(name)
    try:
        with os.fdopen(fd, "wb") as output:
            output.write(data)
            output.flush()
            os.fsync(output.fileno())
        yield path
    finally:
        path.unlink(missing_ok=True)


def archive_journal(folder, previous, case_fd):
    archive = folder / "journal_history"
    archive.mkdir(mode=0o700, exist_ok=True)
    with open_directory(archive) as archive_fd:
        snapshots = []
        for entry in archive.iterdir():
            match = SNAPSHOT_NAME.fullmatch(entry.name)
            if match:
                snapshots.append((int(match[1]), entry))
        number, latest = max(snapshots, default=(0, None))
        if latest is None or read_file(latest) != previous:
            target = archive / f"session_{number + 1:03d}.md"
            with staged_file(archive, previous) as staged:
                os.link(staged, target)
        os.fsync(archive_fd)
    # The archive directory itself may have just been created.
    os.fsync(case_fd)


def write_journal(folder, expected, candidate, mode):
    if not candidate.decode("utf-8").strip():
        raise ValueError("Der neue Journalstand ist leer.")

    with open_directory(folder) as case_fd:
        fcntl.flock(case_fd, fcntl.LOCK_EX)
        previous = read_journal(folder)
        if previous == candidate:
            os.fsync(case_fd)
            return "unchanged"
        if fingerprint(previous) != expected:
            raise ValueError("Journalstand hat sich geaendert. Lies das Journal erneut.")
        if previous is not None and mode not in ("archive", "continue"):
            raise ValueError("Fuer Aenderungen am bestehenden Journal ist --archive oder --continue erforderlich.")

        with staged_file(folder, candidate) as staged:
            if previous is None:
                os.link(staged, folder / JOURNAL)
            else:
                if mode == "archive":
                    archive_journal(folder, previous, case_fd)
                os.replace(staged, folder / JOURNAL)
        os.fsync(case_fd)
    return "written"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("read").add_argument("case_folder", type=Path)
    writer = commands.add_parser("write")
    writer.add_argument("case_folder", type=Path)
    writer.add_argument("--expected", required=True, help="SHA-256 from read, or missing")
    modes = writer.add_mutually_exclusive_group()
    modes.add_argument("--archive", dest="mode", action="store_const", const="archive",
                       help="Save a snapshot before the first change after resuming")
    modes.add_argument("--continue", dest="mode", action="store_const", const="continue",
                       help="Update within the same session without another snapshot")
    args = parser.parse_args()

    try:
        folder = args.case_folder.resolve(strict=True)
        if args.command == "read":
            with open_directory(folder):
                data = read_journal(folder)
            sys.stdout.buffer.write(fingerprint(data).encode("ascii") + b"\n")
            if data is not None:
                sys.stdout.buffer.write(data)
        else:
            print(write_journal(folder, args.expected, sys.stdin.buffer.read(), args.mode))
    except (OSError, ValueError) as error:
        parser.exit(1, f"Journal: {error}\n")


if __name__ == "__main__":
    main()
