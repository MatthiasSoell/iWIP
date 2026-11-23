# Benchmark

Dieser Bereich enthaelt die aktuellen manuellen Regressionstests fuer den
didaktischen Planungsagenten. Die Testdefinitionen sind oeffentlich versioniert;
konkrete Testlaeufe und Rohoutputs bleiben lokal.

## Bestand

- `inputs/`: Fallkontexte und Dialogskripte fuer H01 bis H04
- `evaluations/`: vorhandene Erwartungshorizonte; derzeit H01
- `inputs/H04/`: H04 enthält zusätzlich Rubrik und Bewertungsauftrag. Im Test nur Falltext und einzelne Dialogzüge bereitstellen.
- `historie/`: archivierter Entwicklungsdiff (kein Laufzeitkontext)
- `fixtures/`: versionierte Sollzustaende; derzeit das erwartete H03-Planning-Journal

Die Dialogtests werden derzeit manuell durchgefuehrt. Ein automatischer Runner
oder ein Benchmark-Harness ist nicht vorhanden. Erwartungen duerfen waehrend
eines Testlaufs nicht als Agentenkontext verwendet werden.

Laufartefakte, Transkripte und Rohdaten gehoeren nach
`agent_entwicklung/benchmark_runs/`. Dieser lokale, ignorierte Bereich ist keine
normative Quelle fuer den aktuellen Agenten. Das gilt ebenso fuer historische
Runs; massgeblich sind die aktuellen Agentenregeln und die hier versionierten
Testdefinitionen.

## Prüfstand der Skill-Migration

Basis ist `d75d303`. Die Migration konsolidiert den Skill und verlegt die
technische Abfolge der FINAL-Prüfungen in den Publikationsbereich. KDM, DQM
und Master-Agent sind bis auf die Pfade textgleich. Die Abschnitte zu Planning
State und Journal sind bytegleich. Der lokale, ignorierte Ordner
`agent_entwicklung/` behält seinen Pfad, damit vorhandene Journale und
Testläufe erreichbar bleiben.

| Prüfung | Ergebnis |
| --- | --- |
| `make qa` | Vor und nach dem Umbau erfolgreich. Markdownlint und Hugo-HTML-Build bestanden. |
| Paketprüfung | Skill-Frontmatter und die vier Startdateien geprüft. Dateiverweise im Repo und im separat entpackten Paket aufgelöst. Das Entfernen einer Kerndatei wurde erkannt. |
| H04 | Je sieben Dialogzüge auf dem Ausgangsstand und mit dem separat kopierten Skill. Beide Läufe übernahmen die ausdrückliche Revision. Im portablen Lauf legte der PLAN-Dialog keine Dateien an. Eine Zeitverteilung wurde erst in der Abschlussantwort ausdrücklich als Agentenvorschlag gekennzeichnet. |
| H03 | Sitzung A belegt. A1 und A2 erzeugten keine Datei. A3 legte das Journal an, A4 und A5 ließen es unverändert, A6 dokumentierte die Revision. Für Sitzung B liegt kein abgeschlossener Lauf vor. |
| Links | Bisher öffentlich verlinkte GitHub-Pfade und ihre neuen Ziele wurden lokal geprüft. Lychee im Offline-Modus fand im reinen HTML-Build einen fehlenden Reveal-PDF-Export. Dieser Export ist ein separater Schritt im vorhandenen Workflow. |
| Produktion und Plattformen | Blog- und Reveal-HTML wurden gerendert. Die vollständige Gatefolge und die native Erkennung in der Codex-Oberfläche sind offen. Der Publikationslauf wurde durch das Nutzungslimit unterbrochen. |

Die Benchmarks wurden für die Übergabe nicht erneut ausgeführt.
