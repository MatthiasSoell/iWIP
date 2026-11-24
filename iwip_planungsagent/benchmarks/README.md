# iWIP Benchmark-Suite

**Referenzfassung `benchmark-v1.0`.** Die Suite prüft, wie KI-Systeme Lehrpersonen
bei wirtschaftsdidaktischen Planungsentscheidungen unterstützen, und sichert
die Weiterentwicklung des iWIP-Planungsagenten ab. Sie richtet sich an
Lehrende, Forschende und Maintainer. Für jeden Lauf gelten die Falltexte,
Dialoge und Bewertungsregeln der gewählten Benchmarkfassung.

## Testbereiche und Fälle

- **A · Didaktische Qualität.** Fachliche Diagnose, Ziel-Mittel-Passung,
  funktionale Unterstützung, ökonomische Begründung und Reflexion.
  Dialogqualität und Lehrerautonomie werden zusätzlich ausgewiesen.
  Die Aufgaben funktionieren mit und ohne spezialisierte Agentenkonfiguration.
- **B · Prozess- und Dialogzuverlässigkeit.** Beobachtbare Auftragsdisziplin,
  Entscheidungskontinuität, Revision und bei iWIP auch Journal, Wiederaufnahme
  und freigegebener Übergabestand.
- **C · Publikation und Integration.** Freigabe, Übergabe, Blog- und Reveal-Gates
  sowie technische Prüfung bis zum Deployment. Mechanisch prüfbare Eigenschaften
  werden mit vorhandenen Skripten geprüft.

| Fallversion | Schwerpunkt und Einsatz | Testmaterial | Bewertung |
|---|---|---|---|
| `H01@1.0` | Nachhaltigkeit und Bildung, 90 Minuten Hochschullehre. Diagnose, begrenzte Anpassung und itslearning-HTML. Historischer Regressionstest für einschlägige Änderungen. | [Kontext](inputs/H01_AGENT_INPUT.md), [5 Züge](inputs/H01_DIALOG.md) | [Erwartungen](evaluations/H01_EXPECTED.md) |
| `H02@1.0` | Digitalisierung beruflicher Arbeit, Hochschullehre. B für Kontinuität und ausdrückliche Revision in einer Sitzung. | [Kontext](inputs/H02_AGENT_INPUT.md), [8 Züge](inputs/H02_DIALOG.md) | [Solltabelle](evaluations/H02_EXPECTED.md) |
| `H03@1.0` | Feedback in der betrieblichen Ausbildung, Hochschullehre. B für standardmäßige Journalführung und Wiederaufnahme. | [Kontext](inputs/H03_AGENT_INPUT.md), [6 + 3 Züge](inputs/H03_DIALOG.md) | [Protokoll](evaluations/H03_EXPECTED.md), [Journalsoll](fixtures/H03_JOURNAL_CHECKPOINTS.md) |
| `H04@1.0` | Lieferantenauswahl, Ausbildung Industriekaufleute. A für Diagnose, Intervention und Urteilsbegründung. B für Präferenzen, Revision und Herkunft von Entscheidungen. | [Kontext](inputs/H04/H04_AGENT_INPUT.md), [7 Züge](inputs/H04/H04_DIALOG.md) | [Rubrik](evaluations/H04/H04_EXPECTED.md), [Bewertungsauftrag](evaluations/H04/H04_EVALUATION_PROMPT.md) |
| `H07@1.0` | Mindestlohn, Ausbildung Industriekaufleute. Pilot für Zielklärung und Reflexionsunterstützung einer weniger erfahrenen Lehrperson. Dialogbefund separat. | [Kontext](inputs/H07/H07_AGENT_INPUT.md), [7 Züge](inputs/H07/H07_DIALOG.md) | [Erwartungen](evaluations/H07/H07_EXPECTED.md), [Rubrik](evaluations/H07/H07_EVALUATION_PROMPT.md) |
| `H08@1.0` | Unternehmerische Standortentscheidung, fortgeschrittene Lernende. Gefrorener A-Fall für Reaktionen auf sichtbar werdende Ziel-Mittel-Spannungen. Revision separat. | [Kontext](inputs/H08/H08_AGENT_INPUT.md), [7 Züge](inputs/H08/H08_DIALOG.md) | [Erwartungen](evaluations/H08/H08_EXPECTED.md), [Rubrik](evaluations/H08/H08_EVALUATION_PROMPT.md) |

H04, H07 und H08 decken verschiedene Situationen ab. H04 eignet sich als
Kalibrierungsfall, H07 als Pilotfall und H08 als standardisierter
Robustheitsfall. Sie sind bekannte Fälle. Eine unabhängige Forschungsevaluation
kann zusätzlich zurückgehaltene Fälle mit getrenntem Zugriffsbereich verwenden.

## Einen Dialoglauf durchführen

1. Fallversion, Prüfumfang, geprüfte Konfiguration und Laufzeitbedingungen
   vorab festlegen. Eine frische Sitzung ohne frühere Testdialoge, Memory,
   Zusatzhinweise oder fremde Wissensbasis öffnen. Die reguläre
   Agentenkonfiguration gehört zur definierten Testbedingung.
2. Nur die Modellkonfiguration und den für den aktuellen Zug erlaubten
   Input zugänglich machen. Für H04, H07 und H08 den Falltext mit Zug 1
   als erste Nachricht senden. Für H01 und H02 die im Skript benannte
   Falltextdatei am angegebenen Pfad bereitstellen. Für H03 den Falltext
   mit A1 senden und den beschriebenen frischen Fallordner einsetzen.
   Bei Zugriff auf Dateien ein Testverzeichnis verwenden, das nur die
   erlaubten Eingaben und benötigte Laufzeitdateien enthält. Den ganzen
   Benchmarkordner weder anhängen noch als durchsuchbaren Kontext öffnen.
3. Die Nutzerzüge wortgetreu einzeln nach der jeweiligen Antwort senden.
   Die Bezeichnungen und Hinweise oberhalb der Züge dienen der Durchführung.
   Nur ausdrücklich vorgesehene Platzhalter ersetzen. Bei H01 und H02
   bezieht sich „erste Variante“ auf die tatsächlich angebotene Option.
   Keine Zwischenkorrekturen oder adaptiven Antworten auf Rückfragen.
   Ist ein Folgeturn technisch oder sachlich nicht mehr durchführbar,
   den Abbruch mit Ursache und letztem gültigem Turn protokollieren.
4. Den vollständigen sichtbaren Dialog, einschließlich sichtbarer
   Prozessmeldungen, sichern. Bei B und C beobachtbare Datei- und Toolereignisse
   separat erfassen. Für H03 nach jedem Zug die vorgesehenen Dateisnapshots
   sichern. Unzulässigen Zugriff auf Bewertungsmaterial als
   Protokollverletzung vermerken. Einen kontaminierten Lauf aus dem Vergleich
   ausschließen und im Laufprotokoll behalten.
5. Erst nach dem Dialog bewerten. Für Systemvergleiche Rohdialoge als
   unveränderte lokale Originale behalten und anonymisierte Bewertungskopien
   erstellen. Antworten derselben gültigen Testfassung in gemischter
   Reihenfolge bewerten lassen. Selbstbewertungen nur als Begleitbefund
   dokumentieren. Zwei unabhängige Fachbewertungen im Pilot kalibrieren.
   Bei der Auswertung ursprüngliche Bewertungen und späteren Konsens
   unterscheidbar halten.

## Auswertung und Vergleichbarkeit

Erfasse zuerst **Beobachtung und Belegstelle**. Danach folgen **fachliche
Bewertung anhand der Fallrubrik** und **Interpretation für die Prüf- oder
Forschungsfrage**. Eine Antwort kann dasselbe Lernziel auf unterschiedlichen
fachlich vertretbaren Wegen erreichen. Bezeichnungswahl, Spezialvokabular,
Länge und Technikbegeisterung sind kein Ersatz für einen sichtbaren Beitrag.

| Dimension | Was als Evidenz zählt |
|---|---|
| Didaktische Diagnose | Die Antwort belegt eine entscheidungsrelevante Ziel-Mittel-Spannung oder tragfähige Stärke am konkreten Fall. |
| Funktionale Planungsunterstützung | Die angebotene Hilfe oder Lernaktivität passt zur angestrebten Lernleistung, gegebenen Unterstützung und Sicherung. |
| Wirtschaftsdidaktische Begründungstiefe | Eine fachlich plausible Verknüpfung von Akteuren, Interessen, Bedingungen, möglichen Folgen und Urteilskriterien, soweit es die Aufgabe verlangt. |
| Dialogqualität und Lehrerautonomie | Sichtbare Orientierung mit Entscheidungsspielraum, relevante Rückfragen und korrekte Kennzeichnung angenommener, revidierter und lediglich vorgeschlagener Entscheidungen. |

Nutze die Stufen und kritischen Fehler des jeweiligen Falls. Eine Abweichung
nur dem unmittelbar betroffenen Kriterium zuordnen. Ereignismarker und
technische Befunde zusätzlich dokumentieren. Bei nicht beobachtbarem
Kriterium den Grund nennen und kein vollständiges Profil vortäuschen.
Eine ausbleibende Leistung in einem vollständig vorliegenden Turn wird nach
Rubrik bewertet. Skriptierte Lehrerrevisionen belegen nur die Qualität ihrer
Verarbeitung. Verfügbarkeit eines Journals, fehlender Werkzeugzugang und
ähnliche Plattformmerkmale fließen nicht in didaktische Punktwerte ein.

Vergleiche quantitative Werte direkt nur innerhalb derselben Fall- und
Rubrikversion und bei hinreichend gleichen Bedingungen. Nutze für einen
Agentenvergleich möglichst dasselbe Basismodell, dieselbe Reasoning-Einstellung
und gleichwertige Werkzeuge. Standard-ChatGPT erhält keine zusätzliche
Agentenkonfiguration. iWIP und der Teaching-Agent laufen jeweils mit ihrer
dokumentierten nativen Konfiguration. Weichen Modell, Plattform, Gedächtnis
oder Werkzeugzugang ab, können Ergebnisse die getesteten **Gesamtsysteme**
beschreiben. Ein Architektureffekt lässt sich daraus allein nicht ableiten.
Verschiedene Fallskalen bleiben erhalten. Vergleiche über Fälle hinweg anhand
der Dimensionsprofile und Belege, ohne die historischen Gesamtpunktwerte
zu einem Ranking zusammenzuzählen.

Ein gültiger Lauf je Fall genügt als erste Regression. Kritische
Regelverletzungen unmittelbar dokumentieren. Bei einem unerwarteten,
nichtkritischen Befund den betroffenen Fall unter gleichen Bedingungen
wiederholen und beide Ergebnisse behalten. Für den wissenschaftlichen Pilot
sind **zwei bis drei unabhängige Läufe je Fall und Bedingung** ein praktikabler
Start. Ergebnisse pro Lauf und ihre Streuung berichten. Stichprobengröße
und Bewertungsübereinstimmung für die Hauptuntersuchung separat planen.
Bei kleinen Stichproben konkrete Bewertungsdifferenzen ausweisen.

Gleichstände, niedrigere iWIP-Werte und bessere Ergebnisse anderer Systeme
sind gültig. Die Testaufgaben bleiben nach Ergebnissichtung unverändert.
Standardisierte Simulationsdialoge erlauben Aussagen über sichtbare
Unterstützung in den getesteten Situationen. Unterrichtswirkung,
Professionalisierung und Adaptivität über unterschiedliche
Planungsexpertisen erfordern eigene Untersuchungsdesigns und Daten mit
realen Lehrpersonen beziehungsweise systematisch variierten Aufgaben.

Methodische Grundlagen sind die [Standards für Testinterpretation und Validität](https://www.testingstandards.net/open-access-files.html),
[Constructive Alignment](https://doi.org/10.1007/BF00138871),
[ökonomische Kompetenzanforderungen](https://www.wida.wiwi.uni-due.de/fileadmin/fileupload/BWL-WIDA/Publikationen/Retzmann_ua2010_Gutachten.pdf),
[standardisierte Modellvergleichsbedingungen in HELM](https://arxiv.org/abs/2211.09110)
und [Verfahren zur Übereinstimmung unabhängiger Bewertungen](https://www.asc.upenn.edu/krippendorffs-alpha-reliability).

## Prüfumfang nach Änderung

| Prüfumfang | Wann und was | Ergebnis |
|---|---|---|
| **Kleine Regression** | Bei gezielter Verhaltensänderung H04.1–.3 für Diagnose und Präferenz oder das einschlägige Segment von H03. Für die erste Journalanlage A1–A3. H01 nur bei Änderungen an begrenzter Überarbeitung oder Chat-HTML-Ausgabe. H02 nur bei einem gezielten Revisionsverdacht. Beim Wiedereinstieg den definierten Vorlauf bis A6 verwenden. | Betroffener Sollpunkt mit Beleg und Ergebnis. Einen Teillauf als solchen kennzeichnen. |
| **Erweiterte Regression** | Bei größeren Änderungen an PLAN, KDM, DQM oder Skill-Architektur H04 vollständig. H03 A+B bei State-, Journal- oder Wiederaufnahmeänderungen, H02 bei revisionsrelevanten Änderungen in derselben Sitzung. Bei betroffener Planungsheuristik die im [Entwicklungsworkflow](../../project_governance/development_workflow.md) vorgesehenen offenen Planungsstarts gezielt prüfen. | Dimensionsbefunde, Rohdialoge und gegebenenfalls Snapshots. Je nach Auswahl 7 bis 24 Nutzerzüge für die H-Fälle. |
| **Wissenschaftlicher Vergleich** | H04 zur Kalibrierung, H07 als Pilot und H08 als standardisierter Robustheitsfall. In der Hauptuntersuchung zusätzliche zurückgehaltene Fälle nur für definierte Forschungsfragen. | Anonymisierte externe Bewertung, Profile je Dimension, Streuung und dokumentierte Vergleichsbedingungen. Kein Routineprüfschritt. |
| **Publikation und Integration** | Bei betroffenen technischen Komponenten `make qa-prompts`, `make qa-hugo`, [FINAL-Prüfer](../../scripts/check_final.py), [PDF-Export](../../scripts/export_reveal_pdfs.py) und die CI-Prüfungen für [Pages](../../.github/workflows/hugo.yml) und [OERSI](../../.github/workflows/oersi.yml) passend auswählen. Bei geänderter Freigabe- oder Gate-Logik den [Stationsbogen](../../project_governance/development_workflow.md#45-dry-run-auswertungsvorlage) mit einem bestehenden festgelegten Planungsstand verwenden. | Exitstatus, Zielroute, Dateihashes, betroffene PDFs und ggf. CI-Lauf. Nur die betroffenen Genehmigungs- oder Ableitungsschritte dialogisch prüfen. |

Bei reinen Pfad-, Template- oder Dokumentationsänderungen reichen Diff- und
betroffene technische Prüfungen. Ein vollständiger Gate-Dry-Run ist für
Änderungen am Zusammenspiel der Publikationsstationen vorgesehen.

## Laufprotokoll

Führe pro Lauf einen kurzen Datensatz. Optionale Messwerte nur angeben,
wenn die Plattform sie für die gewählte Laufgrenze ausweist.

```text
Suite, Fallversion, Rubrikfassung und Benchmark-Commit
Agentenbedingung und Agenten-Commit/Konfigurationsversion, lokale Abweichungen
Plattform, Modell, Reasoning, erlaubte Werkzeuge und bereitgestellter Kontext
Zeitpunkt mit Zeitzone, Wiederholungsnummer, gegebenenfalls Session-ID
Verweis auf tatsächlich gesendete Eingaben und sichtbaren Rohdialog
Je Dimension: Turn/Datei, Beobachtung, Bewertung und Begründung
Kritische Fehler, Drift, unnötige Rückfragen, Abbruch und Einschränkungen
Optional: technische Nachweise, Laufzeit, Modellaufrufe und verfügbare Usage-Werte
```

Technische Prüfungen mit `bestanden`, `fehlgeschlagen`, `nicht ausgeführt`
oder `abgebrochen` dokumentieren. Cached und uncached Input getrennt erfassen,
wenn verfügbar. Die Kosten historischer Modellläufe lassen sich aus der
Anzahl der Nutzerzüge allein nicht ableiten.

## Versionierung und Archivierung

- `inputs/` enthält die freigegebenen Testeingaben. `evaluations/` ist für
  Erwartungshorizonte und Bewertungsaufträge bestimmt, `fixtures/` für
  veröffentlichbare technische Sollstände. Die lokalen Rohdialoge,
  Arbeitsdateien und Laufresultate liegen unter
  `iwip_planungsagent/entwicklung/benchmark_runs/`. Historische lokale
  Fassungen liegen unter `benchmarks/historie/`. Die Git-Regeln geben nur
  vorgesehene Fallmaterialien frei.
- Referenziere `benchmark-v1.0` und den zugehörigen Suite-Commit. Änderungen
  an Aufgaben, Bewertungsmaßstäben oder Ausführungsregeln erhalten eine
  neue dokumentierte Fassung. Frühere Ergebnisse bleiben bei ihrer
  ursprünglichen Fall- und Rubrikversion. Eine Neubewertung unveränderter
  Rohdialoge wird als eigene Auswertung gekennzeichnet.
- Private Forschungsdaten, personenbezogene Rohdialoge und zurückgehaltene
  Evaluationsfälle in einem getrennten, zugriffsbeschränkten Bereich außerhalb
  öffentlicher Git- und Hugo-Pfade aufbewahren. Git-Ignorierung allein
  beschränkt keinen Dateizugriff des Agenten.

### Herkunft und historische Einschränkungen

- **H01–H04.** Frühere versionierte Fassungen sind unter anderem in `6567efe`
  unter `iwip_planungsagent_benchmarks/` nachvollziehbar. Der unmittelbar
  vorherige lokale Migrationsbericht, die alten H03-Sollunterlagen und die
  alte H04-Rubrik sind zusätzlich lokal archiviert. H01 bleibt als Test
  inhaltlich unverändert. Die dokumentierten H01-Ergebnisse lagen häufig nahe oder
  genau beim Maximum von 75. Eingabegrenzen, Drift und Rückfragen getrennt
  prüfen. Die früheren Gesamtwerte unterscheiden hohe Leistungen nur
  eingeschränkt. Der dokumentierte Wiedereinstieg unter B1.5 belegt H03
  für diesen historischen Stand. Für die spätere Skill-Migration ist nur
  Sitzung A belegt.
- **H07.** Die Texte wurden aus der protokollierten v2-Paketausgabe und der
  dokumentierten FINAL-Korrektur zum Laden der nativen Konfiguration
  rekonstruiert. Quellen sind das Re-Review und das FINAL-Änderungsprotokoll
  vom 7. September 2026. Die gesendeten Züge wurden gegen den archivierten
  iWIP-Lauf abgeglichen. Details zu den Quellsitzungen bleiben im lokalen Archiv.
  Das damalige Plattformprotokoll ist lokal archiviert. Die Benchmarkfassung
  1.0 übernimmt den Dialog und präzisiert die Bewertungsregeln. Die beiden
  historischen Selbstbewertungen von 72/75 sind Pilotbefunde unter alter Rubrik.
- **H08.** Sechs im Sitzungsprotokoll ausgegebene Ursprungstexte wurden
  anhand der archivierten ZIP-Dateilängen geprüft. Die dokumentierten
  FINAL-Korrekturen vom 8. September 2026 wurden nachvollzogen.
  1.0 übernimmt die rekonstruierte
  FINAL-Aufgabe und grenzt vor der ersten nachgewiesenen Benchmarkdurchführung
  die Bewertungskriterien enger ab. Die 0–10-Skala von D5 bleibt erhalten.
  Ein früherer H08-Lauf ist nicht belegt. Für H07 und H08 fehlen die
  Original-ZIPs und unabhängige Prüfsummen des damaligen FINAL-Archivs.
  Die rekonstruierten Textstände sind lokal archiviert.
- **Weitere Altbestände.** Historische KO-PLAN-Entwürfe, RC-Protokolle,
  Dry-Runs und Migrationsbefunde bleiben Entwicklungsmaterial. Sie gehören
  nicht zu den eingefrorenen Fallversionen dieser Suite.
