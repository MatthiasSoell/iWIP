# Baseline B0 – aktueller iWIP-Agent in Codex VS Code

## Laufkontext

- Datum: 2026-09-01
- Plattform: Codex VS Code
- Modell: `gpt-5.6-sol`
- Reasoning: `low`
- Codex-Version: `0.151.0-alpha.7.2`
- Test: H01, fünf Dialogzüge
- Repository: `/Users/matthias/Documents/GitHub/iWIP`
- Agent: unveränderte bestehende Agentendateien, aktiviert über den dünnen
  `AGENTS.md`-Adapter

## Ergebnis

Alle fünf Dialogzüge bestanden.

| Zug | Auftragstreue | Qualität | Drift | Befund |
|---|---:|---:|---:|---|
| H01.1 | 3/3 | 15/15 | 0 | genau drei priorisierte Spannungen |
| H01.2 | 3/3 | 15/15 | 0 | genau zwei begründete Zuspitzungen |
| H01.3 | 3/3 | 15/15 | 0 | erste Variante erhalten, exakt 90 Minuten |
| H01.4 | 3/3 | 15/15 | 0 | nur Arbeitsaufträge geändert |
| H01.5 | 3/3 | 15/15 | 0 | valides fragmentfähiges HTML im Chat |

Gesamter Drift-Index: **0**. Es wurden keine unnötigen Rückfragen gestellt. Die
gesetzte didaktische Grundentscheidung blieb über alle Folgezüge stabil.

## Ressourcen

Lokale Codex-Sitzung:

`/Users/matthias/.codex/sessions/2026/09/01/rollout-2026-09-01T21-54-55-01a05e89-f672-7ac1-8688-ff59d42531de.jsonl`

Kumulierte Werte des vollständigen Laufs:

| Messwert | Wert |
|---|---:|
| Eingabetokens | 229.974 |
| davon gecachte Eingabetokens | 198.912 |
| Ausgabetokens | 4.234 |
| Reasoning-Tokens | 780 |
| Gesamttokens | 234.208 |
| Modellantworten/Tokenereignisse | 7 |

Die verstrichene Sitzungszeit von etwa 7 Minuten 42 Sekunden enthält menschliche
Pausen und ist daher keine reine Modelllaufzeit.

## Technische Prüfung

- Der Rohoutput von H01.5 enthält unmaskiertes, valides HTML.
- Backslashes und `&#x20;` entstanden erst durch das Einfügen in eine andere
  Chatoberfläche und gehören nicht zum Codex-Rohoutput.
- Codex veränderte während des Benchmarklaufs keine Repository-Datei.
- Das vollständige Rohtranskript wird nicht in Git kopiert; sein lokaler Pfad ist
  oben dokumentiert.

## Ausgangshypothese für die Optimierung

Die inhaltliche Qualität und Driftkontrolle sind in diesem Fall bereits sehr hoch.
Der klare Optimierungsbedarf liegt beim Kontextverbrauch: Jeder Folgezug führt einen
großen Eingabekontext mit. Die nächste Version sollte deshalb die didaktische
Qualität und Entscheidungsstabilität erhalten, aber Regeln und Wissensmodule
bedarfsgerecht statt vollständig laden.

