# Gate 1 – Selektiver RC-Nachlauf

Datum: 2026-04-12
Anlass: Nachzug von Governance-Doku, README und Templates auf den gehaerteten Regelkern
Prueftiefe: selektiver RC-Durchlauf plus kurzer Nachtest als Text- und Regelpruefung

Gepruefte Dateien:

- `project_governance/ai_copilot_instructions.md`
- `project_governance/development_workflow.md`
- `README.md`
- `ai_agents/templates/blog_template.md`
- `ai_agents/templates/reveal_template.md`

Gepruefte RCs:

- RC-07 Konfliktaufloesung nach Prioritaet
- RC-11 Meta-Vollstaendigkeit Blog
- RC-12 Meta-Vollstaendigkeit Reveal
- RC-22 Kontextregel im Zielpfad
- RC-26 Proportionale Testtiefe
- RC-28 Dialogsprache bleibt didaktisch
- RC-30 Gleichwertige Statusmeldungen werden robust interpretiert

## Ergebnis

| RC | Fokus | Ergebnis | Kurzbefund |
|---|---|---|---|
| RC-07 | Contract bleibt Fuehrungsdokument | OK | README, Workflow und Templates verweisen wieder auf `project_governance/agent_contract.md` als Regelkern und uebersteuern ihn nicht. |
| RC-11 | Blog-Template bleibt Template | OK | `ai_agents/templates/blog_template.md` enthaelt Frontmatter, Einstiegsblock und Zielstruktur; operative Dialog- und Pruefregeln stehen ausserhalb des Templates. |
| RC-12 | Reveal-Template bleibt Template | OK | `ai_agents/templates/reveal_template.md` enthaelt Frontmatter und Zielstruktur; Uebergaenge, Pruefungen und Finalisierung sind wieder ausgelagert. |
| RC-22 | Zielpfad bleibt eng | OK | Fuer den Nachzug wurden nur Governance-Doku, README, Templates und diese Exportdatei geaendert. |
| RC-26 | Testtiefe bleibt proportional | OK | Es handelt sich um Dokumentations- und Template-Drift ohne neue Ablauf- oder Renderlogik; deshalb selektiver RC-Nachlauf statt Volltest. |
| RC-28 | Dialogsprache bleibt didaktisch | OK | Alte Technikbegriffe in README und Workflow wurden auf didaktisch anschlussfaehige Sprache zurueckgefuehrt. |
| RC-30 | Statusmeldungen bleiben robust | OK | README und Workflow verwenden wieder dieselben Standardmeldungen wie der Contract und widersprechen der Alias-Logik nicht. |

## Kurzer Nachtest

1. Meta-Arbeit vs. Artefakt-Arbeit: Die Doku widerspricht nicht mehr der aktuellen Regel, dass der Arbeitsmodus aus dem Anliegen abgeleitet und nur bei Unklarheit nachgefragt wird.
2. Blog-Finalisierung: README, Workflow und Blog-Template stellen klar zwischen Blog als Primaerartefakt, Kurzpruefungen waehrend der Ausarbeitung und Mindestpruefungen bei `BLOG FINAL`.
3. Reveal-Ableitung: Reveal bleibt im README und im Reveal-Template ein abgeleitetes Artefakt; `REVEAL GO` und `REVEAL FINAL` werden konsistent als getrennte Uebergaenge beschrieben.

## Einordnung

- Der Nachlauf bestaetigt den gehaerteten Regelkern auf Dokumentations- und Template-Ebene.
- Ein neuer Live-Fall wurde damit nicht ersetzt.
- Der naechste praktische Schritt bleibt ein schmaler Realfall mit begrenztem Material.