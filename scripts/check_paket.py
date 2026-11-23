"""Prüft Skill-Metadaten und lokale Dateiverweise ohne Modellaufruf."""

import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


def check_frontmatter(entry, package_name):
    frontmatter = re.match(r"\A---\n(.+?)\n---\n\s*\S", entry, re.DOTALL)
    if not frontmatter:
        raise ValueError("SKILL.md braucht YAML-Frontmatter und einen Inhalt.")

    # Ruby/Psych ist im Repository bereits für die OERSI-Metadaten im Einsatz.
    result = subprocess.run(
        [
            "ruby", "-ryaml", "-rjson", "-e",
            "source = STDIN.read; node = YAML.parse(source).root; "
            "abort 'Expected YAML mapping' unless node.is_a?(Psych::Nodes::Mapping); "
            "keys = node.children.each_slice(2).map { |key, _| key.value }; "
            "abort 'Duplicate YAML keys' unless keys.uniq == keys; "
            "puts JSON.generate(YAML.safe_load(source))",
        ],
        input=frontmatter[1], text=True, capture_output=True, check=True,
    )
    fields = json.loads(result.stdout)
    name = fields.get("name")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError("Ungültiger Skill-Name im Frontmatter.")
    if len(name) > 64 or name != package_name:
        raise ValueError("Der Skill-Name muss zum Paketordner passen und darf höchstens 64 Zeichen haben.")
    description = fields.get("description")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        raise ValueError("Die Skill-Beschreibung muss ein Text mit 1 bis 1024 Zeichen sein.")


def check_target(root, name, document, directory_allowed=False):
    target = (root / name).resolve()
    if not target.is_relative_to(root) or not (
        target.is_file() or (directory_allowed and target.is_dir())
    ):
        raise ValueError(f"{document}: fehlendes oder ungültiges Ziel {name}")


def check_package(package, repository=None):
    entry = (package / "SKILL.md").read_text(encoding="utf-8")
    check_frontmatter(entry, package.name)
    start_files = re.findall(r"^- `(core/[^/\n`]+\.md)`$", entry, re.MULTILINE)
    expected = {
        "core/plan_core.md", "core/kdm_core.md",
        "core/didaktisches_qualitaetsmodell_core.md", "core/master_agent.md",
    }
    if len(start_files) != len(expected) or set(start_files) != expected:
        raise ValueError("Der SKILL-Einstieg muss die vier Kerndateien einzeln laden.")

    for filename in ["README.md", "LICENSE.md", *sorted(expected)]:
        check_target(package, filename, package / "SKILL.md")

    for document in package.rglob("*.md"):
        contents = document.read_text(encoding="utf-8")
        for name in re.findall(r"`([^ `\n<>]+/[^ `\n<>]+\.md)`", contents):
            if name.startswith(("content/", "project_governance/")):
                if repository is not None:
                    check_target(repository, name, document)
            else:
                check_target(package, name, document)

        for link in re.findall(r"\]\(([^)\s]+)\)", contents):
            uri = urlsplit(link)
            if uri.path and not uri.scheme and not uri.netloc:
                path = (document.parent / unquote(uri.path)).relative_to(package)
                check_target(package, path, document, directory_allowed=True)


if __name__ == "__main__":
    repo = Path(__file__).resolve().parents[1]
    try:
        if len(sys.argv) == 1:
            check_package(repo / ".agents/skills/iwip-planungsagent", repo)
        elif len(sys.argv) == 2:
            check_package(Path(sys.argv[1]).resolve())
        else:
            sys.exit("Aufruf: check_paket.py [entpackter Skill-Ordner]")
    except subprocess.CalledProcessError as error:
        sys.exit(f"Ungültiges Skill-Frontmatter: {error.stderr.strip()}")
    except (OSError, ValueError) as error:
        sys.exit(str(error))
    print("Skill-Frontmatter, Paket und Dateiverweise geprüft.")
