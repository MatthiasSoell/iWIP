# Bisy Dry Run – Gate 1

Datum: 2026-04-11
Fall: Einfuehrungsveranstaltung Modul Bildungssysteme
Typ: geschlossener Repo-Fall gegen den gehaerteten Gate-1-Regelstand

## Grundlage

Ausgewertet wurden:

- exports/chatverlauf_bisy_agent_2026-04-10.md
- content/blog/lehre/bisy/einfuehrung/einfuehrung_ursprung_agent.txt
- content/blog/lehre/bisy/einfuehrung/index.md
- content/praesentation/lehre/bisy/einfuehrung/Ursprungs _index des Agenten.txt
- content/praesentation/lehre/bisy/einfuehrung/_index.md
- project_governance/agent_contract.md
- ai_agents/master_agent.md
- prompts/create.md
- prompts/check.md
- project_governance/development_workflow.md

## Prueftabelle

| Station | Pruefschritt | Status | Kurzbefund | Folgeort |
|---|---|---|---|---|
| Meta-Arbeit am Agenten | Keine Artefakterstellung | OK | Meta-Arbeit blieb artefaktfrei. | — |
| Meta-Arbeit am Agenten | Sprache bleibt meta- und reviewgerecht | Teilweise | Historischer Fall war stark prozessgetrieben formuliert. | master_agent.md |
| BLOG FINAL | Kontextluecken fuehren zu genau einer Rueckfrage | Teilweise | Rueckfragen erfolgten, aber nicht immer im jetzt geforderten engen Signalraster. | prompts/create.md |
| BLOG FINAL | Profilsteuerung A/B/C ist sichtbar korrekt | Nein | Im historischen Fall nicht explizit dokumentiert. | prompts/create.md, prompts/check.md |
| BLOG FINAL | Blog-first und Gate-Disziplin bleiben intakt | Teilweise | Blog-first war intakt, Blog-Finalsignal aber nicht sichtbar genug. | master_agent.md |
| BLOG FINAL | Dialogstil bleibt didaktisch und adressatenorientiert | Teilweise | Fachlich brauchbar, aber noch zu stark prozessprotokollartig. | master_agent.md |
| BLOG FINAL | Uploads werden nur als Quellmaterial behandelt | OK | Uploads wurden analysiert, nicht implizit finalisiert. | — |
| BLOG FINAL | Hardchecks und Summary-Block greifen korrekt | Teilweise | Frontmatter/Quellen okay, DQM-Bericht und Summary-Block historisch nicht sichtbar. | master_agent.md, prompts/check.md |
| REVEAL GO -> REVEAL FINAL | Reveal startet erst nach Gate/Freigabe | OK | Reveal startete nicht parallel zum Blog. | — |
| REVEAL GO -> REVEAL FINAL | Alias-Signale werden korrekt interpretiert | OK | Umgangssprachliche Startsignale wurden funktional richtig gedeutet. | — |
| REVEAL GO -> REVEAL FINAL | Snapshot- und Bundle-Hygiene bleiben sauber | OK | Snapshot-Logik und Bundle-Hygiene sind im gehaerteten Stand sauber. | — |
| REVEAL GO -> REVEAL FINAL | Delta-Check, Asset-Inventar und Finalisierung stimmen | Teilweise | Historischer Fall dokumentierte diese Outputs nicht sichtbar. | master_agent.md, prompts/check.md |

## Hauptbefunde

1. Blog-first, Snapshot-Logik und Upload-Behandlung sind tragfaehig.
2. Die fruehere Hauptluecke lag nicht in der Artefaktlogik, sondern in der Sichtbarkeit verpflichtender Finalisierungsoutputs.
3. Profilsteuerung A/B/C musste im Start- und Check-Prompt expliziter gemacht werden.
4. Didaktischer Dialogstil musste gegen reines Prozessprotokoll geschaerft werden.

## Nachgezogene Haertung am 2026-04-11

Zur Schliessung der im Dry Run sichtbaren Restluecken wurden nachgezogen:

- ai_agents/master_agent.md
  - DQM-Pruefbericht vor BLOG FINAL sichtbar verpflichtend
  - Delta-Check vor REVEAL FINAL sichtbar verpflichtend
  - Asset-Inventar vor REVEAL FINAL sichtbar verpflichtend
  - Summary-Block bei Finalisierungen sichtbar verpflichtend
- prompts/create.md
  - Profil A/B/C als explizite Pflichtklaerung vor Planungsstart
  - Default A nur noch sichtbar benannt
- prompts/check.md
  - fehlende sichtbare Profilklaerung wird vor Finalbewertung zum Pflichtpunkt
  - sichtbare Ausgabe-Reihenfolge fuer BLOG FINAL und REVEAL FINAL festgezogen

## Gate-1-Verdikt

Gate 1 gilt nach den Nachhaertungen vom 2026-04-11 als geschlossen.

Begruendung:

- Kernlogik zwischen Contract, Master-Agent, Create, Check, Templates, Workflow und README ist synchronisiert.
- Testlogik ist proportional und in ai_copilot_instructions.md sowie development_workflow.md konsistent beschrieben.
- Template-Drift ist reduziert; operative Regeln liegen wieder primaer in Contract, Master-Agent und Check.
- Ein dokumentierter Dry Run auf Basis des Bisy-Falls liegt vor.

## Naechster Schritt

Ein schmaler neuer Realfall mit begrenztem Material kann jetzt als erster echter Gate-1-Nachtest genutzt werden.
