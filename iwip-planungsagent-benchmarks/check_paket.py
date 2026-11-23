"""Prüft die statischen Dateiverweise des Planungsagenten ohne Modellaufruf."""

import re
import sys
from pathlib import Path


def check_package(package, repository=None):
    entry = (package / "SKILL.md").read_text(encoding="utf-8")
    start_files = re.findall(r"^- `(core/[^/\n`]+\.md)`$", entry, re.MULTILINE)
    core_files = set(package.glob("core/*.md"))
    if len(start_files) != 4 or {package / name for name in start_files} != core_files:
        raise ValueError("Der SKILL-Einstieg muss die vier Kerndateien einzeln laden.")

    for filename in ["README.md", "LICENSE.md"]:
        if not (package / filename).is_file():
            raise FileNotFoundError(package / filename)

    for document in package.rglob("*.md"):
        contents = document.read_text(encoding="utf-8")
        references = re.findall(
            r"`((?:core|references|tasks|publikation|project_governance|content)/"
            r"[^`\n<>]*?\.md)`", contents
        )
        for name in references:
            root = repository if name.startswith(("project_governance/", "content/")) else package
            if root is not None and not (root / name).is_file():
                raise FileNotFoundError(f"{document}: {name}")


if __name__ == "__main__":
    repo = Path(__file__).resolve().parents[1]
    if len(sys.argv) == 1:
        check_package(repo / ".agents/skills/iwip-planungsagent", repo)
    elif len(sys.argv) == 2:
        check_package(Path(sys.argv[1]).resolve())
    else:
        sys.exit("Aufruf: check_paket.py [entpackter Skill-Ordner]")
    print("Paket und Dateiverweise geprüft.")
