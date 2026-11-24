# iWIP Benchmark-Suite

Diese README ist die verbindliche Anleitung für `benchmark-v1.0`. Die Suite
prüft sichtbare wirtschaftsdidaktische Planungsunterstützung und sichert
Änderungen am iWIP-Planungsagenten durch gezielte Regressionen ab.

## 1. Benchmark auswählen

| Fallversion | Schwerpunkt und Einsatz | Testmaterial | Bewertung |
|---|---|---|---|
| `H01@1.0` | Nachhaltigkeit und Bildung, 90 Minuten Hochschullehre. Diagnose, begrenzte Anpassung und itslearning-HTML. Regression für begrenzte Überarbeitung und HTML-Ausgabe. | [Kontext](inputs/H01_AGENT_INPUT.md), [5 Züge](inputs/H01_DIALOG.md) | [Erwartungen](evaluations/H01_EXPECTED.md) |
| `H02@1.0` | Digitalisierung beruflicher Arbeit, Hochschullehre. Prozessregression für Kontinuität und ausdrückliche Revision in einer Sitzung. | [Kontext](inputs/H02_AGENT_INPUT.md), [8 Züge](inputs/H02_DIALOG.md) | [Solltabelle](evaluations/H02_EXPECTED.md) |
| `H03@1.0` | Feedback in der betrieblichen Ausbildung, Hochschullehre. iWIP-Prozessregression für Journalführung und Sitzungswechsel. | [Kontext](inputs/H03_AGENT_INPUT.md), [6 + 3 Züge](inputs/H03_DIALOG.md) | [Protokoll](evaluations/H03_EXPECTED.md), [Journalsoll](fixtures/H03_JOURNAL_CHECKPOINTS.md) |
| `H04@1.0` | Lieferantenauswahl, Ausbildung Industriekaufleute. Kalibrierung für Diagnose und Urteilsbegründung sowie für Präferenzen, Revision und Herkunft von Entscheidungen. | [Kontext](inputs/H04/H04_AGENT_INPUT.md), [7 Züge](inputs/H04/H04_DIALOG.md) | [Rubrik](evaluations/H04/H04_EXPECTED.md), [Bewertungsauftrag](evaluations/H04/H04_EVALUATION_PROMPT.md) |
| `H07@1.0` | Mindestlohn, Ausbildung Industriekaufleute. Pilot für Zielklärung und Reflexionsunterstützung einer weniger erfahrenen Lehrperson. Dialogbefund separat. | [Kontext](inputs/H07/H07_AGENT_INPUT.md), [7 Züge](inputs/H07/H07_DIALOG.md) | [Erwartungen](evaluations/H07/H07_EXPECTED.md), [Rubrik](evaluations/H07/H07_EVALUATION_PROMPT.md) |
| `H08@1.0` | Unternehmerische Standortentscheidung, fortgeschrittene Lernende. Robustheit gegenüber schrittweise offengelegten Ziel-Mittel-Spannungen. Revision separat. | [Kontext](inputs/H08/H08_AGENT_INPUT.md), [7 Züge](inputs/H08/H08_DIALOG.md) | [Erwartungen](evaluations/H08/H08_EXPECTED.md), [Rubrik](evaluations/H08/H08_EVALUATION_PROMPT.md) |

| Prüfumfang | Auswahl |
|---|---|
| **Kleine Regression** | Nur den betroffenen Fall oder Abschnitt mit dem vorgesehenen Vorlauf prüfen. Beispiele sind H04.1–.3 für Diagnose und Präferenzen oder H03.A1–A3 für die erste Journalanlage. Für H03.B stets den Vorlauf A1–A6 durchführen. Teilläufe im Protokoll kennzeichnen. |
| **Mittlere Regression** | Bei Änderungen an mehreren zusammenhängenden Verhaltensregeln die einschlägigen Fälle vollständig fahren. H04 für Diagnose und Entscheidungskontinuität, H03 A+B für Journal und Wiederaufnahme, H02 für Revision innerhalb einer Sitzung und H01 für begrenzte Überarbeitung oder Chat-HTML auswählen. |
| **Umfassende Regression** | Bei Änderungen am Zusammenspiel von Planungsheuristik, Dialogsteuerung und Fallzustand H02, H03 A+B und H04 vollständig fahren. H01 bei betroffener HTML-Übergabe ergänzen. H07 oder H08 ergänzen, wenn sich Zielklärung, Reflexionsunterstützung oder der Umgang mit Ziel-Mittel-Spannungen ändern. |
| **Wissenschaftlicher Vergleich** | H04 zur Bewertungskalibrierung, H07 für den Pilot zur Zielklärung und H08 für standardisierte Robustheitsbeobachtungen verwenden. H03 prüft den iWIP-Journalvertrag separat. |

Technische Publikations- und Integrationstests prüfen Freigabe, Blog/Reveal,
Build oder Deployment. Dafür gelten die gezielten Prüfungen im
[Entwicklungsworkflow](../../project_governance/development_workflow.md#43-agenten-validierung)
und sein [Stationsbogen](../../project_governance/development_workflow.md#45-dry-run-auswertungsvorlage).

## 2. Test vorbereiten

1. Suite, Fall- und Rubrikfassung, Benchmark-Commit, Agenten-Commit oder
   Konfigurationsversion, Plattform, genaues Modell, Reasoning-Level und
   erlaubte Werkzeuge festhalten. Die reguläre native Agentenkonfiguration
   gehört zur jeweiligen Testbedingung. Eine Standard-ChatGPT-Bedingung
   verwendet keine zusätzliche Agentenkonfiguration.
2. Eine frische Sitzung ohne Memory, frühere Testdialoge oder Zusatzhinweise
   öffnen. Bei Dateizugriff einen isolierten Arbeitsbereich mit den erlaubten
   Eingaben und Laufzeitdateien verwenden. Bewertungsdateien, Sollstände und
   frühere Läufe für den getesteten Agenten unzugänglich halten. Den
   Benchmarkordner daher weder anhängen noch als Arbeitsbereich öffnen.
3. H01/H02 erhalten die Falltextdatei am im ersten Zug genannten relativen
   Pfad. Bei H04/H07/H08 den Falltext und Zug 1 gemeinsam als erste Nachricht
   senden. Für H03 den Falltext mit A1 senden und vorher den leeren, bestätigten
   und beschreibbaren Fallordner gemäß [H03-Dialog](inputs/H03_DIALOG.md)
   vorbereiten. Die Snapshot-Ablage gemäß
   [H03-Protokoll](evaluations/H03_EXPECTED.md) liegt außerhalb des Fallordners.

## 3. Dialog durchführen

- Jeden Nutzerzug wortgetreu und einzeln senden. Turnüberschriften und
  Durchführungshinweise bleiben bei der testleitenden Person. Nur vorgesehene
  Platzhalter ersetzen. Bei H01/H02 meint die Annahme der ersten Variante die
  tatsächlich zuerst angebotene Option.
- Nach jeder Antwort mit dem nächsten Skriptzug fortfahren. Auf Rückfragen
  keine zusätzlichen Angaben geben und keine Zwischenkorrekturen vornehmen.
  Ist ein Folgeturn technisch oder sachlich unmöglich, Ursache und letzten
  gültigen Zug festhalten.
- Den vollständigen sichtbaren Dialog einschließlich Prozessmeldungen sichern.
  Beobachtbare Tool- und Dateiaktionen separat dokumentieren. Bei H03 nach
  jeder Agentenantwort den Snapshot vor dem nächsten Nutzerzug sichern. Nach
  A6 Sitzung B mit derselben Agentenkonfiguration und demselben Fallordner
  frisch öffnen. B hat keinen Zugriff auf den Dialog aus A.
- Zugriff auf Bewertungsmaterial als Protokollverletzung erfassen. Den
  kontaminierten Lauf dokumentieren und aus dem Vergleich ausschließen.

## 4. Ergebnisse bewerten

Erst nach Abschluss des Dialogs den Erwartungshorizont bzw. die Rubrik der
gewählten Fassung verwenden. Pro Kriterium Beobachtung und Belegstelle
festhalten, dann den Rubrikwert oder Status vergeben. Didaktik,
Dialogzuverlässigkeit und Aufwand nach der jeweiligen Rubrik berichten.
Datei- und Toolbefunde separat ausweisen. Eine Abweichung nur dem unmittelbar
betroffenen Kriterium zuordnen. Kritische Fehler und Drift gemäß Fallrubrik
dokumentieren. Fehlende Beobachtungsgrundlagen kennzeichnen, statt ein
vollständiges Profil zu bilden. Eine ausgebliebene Leistung im vollständig
vorliegenden Zug nach Rubrik bewerten.

Bewerte den sichtbaren Beitrag des Agenten. Fachlich gleichwertige Lösungen
können dieselbe Bewertung erhalten. Skriptierte Lehrerrevisionen belegen nur,
wie der Agent sie verarbeitet. Selbstbewertungen sind Begleitbefunde.
Für Systemvergleiche unveränderte Rohdialoge behalten und komplette,
anonymisierte Dialoge in gemischter Reihenfolge bewerten lassen. Zwei
unabhängige Fachbewertungen im Pilot kalibrieren und Einzelbewertungen
vom späteren Konsens unterscheidbar halten.

### Laufprotokoll zum Kopieren

```text
Suite / Fallversion / Rubrikfassung / Benchmark-Commit:
Agent / Git-Commit oder Konfigurationsversion / lokale Abweichungen:
Datum mit Zeitzone / Wiederholungsnummer:
Plattform / Modell / Reasoning-Level:
Testbedingungen (Prüfumfang, Werkzeuge, bereitgestellter Kontext):
Gesendete Eingaben / Rohdialog / ggf. H03-Snapshots:
Je Dimension: Kriterium / Turn oder Datei / Beobachtung / Bewertung / Begründung:
Technische Befunde und Status:
Kritische Abweichungen / Drift / unnötige Rückfragen / Abbruchgrund:
Gesamteinschätzung und Einschränkungen:
Optional: Laufzeit / Modellaufrufe / verfügbare Usage-Werte:
```

Technische Prüfungen als `bestanden`, `fehlgeschlagen`, `nicht ausgeführt`
oder `abgebrochen` ausweisen. Optionale Aufwandsdaten nur berichten, wenn
sie für dieselbe Laufgrenze vorliegen. Cached und uncached Input getrennt
erfassen, wenn die Plattform beide Werte ausweist.

## 5. Ergebnisse vergleichen

- Werte direkt nur innerhalb derselben Benchmark-, Fall- und Rubrikfassung
  vergleichen. Für Agentenvergleiche möglichst Basismodell, Reasoning-Level
  und Werkzeuge angleichen. Abweichende Modelle, Plattformen und
  Werkzeugzugänge berücksichtigen. Bei unterschiedlichen Bedingungen beschreiben
  die Ergebnisse die getesteten Gesamtsysteme. Über Fälle hinweg anhand von
  Dimensionsprofilen und Belegen vergleichen.
- Ein gültiger Lauf je Fall genügt für eine erste Regression. Bei einem
  unerwarteten, nichtkritischen Befund unter gleichen Bedingungen wiederholen
  und beide Befunde behalten. Einzelne Schwankungen sind kein belastbarer
  Nachweis einer Qualitätsveränderung. Für einen wissenschaftlichen Pilot mit
  zwei bis drei unabhängigen Läufen je Fall und Bedingung beginnen.
  Einzelwerte, Streuung und Bewertungsdifferenzen berichten. Stichprobengröße
  und Bewertungsübereinstimmung für die Hauptuntersuchung separat planen.
- Die öffentlichen Fälle erfassen sichtbare Unterstützung in standardisierten
  Situationen. Nahe der Höchstwertung können Unterschiede zwischen starken
  Systemen schwer erkennbar sein. Ergebnisse zu realer Unterrichtswirkung,
  Professionalisierung oder Adaptivität über verschiedene Expertisen hinweg
  benötigen eigene Untersuchungen. Zurückgehaltene Fälle getrennt verwahren.

## Versionierung und Ablage

- `inputs/` enthält ausschließlich Eingabematerial für die Testleitung.
  `evaluations/` und `fixtures/` enthalten Rubriken, Bewertungsaufträge und
  Sollstände. Rohdialoge und Laufdateien in einem separaten lokalen
  Laufordner ablegen, beispielsweise unter
  `iwip_planungsagent/entwicklung/benchmark_runs/`. Private Forschungsdaten
  zugriffsgeschützt außerhalb öffentlicher Git- und Hugo-Pfade speichern.
- Beim Einfrieren bindet `benchmark-v1.0` den genauen Suite-Commit
  einschließlich Rubriken, Durchführungsvorgaben und H03-Prüfer. Für die
  vorliegende Fassung bezeichnet `1.0` auch die jeweilige Fallrubrik bzw. den
  Fallsollstand. Jede Änderung an Aufgaben, Bewertung oder Ausführung nach
  dem Freeze erhält eine neue dokumentierte Fassung.
- Frühere Ergebnisse behalten ihre ursprüngliche Fall- und Rubrikfassung.
  Eine Neubewertung unveränderter Rohdialoge ist eine eigene Auswertung.
  Ältere versionierte Teststände und Herkunftshinweise bleiben in Git
  nachvollziehbar.
