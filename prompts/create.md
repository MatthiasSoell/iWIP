# /create — Didaktische Planung starten

Version: 1.1.0
Status: Start- und Router-Prompt
Kontext: Einstieg und Routing in die Arbeit nach Contract

---

Dieser Prompt startet eine neue didaktische Planung im SciBlog iWIP
und routet den Fall in die Steuerlogik aus `project_governance/agent_contract.md`.

Arbeite strikt nach:

- `project_governance/agent_contract.md`
- `ai_agents/master_agent.md`
- `ai_agents/didaktisches_qualitaetsmodell.md`
- `ai_agents/templates/blog_template.md`
- `ai_agents/templates/reveal_template.md`

`prompts/create.md` fuehrt keine eigene Steuerlogik ein.

---

## Rolle

`create` ist ein Router.

---

## Aufgabe

`create` interpretiert den Nutzereinstieg,
ueberfuehrt ihn in den passenden Arbeitsmodus
und uebergibt vollstaendig an den Contract.

Dabei gilt fuer den Handoff an den Contract:

- In `P1` und `P2` bleibt `create` strikt im Planungsmodus; es werden keine publizierbaren Blog- oder Reveal-Passagen vorweggenommen.
- Der Uebergang in `P3` erzeugt erst dann `blog_snapshot.txt` und `index.md`, wenn Planungslogik in Artefaktsprache ueberfuehrt werden kann.
- Der Uebergang in die Reveal-Arbeit nutzt ausschliesslich das finale Blog-`index.md`; Planungsnotizen, Fruehfassungen und Snapshots werden nicht direkt transformiert.

---

## WICHTIG

Keine eigene Steuerlogik.

Aktiver Editorpfad, geoeffnete oder markierte Prompt- oder Regeldateien, aktive Textauswahlen oder sonstiger Editor-Kontext steuern den Arbeitsmodus nicht.