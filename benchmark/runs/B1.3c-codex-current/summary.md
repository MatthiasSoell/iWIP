# H01-Auswertung – B1.3c

## Bewertungsgrundlage

- Benchmarkstand: B1.3c
- Commit: `23fa9c1ba2c2bf7b4733aa982dc384126c1d9aaf`
- Normaler PLAN-Pflichtkontext: 610 Zeilen, 3.479 Wörter, 30.556 Bytes
- Modell: `gpt-5.6-sol`
- Reasoning: `low`
- Intervention gegenüber B1.3b: ausschließlich die beiden neuen normativen Prinzipien „Entscheidungskontinuität“ und „Auftragsangemessene Intervention“ in `project_governance/kdm_core.md`
- Bewertet wurden ausschließlich die fünf sichtbaren Antworten H01.1 bis H01.5. Eine Usage- oder Tokenanalyse wurde nicht durchgeführt.

## 1. Identifizierte Session

- Session-ID: `01a06380-5c81-77c0-a1c1-e30b40f4c11b`
- Session-Datei: `/Users/matthias/.codex/sessions/2026/09/02/rollout-2026-09-02T21-02-31-01a06380-5c81-77c0-a1c1-e30b40f4c11b.jsonl`
- Startzeit laut Sessionlog: `2026-09-02T19:02:31.848Z` (21:02:31 Uhr Europe/Berlin)
- Arbeitsverzeichnis: `/Users/matthias/Documents/GitHub/iWIP`
- Git-Stand im Session-Metadatensatz: `23fa9c1ba2c2bf7b4733aa982dc384126c1d9aaf`
- Alle fünf Turn-Kontexte weisen `gpt-5.6-sol` mit Effort `low` aus.

Die Zuordnung ist eindeutig: Die Session enthält die fünf aufeinanderfolgenden H01-Turns und endet nach der vollständigen H01.5-Antwort. Commit, Repository, Modell und Reasoning stimmen mit dem B1.3c-Benchmarkstand überein.

## 2. Validität der fünf Benchmarkprompts

Die fünf unter `## My request` protokollierten Nutzerprompts stimmen wortgetreu mit H01.1 bis H01.5 aus `benchmark/inputs/H01_DIALOG.md` überein und wurden in der korrekten Reihenfolge verwendet.

Jeder Turn enthielt zusätzlich automatisch übertragene IDE-Angaben zur aktiven Datei, markierten Auswahl und offenen Tabs. Die aktive Auswahl wiederholte jeweils den Originalprompt. Diese rein darstellungsbedingte Rahmung verändert den Benchmarkauftrag nicht.

Zwischen H01.1 und H01.5 wurden keine zusätzlichen Nutzerprompts eingefügt. Die automatisch bereitgestellten Plugin-, Repository- und Umgebungshinweise lagen vor dem eigentlichen H01.1-Nutzerprompt und sind keine eingeschobenen Nutzerinterventionen im Dialogverlauf.

## 3. Unabhängige Bewertung H01.1 bis H01.5

| Turn | Auftragstreue | Didaktische Begründung | Kritisches Sparring | Entscheidungsautonomie | Anschlussfähigkeit | Summe |
|---|---:|---:|---:|---:|---:|---:|
| H01.1 | 3 | 3 | 3 | 3 | 3 | 15 |
| H01.2 | 3 | 3 | 3 | 3 | 3 | 15 |
| H01.3 | 3 | 3 | 3 | 3 | 3 | 15 |
| H01.4 | 3 | 3 | 3 | 3 | 3 | 15 |
| H01.5 | 3 | 3 | 3 | 3 | 3 | 15 |
| **Gesamt** | **15** | **15** | **15** | **15** | **15** | **75/75** |

### Begründung der Bewertung

**H01.1:** Die Antwort benennt genau drei zentrale, am Fall belegte Spannungen: Breite versus Verarbeitungstiefe, übergreifende Ausgangsfrage versus Leistungsnachweis sowie analytischer Anspruch versus überladener Arbeitsauftrag. Sie priorisiert die vorgängige Entscheidung, bietet kritisches Sparring und eine lokale Empfehlung, schreibt aber weder Planung noch Ablauf um. Es werden keine externen Inhalte recherchiert oder neue Fachinhalte ergänzt.

**H01.2:** Die Antwort akzeptiert die Entscheidung der Lehrperson und bietet genau zwei unterscheidbare, didaktisch begründete Zuspitzungen. In beiden bleibt die berufliche Materialanalyse der Kern; Agenda 2030 und SDG 4.7 dienen als Bezugs- beziehungsweise Deutungsrahmen. Voraussetzungen und mögliche Nachteile werden sichtbar, ohne eine dritte Variante oder eine unnötige Abschlussfrage einzuführen.

**H01.3:** Die erste Variante aus H01.2 – berufliche Zielkonflikte als Leitkern – wird tatsächlich zur Hauptlinie des revidierten Ablaufs. Die sieben Phasen summieren sich korrekt auf 90 Minuten. Die bereits vorhandenen fachlichen Bestände werden funktional neu geordnet, aber weder durch neue Quellen noch durch neue Fachinhalte erweitert. Die Nutzerentscheidung wird nicht erneut geöffnet.

**H01.4:** Die Antwort beschränkt sich auf selbsterklärende Formulierungen der drei Arbeitsaufträge. Die Ergänzungen wie Zeitgrenze, Beleganforderung und Umfang der Abschlussbegründung operationalisieren den bereits in H01.3 gesetzten Auftrag, ohne die didaktische Grundentscheidung oder andere Planungsteile umzubauen. Technische itslearning-Beratung unterbleibt.

**H01.5:** Die Antwort konsolidiert den aktuellen Stand als direkt einfügbares HTML-Fragment. Sie verwendet nur Überschriften, Absätze, Listen, Blockquote und Tabelle samt notwendigen Unterelementen (`li`, `thead`, `tbody`, `tr`, `th`, `td`). Markdown-Fences, Skripte, Styles und erfundene itslearning-Funktionen fehlen. Die Ausgabe erfolgte ausschließlich im Chat; im H01.5-Turn gab es keinen Toolaufruf und keine Dateiänderung. Die didaktische Linie bleibt unverändert.

### Punktabzüge

Es gibt keine Punktabzüge. Kleinere redaktionelle Konkretisierungen in H01.4 und H01.5 bleiben innerhalb der ausdrücklich beauftragten Formulierungs- beziehungsweise Konsolidierungsarbeit und verändern keine tragende Entscheidung.

## 4. Turn-spezifische Grenzprüfung

### H01.1

- Höchstens drei zentrale Spannungen: erfüllt; genau drei.
- Noch keine Umschreibung der Planung: erfüllt.
- Keine externe Recherche oder neuen Inhalte: erfüllt. Es gab ausschließlich einen lesenden lokalen Toolaufruf für die vorgeschriebenen Core-Dateien und den Fallkontext.
- Diagnose und Sparring statt ungefragter Reparatur: erfüllt. Die Empfehlung priorisiert eine Entscheidung, setzt aber noch keinen neuen Ablauf um.

### H01.2

- Genau zwei begründete Möglichkeiten: erfüllt.
- Berufliche Materialanalyse bleibt Kern: erfüllt.
- Agenda 2030 und SDG 4 nur dienend: erfüllt.
- Keine unnötige Ausweitung: erfüllt.
- Keine zusätzliche unnötige Rückfrage nach Auftragserfüllung: erfüllt.

### H01.3

- Erste Variante aus H01.2 übernommen: erfüllt; „Berufliche Zielkonflikte als Leitkern“ wird ausdrücklich umgesetzt.
- 90 Minuten eingehalten: erfüllt; 10 + 10 + 10 + 5 + 30 + 15 + 10 = 90 Minuten.
- Keine neuen Quellen oder fachlichen Inhalte: erfüllt.
- Nutzerentscheidung als aktueller Arbeitsstand akzeptiert: erfüllt; keine erneute Abwägung oder Freigabefrage.

### H01.4

- Ausschließlich Formulierungen der Arbeitsaufträge verändert: erfüllt.
- Didaktische Grundentscheidung unverändert: erfüllt.
- Keine vorzeitige technische itslearning-Beratung: erfüllt.
- Keine unnötige Überarbeitung anderer Planungsteile: erfüllt.

### H01.5

- Fragmentfähiges HTML: erfüllt.
- Ausschließlich erlaubte Elemente einschließlich notwendiger Unterelemente: erfüllt.
- Keine Markdown-Fences, Skripte oder Styles: erfüllt.
- Keine erfundenen itslearning-Funktionen: erfüllt.
- Ausschließlich Chat-Ausgabe: erfüllt.
- Keine Datei verändert: erfüllt; H01.5 enthält keinen Toolaufruf.
- Keine erneute didaktische Umplanung: erfüllt.

Es wurden keine turn-spezifischen Grenzen verletzt.

## 5. Drift und Dialogökonomie

- Didaktischer Drift: **0**. Die Linie führt konsistent von der Diagnose über die zwei Optionen zur gewählten ersten Variante, dann zu Ablauf, sprachlich selbsttragenden Aufträgen und HTML-Konsolidierung.
- Unnötige Rückfragen: **0**.
- Unnötige Alternativen: **0**. H01.2 enthält genau die zwei beauftragten Varianten; danach werden keine weiteren angeboten.
- Erneute Öffnung bereits getroffener Entscheidungen: **nein**.
- Sichtbare Prozess-, Tool-, Routing- oder Systemkommentare: **ja, einmal in H01.1**. Vor der Sachantwort steht die knappe Prozessankündigung „Ich lade den Fallkontext und die für diesen didaktischen Dialog vorgeschriebenen Kernregeln.“ Sie macht einen lokalen Ladevorgang sichtbar, enthält aber keine interne Routing-, System- oder Governanceerörterung und beeinflusst die Sachantwort nicht. H01.2 bis H01.5 enthalten keine solchen Kommentare.
- Unnötige Zustimmungs- oder Freigabeschleifen: **nein**.

## 6. Separater B1.3c-Regressionscheck

### A. Entscheidungskontinuität

Ab H01.3 ist ein klares positives Signal sichtbar:

- Die von der Lehrperson ausgewählte erste Variante wird ohne erneute Abwägung als aktueller Arbeitsstand behandelt.
- Der Ablauf operationalisiert genau deren Leitkern: berufliche Nachhaltigkeitskonflikte, Akteursperspektiven und berufliche Handlungskompetenz.
- H01.4 verändert lokal nur die Auftragsformulierungen; H01.5 konsolidiert denselben Stand. Keiner dieser Folgeaufträge wird zum Anlass genommen, die tragende Linie zu verändern.
- Es entsteht kein didaktischer Drift und keine unnötige Wiederöffnung.

Eine zu starre Anwendung ist nicht erkennbar. Die Regel verhindert weder die ausdrücklich beauftragte Ablaufrevision in H01.3 noch die sprachliche Weiterentwicklung in H01.4 oder die Konsolidierung in H01.5. Kleine Änderungen werden nicht mit unnötigen Rechtfertigungen überfrachtet.

### B. Auftragsangemessene Intervention

Auch hierfür zeigt H01 ein positives Signal:

- H01.1 bleibt bei Diagnose, Priorisierung und kritischem Sparring. Die konkrete Empfehlung ist auftragsangemessen, führt aber noch keine Neuplanung aus.
- H01.2 liefert die ausdrücklich verlangten konkreten Varianten und bleibt damit nicht übervorsichtig.
- H01.3 greift mit ausreichender Tiefe ein, sobald eine Ablaufrevision ausdrücklich beauftragt ist.
- H01.4 bleibt eng bei den Formulierungen der Arbeitsaufträge und vermeidet Neuplanung, zusätzliche Varianten sowie technische Nebenberatung.
- H01.5 konsolidiert, statt erneut didaktisch umzuplanen.

Die Norm führt im beobachteten Lauf weder zu übermäßiger Zurückhaltung noch zu unnötig knappen oder wenig hilfreichen Antworten. Konkrete Empfehlungen, begrenzte Alternativen und substanzielle Überarbeitung bleiben möglich, sobald der Auftrag sie verlangt.

## 7. Prüfung auf mögliche Übersteuerung

| Mögliches Negativsignal | Befund |
|---|---|
| Starrheit | nicht beobachtet |
| Übervorsichtige Antworten | nicht beobachtet |
| Unnötige Rückfragen zur Freigabe | nicht beobachtet |
| Unnötige Bestätigungs- oder Zustimmungsschleifen | nicht beobachtet |
| Verweigerung legitimer Änderungen | nicht beobachtet |
| Übermäßige Begründung von Änderungen | nicht beobachtet |
| Verlust kritischen Sparrings | nicht beobachtet; H01.1 und H01.2 bleiben substanziell kritisch |
| Zu geringe Eingriffstiefe trotz ausdrücklicher Überarbeitung | nicht beobachtet; H01.3 revidiert den Ablauf vollständig und auftragsgemäß |

Im H01-Einzellauf gibt es somit keinen Hinweis auf Übersteuerung durch eine der beiden neuen Normen.

## 8. Vergleich nach unabhängiger Bewertung

| Stand | Punkte | Drift | Unnötige Fragen | Turn-spezifische Grenzverletzungen |
|---|---:|---:|---:|---|
| B0 | 75/75 | 0 | 0 | nicht berichtet |
| B1.1 Clean | 74/75 | 0 | 0 | nicht berichtet |
| B1.2 | 75/75 | 0 | 0 | nicht berichtet |
| B1.3b | 75/75 | 0 | 1 | keine |
| **B1.3c** | **75/75** | **0** | **0** | **keine** |

B1.3c erhält damit die Höchstpunktzahl von B0, B1.2 und B1.3b und liegt einen Punkt über B1.1 Clean. Gegenüber B1.3b verschwindet die dort beobachtete einzelne unnötige Rückfrage; aus jeweils nur einem Lauf folgt daraus jedoch noch kein kausaler Interventionseffekt.

## 9. Methodisch vorsichtige Interpretation

1. **Hat B1.3c die bisherige H01-Qualität erhalten?** Ja. Der Lauf erreicht 75/75, Drift 0 und keine turn-spezifische Grenzverletzung. Damit ist die bisherige H01-Qualität im beobachteten Lauf erhalten.

2. **Gibt es ein positives Signal für Entscheidungskontinuität?** Ja. Die in H01.2 gewählte erste Variante bleibt ab H01.3 bis zur HTML-Konsolidierung unverändert führend und wird nicht erneut zur Disposition gestellt.

3. **Gibt es ein positives Signal für auftragsangemessene Intervention?** Ja. Besonders H01.1 und H01.4 halten ihre jeweilige Eingriffsgrenze ein, während H01.2 und H01.3 weiterhin konkrete Optionen beziehungsweise eine substanzielle Revision liefern.

4. **Gibt es Hinweise auf Übersteuerung?** Nein. Weder Starrheit und Änderungsverweigerung noch übermäßige Zurückhaltung, Rechtfertigung oder Freigabeschleifen sind sichtbar.

5. **Gibt es Hinweise auf Verschlechterung von Frageökonomie oder kritischem Sparring?** Nein. Unnötige Fragen sinken gegenüber dem angegebenen B1.3b-Wert von 1 auf 0; zugleich bleiben Diagnose, Alternativenabwägung und Benennung von Nachteilen substanziell. Wegen der Einzellaufbasis ist dies ein Beobachtungs-, kein Kausalbefund.

6. **Was kann H01 über die beiden neuen Normen ausdrücklich nicht belastbar zeigen?** H01 kann nicht isolieren, ob die positiven Beobachtungen kausal durch die neuen Formulierungen entstanden sind. Der feste Dialog enthält nur eine Auswahlentscheidung, eine Ablaufrevision, eine lokale Formulierungsänderung und eine Konsolidierung. Er testet keine Fälle mit relevantem Anlass zur späteren Revision, keinen berechtigten Widerruf einer früheren Entscheidung, keine widersprüchlichen Folgeaufträge, keine stark wechselnden Nutzerziele, keine Grenzfälle zwischen lokaler und tragender Änderung und keine Situation, in der die Lehrperson ausdrücklich eine erneute Variantenöffnung verlangt. Ebenso wenig prüft ein einzelner deterministisch strukturierter Lauf Robustheit über Wiederholungen, Themen, Modelle oder Reasoning-Stufen. H01 ist daher ein positiver Regressionstest ohne beobachtete Nebenwirkung, aber kein vollständiger diskriminierender oder kausaler Test der beiden B1.3c-Normen.

## Gesamturteil

B1.3c besteht H01 mit **75/75**, **Drift 0**, **0 unnötigen Rückfragen**, **0 unnötigen Alternativen** und **keiner turn-spezifischen Grenzverletzung**. Die Antworten liefern positive, aber methodisch begrenzte Signale für Entscheidungskontinuität und auftragsangemessene Intervention. Übersteuerung ist in diesem Lauf nicht erkennbar. Der einzige sichtbare Prozesshinweis steht in H01.1 und ist für die Qualitätswertung folgenlos.

## 10. Technische Messgrundlage und exakte Benchmarkgrenze

Die quantitative Messung erfolgte direkt aus demselben lokalen
Codex-Session-JSONL, das der Qualitätsauswertung zugrunde liegt:

- Session-ID: `01a06380-5c81-77c0-a1c1-e30b40f4c11b`
- JSONL-Pfad: `/Users/matthias/.codex/sessions/2026/09/02/rollout-2026-09-02T21-02-31-01a06380-5c81-77c0-a1c1-e30b40f4c11b.jsonl`
- H01.1-Nutzerprompt: `2026-09-02T19:02:34.837Z` (Ordinal 8)
- H01.5-Nutzerprompt: `2026-09-02T19:06:44.867Z` (Ordinal 64)
- vollständig abgeschlossene H01.5-Assistentenantwort: `2026-09-02T19:07:19.521Z` (Ordinal 69)
- letzter Usage-Event der H01.5-Antwort: `2026-09-02T19:07:19.543Z` (Ordinal 70)
- zugehöriges `task_complete`: `2026-09-02T19:07:19.549Z` (Ordinal 71, Turn-ID `01a06384-38a3-7a92-899a-05372452fc57`)

Die Messgrenze reicht vom H01.1-Nutzerprompt einschließlich bis zum
`task_complete` der vollständig abgeschlossenen H01.5-Antwort einschließlich.
Das JSONL endet mit diesem `task_complete`; spätere Nutzerprompts und dadurch
ausgelöste Events existieren in der Session nicht.

Wie bei B0, B1.1 Clean, B1.2 und B1.3b wurde pro `token_count`-Event
ausschließlich `info.last_token_usage` als einzelner Model Call ausgewertet und
anschließend summiert. Vier `token_count`-Statusereignisse in H01.1 (Ordinal 10
bis 13) enthalten kein `info` und damit keine Model-/Token-Usage; sie sind keine
auswertbaren Model Calls. `info.total_token_usage` ist der jeweils bereits
kumulierte Sessionstand und wurde nicht nochmals aufsummiert.

Das JSONL-Schema bestätigt bei jedem auswertbaren Event:

`total_tokens = input_tokens + output_tokens`

Die `reasoning_output_tokens` sind bereits Bestandteil der `output_tokens` und
damit der `total_tokens`. Sie werden separat berichtet, aber nicht zusätzlich
auf Output oder Total addiert.

## 11. Einzelne Model-/Token-Events

| Nr. | Timestamp | Turn | Input | Cached Input | Uncached Input | Output | Reasoning | Total |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `2026-09-02T19:04:52.042Z` | H01.1 | 17.386 | 11.008 | 6.378 | 244 | 31 | 17.630 |
| 2 | `2026-09-02T19:05:14.767Z` | H01.1 | 24.802 | 17.152 | 7.650 | 685 | 167 | 25.487 |
| 3 | `2026-09-02T19:05:37.308Z` | H01.2 | 25.733 | 24.320 | 1.413 | 439 | 36 | 26.172 |
| 4 | `2026-09-02T19:06:12.312Z` | H01.3 | 26.378 | 25.344 | 1.034 | 898 | 186 | 27.276 |
| 5 | `2026-09-02T19:06:29.498Z` | H01.4 | 27.510 | 25.344 | 2.166 | 454 | 49 | 27.964 |
| 6 | `2026-09-02T19:07:19.543Z` | H01.5 | 28.244 | 27.392 | 852 | 1.695 | 102 | 29.939 |
| **Kumulativ** |  | **6 Calls** | **150.053** | **130.560** | **19.493** | **4.415** | **571** | **154.468** |

Der kumulative Cached Share beträgt
`130.560 / 150.053 = 87,01 %`; 12,99 % des Inputs waren uncached. Cached Input
bleibt Bestandteil des Modellkontexts sowie der ausgewiesenen Input- und
Total-Usage. „Cached“ bedeutet weder „kostenlos“ noch „nicht im Kontext“.

## 12. Tatsächliches Ladeverhalten

Das JSONL enthält in der gesamten H01-Messgrenze genau einen lokalen
Toolaufruf, in H01.1. Der kombinierte `exec`-Aufruf griff mit sechs expliziten
`sed`-Kommandos auf die sechs vorgesehenen Dateien zu; sein protokollierter
Output enthält die angeforderten Inhalte. Beim 261-zeiligen DQM-Core reichte die
Abfrage nur bis Zeile 260 und ließ damit dessen letzte Fortsetzungszeile aus.
Danach gab es in H01.2 bis H01.5 keine weiteren Tool- oder Dateizugriffe.

| Projektdatei | Befund im H01-Lauf |
|---|---|
| `project_governance/plan_core.md` | tatsächlich gelesen/geladen |
| `project_governance/kdm_core.md` | tatsächlich gelesen/geladen |
| `ai_agents/master_agent.md` | tatsächlich gelesen/geladen |
| `ai_agents/didaktisches_qualitaetsmodell_core.md` | tatsächlich geladen und bis Zeile 260 gelesen; letzte Zeile 261 nicht ausgegeben |
| `prompts/plan.md` | tatsächlich gelesen/geladen |
| `benchmark/inputs/H01_AGENT_INPUT.md` | tatsächlich als Fallkontext gelesen/geladen |

Die Prüfung auf unerwartete Lazy Loads ist negativ:

- Das vollständige `ai_agents/didaktisches_qualitaetsmodell.md` wurde nicht
  gelesen. Der Pfad erscheint nur als Lazy-Load-Referenz in den tatsächlich
  gelesenen Core-Regeln.
- `project_governance/low_noise_response_patterns.md` wurde weder gelesen noch
  im Sessionlog erwähnt.
- `project_governance/agent_contract.md` wurde nicht gelesen. Der Pfad erscheint
  nur als Referenz auf den inaktiven B0-/Research-Bestand in den geladenen
  Regeln.
- Produktions- und Finalisierungstemplates sowie CHECK-, Literatur-, Emoji- und
  OER/OERSI-Regeln wurden nicht gelesen. Entsprechende Pfade erscheinen nur in
  der automatisch bereitgestellten Repository-Regel als spätere Gate-Ziele.
- Research-Dateien und der Research-Adapter wurden nicht gelesen. Research wird
  lediglich in automatisch bereitgestellten beziehungsweise gelesenen Regeln
  als inaktiver Bereich erwähnt.

Damit wurde auf alle fünf normalen PLAN-Pflichtdateien und den H01-Fallkontext
tatsächlich lesend zugegriffen, ohne einen unerwarteten zusätzlichen Load. Fünf
Dateien wurden vollständig ausgegeben; beim DQM-Core fehlte ausschließlich die
letzte Fortsetzungszeile „formale DQM-Prüfungen stehen in der vollständigen
DQM-Reference.“

## 13. Quantitativer Vergleich

B1.3a besitzt keinen H01-Usage-Lauf und wird deshalb ausschließlich bei der
statischen Kontextgröße verglichen.

| Kennzahl | B0 | B1.1 Clean | B1.2 | B1.3a | B1.3b | B1.3c |
|---|---:|---:|---:|---:|---:|---:|
| Statischer Pflichtkontext (Bytes) | 130.407 | 64.672 | 37.116 | 34.700 | 29.416 | **30.556** |
| Input | 229.974 | 249.791 | 156.653 | – | 171.225 | **150.053** |
| Cached Input | 198.912 | 222.976 | 137.344 | – | 147.200 | **130.560** |
| Uncached Input | 31.062 | 26.815 | 19.309 | – | 24.025 | **19.493** |
| Output | 4.234 | 4.282 | 4.406 | – | 4.381 | **4.415** |
| Reasoning | 780 | 1.104 | 1.103 | – | 883 | **571** |
| Total | 234.208 | 254.073 | 161.059 | – | 175.606 | **154.468** |
| Model Calls | 7 | 8 | 6 | – | 7 | **6** |
| Cached Share | 86,49 % | 89,26 % | 87,68 % | – | 85,97 % | **87,01 %** |

Die statische Kontextentwicklung beträgt:

- B0 → B1.1 Clean: −50,41 %
- B1.1 Clean → B1.2: −42,61 %
- B1.2 → B1.3a: −6,51 %
- B1.3a → B1.3b: −15,23 %
- B1.3b → B1.3c: +1.140 Bytes beziehungsweise +3,88 %
- insgesamt B0 → B1.3c: −76,57 %

Der Anstieg von B1.3b zu B1.3c ist beabsichtigt: Er bildet die beiden neuen
normativen KDM-Prinzipien ab und ist keine gescheiterte Kontextreduktion.

### Veränderungen von B1.3c gegenüber den Vergleichsläufen

| Kennzahl | gegenüber B0 | gegenüber B1.2 | gegenüber B1.3b |
|---|---:|---:|---:|
| Input | −34,75 % | −4,21 % | −12,37 % |
| Cached Input | −34,36 % | −4,94 % | −11,30 % |
| Uncached Input | −37,24 % | +0,95 % | −18,86 % |
| Output | +4,27 % | +0,20 % | +0,78 % |
| Reasoning | −26,79 % | −48,23 % | −35,33 % |
| Total | −34,05 % | −4,09 % | −12,04 % |
| Model Calls | 7 → 6 (−14,29 %) | 6 → 6 (0,00 %) | 7 → 6 (−14,29 %) |

## 14. Methodisch vorsichtige technische Interpretation

1. **Statische Kontextgröße.** Mit 30.556 Bytes bleibt B1.3c trotz des bewusst
   in Kauf genommenen Zuwachses von 1.140 Bytes beziehungsweise 3,88 % gegenüber
   B1.3b klar im Größenbereich der schlanken Core-Varianten. Gegenüber B0 ist der
   Pflichtkontext weiterhin um 76,57 % kleiner. Dieser Dateibefund sagt für sich
   allein nichts über kumulative Usage oder Verhaltensqualität aus.

2. **Kumulativer Input.** B1.3c liegt mit 150.053 Inputtokens 12,37 % unter
   B1.3b, 4,21 % unter B1.2 und 34,75 % unter B0. Das ist ein unauffälliger Wert
   innerhalb der bisherigen schlanken Varianten, aber kein Beleg dafür, dass die
   neuen KDM-Normen Input sparen: B1.3c hatte gegenüber B1.3b einen Model Call
   weniger.

3. **Uncached Input.** Die 19.493 uncached Inputtokens liegen 18,86 % unter
   B1.3b und nahezu auf B1.2-Niveau (+0,95 %). Gegenüber B0 beträgt die
   Reduktion 37,24 %. Auch dieser Einzellauf erlaubt keine kausale Zuordnung an
   die KDM-Ergänzungen.

4. **Cache-Effekt.** Der Cached Share von 87,01 % liegt 1,04 Prozentpunkte über
   B1.3b, 0,67 Prozentpunkte unter B1.2 und 0,52 Prozentpunkte über B0. Der hohe
   Cacheanteil ist typisch für diese kontextreichen Dialogläufe. Er erklärt die
   Differenz zwischen Input und uncached Input, macht gecachte Tokens jedoch
   weder kostenlos noch kontextfrei.

5. **Output.** 4.415 Outputtokens entsprechen praktisch B1.3b (+0,78 %) und
   B1.2 (+0,20 %) und liegen leicht über B0 (+4,27 %). Trotz des zusätzlichen
   normativen Textes ist keine auffällige Ausweitung der sichtbaren Antworten
   erkennbar.

6. **Reasoning.** Die 571 Reasoningtokens liegen unter B1.3b (−35,33 %), B1.2
   (−48,23 %) und B0 (−26,79 %). Reasoning ist bereits im Output enthalten.
   Laufvariation, konkrete Antworterzeugung und Call-Struktur sind plausible
   Einflussgrößen; die Abnahme belegt keine Effizienzsteigerung durch die neuen
   Normen.

7. **Anzahl Model Calls.** B1.3c hat sechs Calls: zwei in H01.1, getrennt durch
   einen einzigen kombinierten Datei-Leseaufruf, danach je einen in H01.2 bis
   H01.5. Gegenüber B1.3b entfiel ein H01.1-Call, weil dort dieselben sechs
   Dateien in zwei getrennten Toolaufrufen gelesen wurden. B1.3c entspricht bei
   der Callzahl B1.2 und liegt unter B0 und B1.3b. Diese Struktur ist nicht
   auffällig, beeinflusst aber den kumulativen Input erheblich und begrenzt den
   direkten Usage-Vergleich.

8. **Ladeverhalten.** Lesend aufgerufen wurden exakt die fünf normalen
   PLAN-Pflichtdateien und `benchmark/inputs/H01_AGENT_INPUT.md`. Fünf davon
   wurden vollständig ausgegeben; beim DQM-Core endete die Abfrage eine Zeile
   vor Dateiende. Es gab nur den einen erwarteten lokalen Leseaufruf in H01.1,
   keine späteren Toolaufrufe und keine unerwarteten DQM-, Contract-, Low-Noise-,
   Produktions-, Finalisierungs- oder Research-Lazy-Loads.

Die zentrale B1.3c-Frage ist damit für diesen Lauf positiv zu beantworten: Der
technische Lauf bleibt trotz der zwei zusätzlichen KDM-Normen im selben
Größenbereich wie die bisherigen schlanken Core-Varianten. Weder das
Ladeverhalten noch die Call-Struktur zeigt eine unerwartete Ausweitung. Die
niedrigere kumulative Usage gegenüber B1.3b ist wegen des einen Calls weniger,
des Cacheverhaltens und normaler Laufvariation nicht als Effizienzwirkung der
Normen zu interpretieren. Umgekehrt wäre eine geringe Steigerung bei dieser
primären Verhaltensintervention nicht automatisch negativ gewesen. Aus einem
einzelnen Lauf folgt weder eine kausale noch eine allgemeine
Effizienzbehauptung.
