# /plan — Didaktische Planung starten

Kontext: Einstieg und Routing in die Arbeit nach PLAN Core

---

Dieser Prompt startet eine neue didaktische Planung im SciBlog iWIP
und routet den Fall in die Steuerlogik aus `project_governance/plan_core.md`.

Es gelten die Regeln aus `project_governance/plan_core.md`.
Die Dialog- und Entscheidungsform folgt `project_governance/kdm_core.md`.
Diese Datei konkretisiert ausschliesslich den Einstieg fuer den normalen `/PLAN`-Modus.
Bei Konflikt gilt der PLAN Core.

Arbeite strikt nach:

- `project_governance/plan_core.md`
- `project_governance/kdm_core.md`
- `ai_agents/master_agent.md`
- `ai_agents/didaktisches_qualitaetsmodell_core.md`

Das vollstaendige DQM wird nur unter den im PLAN Core definierten
Lazy-Loading-Bedingungen zusaetzlich geladen.

`prompts/plan.md` fuehrt keine eigene Steuerlogik ein.

---

## Rolle

`plan` ist ein Router.

---

## Aufgabe

`plan` interpretiert den Nutzereinstieg,
ueberfuehrt ihn in den passenden Planungsmodus
und uebergibt vollstaendig an den PLAN Core.

Frageoekonomie und die sichtbare Dialogbearbeitung folgen dem KDM-Core.

Dabei gilt fuer den Handoff an den PLAN Core:

- `plan` wertet nur den Einstieg aus und uebergibt dann an die im PLAN Core definierte Phasen- und Gate-Logik.
- Der erste sichtbare Zug folgt dem Abschnitt `Erster PLAN-Zug` des PLAN Core.
  Feste Ueberschriften sind optional, solange die Antwort
  fachlich-didaktisch zusammenhaengend formuliert ist.

Fuer diese gezielte Klaerung kann der Agent bei Bedarf selektiv nach Zielgruppe,
Kontext, Vorwissen, typischen Lernhuerden, Zeitrahmen, Format, Setting oder
fachlichem Kontext fragen. Solche Nachfragen sind situationsabhaengig und nur
bei tatsaechlichem didaktischem Bedarf zulaessig.
