# Token-Optimierung: Summary des minimalinvasiven Patches (G1-G3)

Datum: 2026-06-04
Umfang: ausschliesslich Umsetzung der Schritte G1 bis G3 aus dem Patch-Plan

## 1) Geaenderte Dateien

1. `prompts/plan.md`
2. `.github/copilot-instructions.md`
3. `project_governance/agent_contract.md`

## 2) Konkrete Aenderungen

### 2.1 `prompts/plan.md`
- Die fruehe `/PLAN`-Pflichtliste unter `Arbeite strikt nach` wurde so angepasst, dass
  - `ai_agents/templates/blog_template.md` nicht mehr im fruehen Pflichtkontext steht,
  - `ai_agents/templates/reveal_template.md` nicht mehr im fruehen Pflichtkontext steht.
- Stattdessen wurde eine explizite Template-Ladelogik eingefuegt:
  - `blog_template.md` erst ab `BLOG GO`
  - `reveal_template.md` erst ab `REVEAL GO`

### 2.2 `.github/copilot-instructions.md`
- Die Governance-Dateien fuer Dev/QA/Architektur wurden aus einer unbedingten Frueh-Leseliste in eine triggerbasierte Regel ueberfuehrt.
- Klarstellung eingefuegt, dass folgende Dateien nur bei Technik-, QA-, FINAL-, Workflow- oder Architekturfragen geladen werden (nicht als frueher Pflichtkontext fuer normale `/PLAN`-Aufgaben):
  - `project_governance/ai_copilot_instructions.md`
  - `project_governance/css_architecture.md`
  - `project_governance/repo_architecture.md`
  - `project_governance/development_workflow.md`

### 2.3 `project_governance/agent_contract.md`
- Im Abschnitt `Normativer Vorrang und Dokumentrollen` wurde eine kurze Klarstellung ergaenzt:
  - Verweise auf Workflow-/Architektur-Governance sind zweckgebunden und kein frueher Pflichtkontext fuer normalen `/PLAN`-Erstzug.
- In der Dokumentrollen-Tabelle wurden on-demand-Kennzeichnungen praezisiert:
  - `ai_agents/blog_wissensbasis.md` als on-demand bei explizitem Blog-/OER-/Wissensbasisbedarf
  - `ai_agents/blog_literaturbasis.md` als on-demand bei Literaturbezug, Quellenpruefung oder wissenschaftlicher Ausarbeitung

## 3) Nicht geaenderte Bereiche

- Keine DQM-Kuerzung (`ai_agents/didaktisches_qualitaetsmodell.md` unveraendert).
- Keine Contract-Modularisierung und kein Prozess-Refactoring.
- Keine Aenderungen an Templates selbst (`ai_agents/templates/blog_template.md`, `ai_agents/templates/reveal_template.md` unveraendert).
- Keine inhaltliche Aenderung an Wissensbasis oder Literaturbasis (`ai_agents/blog_wissensbasis.md`, `ai_agents/blog_literaturbasis.md` unveraendert).
- Keine Aenderungen an:
  - `project_governance/development_workflow.md`
  - `project_governance/repo_architecture.md`
  - `project_governance/css_architecture.md`

## 4) Erwartete Wirkung

- Reduktion unnoetiger Fruehladung in `/PLAN`-Erstzuegen.
- Klarere Triggerdisziplin:
  - Templates erst an den zugehoerigen GO-Gates,
  - Wissens-/Literaturbasis on-demand,
  - Dev/QA/Architektur-Governance nur bei passendem Kontext.
- Erhalt der bestehenden didaktisch-normativen Kernlogik (Contract/DQM unveraendert).

## 5) Moegliche Risiken

- Trigger koennen in Grenzfaellen zu spaet greifen (z. B. frueher Bedarf an Literaturbezug in atypischen Planungsdialogen).
- Unterschiedliche Interpretation von "Technik-/QA-/FINAL-/Workflow-/Architekturfrage" kann zu inkonsistenter Nachladung fuehren.
- Bei fehlender Triggerdisziplin kann es trotz Regeltext zu gelegentlicher Fruehladung kommen.

## 6) Empfohlene Testfaelle

1. `/PLAN` Standardfall: keine fruehe Template-Ladung, keine fruehe Dev/QA/Architektur-Governance.
2. `/PLAN FORSCHUNG`: unveraenderte Contract-Initialisierung, weiterhin ohne fruehe Template-Ladung.
3. `/PLAN` mit frueher Blog-Produktionsabsicht, aber ohne `BLOG GO`: Templates bleiben noch ungeladen.
4. `BLOG GO`: `blog_template.md` wird dann beruecksichtigt.
5. `REVEAL GO`: `reveal_template.md` wird dann beruecksichtigt.
6. `BLOG FINAL` und `REVEAL FINAL`: QA-/FINAL-bezogene Governance-Dateien werden bei Bedarf weiterhin beruecksichtigt.
7. Literatur-/Quellenlastiger Fall: `blog_literaturbasis.md` wird on-demand korrekt einbezogen.
8. Wissensbasis-Anschluss nach `BLOG FINAL`: `blog_wissensbasis.md` wird on-demand korrekt einbezogen.
