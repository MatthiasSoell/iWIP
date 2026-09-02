# H01-Auswertung – B1.3b

## Bewertungsgrundlage

- Benchmarkstand: B1.3b
- Commit: `a3b7784f6337817da9d7983cc9fe2b7d3c65a1bf`
- Pflichtkontext: 594 Zeilen, 3.357 Wörter, 29.416 Bytes
- Modell: `gpt-5.6-sol`
- Reasoning: `low`
- Bewertet wurden ausschließlich die fünf sichtbaren Antworten H01.1 bis H01.5. Eine Usage- oder Tokenanalyse wurde nicht durchgeführt.

## 1. Identifizierte Session

- Session-ID: `01a0635b-7a02-7bc1-8d81-cf9cc673a03e`
- Session-Datei: `/Users/matthias/.codex/sessions/2026/09/02/rollout-2026-09-02T20-22-14-01a0635b-7a02-7bc1-8d81-cf9cc673a03e.jsonl`
- Startzeit laut Sessionlog: 2026-09-02T18:22:14.574Z
- Arbeitsverzeichnis: `/Users/matthias/Documents/GitHub/iWIP`
- Git-Stand im Session-Metadatensatz: exakt der angegebene Commit
- Alle fünf Turn-Kontexte weisen `gpt-5.6-sol` mit Reasoning `low` aus.

Die Zuordnung ist eindeutig: Die Session enthält genau die fünf H01-Turns, wurde unmittelbar vor der Auswertung beendet und stimmt bei Repository, Commit, Modell und Reasoning mit dem angegebenen Benchmarkstand überein.

## 2. Validität der Benchmarkprompts

Die fünf unter `## My request` protokollierten Nutzerprompts stimmen wortgetreu mit H01.1 bis H01.5 aus `benchmark/inputs/H01_DIALOG.md` überein und wurden in der korrekten Reihenfolge gesendet.

Jeder Nutzerturn enthielt zusätzlich automatisch übertragene IDE-Kontextangaben (aktive Datei, markierter Text und offene Tabs). Der markierte Text wiederholte jeweils denselben Originalprompt. Diese rein darstellungs- und umgebungsbedingte Rahmung verändert den semantischen Auftrag nicht.

Zwischen H01.1 und H01.5 wurden keine zusätzlichen Nutzerprompts eingefügt. Damit liegt kein promptseitiger Eingriff vor, der den Benchmarkverlauf beeinflusst haben könnte.

## 3. Bewertung H01.1 bis H01.5

| Turn | Auftragstreue | Didaktische Begründung | Kritisches Sparring | Entscheidungsautonomie | Anschlussfähigkeit | Summe |
|---|---:|---:|---:|---:|---:|---:|
| H01.1 | 3 | 3 | 3 | 3 | 3 | 15 |
| H01.2 | 3 | 3 | 3 | 3 | 3 | 15 |
| H01.3 | 3 | 3 | 3 | 3 | 3 | 15 |
| H01.4 | 3 | 3 | 3 | 3 | 3 | 15 |
| H01.5 | 3 | 3 | 3 | 3 | 3 | 15 |
| **Gesamt** | **15** | **15** | **15** | **15** | **15** | **75/75** |

### Begründung

H01.1 verdichtet die Planung auf genau drei entscheidungsrelevante Spannungen. Die Punkte sind am Fall belegt, didaktisch erklärt und führen zu einer klaren Entscheidungsfrage, ohne die Planung bereits umzuschreiben.

H01.2 bietet genau zwei unterscheidbare und begründete Zuspitzungen. Beide halten die berufliche Materialanalyse im Zentrum; Agenda 2030 und SDG 4.7 bleiben dienende Orientierungsrahmen. Die Vor- und Nachteile der Varianten bilden angemessenes kritisches Sparring.

H01.3 setzt tatsächlich die erste Variante, den kriteriengeleiteten Materialaudit, um. Der Ablauf summiert sich korrekt auf 90 Minuten. Die vorbereitenden Inhalte werden funktional auf das Audit ausgerichtet, ohne den fachlichen Bestand zu erweitern.

H01.4 verändert nur die Formulierungen der Arbeitsaufträge. Die Aufgaben werden ohne mündliche Erläuterung bearbeitbar, während Materialaudit, vier Prüffelder, Belegpflicht, Gesamturteil und Reflexion unverändert bleiben. Es erfolgt keine technische itslearning-Beratung.

H01.5 konsolidiert den gewählten Stand als HTML-Fragment. Verwendet werden ausschließlich Überschriften, Absätze, Listen, Blockquote und Tabelle einschließlich ihrer notwendigen HTML-Unterelemente. Es gibt keine Markdown-Fences, Skripte, Styles oder erfundenen itslearning-Funktionen. Die Ausgabe erfolgte nur im Chat.

Es gibt keine rubric-relevanten Punktabzüge. Die unten ausgewiesene unnötige Rückfrage in H01.2 ist eine Frageökonomie-Schwäche, beeinträchtigt die Erfüllung der fünf Bewertungskriterien in diesem Lauf aber nicht so stark, dass eine Abwertung auf 2 gerechtfertigt wäre.

## 4. Turn-spezifische Zusatzprüfungen

### H01.1

- Höchstens drei zentrale Spannungen: erfüllt; es werden genau drei genannt.
- Noch keine Umschreibung der Planung: erfüllt.
- Keine externe Recherche oder neuen Inhalte: erfüllt. Die Session nutzt nur lesende lokale Zugriffe auf Pflichtkontext und Fallkontext.

### H01.2

- Genau zwei begründete Möglichkeiten: erfüllt.
- Berufliche Materialanalyse bleibt Kern: erfüllt.
- Agenda 2030 und SDG 4 nur dienend: erfüllt.
- Keine unnötige inhaltliche Ausweitung: erfüllt.

### H01.3

- Erste Variante aus H01.2 übernommen: erfüllt; der „Materialaudit“ wird ausdrücklich zur Hauptlinie.
- 90 Minuten eingehalten: erfüllt; 10 + 10 + 10 + 35 + 15 + 10 = 90 Minuten.
- Keine neuen Quellen oder fachlichen Inhalte: erfüllt. Brundtland-Definition, Nachhaltigkeitsdimensionen, Agenda 2030, SDG 4.7, BBNE, Standardberufsbildpositionen und NaVeBb waren bereits im Fallkontext enthalten.

### H01.4

- Ausschließlich Formulierungen der Arbeitsaufträge verändert: erfüllt.
- Didaktische Grundentscheidung unverändert: erfüllt.
- Keine vorzeitige technische itslearning-Beratung: erfüllt.

### H01.5

- Fragmentfähiges HTML: erfüllt.
- Nur erlaubte Elementarten: erfüllt. `thead`, `tbody`, `tr`, `th` und `td` sind notwendige Unterelemente der erlaubten Tabelle; `li` ist notwendiges Unterelement der erlaubten Listen.
- Keine Markdown-Fences, Skripte oder Styles: erfüllt.
- Keine erfundenen itslearning-Funktionen: erfüllt.
- Ausschließlich Chat-Ausgabe: erfüllt.
- Keine Datei verändert: erfüllt. Das Sessionlog enthält nur zwei lesende lokale Toolaufrufe in H01.1 und danach keine Toolaufrufe; der Arbeitsbaum war vor der Auswertungsdokumentation sauber.

Es wurden keine turn-spezifischen Grenzen verletzt.

## 5. Drift und Dialogökonomie

- Didaktischer Drift: **0**. Die Linie entwickelt sich nachvollziehbar von der Diagnose über zwei Optionen zur gewählten Audit-Variante, deren Ablauf, Auftragsformulierungen und HTML-Konsolidierung.
- Stabilität der ersten Variante: vollständig stabil. Der in H01.2 angebotene „Materialaudit“ bleibt von H01.3 bis H01.5 die führende Hauptlinie.
- Neue fachliche Inhalte oder Quellen: keine.
- Unnötige Rückfragen: **1**. H01.2 endet trotz eines vollständig erfüllten Zwei-Varianten-Auftrags mit der zusätzlichen Frage, ob das Material ein echtes Entscheidungsproblem trage oder vor allem seine didaktische Qualität geprüft werden solle. Die Frage ist fachlich anschlussfähig, aber für das feste Skript nicht erforderlich und öffnet die bereits ausreichend strukturierte Auswahl nochmals. H01.1 enthält ebenfalls eine entscheidungsorientierte Gegenüberstellung, aber keine isolierte Rückfrage, die für den Fortgang beantwortet werden musste.
- Unnötige Alternativen oder erneute Öffnung getroffener Entscheidungen: keine zusätzliche dritte Alternative. Die abschließende Frage in H01.2 öffnet die Wahl zwischen den beiden angeforderten Varianten nochmals, überschreibt jedoch keine bereits getroffene Variantenentscheidung. Ab H01.3 wird die Auswahl nicht erneut relativiert.
- Sichtbare Prozess-, Tool-, Routing- oder Systemkommentare: In H01.1 erscheint vor der Sachantwort eine knappe Prozessankündigung („Ich lade den Fallkontext …“). Sie ist sichtbar, enthält aber keine problematische System-, Routing- oder interne Governanceerörterung. Weitere solche Kommentare gibt es nicht.

## 6. Vergleich mit früheren Läufen

| Stand | Punkte | Drift | Unnötige Fragen |
|---|---:|---:|---:|
| B0 | 75/75 | 0 | 0 |
| B1.1 Clean | 74/75 | 0 | 0 |
| B1.2 | 75/75 | 0 | 0 |
| **B1.3b** | **75/75** | **0** | **1** |

Die B1.3b-Antworten erreichen dieselbe Gesamtpunktzahl wie B0 und B1.2 und liegen einen Punkt über B1.1 Clean. Kritisches Sparring, führende Hauptlinie sowie Gate- und Auftragsgrenzen sind im beobachteten Lauf nicht schwächer. Die einzige negative Veränderung gegenüber den angegebenen Vergleichsdaten ist die eine unnötige Abschlussfrage in H01.2.

## 7. Vorsichtige Interpretation der Deduplizierung

Der Einzellauf liefert **keinen belastbaren Hinweis**, dass die entfernte redundante Verstärkung für die fachlich-didaktische Qualität oder die Grenztreue von H01 verhaltensrelevant war: Alle fünf Turns erfüllen die Rubrik vollständig, Drift bleibt bei 0, die gewählte Hauptlinie bleibt stabil und sämtliche turn-spezifischen Verbote werden eingehalten.

Für die Frageökonomie gibt es ein schwaches Beobachtungssignal: B1.3b stellt in H01.2 eine nicht erforderliche Rückfrage, während für B0, B1.1 Clean und B1.2 jeweils 0 unnötige Fragen berichtet sind. Aus einem einzelnen nicht kontrolliert replizierten Lauf lässt sich daraus jedoch keine kausale Wirkung der Deduplizierung ableiten. Die Frage kann ebenso stochastische Laufvariation oder Ausdruck des weiterhin funktionierenden Sparrings sein. Belastbar wäre eine Aussage erst nach mehreren vergleichbaren Wiederholungen beziehungsweise einem kontrollierten A/B-Vergleich.

Kurzurteil zur B1.3b-Hypothese:

- Entfernte redundante Verstärkung verhaltensrelevant: für H01 insgesamt nicht belegt; allenfalls schwaches Signal bei der Frageökonomie.
- Kritisches Sparring schwächer: nein.
- Frageökonomie schwächer: in diesem Lauf ja, geringfügig (eine unnötige Frage), kausal nicht zuordenbar.
- Führende Hauptlinie weniger stabil: nein.
- Gate- oder Auftragsgrenzen schlechter eingehalten: nein.

## 8. Technische Messgrundlage und Benchmarkgrenze

Die quantitative Messung erfolgte direkt aus demselben lokalen
Codex-Session-JSONL, das der Qualitätsauswertung zugrunde liegt:

- Session-ID: `01a0635b-7a02-7bc1-8d81-cf9cc673a03e`
- JSONL-Pfad: `/Users/matthias/.codex/sessions/2026/09/02/rollout-2026-09-02T20-22-14-01a0635b-7a02-7bc1-8d81-cf9cc673a03e.jsonl`
- H01.1-Nutzerprompt: `2026-09-02T18:22:20.653Z` (Ordinal 8)
- H01.5-Nutzerprompt: `2026-09-02T18:23:54.773Z` (Ordinal 66)
- abgeschlossene H01.5-Assistentenantwort: `2026-09-02T18:24:20.986Z` (Ordinal 71)
- letzter Usage-Event der H01.5-Antwort: `2026-09-02T18:24:21.009Z` (Ordinal 72)
- zugehöriges `task_complete`: `2026-09-02T18:24:21.014Z` (Ordinal 73, Turn-ID `01a0635d-0142-7122-b1f3-75d90d3b5781`)

Die Messgrenze reicht damit vom H01.1-Nutzerprompt einschließlich bis zum
`task_complete` der vollständig abgeschlossenen H01.5-Antwort einschließlich.
Das Sessionlog endet an dieser Stelle; spätere Nutzerprompts oder dadurch
ausgelöste Events existieren in dieser Session nicht.

Wie bei den früheren Läufen wurde pro `token_count`-Event ausschließlich
`info.last_token_usage` als einzelner Model Call ausgewertet und anschließend
summiert. `info.total_token_usage` ist dagegen der jeweils bereits kumulierte
Sessionstand und wurde nicht nochmals aufsummiert. Das Schema zeigt für jeden
Event:

`total_tokens = input_tokens + output_tokens`

Die `reasoning_output_tokens` sind somit bereits Bestandteil der
`output_tokens` und damit auch von `total_tokens`; sie wurden separat berichtet,
aber nicht zusätzlich auf Output oder Total addiert.

## 9. Einzelne Model-/Token-Events

| Nr. | Timestamp | Turn | Input | Cached Input | Uncached Input | Output | Reasoning | Total |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `2026-09-02T18:22:26.671Z` | H01.1 | 17.367 | 11.264 | 6.103 | 254 | 40 | 17.621 |
| 2 | `2026-09-02T18:22:30.290Z` | H01.1 | 21.033 | 11.264 | 9.769 | 129 | 9 | 21.162 |
| 3 | `2026-09-02T18:22:52.376Z` | H01.1 | 24.775 | 20.864 | 3.911 | 755 | 303 | 25.530 |
| 4 | `2026-09-02T18:23:06.501Z` | H01.2 | 25.757 | 24.576 | 1.181 | 464 | 67 | 26.221 |
| 5 | `2026-09-02T18:23:32.064Z` | H01.3 | 26.408 | 25.600 | 808 | 957 | 314 | 27.365 |
| 6 | `2026-09-02T18:23:45.639Z` | H01.4 | 27.580 | 26.240 | 1.340 | 464 | 52 | 28.044 |
| 7 | `2026-09-02T18:24:21.009Z` | H01.5 | 28.305 | 27.392 | 913 | 1.358 | 98 | 29.663 |
| **Kumulativ** |  | **7 Calls** | **171.225** | **147.200** | **24.025** | **4.381** | **883** | **175.606** |

Der kumulative Cached Share beträgt
`147.200 / 171.225 = 85,97 %`. Entsprechend entfallen 14,03 % des Inputs auf
uncached Input. Cached Input war weiterhin Bestandteil des Modellkontexts und
der ausgewiesenen Input- und Total-Usage; „cached“ bedeutet weder „kostenlos“
noch „nicht im Kontext“.

## 10. Tatsächliches Ladeverhalten

Das JSONL enthält während H01 genau zwei lokale Toolaufrufe, beide in H01.1.
Aus den protokollierten Befehlen und ihren Outputs ergibt sich folgende
Unterscheidung:

| Projektdatei | Status im H01-Lauf |
|---|---|
| `project_governance/plan_core.md` | tatsächlich vollständig gelesen |
| `project_governance/kdm_core.md` | tatsächlich vollständig gelesen |
| `ai_agents/master_agent.md` | tatsächlich vollständig gelesen |
| `ai_agents/didaktisches_qualitaetsmodell_core.md` | tatsächlich vollständig gelesen |
| `prompts/plan.md` | tatsächlich vollständig gelesen |
| `benchmark/inputs/H01_AGENT_INPUT.md` | tatsächlich vollständig als Fallkontext gelesen |

Der erste Aufruf las PLAN-Core, KDM-Core und Master-Agent; der zweite Aufruf las
DQM-Core, PLAN-Prompt und H01-Fallkontext. Nach diesen beiden Aufrufen gab es in
H01.2 bis H01.5 keine weiteren Tool- oder Dateizugriffe.

Die Prüfung auf unerwartete Lazy Loads ist negativ:

- `ai_agents/didaktisches_qualitaetsmodell.md` wurde nicht gelesen; der Pfad
  erschien lediglich in den gelesenen Core-Regeln.
- `project_governance/low_noise_response_patterns.md` wurde weder gelesen noch
  durch einen Toolaufruf geladen.
- `project_governance/agent_contract.md` wurde nicht gelesen; der Pfad wurde
  lediglich als inaktiver B0-/Research-Bestand in `plan_core.md` erwähnt.
- Produktions- und Finalisierungstemplates sowie die zugehörigen CHECK-,
  Literatur-, Emoji- und OER/OERSI-Regeln wurden nicht gelesen. Templatepfade
  waren nur in der automatisch bereitgestellten Repository-Regel als spätere
  Gate-Ziele erwähnt.
- Research-Dateien oder ein Research-Adapter wurden nicht gelesen. Research
  erschien ausschließlich als inaktive Regel beziehungsweise Pfadkontext.

Damit wurden alle fünf normalen PLAN-Pflichtdateien tatsächlich geladen, aber
keine der ausdrücklich zu prüfenden Lazy-Load-Gruppen.

## 11. Quantitativer Vergleich

B1.3a besitzt keinen H01-Lauf. Seine Usage-Felder bleiben deshalb bewusst leer;
es wird nur in der statischen Kontextentwicklung berücksichtigt.

| Kennzahl | B0 | B1.1 Clean | B1.2 | B1.3a | B1.3b |
|---|---:|---:|---:|---:|---:|
| Statischer Pflichtkontext (Bytes) | 130.407 | 64.672 | 37.116 | 34.700 | 29.416 |
| Input | 229.974 | 249.791 | 156.653 | – | **171.225** |
| Cached Input | 198.912 | 222.976 | 137.344 | – | **147.200** |
| Uncached Input | 31.062 | 26.815 | 19.309 | – | **24.025** |
| Output | 4.234 | 4.282 | 4.406 | – | **4.381** |
| Reasoning | 780 | 1.104 | 1.103 | – | **883** |
| Total | 234.208 | 254.073 | 161.059 | – | **175.606** |
| Model Calls | 7 | 8 | 6 | – | **7** |
| Cached Share | 86,49 % | 89,26 % | 87,68 % | – | **85,97 %** |

Die statische Byteentwicklung beträgt:

- B0 → B1.1: −50,41 %
- B1.1 → B1.2: −42,61 %
- B1.2 → B1.3a: −6,51 %
- B1.3a → B1.3b: −15,23 %
- insgesamt B0 → B1.3b: −77,44 %
- für die hier besonders relevante Strecke B1.2 → B1.3b: −20,75 %

### Veränderungen von B1.3b gegenüber den H01-Vergleichsläufen

| Kennzahl | gegenüber B0 | gegenüber B1.1 Clean | gegenüber B1.2 |
|---|---:|---:|---:|
| Input | −25,55 % | −31,45 % | +9,30 % |
| Cached Input | −26,00 % | −33,98 % | +7,18 % |
| Uncached Input | −22,65 % | −10,40 % | +24,42 % |
| Output | +3,47 % | +2,31 % | −0,57 % |
| Reasoning | +13,21 % | −20,02 % | −19,95 % |
| Total | −25,02 % | −30,88 % | +9,03 % |
| Model Calls | 7 → 7 (0,00 %) | 8 → 7 (−12,50 %) | 6 → 7 (+16,67 %) |

## 12. Methodisch vorsichtige Interpretation

1. **Statische Kontextreduktion.** B1.3b reduziert den statischen
   PLAN-Pflichtkontext gegenüber B1.2 um 7.700 Bytes beziehungsweise 20,75 %
   und gegenüber B1.3a nochmals um 5.284 Bytes beziehungsweise 15,23 %. Die
   zusätzliche Deduplizierung hat damit auf Dateiebene den beabsichtigten
   Reduktionseffekt. B1.3a ist mangels H01-Lauf darüber hinaus kein
   Usage-Vergleichspunkt.

2. **Kumulativer Input.** Trotz des kleineren statischen Pflichtkontexts liegt
   B1.3b beim kumulativen Input 9,30 % über B1.2. Gegenüber B0 und B1.1 Clean
   bleibt er deutlich niedriger. Eine statische Kontextreduktion übersetzt sich
   folglich in diesem Einzellauf nicht proportional in kumulierte Tokens.

3. **Uncached Input.** Gegenüber B0 sinkt der uncached Input um 22,65 % und
   gegenüber B1.1 Clean um 10,40 %. Gegenüber B1.2 steigt er jedoch um 24,42 %.
   Die Hypothese, die zusätzliche Deduplizierung habe gegenüber B1.2 auch den
   uncached Input reduziert, wird durch diesen Lauf nicht gestützt.

4. **Cache-Effekt.** 85,97 % des B1.3b-Inputs waren cached. Der Anteil liegt
   leicht unter B0 (86,49 %), B1.1 Clean (89,26 %) und B1.2 (87,68 %). Die hohe
   Cachequote erklärt, weshalb uncached und gesamter Input unterschiedlich
   reagieren können; sie beseitigt die gecachten Tokens aber weder aus dem
   Kontext noch aus der Usage.

5. **Output.** Mit 4.381 Outputtokens liegt B1.3b praktisch auf dem Niveau von
   B1.2 (−0,57 %), leicht über B0 (+3,47 %) und B1.1 Clean (+2,31 %). Es gibt
   kein auffälliges Signal einer veränderten sichtbaren Ausgabelänge.

6. **Reasoning.** Die 883 Reasoningtokens liegen knapp 20 % unter B1.1 Clean
   und B1.2, aber 13,21 % über B0. Reasoning ist eine Teilmenge des Outputs und
   darf nicht zusätzlich zu Total gerechnet werden. Laufvariation und
   Aufgabenbearbeitung sind plausible Einflussgrößen; eine kausale Zuordnung
   zur Deduplizierung ist nicht möglich.

7. **Model Calls.** B1.3b umfasst sieben Calls: drei in H01.1 aufgrund der zwei
   Datei-Leseunterbrechungen, danach je einen in H01.2 bis H01.5. Das sind gleich
   viele wie B0, einer weniger als B1.1 Clean und einer mehr als B1.2. Gerade
   gegenüber B1.2 trägt der zusätzliche Call zum höheren kumulativen Input und
   Total bei. Ob die Deduplizierung die Callzahl beeinflusst hat, lässt sich aus
   den Läufen nicht bestimmen; beobachtet wird nur die unterschiedliche
   Tool-/Call-Struktur.

Für die B1.3b-Hypothese lautet das vorsichtige Gesamturteil daher: Die weitere
Reduktion des statischen Kontexts ist direkt belegt. Eine Reduktion von
uncached Input oder kumulativem Input gegenüber B1.2 ist nicht eingetreten;
beide Werte stiegen, während die Callzahl von sechs auf sieben stieg. Diese
Veränderungen dürfen wegen unterschiedlicher Callzahl, Cacheverhalten und
stochastischer Laufvariation nicht automatisch kausal der Deduplizierung
zugeschrieben werden. Ein einzelner H01-Lauf erlaubt keine allgemeine
Effizienzbehauptung; dafür wären kontrollierte Wiederholungen mit vergleichbarer
Callstruktur erforderlich.
