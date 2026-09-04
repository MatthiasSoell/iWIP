# B1-Architektur- und Inhaltsaudit des KO-PLAN-/iWIP-Agenten

**Stand:** 2. September 2026  
**Auftrag:** Analyse des unveränderten B0-Systems; keine Implementierung und kein neuer Benchmark  
**Leitkriterium:** Qualität des professionellen Planungs- und Entscheidungsprozesses der Lehrperson dialogisch und ko-konstruktiv verbessern

**Status:** Historischer B0/B1-Entwicklungsnachweis; keine aktuelle Laufzeit- oder Steuerquelle. Fuer den geltenden Stand sind die in `AGENTS.md` genannten Cores massgeblich.

## 1. Executive Summary

KO-PLAN/B0 ist didaktisch und dialogisch ungewöhnlich robust, architektonisch aber stark dokumentzentriert und überkoppelt. Seine nachgewiesene Stärke liegt nicht in einer technisch ausgeführten State Machine, sondern in einer umfangreichen, mehrfach abgesicherten Promptarchitektur: klare menschliche Entscheidungsautonomie, eine führende didaktische Verdichtung, genau eine priorisierte Rückfrage, explizite Behandlung didaktischer Spannungen, Blog-first-Gates, Quellenintegrität und ein breites didaktisches Qualitätsmodell. Diese Kombination erklärt plausibel die in B0 beobachteten 5 × 15/15, Drift 0 und null unnötige Rückfragen. Die Redundanz ist daher nicht nur Ballast; sie wirkt teilweise als Sicherheitsverstärkung. Sie darf nur kontrolliert und regressionsgeprüft reduziert werden.

Der größte Pflichtkontext entsteht beim normalen Planungsstart durch die Adapterregel in `AGENTS.md`: Contract, Low-noise-Muster, Master-Agent, vollständiges DQM und Plan-Prompt werden immer geladen. Einschließlich Adapter sind das 2.127 Zeilen, etwa 15.140 Wörter und 130.407 Bytes. Rund vier Fünftel der Wörter entfallen allein auf Contract und DQM. Dieser Befund belegt hohes strukturelles Einsparpotenzial, aber nicht, welcher Anteil der B0-Tokenmessung durch welche Datei verursacht wurde; Cache, Chatverlauf und Plattformkontext bleiben Mitursachen.

Die tatsächliche Architektur ist eine deklarative Laufzeitarchitektur. Es gibt keinen im Repository implementierten ausführbaren Router, keinen maschinenpersistierten Planning State und keine technisch erzwungenen Gates. `AGENTS.md` lädt die fünf Pflichtmodule; das Modell interpretiert anschließend die in Markdown definierte State Machine. Die dokumentierte Absicht einer einzigen kanonischen Quelle ist nur teilweise erreicht. Der Contract ist zwar formal vorrangig, bündelt aber mindestens sieben Verantwortungsarten: Core-Haltung, Routing/State, Forschung, Produktionsregeln, Blog-/Reveal-/OER-Profile, QA/Finalisierung und sichtbare Antwortform. Innerhalb des Contracts werden zentrale Regeln mehrfach wiederholt; außerhalb replizieren Master, Plan, Check, Low-noise, Templates und Development Workflow dieselben Semantiken.

Für B1 sollte der Contract nicht pauschal gekürzt, sondern zunächst in Verantwortlichkeiten entkoppelt werden. Ein kleiner stabiler Core muss Rolle, Autonomie, Auftragstreue, Entscheidungsstabilität, Quellenintegrität, Rückfrageökonomie, Gate-Disziplin und Routing enthalten. Taskmodule sollten Planungsstart, Artefaktproduktion, Review/Finalisierung, Literaturpflege und Export abdecken. Blog, Reveal und OER/OERSI sind überwiegend Produktionsprofile beziehungsweise Artefaktspezifikationen, nicht normaler Planungskern. Forschung ist ein orthogonaler Adapter. Die Blog-Wissens- und Literaturbasis bleiben References. KBS, DJP und itslearning sind im heutigen Repository nicht als aktive Regelmodule implementiert und dürfen in B1 nicht aus dem Zielbild heraus erfunden werden.

Das DQM sollte nicht durch eine sehr kleine Checkliste ersetzt werden. Sein operativer Kern lässt sich jedoch auf sechs verknüpfte Fragen verdichten: Ziel-/Assessment-Passung; lernlogische statt additive Struktur; aktive, verstehende Auseinandersetzung; kognitive Tiefe und Aufgabenqualität; funktionale Reflexion/Transfer; Adaptivität auf plausibler diagnostischer Grundlage. Hinzu kommt bei einschlägigen sozioökonomischen Gegenständen Multiperspektivität und Zielkonfliktreflexion. Profile, Ablaufmodelle, Kontextausprägungen, Qualitätslisten, Schwachstellen, theoretische Erläuterungen und Literatur gehören überwiegend in DQM-Reference. Besonders riskant wäre die Entfernung der Unterscheidung von bloßer Aktivität und kognitiver Aktivierung, von Struktur- und Tiefenqualität sowie des Constructive Alignment.

Ein eigener KDM-Core muss keine neue Wissensbasis werden. Seine Prinzipien sind bereits vorhanden und sollten lediglich kanonisch zusammengeführt werden: Lehrperson entscheidet; Agent macht die wichtigste Spannung sichtbar; er führt mit einer begründeten Empfehlung; Alternativen bleiben knapp und entscheidungsrelevant; Rückfragen werden nur bei entscheidungsrelevanter Unsicherheit gestellt; bestätigte Entscheidungen bleiben stabil; Review führt nicht automatisch zur Reparatur; Auftrag und aktueller Task begrenzen den Dialog. Ein kompakter Planning State kann diese Stabilität unterstützen, indem er Kontext, Ziele, bestätigte Entscheidungen samt kurzer Begründung, offene Entscheidungen, aktuellen Task und Artefaktstatus hält. Der bestehende Forschungs-Trace ist dafür ungeeignet: Er ist Rohdatenprotokoll, kein Laufzeitgedächtnis.

Die beste erste B1-Variante ist konservativ: unveränderte Gate- und Autonomieregeln, kleiner normaler Planungs-Core, KDM-Kurzfassung, DQM-Core mit Links in das unveränderte vollständige DQM, sowie echtes Lazy Loading für Produktion, Finalisierung und Forschung. Noch kein neues Task-Feingranulat, keine Profile für nicht implementierte Plattformen, keine Learner Lens als Standard und kein Ersatz der Chat-Historie durch einen ungeprüften State. Diese Minimalvariante sollte anschließend mit demselben H01-Protokoll gegen B0 verglichen werden: Qualität, Drift, Rückfragen, Auftragstreue, Entscheidungsstabilität, Anschlussfähigkeit und Input-/Cachewerte. Erst nach bestandenem Regressionstest sollte ein Planning-State-Ablationstest folgen.

## 2. Methode, Evidenzgrenzen und Begriffe

Der Audit rekonstruiert ausschließlich den Repository-Stand. Das Development Journal wurde zuerst vollständig gelesen und als Entwicklungsdokumentation, nicht als Laufzeitinstruktion behandelt. Dateien unter `benchmark/evaluations/` wurden nicht gelesen. Es wurde kein Benchmark ausgeführt. Bestehende Dateien wurden nicht verändert.

Die Befunde unterscheiden drei Evidenzklassen:

- **A – implementiert:** im aktuellen Adapter oder in aktiven Laufzeitdokumenten tatsächlich als zu ladende beziehungsweise anzuwendende Regel vorhanden. „Implementiert“ bedeutet hier überwiegend promptseitig/deklarativ, nicht programmatisch erzwungen.
- **B – dokumentierte Absicht:** Zielbild oder Architekturbehauptung, insbesondere aus Development Journal, README oder Governance, für die noch kein technischer Mechanismus nachweisbar ist.
- **C – Empfehlung/Interpretation:** aus dem Audit abgeleitete B1-Option; noch keine bestehende Regel.

Die Klassifikation bedeutet:

- **CORE:** bei normalen Planungsdialogen dauerhaft nötig.
- **TASK:** nur für eine konkrete Tätigkeit nötig.
- **REFERENCE:** vertiefendes Wissen, bei Bedarf zu laden.
- **PROFILE:** kontext- oder artefaktspezifische Regel.
- **REDUNDANT:** ohne zusätzlichen Steuerungsnutzen doppelt oder weitgehend doppelt; „redundant“ bedeutet nicht automatisch gefahrlos löschbar.

## 3. Rekonstruktion der Ist-Architektur

### 3.1 Kompakte Architekturübersicht

```text
Plattformadapter
  AGENTS.md (Codex) / .github/copilot-instructions.md (Entwicklung/QA)
        |
        +-- normaler didaktischer PLAN: fünf Pflichtmodule
        |     1. agent_contract.md            normative Gesamtsteuerung
        |     2. low_noise_response_patterns  sichtbare Antwortmuster
        |     3. master_agent.md              Rolle/Dialog/Entscheidungslogik
        |     4. didaktisches_qualitaetsmodell DQM + Profile + Prüfraster
        |     5. prompts/plan.md               Einstiegsrouter
        |
        +-- ab BLOG GO: blog_template.md
        +-- ab REVEAL GO: reveal_template.md
        +-- bei FINAL: prompts/check.md + Emoji-/Literatur-Tasks + Technik/QA
        +-- on demand: Blog-Wissensbasis, Blog-Literaturbasis
        +-- nur /PLAN FORSCHUNG: Research-Regeln im Contract
```

Die einzige tatsächlich nachweisbare automatische Ladeentscheidung für den normalen PLAN-Start steht im Codex-Adapter `AGENTS.md:6-15`. Der Plan-Prompt bestätigt dieselbe Pflichtmenge (`prompts/plan.md:14-24`). Templates sind explizit lazy: Blog ab `BLOG GO`, Reveal ab `REVEAL GO`. Dagegen wird das vollständige DQM bereits beim ersten Planungszug geladen.

### 3.2 Einstiegspunkte

| Einstieg | Implementiertes Verhalten (A) | Dokumentierte Rolle (B) | Auditbewertung (C) |
|---|---|---|---|
| natürliche didaktische Planungsanfrage oder `/PLAN` | Adapter lädt fünf Pflichtmodule; `plan.md` routet deklarativ an Contract | Start in P1/P2 ohne Datei- oder Artefakterzeugung (`agent_contract.md:143-170`, `plan.md:36-63`) | Der Router ist semantisch, nicht ausführbar. Der Startprompt dupliziert viele Contract-Regeln. |
| `/PLAN FORSCHUNG` | gleiche Module plus sofortige, promptseitig verlangte Dateiinitalisierung (`agent_contract.md:68-141`; `plan.md:50-53`) | orthogonaler Forschungsmodus | Eigenes Task-/Adaptermodul; kein normaler Core. |
| `BLOG GO` | Gate im Contract; Blog-Template wird geladen (`agent_contract.md:170,242`; `plan.md:21-24`) | Beginn der publizierbaren Blog-Arbeitsdatei | sinnvoller Produktions-Task plus Blog-Profil. |
| `BLOG FINAL` | Contract, Check, Blog-Template, Literatur- und Emoji-Schritt, Build/Linkcheck, Wissensbasis-Hook | Finalisierung mit QA und Nachlauf | stark gekoppelte Orchestrierung; nicht normaler Planungs-Core. |
| `REVEAL GO` | Gate; Reveal-Template wird geladen; Ableitung nur aus finalem Blog | Reveal-Transformation | eigener Produktions-Task/Reveal-Profil. |
| `REVEAL FINAL` | Check, Emoji-Postprocessing, Build; ggf. Research-Exit | Finalisierung und Exit Action | eigener Review-/Final-Task. |
| `LITERATUR GO` / `LITERATUR RECHERCHE GO` | eigenständiger Prompt, formal bzw. recherchierend (`prompts/literatur.md:44-153`) | Literaturpflege | Task; Recherchemodus zusätzlich Reference/Toolregel. |

### 3.3 State Machine, Gates, Guards, Hooks und Exit Actions

**A – implementiert:** Die normative Beschreibung steht im Contract: P1–P5 (`agent_contract.md:43-66`), Statussignale (`143-156`), tabellarisches Zustandsmodell (`158-173`), Rücksprünge (`175-185`) und verbindliche Regeln (`228-265`). Gates sind `BLOG GO`, `BLOG FINAL`, `REVEAL GO`, `REVEAL FINAL`. Guards sind insbesondere sichtbarer Planungsstand, valider Blogentwurf, `draft: false`, finaler Blog als Reveal-Grundlage und vollständige Pflichtprüfungen. Hooks/Exit Actions sind der Wissensbasis-Anschluss nach `BLOG FINAL` sowie Research-Abschluss nach `REVEAL FINAL` beziehungsweise `blog_only`.

**B – dokumentierte Absicht:** Der Contract nennt dies „einzige normative Ablaufstruktur“ und „kompaktes Zustandsmodell“. Das Development Journal sieht künftig einen expliziten Planning State vor.

**C – Interpretation:** Die State Machine ist nicht technisch materialisiert. Kein Skript liest einen Zustand, erzwingt Transitionen oder speichert einen normalen Planungsfall. Das Modell muss Phase, Freigaben, Entscheidungen und Artefaktstatus aus Chat und Dateien rekonstruieren. Die Tabelle ist deshalb ein gutes Regelmodell, aber noch kein persistenter State.

### 3.4 Finalisierung und QA

Die heutige QA besteht aus vier Schichten:

1. Contract-DoD und Release-Gates (`agent_contract.md:267-273,317-420`).
2. DQM-Diagnose mit sechs Dimensionen (`prompts/check.md:54-71`, DQM-Prüfmatrix `1055-1070`).
3. artefaktspezifische Prüfung für Blog/Reveal inklusive Frontmatter und OER (`check.md:91-259`).
4. technische Nachläufe: Linkcheck, `hugo --minify`, Literatur-Normalisierung, Emoji-Postprocessing und ggf. Research-Finalisierung.

`check.md` bewertet nur und repariert nicht (`43-45`). Diese Trennung ist konzeptionell stark und sollte erhalten bleiben. Allerdings enthält Check zahlreiche Kopien von Template- und Contract-Regeln; die kanonische Quelle ist in der Praxis unklarer als behauptet.

### 3.5 Blog, Reveal, OER/OERSI und Forschung

- **Blog:** Primärartefakt; Frontmatter, Einstiegsblock, Zielgliederung und Visualisierungsregeln im Blog-Template. Produktion ab `BLOG GO`, Finalisierung über Contract/Check.
- **Reveal:** ausschließlich aus finalem Blog; Frontmatter und Folienstruktur im Reveal-Template. OER-Metadaten verboten.
- **OER/OERSI:** Blog-Frontmatter-Profil mit festen Hochschulmetadaten; Regeln kommen gleichzeitig in Template, Contract-Rule 10/22, Blog-DoD und Check vor.
- **Forschung:** vollständiges Subsystem im Contract (`68-141`) mit Initialisierung, vier Startdateien, Schemas, Snapshots, Kopien, Datenschutz und Sonderfällen. Es ist orthogonal gedacht, aber im wichtigsten Core-Dokument eingebettet.
- **Wissensbasis:** on-demand Reference (`agent_contract.md:215`) plus verpflichtend zu prüfender, aber optional zu übernehmender Hook nach `BLOG FINAL` (`261`).
- **Literaturbasis:** on-demand Reference (`216`); Literatur-Task ist separat.

### 3.6 Plattformadapter

- `AGENTS.md:1-23` ist der aktive Codex-Adapter und erzeugt den großen PLAN-Pflichtkontext.
- `.github/copilot-instructions.md:1-23` ist ausdrücklich Entwicklung/QA, nicht PLAN-Laufzeit. Es lädt Technik-Governance nur bei Bedarf.
- `project_governance/ai_copilot_instructions.md:1-12` ist ebenfalls Entwicklungs-/QA-Governance.
- Ein fobizz-, KBS-, DJP- oder itslearning-Laufzeitadapter ist im untersuchten Repository nicht vorhanden. Diese Kontexte erscheinen nur als B1-Zielbild im Journal und dürfen nicht als heutige Implementierung beschrieben werden.

## 4. Abhängigkeits- und Ladeübersicht

### 4.1 Normaler PLAN-Pflichtkontext

| Datei | Zeilen | Wörter | Bytes | heutige Ladeart | relative Entlastung bei Modularisierung |
|---|---:|---:|---:|---|---|
| `AGENTS.md` | 24 | 115 | 890 | Adapter, immer | gering; unverzichtbarer Einstieg |
| `agent_contract.md` | 458 | 6.875 | 60.987 | immer | hoch; großer Anteil ist Produktion/Forschung/QA |
| `low_noise_response_patterns.md` | 307 | 1.275 | 9.967 | immer | mittel; viele Beispiele und FINAL/Mikrofix/Forschung |
| `master_agent.md` | 113 | 1.213 | 10.291 | immer | mittel; erhebliche Contract-/Plan-Dopplung |
| `didaktisches_qualitaetsmodell.md` | 1.119 | 4.846 | 41.172 | immer | hoch; Theorie, Literatur und Spezialkontexte |
| `prompts/plan.md` | 106 | 816 | 7.100 | immer | mittel; Router wiederholt Contract und DQM-Core |
| **Summe** | **2.127** | **15.140** | **130.407** | | |

Die Zahlen sind Dateiumfang, keine Tokenprognose. Contract und DQM umfassen zusammen rund 77 % der Wörter dieses Pflichtsets. B0s 229.974 Inputtokens, davon 198.912 cached und 31.062 uncached, lassen sich nicht monokausal auf diese Dateien zurückführen. Sie stützen jedoch die Hypothese, dass wiederkehrender Kontext der Haupthebel ist: Ausgabe (4.234) und Reasoning (780) sind im Verhältnis klein.

### 4.2 Lazy/on demand

| Datei/Funktion | Ladebedingung | Bewertung |
|---|---|---|
| `blog_template.md` | ab `BLOG GO` | korrekt lazy; PROFILE/TASK |
| `reveal_template.md` | ab `REVEAL GO` | korrekt lazy; PROFILE/TASK |
| `prompts/check.md` | FINAL/Review | nicht normaler PLAN; TASK |
| `prompts/literatur.md` | explizit oder innerhalb `BLOG FINAL` | TASK |
| Emoji-Postprocessing-Prompts | jeweilige Finalisierung | TASK |
| `content_emoji_policy.md` | im Adapter pauschal Entwicklung/QA; artefaktbezogen relevant | PROFILE/REFERENCE; nicht Plan-Core |
| Blog-Wissensbasis | expliziter Blog-/OER-/Wissensbasisbedarf oder Hook | REFERENCE |
| Blog-Literaturbasis | Literaturbezug, Quellenprüfung, wissenschaftliche Ausarbeitung | REFERENCE |
| Repo-/CSS-/Workflow-Governance | Technik, QA, FINAL, Architektur | REFERENCE/TASK, nicht normaler PLAN |

## 5. Befunde zu `agent_contract.md`

### 5.1 Verantwortungsbündel

Der Contract bündelt:

| Verantwortungsart | Fundstellen | Klassifikation |
|---|---|---|
| Zielbild, Human-in-the-loop, führende Verdichtung | `7-21` | CORE/KDM |
| Glossar | `23-39` | REFERENCE; wenige Begriffe CORE |
| P1–P5 und Modus | `43-66` | CORE-Routing, teilweise Produktions-TASK |
| Forschungsmodus samt Dateischemata | `68-141` | TASK/PROFILE (Research Adapter) |
| Statussignale und Zustandsmodell | `143-185` | CORE-Routing plus TASK-Gates |
| Sichtbarkeit/Low-noise | `187-200`, `275-283`, `372-420` | CORE-Oberfläche plus FINAL-TASK; intern redundant |
| Dokumentrollen/Priorität | `202-223`, `435-449` | CORE-Architektur/REFERENCE |
| allgemeine Regeln | `228-265` | Mischung aus CORE, TASK, PROFILE, REDUNDANT |
| Konfliktregel | `287-313` | CORE, aber starres Ausgabeformat TASK-/Dialogdetail |
| DoD Planung | `317-327` | TASK: plan-refine/review; Kernheuristiken teilweise CORE |
| DoD Blog/Reveal | `330-369` | PROFILE/TASK |
| Finalausgabe | `372-420` | TASK |
| Systemgrenzen/Dry Run | `424-457` | REFERENCE/QA-TASK |

**Urteil:** Ja, der Contract bündelt zu viele Verantwortlichkeiten. Seine Größe entsteht weniger aus einer komplexen Planungs-State-Machine als aus Forschungsschemata, Produktionsprofilen, QA/DoD, sichtbaren Ausgabeformaten und wiederholten Absicherungen derselben Gates.

### 5.2 Für B0 wahrscheinlich unverzichtbare Drift- und Stabilitätsregeln

Diese Regeln sollten nicht leichtfertig entfernt oder nur indirekt referenziert werden:

- Human-in-the-loop und explizite Bearbeitung von Spannungen vor Artefakterstellung (`17-21`).
- P1/P2 strikt vor P3; keine Artefakte im ersten PLAN-Turn (`52-58`, `241`).
- führende empfohlene Verdichtung; Alternativen knapp, nachgeordnet und nur bei echter offener Lage (`21`, `241`, `252`, `255`).
- maximal eine entscheidende Rückfrage, keine parallele Abfragekette (`235`, `254-255`).
- Blog-first und Reveal nur aus finalem Blog (`232`, `243-244`).
- Quellenintegrität und keine erfundenen spezifischen Quellen (`233-235`).
- klare Unterscheidung produktiver Spannung versus harter DQM-Konflikt (`287-313`).
- explizite Nutzerfreigaben/Gates und Vorrang eindeutiger Statussignale (`147-156`, `166-181`, `254`).
- Fortschritt vor Absicherung, aber ohne Gate-/Pflichtprüfungsumgehung (`265`).
- Low-noise: Ergebnis/Diagnose/Frage statt interner Prozessrhetorik (`187-200`, `275-283`).

Diese Regeln erklären plausibel Auftragstreue, wenige Rückfragen, keine vorzeitige Produktion und Entscheidungsstabilität. Ihre Redundanz kann zur B0-Robustheit beigetragen haben. Zusammenführung deshalb Risiko **mittel bis hoch**, solange kein Regressionstest vorliegt.

### 5.3 Verschiebekandidaten

- Forschung `68-141` in einen Research Adapter: hoher Kontextgewinn, niedriges Risiko für Standard-PLAN, mittleres Risiko für Forschungsfälle.
- Blog-/Reveal-/OER-Regeln `237-250`, `330-369` in Artefaktprofile/Templates/Validator-Spezifikationen: hoher Gewinn, mittleres Risiko wegen Gate-/DoD-Kopplung.
- Finalausgabe `372-420` in Final-Check-Task: mittlerer Gewinn, niedrig bis mittel.
- Systemgrenzen/Dry Run `424-457` in Plattform-/QA-Reference: geringer bis mittlerer Gewinn, niedrig.
- starre Konfliktblock-Wortlaute `292-309` als Dialog-Pattern referenzieren, die Konfliktsemantik aber im Core behalten: geringer Gewinn, mittleres Risiko.

## 6. Befunde zu `master_agent.md`

Der Master-Agent enthält wichtige Identitäts- und Dialogelemente, ist aber kein klar isoliertes Rollenmodul.

- **CORE:** Rolle und Arbeitsfokus (`11-32`); fachliche Diagnose und ko-kreative Führung (`34-49`); DQM als Gesprächsfilter, zentrale Spannung, profilsensitive Einordnung und Lernhürden als Annahmen (`67-78`); Quellenintegrität (`80-84`); Umgang mit Unsicherheit (`89-96`).
- **TASK/PROFILE:** Blog-first-Textarbeit, H2/H3, Blogsprache, `BLOG GO` (`53-65`); externe Linkformatierung und `do-not-touch` (`85-86`).
- **REFERENCE:** historische Inspirationsquellen (`98-114`).
- **REDUNDANT:** führende Verdichtung/Alternativen (`36-39`, `72-73`, `91-92`) kopiert Contract/Plan; Fortschritt vor Absicherung (`41`); Light Operations (`42`); State/Gates (`46`); Blog-first (`57-63`); Quellenneuerfindung (`82-84`); Konfliktregel (`95-96`).

Empfehlung: Master-Agent künftig auf professionelle Rolle, Dialoghaltung und didaktische Entscheidungslogik begrenzen. Artefaktregeln in Tasks/Profile, Gate- und Sichtbarkeitsregeln in Core/KDM referenzieren. Erwarteter Nutzen: mittlere Kontextreduktion und klarere Ownership; Risiko mittel, weil die wiederholte Dialoglogik vermutlich stabilisierend wirkt.

## 7. Tiefenanalyse des DQM

### 7.1 Funktionsschichten

| DQM-Bereich | Fundstelle | Funktion | Klassifikation |
|---|---|---|---|
| Nutzungsprinzipien | `15-43` | heuristischer Status, keine Scheinsicherheit, Mindestbeachtung | DQM-CORE; Konfliktverweis redundant |
| Quellenkanon | `45-72` | Theorie-/Pflegebegründung | DQM-REFERENCE |
| sozioökonomisches Fachverständnis | `76-105` | fachlicher Leitanker, Multiperspektivität/Zielkonflikte | PROFILE/REFERENCE; bei einschlägigem Thema DQM-CORE |
| Zielorientierung: Grundsatz + Alignment | `111-156` | beobachtbare Ziele, Niveau, Zeit, Ziel-Aktivität-Prüfung | DQM-CORE |
| berufliche/erweiterte Kompetenz | `160-181` | Spezialkontexte | PROFILE/REFERENCE |
| Ziel-Qualitätslisten/Schwachstellen/Referenzen | `185-213` | Review und Vertiefung | TASK/REFERENCE; teilweise redundant zum Grundsatz |
| Strukturierung: Grundsatz | `215-230` | lernlogisch, funktional, nicht additiv | DQM-CORE |
| Ablaufmodelle | `232-287` | problemorientiert, vollständige Handlung, klassische Phasen | REFERENCE/PROFILE |
| Hochschulprogression | `291-305` | Bachelor/Master | PROFILE |
| Struktur-Listen | `315-341` | Review/Vertiefung | TASK/REFERENCE |
| Lernverständnis: Grundsatz, Aktivität, Vorwissen, Tiefe | `343-425` | aktives Verstehen statt Rezeption/Beschäftigung | DQM-CORE |
| Motivation, Kontext, Lehrperson | `393-460` | situationsabhängige Vertiefung | REFERENCE/PROFILE |
| Lernverständnis-Listen | `464-492` | Review/Vertiefung | TASK/REFERENCE |
| Lernqualität: Grundsatz, kognitive Aktivierung, Aufgaben | `494-560` | konkrete Tiefenqualität | DQM-CORE |
| Organisation, Feedback, Assessment, Fachspezifik | `564-618` | task-/kontextabhängig | TASK/REFERENCE; Alignment teilweise redundant |
| Lernqualitätslisten | `628-657` | Review/Vertiefung | TASK/REFERENCE |
| Reflexion: Grundsatz/Funktion | `659-700` | funktional integrierte Reflexion/Transfer | DQM-CORE |
| zeitliche/Lehrkräfte-/Zyklusausprägung | `704-739` | Spezialvertiefung | REFERENCE/PROFILE |
| Reflexionslisten | `747-772` | Review/Vertiefung | TASK/REFERENCE |
| Adaptivität: Grundsatz/Diagnose | `774-817` | Unterschiede plausibel berücksichtigen, keine Scheindiagnose | DQM-CORE |
| Differenzierung/Prozess/Lehrperson/KI | `821-869` | konkrete Spezialausprägungen | TASK/REFERENCE/PROFILE |
| Adaptivitätslisten | `879-903` | Review/Vertiefung | TASK/REFERENCE |
| Profile A–C | `907-1018` | Gewichtungskonfigurationen | PROFILE; Default-Regel im Contract |
| Querschnittsprinzipien | `1022-1051` | synthetische Zusatzheuristik | gemischt: Fundierung/Methodenbegründung CORE; OER PROFILE; Rest REFERENCE |
| kompakte Prüfmatrix | `1055-1070` | Review-Raster | TASK; starke Basis für DQM-Core |
| Literatur | `1074-1119` | Quellenreferenz | REFERENCE |

### 7.2 Operative Kernheuristiken

Bei fast jeder Planung müssen präsent sein:

1. **Kohärenz:** Passen beobachtbare, realistische Ziele zu Inhalten, Lernaktivitäten und – falls relevant – Assessment? (`113-156`, `134-140`, `602-605`)
2. **Lernlogik:** Bilden Phasen eine funktionale, zeitlich plausible Lernbewegung statt einer Methodenaddition? (`215-230`, `315-332`)
3. **Aktives Verstehen:** Was tun und denken Lernende tatsächlich; geht es über Rezeption oder bloße Beschäftigung hinaus? (`343-389`, `464-482`)
4. **Kognitive Tiefe/Aufgabenqualität:** Verlangen Aufgaben Begründen, Vergleichen, Anwenden, Entscheiden oder Transfer in fachlich angemessener Weise? (`494-560`, `609-618`)
5. **Reflexion/Transfer:** Hat Reflexion eine inhaltliche Funktion und wirkt sie auf Verstehen, Urteil oder zukünftiges Handeln, statt additiv zu sein? (`659-700`, `747-764`)
6. **Adaptivität ohne Scheinsicherheit:** Sind relevante Voraussetzungen/Hürden als plausible Annahmen berücksichtigt und gibt es angemessene Hilfen/Zugänge? (`24-27`, `774-817`)
7. **Fach-/Kontextspezifik:** Ist die fachliche Denk- und Handlungslogik gewahrt; bei sozioökonomischen Gegenständen werden Perspektiven, Interessen und Zielkonflikte nicht instrumentell verkürzt? (`76-97`, `609-618`)

### 7.3 DQM-CORE-Kandidat (noch keine Zieldatei)

| Kernheuristik | Verweis in vollständiges DQM | Kompressionsrisiko |
|---|---|---|
| Ziele–Inhalte–Aktivitäten–Assessment kohärent und zeitlich/niveaubezogen | `111-156`, `185-203`, `591-605` | **hoch**, wenn Assessment oder Anspruchsniveau verschwinden |
| lernlogische, funktionale Struktur statt additiver Methodenfolge | `215-341` | **mittel**; Ablaufmodelle können lazy sein |
| Lernende aktivieren: Denken und Verstehen statt nur Rezeption/Beschäftigung | `343-425`, `464-482` | **hoch**, zentrale Qualitätsdifferenz |
| Aufgaben erzeugen fachlich angemessene kognitive Tiefe, Anwendung/Urteil/Transfer | `494-560`, `609-618` | **hoch** |
| Reflexion funktional mit Inhalt, Lernen und künftigem Handeln verbinden | `659-764` | **mittel bis hoch** |
| Voraussetzungen/Hürden nur plausibel diagnostizieren und Unterstützung adaptiv planen | `24-27`, `774-895` | **hoch**, wegen Scheinsicherheits- und Inklusionsrisiko |
| Kontext-/Fachlogik prüfen; einschlägig multiperspektivisch und zielkonfliktsensibel | `76-105`, `609-618` | **hoch** für sozioökonomische Themen, sonst profilabhängig |

### 7.4 DQM-REFERENCE-Kandidat

Reference bleiben sollten: vollständiger Quellenkanon und Literatur; Kompetenztaxonomien; Ablaufmodelle; berufliche doppelte Zielorientierung; Bachelor-/Master-Progression; Motivationstheorie; Rollen- und Scaffolding-Ausführungen; Feedbackmodell; Formen und Zeitpunkte der Reflexion; konkrete Differenzierungsformen; KI-Adaptivität; Profile A–C; Qualitäts- und Schwachstellenlisten für Reviews.

### 7.5 Redundanz und Erklärungsanteile

Die sechs Dimensionen folgen jeweils einem wiederkehrenden Muster aus Grundsatz, Erläuterung, Kontext, Profilhinweis, Qualitätskriterien, Schwachstellen und Referenzen. Das ist als Wissensbasis sinnvoll, als permanenter Laufzeitprompt aber redundant. Besonders groß ist die semantische Überlappung von „Lernverständnis“ und „Lernqualität“: Aktivierung, Tiefenlernen, Transfer und Reproduktionskritik erscheinen mehrfach (`343-425`, `464-482`, `494-560`, `628-647`). Beide Dimensionen sollten dennoch nicht vorschnell verschmolzen werden: Die produktive Unterscheidung lautet „angenommenes Lernverständnis“ versus „Qualität konkreter Aufgaben/Interaktionen“.

Erläuterung/Begründung statt operativer Regel sind vor allem Theorieeinführungen („Didaktischer Bezug“), Quellenkanon, Leitreferenzen und Literatur. Diese sind wissenschaftlich wertvoll und sollten erhalten, aber nicht dauerhaft geladen werden.

Nicht ohne empirische Prüfung entfernen: Profilgewichtung; DQM-Mindestbeachtung; Lernhürden als plausible Annahmen; Constructive Alignment; kognitive Aktivierung; fach-/domänenspezifische Lernqualität; funktionale Reflexion; Adaptivität; sozioökonomische Multiperspektivität für einschlägige Fälle.

## 8. Befunde zu `low_noise_response_patterns.md`

Die Datei ist nützlich als Style-Reference, aber zu breit für jeden PLAN-Turn.

- **CORE/KDM:** Zielbild und Grundprinzipien (`11-47`), PLAN-Heuristik (`75-112`).
- **TASK:** FINAL (`116-148`), Mikrofix (`152-175`), Forschung (`179-199`).
- **REFERENCE:** positive/negative Beispiele (`203-283`), Grenzfälle und Begründung (`287-308`).
- **REDUNDANT:** Sichtbar/unsichtbar (`51-71`) wiederholt Contract `187-200`; PLAN-Schema wiederholt Contract `241` und Plan-Prompt `54-78`; Final-Summary wiederholt Contract `372-420`; Research-Sichtbarkeit wiederholt Contract `198,391`.

Empfehlung: Im normalen Core nur „Ergebnis/Diagnose zuerst; eine priorisierte Frage; Prozessmechanik unsichtbar; fachliche Erklärung bleibt erlaubt“. PLAN-/FINAL-/Mikrofix-/Research-Muster taskbezogen laden. Risiko niedrig bis mittel, solange die vier Grundsätze und das erste PLAN-Verhalten regressionserprobt erhalten bleiben.

## 9. Relevante Befunde zu weiteren Dateien

### `prompts/plan.md`

Der Router enthält echte Einstiegssemantik, wiederholt aber auf 106 Zeilen große Teile von Contract, Master und DQM. CORE/TASK-relevant sind nur: Anliegen und Kontext nutzen; keine Standardvollabfrage (`42-46`); Modus erkennen und handoff (`48-53`); erster Zug als kompakte Verdichtung mit höchstens einer entscheidenden Frage (`54-63`); selektive Kontextfragen (`65-68`). Die DQM-Kurzfassung `87-98` ist bereits ein brauchbarer Vorläufer des DQM-Core, allerdings ohne explizites Assessment und Entscheidungsstabilität.

### `prompts/check.md`

Check ist ein klarer Review-/Final-Task und sollte nicht im normalen PLAN-Kontext liegen. Positiv sind reine Bewertung ohne Reparatur (`43-45`), Trennung von Blocker/Warnung (`35-48`) und Soft-Heuristiken ohne Hard Fail (`73-88`). Problematisch ist die vollständige Wiederholung zahlreicher Blog-/Reveal-/Frontmatter-/OER-Regeln (`91-259`) sowie der Contract-Ausgabeordnung (`262-299`). Eine spätere Validator-Spezifikation sollte Templatefelder mechanisch prüfen, während Check nur Kategorien, Severity und didaktische Lens definiert.

### Templates

Blog- und Reveal-Templates sind korrekt lazy, vermischen aber Strukturvorlage und Validierungsregeln. Sie sind heute die sinnvollste kanonische Quelle für konkrete Frontmatter-Schemata, Zielgliederung und Visualisierungsmuster. Contract und Check sollten diese Regeln referenzieren, nicht kopieren. Risiko mittel, da maschinelle Validierung erst noch fehlt.

### Literatur, Emoji, Wissensbasis

- `prompts/literatur.md` ist ein gut abgrenzbarer Task. Quellenneuerfindungsverbot überschneidet sich sinnvoll mit Core; konkrete Link-/APA-Regeln sind Task.
- Emoji-Prompts sind technische Postprocessing-Tasks. Die Policy ist Artefaktprofil/Reference, kein Plan-Core.
- Blog-Wissensbasis und Blog-Literaturbasis sind nach Contract on demand. Ihre Einbindung ist korrekt; sie wurden für diesen Audit nur hinsichtlich Struktur, Status und Ladebedingungen, nicht vollständig semantisch ausgewertet.

### Entwicklungs- und Repository-Governance

`.github/copilot-instructions.md`, `ai_copilot_instructions.md`, `repo_architecture.md` und `development_workflow.md` trennen Entwicklung/QA ausdrücklich vom normalen PLAN. Das ist konzeptionell richtig. Der Development Workflow dupliziert jedoch zur Testbeschreibung zahlreiche Laufzeitregeln (`development_workflow.md:68-88,96-172`). Als QA-Erwartung ist dies nachvollziehbar, erhöht aber Wartungsrisiko. Künftig sollten Testfälle auf Regel-IDs oder kanonische Spezifikationen verweisen.

## 10. CORE/TASK/REFERENCE/PROFILE/REDUNDANT-Matrix der Hauptdateien

| Datei / Abschnitt | Klasse | Begründung / Fundstelle |
|---|---|---|
| Contract Zielbild Human-in-the-loop | CORE | Dialogidentität und Autonomie, `7-21` |
| Contract Glossar | REFERENCE | Definitionshilfe, `23-39`; nur Gate/Mode-Begriffe im Core |
| Contract P1/P2 und Freigabegrundsatz | CORE | Drift-/Produktionsschutz, `43-58,241` |
| Contract P3–P5 | TASK | Produktion/Finalisierung, `56-58` |
| Contract Forschung | TASK/PROFILE | nur `/PLAN FORSCHUNG`, `68-141` |
| Contract Status/Gates | CORE + TASK | Erkennung dauerhaft; konkrete Produktion taskbezogen, `143-185` |
| Contract Sichtbarkeit | CORE | ruhige Dialogoberfläche, `187-200` |
| Contract Dokumentrollen/Priorität | REFERENCE/CORE | Architekturauflösung, `202-223,435-443` |
| Contract Quellen/Rückfrage/Autonomie | CORE | `233-236,252-255,265` |
| Contract Frontmatter/OER/Reveal/Bildpfade | PROFILE/TASK | `237-250,259,262` |
| Contract Konfliktsemantik | CORE | `287-313` |
| Contract DoD/Finalausgaben | TASK | `317-420` |
| Master Rolle/Dialog/Spannungen/Unsicherheit | CORE/KDM | `11-49,67-96` |
| Master Blog-/Artefaktregeln | TASK/PROFILE | `53-65,80-87` |
| Master Hintergrund | REFERENCE | `98-114` |
| DQM Kernheuristiken | CORE | siehe Kapitel 7.3 |
| DQM Theorie, Modelle, Listen, Literatur | REFERENCE | siehe Kapitel 7.4 |
| DQM Profile A–C | PROFILE | `907-1018` |
| Low-noise Grundprinzip + PLAN | CORE/KDM | `11-47,75-112` |
| Low-noise FINAL/Mikrofix/Forschung | TASK | `116-199` |
| Low-noise Beispiele | REFERENCE | `203-308` |
| Plan Router/Handoff | TASK (Start) | `30-68` |
| Plan DQM-Kurzheuristik | CORE, heute doppelt | `87-98` |
| Check vollständig | TASK | Final-/Review-Pfad, `1-299` |
| Templates | PROFILE/TASK | ab Artefaktgate |
| Emoji Policy | PROFILE/REFERENCE | Artefaktdarstellung |
| Wissens-/Literaturbasis | REFERENCE | on demand |
| wiederholte Gates, Alternativen, Sichtbarkeit, Finalschemata | REDUNDANT | Matrix in Kapitel 11 |

## 11. Redundanzmatrix

| Regel | Fundstellen | kanonische Quelle heute | empfohlene kanonische Quelle | Risiko bei Zusammenführung |
|---|---|---|---|---|
| Human-in-the-loop/kritisches Sparring | Contract `17-21`; Master `69-78,89-96`; DQM Nutzungsprinzipien | Contract | KDM/Core | **hoch**: trägt B0-Dialogqualität |
| führende Verdichtung + begrenzte Alternativen | Contract `21,241,252,255`; Master `37,72-73,92`; Low-noise `39,75-112`; Plan `54-78`; Workflow `86,140` | Contract | KDM-Core; Tasks referenzieren | **hoch** |
| maximal eine priorisierte Rückfrage | Contract `235,254-255`; Master `38,91-94`; Low-noise `38,55,86`; Plan `42-46,54,65-68` | Contract | KDM-Core | **hoch** |
| keine Artefakterstellung im ersten PLAN | Contract `145,168,241,388`; Plan `54-63`; Workflow `138-142` | Contract | Core Gate-Spezifikation | **hoch** |
| State/Gates/Statussignale | Contract `143-185,228,241-246,254`; Master `46,57-63`; Plan `48-60`; Workflow `79-87,108-157` | Contract | Core-Router + Task-Guards | **hoch** |
| Blog-first/Reveal nur aus finalem Blog | Contract `9-15,151-153,172-173,232,243-244,355-359`; Master `55-64`; Plan `58`; Reveal Template `8`; Check `185-191` | Contract | Artefaktpipeline im Core; Details in Tasks | **hoch** |
| Quellen nicht erfinden | Contract `233-235`; Master `82-84`; Literatur `24-40,84-88,100-131`; Check `103` | Contract | Core-Quellenintegrität; Taskdetails Literatur | **hoch** |
| Low-noise/Sichtbarkeit | Contract `187-200,252,260,275-283,372-420`; Master `34-42`; Low-noise nahezu vollständig; Plan `56-57`; Check `46-48,262-299` | Contract | KDM-Core + taskbezogene Antwortmuster | **mittel bis hoch** |
| Profil A Default/Profilgewichtung | Contract `236,322`; Master `69-76`; Plan `80-85`; Check `68-70`; DQM `907-1018` | Default Contract, Gewichte DQM | Core enthält nur Auswahl/default; Profilmodul enthält Gewichte | **mittel** |
| DQM-Konflikt | Contract `287-313`; Master `72,95-96`; DQM `34-36`; Plan implizit | Contract | KDM/Core Konfliktsemantik; DQM diagnostiziert | **hoch** |
| Forschungsmodus | Contract `26,68-141,146,153,162-183,198,244,251,263-264,389-391`; Plan `51-53`; Check `287-289`; Workflow `85,142,155`; Repo `118-137` | Contract | Research Adapter; Core nur Aktivierung/Routing | **niedrig** für Standard, **mittel** für Forschung |
| Wissensbasis-Hook | Contract `164,171,185,215,261,347,406`; Low-noise `58,127,140-143,247-257`; Check `275-276`; Workflow `87,152` | Contract | Blog-Final-Task/Hook-Spezifikation | **mittel** |
| Final Summary | Contract `374-420`; Low-noise `129-148`; Check `262-299` | Contract | Final-Task, Low-noise referenziert | **niedrig bis mittel** |
| Blog-Frontmatter/OER | Contract `237,247-249,334-347`; Blog Template `19-125`; Check `137-175` | formal Contract, praktisch Template | Blog-Schema/Template als kanonische Quelle; Validator liest es | **mittel** |
| Reveal-Frontmatter/OER-Verbot/PDF | Contract `238-250,353-369`; Reveal Template `19-90`; Check `228-259` | formal Contract, praktisch Template | Reveal-Schema/Template | **mittel** |
| Visualisierungs-/Bildquellenregeln | Contract `343,368`; Templates `243-262`/`210-229`; Check `113-114,198-200` | Contract/Templates konkurrieren | jeweiliges Artefaktprofil | **mittel** |
| Emoji-Regeln | Contract `259,344,365`; Policy vollständig; Templates; Check; Emoji-Prompts | Emoji Policy | Emoji Policy + Postprocessing Task | **niedrig** |
| DQM-Qualitätskriterien/Schwachstellen/Prüfmatrix | pro Dimension + `1055-1070`; Plan `87-98`; Check `54-71` | DQM | DQM-Core für Planung, DQM-Review-Lens für Prüfung | **hoch** bei zu starker Kompression |

Widersprüche sind überwiegend Verantwortungs- und Granularitätskonflikte, keine harten logischen Gegensätze. Auffällig sind jedoch:

- Contract nennt DQM „einziges didaktisches Referenzmodell“, während Plan bereits eine eigene verdichtete operative Heuristik enthält.
- Contract erklärt Templates als nachgeordnet, kopiert aber ihre Detailregeln. Änderungen können divergieren.
- Contract nennt Forschungsartefakte „schlank“, definiert zugleich umfangreiche Schemas und viele Wiederholungen.
- DQM sagt, keine Dimension solle fehlen (`29-32`), während Profil C Lernverständnis/Reflexion niedrig gewichtet; das ist vereinbar, aber leicht als Erlaubnis zur Vernachlässigung misszuverstehen.
- `check.md` verlangt bei Blogartefakten alle OER-Pflichtfelder als Blocker (`161-166`), obwohl der Contract die Vollpflicht konditional an `draft: false` und `oer.is_oer: true` bindet (`249`). Der Check-Kontext ist FINAL, sollte diese Bedingung aber explizit und konsistent halten.

## 12. Kandidat für einen kleinen KDM-Core

Die Prinzipien sind bereits vorhanden; ein neues Großmodell ist nicht nötig.

1. **Autonomie:** Die Lehrperson entscheidet. KO-PLAN diagnostiziert, begründet und dokumentiert, überschreibt Entscheidungen aber nicht ungefragt. Grundlage: Contract `17-21,311`; Journal Leitidee.
2. **Relevante Spannung zuerst:** Benenne höchstens die wichtigste didaktische Spannung als konkreten Ziel-Mittel-Zusammenhang. Grundlage: Contract `252,287-290`; Master `72`.
3. **Führende Empfehlung:** Gib eine begründete Verdichtung; zeige nur entscheidungsrelevante Alternativen kurz und nachgeordnet. Grundlage: Contract `21,241,255`; Low-noise `36-47`.
4. **Rückfrageökonomie:** Frage nur, wenn eine wesentliche Entscheidung nicht tragfähig ableitbar ist; dann genau die nächste entscheidende Frage. Grundlage: Contract `235,254-255`; Plan `42-46`.
5. **Entscheidungsstabilität:** Bestätigte Ziele, Prioritäten, Constraints und Overrides bleiben gültig, bis die Lehrperson sie ändert oder ein klarer Konflikt sichtbar gemacht wird. Heute nur indirekt über Gates, Overrides und Anschlussfähigkeit vorhanden; im Journal explizit.
6. **Kritisches Sparring statt Reparatur:** Review-Befunde führen zu Konsequenzen/Optionen, nicht automatisch zu Änderungen. Heute in Check `43-45` und Konfliktregel angelegt; Journal explizit.
7. **Auftragstreue und Proportionalität:** Bleibe beim aktuellen Task; vermeide vorzeitige Artefakte, unnötige Komplexität und Prozessrhetorik. Grundlage: Contract `241,245,252,265`; Low-noise.
8. **Begründete Anschlussfähigkeit:** Halte Entscheidung, kurze Begründung, offene Frage und nächsten sinnvollen Schritt konsistent. Heute verteilt; Kandidat für State-Unterstützung.

Kompressionsrisiko: **hoch**, wenn KDM nur als Stilregel formuliert wird. Es muss Entscheidungsautonomie, Spannung, Begründung, Stabilität und Taskgrenze gemeinsam enthalten.

## 13. Kandidat für Planning-State-Inhalte

Heute muss das Modell aus Chat, aktuellen Dateien und Statussignalen rekonstruieren: Arbeitsmodus, Phase, Zielgruppe/Rahmen, Thema, Profil, Leitfrage, Ziele, Schwerpunkte, freigegebene Entscheidungen, DQM-Konflikte/Overrides, offene Fragen, Existenz/Finalität von Blog und Reveal sowie Research-Status.

### Zwingend speichern

| Feldgruppe | Inhalt | Grund |
|---|---|---|
| Fallkontext | Zielgruppe, Setting, Zeit, harte Rahmenbedingungen | verhindert Wiederholungsfragen und Fehlplanung |
| Planungsziel | Zweck, vorläufige/finale Leitfrage, priorisierte Ziele | hält Hauptlinie stabil |
| bestätigte Entscheidungen | Entscheidung + knappe Nutzer-/Fachbegründung + Status bestätigt/vorläufig | Kern der Entscheidungsstabilität |
| offene Entscheidungen | nur entscheidungsrelevante offene Punkte | steuert nächste Frage |
| aktueller Task/Phase | planning, blog production, review, reveal usw. + Gate-Status | verhindert Drift und vorzeitige Artefakte |
| Artefaktstatus | Pfad, vorhanden/working/final, Quelle der Ableitung | sichert Blog-first und Finalisierung |
| bewusste Overrides | abweichende Nutzervorgabe + dokumentierte Konsequenz | bewahrt Autonomie und Konfliktklärung |

### Optional speichern

- verworfene Optionen nur, wenn sie später wahrscheinlich wieder relevant werden oder eine Entscheidung erklären;
- Quellenbasis auf Identifikatorebene, wenn sie die Planung einschränkt;
- Profil nur, wenn tatsächlich gewählt/entscheidungsrelevant;
- relevante DQM-Spannung als kurze Diagnose, nicht als vollständiger Prüfbericht;
- nächster sinnvoller Schritt.

### Nicht speichern

- vollständigen Chattext;
- allgemeines DQM-Wissen;
- interne Tool-, Build- oder Routingprotokolle;
- Forschungszählwerte und technische Auditspur;
- hypothetische Lernendeneigenschaften als Tatsachen;
- jede kurz erwogene, folgenlose Variante.

Ein State könnte Wiederholungen zu Kontext, Profil, Gate und Anschlussfähigkeit vereinfachen. Er ersetzt aber weder kanonische Regeln noch Research Trace. Risiko **hoch**, wenn State-Updates unzuverlässig sind oder Chat-Historie zu früh abgeschnitten wird. Deshalb zunächst Shadow State/Ablation, nicht sofortiger Ersatz.

## 14. Vorgeschlagene Tasks und Profiles

Die im Journal vorgeschlagene Liste ist zu feingranular für B1. `analyse`, `goals`, `content`, `learning-activities` und `assessment` sind eng gekoppelte Denkoperationen; getrennte Tasks würden häufiges Routing und State-Handoffs erzeugen.

### Empfohlene erste Task-Granularität

| Task | Umfang | Begründung |
|---|---|---|
| `plan` | Intake, Analyse, Ziele, Inhalte, Lernaktivitäten, Assessment und Verdichtung | kohärenter professioneller Planungsprozess; DQM-Core durchgängig nötig |
| `plan-refine` | bestehende Planung prüfen, Spannung fokussieren, Entscheidung nachschärfen | anderes Eingangsmaterial, aber gleicher KDM/DQM-Core |
| `blog-produce` | `BLOG GO`, Blogausarbeitung, Blogprofil/Template | klarer Artefaktwechsel |
| `blog-finalize` | didaktischer/formaler Review, Literatur, Emoji, Build, Hook | eigene Orchestrierung; Check repariert nicht automatisch |
| `reveal-produce` | `REVEAL GO`, Transformation aus finalem Blog | klarer Artefaktwechsel |
| `reveal-finalize` | Abgleich, Formalprüfung, Emoji/Build, Research-Exit | eigene QA/Exit-Logik |
| `literature` | formale Pflege oder explizite Recherche | bereits separat implementiert |
| `light-edit` | proportionale Mikro-/Fokusänderung | bestehende Contract-Kategorie |
| `review` | optionaler didaktischer Perspektivwechsel ohne Produktion | für DQM-/Learner-Lens |

`export` ist heute kein eigenständiger didaktischer Task; PDF-Export ist Reveal-Produktions-/Finalisierungsdetail. `final-check` ist Teil der beiden Finalize-Tasks. Ein separates `intake` lohnt sich erst, wenn empirisch komplexe Fälle wiederholt strukturiertes Intake benötigen.

### Profiles

| möglicher Kontext | Empfehlung | Begründung |
|---|---|---|
| Prof-WiDi/Hochschullehre | PROFILE, aber in Hochschul- und Fachprofil trennen | DQM enthält Bachelor/Master und sozioökonomische Fachlogik; nicht jeder Hochschulfall ist Prof-WiDi |
| Blog | Artefaktprofil innerhalb `blog-produce`, kein allgemeines Nutzerprofil | Struktur/Frontmatter/Sprachmodus |
| Reveal | Artefaktprofil innerhalb `reveal-produce` | Transformation/Frontmatter/Slide-Heuristik |
| OER/OERSI | Subprofil von Blog/Publikation | Metadaten und Lizenz, nicht Planungsidentität |
| KBS | erst Profile, wenn aktuelle Regeln/Anwendungsfälle vorliegen | heute nicht implementiert |
| DJP | eher Task-/Reference-Komponente innerhalb KBS | heute keine Regelbasis |
| itslearning | Plattform-/Exportadapter, kein didaktisches Profil | Ausgabeformat/Plattformlogik |
| Forschungsmodus | Adapter/Task-Modus, kein pädagogisches Profile | orthogonal, technische Rohdatenerfassung |

## 15. Review-Lens-Analyse

### Heutige Lenses

| Lens | heutige Basis | Funktion |
|---|---|---|
| mechanisch/formal | Check-Frontmatter, OER, Pfade, Build, Links, Emoji | deterministische oder semi-deterministische Validierung |
| didaktisch | DQM sechs Dimensionen + Profilgewichtung | Kohärenz und Planungsqualität |
| Quellen/Literatur | Core-Quellenintegrität + Literaturtask | Belegkonsistenz, formale Normalisierung, optionale Recherche |
| Format/Artefakt | Templates + Blog-/Reveal-Prüfmatrix | Publikations- und Transformationsqualität |

Die Trennung ist konzeptionell vorhanden, aber in `check.md` zu einem großen Task verschmolzen.

### Learner Lens

Zusätzlicher Nutzen gegenüber DQM entsteht durch eine konsequent konkrete Simulation der Nutzungssituation: „Was muss eine lernende Person an dieser Stelle verstehen, voraussetzen, tun und verbinden?“ Das DQM fragt abstrakter nach Ziel, Aktivierung, Tiefe, Reflexion und Adaptivität. Eine Learner Lens kann insbesondere entdecken:

- unklare oder mehrdeutige Arbeitsaufträge;
- versteckte Zwischenschritte und vorausgesetztes Vorwissen;
- Diskrepanz zwischen nominellem Lernziel und tatsächlicher kognitiver Tätigkeit;
- bloßes Abarbeiten trotz sichtbarer Aktivität;
- fehlende Sinntransparenz und verloren gehende fachliche Zusammenhänge.

Doppelungsgefahr besteht mit DQM Lernverständnis (`343-482`), Lernqualität (`494-647`) und Adaptivität (`774-895`). Die Lens sollte deshalb keine zweite Qualitätsmatrix sein, sondern ein optionaler, kurzer Walk-through eines konkreten Entwurfs. Befunde sind Hypothesen, keine Aussagen über reale Lernende. Aktivierung: explizit, bei komplexen/risikoreichen Aufgaben oder wenn DQM-Befunde zu abstrakt bleiben. Nicht permanent und nicht automatisch reparierend. Risiko **mittel**; Nutzen empirisch prüfen.

## 16. Relative Einsparpotenziale

| Maßnahme | Potenzial | Begründung | Risiko |
|---|---|---|---|
| Research-Regeln aus normalem Contract-Pflichtkontext auslagern | **hoch** | `68-141` plus zahlreiche Wiederholungen werden in Standardfällen nie benötigt | niedrig für Standard, mittel für Research |
| DQM-Core + vollständiges DQM als Lazy Reference | **hoch** | 1.119 Zeilen; große Theorie-, Kontext-, Listen- und Literaturanteile | hoch ohne Regression/Ablation |
| Produktions-/Final-/OER-Regeln aus PLAN-Core entfernen | **hoch** | großer Contract-Anteil plus Templates/Check erst später nötig | mittel |
| Plan/Master/Low-noise auf Referenzen statt Regelkopien reduzieren | **mittel** | zusammen 526 Zeilen zusätzlich, viele Semantikduplikate | mittel bis hoch für Dialogregeln |
| Check gegen kanonische Schemas statt Feldkopien | **mittel** | spart Final-Kontext und Wartung, nicht frühen PLAN-Kontext | mittel |
| Beispiele aus Low-noise lazy laden | **gering bis mittel** | 100+ Zeilen, geringe semantische Einzigartigkeit | niedrig |
| Planning State statt langer Chatrekonstruktion | **potenziell hoch**, derzeit ungemessen | adressiert wachsenden Gesprächskontext, nicht nur Instruktionskontext | hoch |
| Wissens-/Literaturbasis weiter lazy halten | **bereits realisiert** | keine zusätzliche B1-Einsparung, aber wichtig beizubehalten | niedrig |

## 17. Risiken der Optimierung

| Risiko | Ursache | Gegenmaßnahme |
|---|---|---|
| Verlust der Driftkontrolle | Gate-/Blog-first-/Taskgrenzen zu stark indirekt | Core-Gates unverändert; H01 Drift 0 als harte Regression |
| Verlust didaktischer Tiefe | DQM auf generische Checkliste reduzieren | DQM-Reference erhalten; Ablation Full vs Core; Fachfälle ergänzen |
| Verlust Entscheidungsstabilität | Alternativregeln oder bestätigte Entscheidungen nicht präsent | KDM-Core + State-Decision Log; turnweise Driftprüfung |
| unnötige Rückfragen | Kontext/State fehlt oder Core fordert Vollständigkeit | „eine entscheidende Frage“ + Fortschritt vor Absicherung behalten |
| falsches Lazy Loading | benötigte Fach-/Profilregel wird nicht aktiviert | explizite Trigger, Fallback auf Reference, Trace der geladenen Module |
| zu starke Fragmentierung | zu viele kleine Tasks/Profile | zunächst grobe Tasks; maximal ein aktiver Task; klare Owners |
| versteckte Abhängigkeiten | bloße Markdown-Verweise werden nicht aufgelöst | maschinenlesbare Manifest-/Dependency-Checks später erwägen |
| State-Verlust/-Verfälschung | unvollständige Aktualisierung oder falsche Zusammenfassung | Shadow State, bestätigte Entscheidungen markieren, Chat zunächst behalten |
| inkonsistente Adapter | Codex/Copilot/fobizz laden unterschiedliche Cores | kanonische Plattformneutralität + dünne Adaptertests |
| Forschungsgegenstand verändert | Research-Instrumentierung beeinflusst Dialog oder State | Research Adapter strikt orthogonal; B0/B1 Bedingungen dokumentieren |
| Scheinsicherheit der Learner Lens | simulierte Perspektive als empirische Evidenz | stets als Hypothese markieren; optionaler Review |
| Rule-source Drift | Contract, Tasks, Templates, Check divergieren | eine Owner-Quelle je Regel + Referenz-/Schema-Validierung |

## 18. Priorisierte Empfehlungen für B1

### P1 – hoher Nutzen, relativ geringes Risiko

1. **Research-Subsystem aus dem normalen Pflichtcontract lösen.** Fundstellen: Contract `68-141` und Wiederholungen `146,153,162-183,198,244,251,263-264,389-391`; Plan `51-53`; Check `287-289`. Nutzen: hoher Pflichtkontextgewinn und klare Trennung von Forschung/Planung. Risiko: niedrig für Standard, mittel für Forschungsmodus. B0-Test: H01 Standard unverändert; separater späterer Research-Dry-Run ohne zusätzlichen Dialogeinfluss.

2. **Artefakt-/Finalisierungsdetails erst an Gates laden.** Fundstellen: Contract `237-250,317-420`; Templates; Check. Nutzen: hoher PLAN-Kontextgewinn, klarere Task-Ownership. Risiko: mittel. B0-Test: H01 Züge 1–4 auf Dialog/Drift; Zug 5 vollständig auf HTML-/Finalqualität und Gatefolge.

3. **Kanonische Ownership dokumentieren, ohne Semantik zu ändern.** Core besitzt Rolle/Gates/Autonomie; DQM didaktische Heuristik; Templates Schemas; Check Severity/Review; Tasks Orchestrierung. Nutzen: Wartbarkeit, Vorbedingung sicherer Kompression. Risiko: niedrig, sofern zunächst nur Architekturvariante außerhalb B0. Test: statische Regelreferenzprüfung plus H01.

4. **Low-noise taskbezogen splitten; vier Grundprinzipien im KDM-Core halten.** Fundstellen: Low-noise `11-47,75-199,203-308`. Nutzen: mittlere Einsparung, klare Dialogoberfläche. Risiko: niedrig bis mittel. Test: unnötige Rückfragen 0, keine Prozessrhetorik, gleiche Anschlussfähigkeit.

### P2 – sinnvoll, empirisch zu prüfen

5. **DQM-Core als sieben Heuristiken, vollständiges DQM unverändert als Reference.** Fundstellen Kapitel 7. Nutzen: sehr hoch. Risiko: hoch, wenn Trigger/Heuristik zu knapp. Test: H01 Full-vs-Core-Ablation; zusätzlich Fälle zu Assessment, Adaptivität, beruflicher Bildung und multiperspektivischem Konflikt, um Deckeneffekt zu vermeiden.

6. **KDM-Core aus vorhandenen Dialogregeln zusammenführen.** Fundstellen Kapitel 12. Nutzen: Qualitätserhalt und weniger Duplikation. Risiko: mittel bis hoch. Test: turnweise Entscheidungskontinuität, Alternativenzahl, Rückfragenrelevanz, Nutzeroverride.

7. **Master und Plan nach erfolgreichem Core-Test entduplizieren.** Fundstellen Kapitel 6/9. Nutzen: mittel. Risiko: mittel bis hoch, da Wiederholung B0 stabilisiert haben kann. Test: sequenzielle Ablation, nicht gleichzeitig mit DQM-Kompression.

8. **Optionalen Shadow Planning State einführen.** Fundstellen Contract State `158-185`, Journal Zielbild, Kapitel 13. Nutzen: potenziell hoch bei langen Dialogen. Risiko: hoch. Test: zunächst Chat vollständig behalten und State nur vergleichen; erst später Chatreduktion testen.

9. **Check in mechanische, didaktische und Artefakt-Lenses trennen.** Fundstellen `check.md:35-259`. Nutzen: Wartbarkeit und bedarfsgerechte Reviews. Risiko: mittel. Test: identische Blocker/Warnungen auf bestehenden, nicht benchmark-evaluativen Beispieldateien; danach B0-Finalzug.

### P3 – größere Architekturänderung, später

10. **Maschinenlesbare Router-/Manifest- oder Validator-Schicht.** Nutzen: tatsächliches statt rein deklaratives Lazy Loading und Schema-Checks. Risiko: hoch; könnte Plattformneutralität verändern. Erst nach B1-Core-Stabilisierung.

11. **Learner Lens als optionales Review-Instrument.** Nutzen: zusätzliche konkrete Nutzungsperspektive. Risiko: mittel; Doppelung/Scheinsicherheit. Separater Ablationstest.

12. **Neue KBS-/DJP-/itslearning-Profile.** Heute fehlt die Regelbasis. Nutzen unklar, Risiko hoch durch erfundene Architektur. Erst anhand realer Fälle/Adapter.

13. **Chat-History durch State ersetzen.** Potenziell großer Tokengewinn, aber derzeit höchstes Stabilitätsrisiko. Erst nach erfolgreichem Shadow-State-Test.

## 19. Antworten auf die fünf Abschlussfragen

### 1. Welche Teile sind wahrscheinlich unverzichtbar?

Human-in-the-loop und Lehrpersonenautonomie; führende begründete Verdichtung; knappe, entscheidungsrelevante Alternativen; genau eine priorisierte Rückfrage; klare Spannung-/Konfliktbehandlung; explizite Gates und striktes Blog-first; Quellenintegrität; Fortschritt vor Absicherung ohne Gate-Umgehung; DQM-Kohärenz, kognitive Aktivierung, Aufgaben-/Tiefenqualität, Reflexion, Adaptivität und Fachspezifik; Low-noise-Ergebnisorientierung. Diese Elemente sind die plausibelsten Träger von B0-Qualität, Driftfreiheit und Entscheidungsstabilität.

### 2. Welche Teile erzeugen wahrscheinlich viel Kontext ohne proportionalen Normalplanungsnutzen?

Vollständige Forschungsschemata; Blog-/Reveal-/OER-/OERSI-Frontmatter und DoD; Finalausgabe- und Buildregeln; Low-noise-Beispiele für FINAL/Mikrofix/Forschung; DQM-Literatur, Theorieerläuterungen, Ablaufmodelle und Spezialkontexte; historische Master-Hintergründe. Diese Inhalte sind nicht nutzlos, aber beim ersten normalen PLAN-Zug zu früh.

### 3. Welche fünf Änderungen bieten das beste Verhältnis?

1. Research Adapter lazy laden.
2. Produktion/Finalisierung/OER erst an Artefaktgates laden.
3. kleinen KDM-Core aus bestehenden Regeln kanonisieren.
4. DQM-Core plus unveränderte DQM-Reference im kontrollierten Ablationstest.
5. Plan/Master/Low-noise erst nach Core-Nachweis entduplizieren und nur referenzieren.

### 4. Was vorerst nicht tun?

Nicht das vollständige DQM löschen; nicht Lernverständnis und Lernqualität blind verschmelzen; nicht Gate-/Alternativen-/Rückfrageregeln gleichzeitig stark kürzen; nicht sofort Chat-History durch State ersetzen; nicht automatisch nach Reviews reparieren; keine Multi-Agent-Architektur; keine KBS/DJP/itslearning-Profile ohne empirische Regelbasis; Research nicht mit Planning State vermischen.

### 5. Wie sieht eine minimale erste B1-Version aus?

Ein Single Agent mit dünnem Adapter und einem kleinen, stabilen Core: Rolle/Autonomie, Auftragstreue, Gate-/Blog-first-Regeln, Quellenintegrität, KDM-Kurzfassung und sieben DQM-Kernheuristiken. Das vollständige DQM bleibt unverändert als bedarfsgeladene Reference. Forschung, Blog, Reveal, OER, Literatur und Final-Check werden erst durch eindeutige Tasks/Gates geladen. Noch kein State-Ersatz und keine neue Lens. Zuerst H01 unter möglichst identischen Bedingungen; Bestehenskriterien mindestens B0-Niveau bei Qualität, Drift 0, keine zusätzlichen unnötigen Rückfragen und erkennbar geringerem Pflicht-/Inputkontext. Danach getrennte Ablationen für DQM-Core und Shadow State.

## 20. Tatsächlich analysierte Repository-Dateien

### Vollständig semantisch gelesen

- `docs/agent_development/development_journal.md`
- `AGENTS.md`
- `.github/copilot-instructions.md`
- `project_governance/agent_contract.md`
- `project_governance/low_noise_response_patterns.md`
- `project_governance/ai_copilot_instructions.md`
- `project_governance/ai_project_context.md`
- `project_governance/repo_architecture.md`
- `project_governance/development_workflow.md`
- `project_governance/content_emoji_policy.md`
- `ai_agents/master_agent.md`
- `ai_agents/didaktisches_qualitaetsmodell.md`
- `ai_agents/templates/blog_template.md`
- `ai_agents/templates/reveal_template.md`
- `prompts/plan.md`
- `prompts/check.md`
- `prompts/literatur.md`
- `prompts/content_emojis_blog.md`
- `prompts/content_emojis_reveal.md`

### Für Rolle, Struktur, Referenzen und Ladebedingungen untersucht

- `README.md`
- `ai_agents/README.md`
- `ai_agents/blog_wissensbasis.md`
- `ai_agents/blog_literaturbasis.md`
- `ai_agents/terminologie_mapping.md`
- Repository-Dateiinventar und Querverweise der genannten Hauptdateien

Nicht gelesen wurden `benchmark/evaluations/**` und die archivierte Regression Suite. Content-Beiträge, CSS, Layouts und große Wissensbasis-Einträge wurden nicht inhaltlich auditiert, weil sie keine frühe PLAN-Laufzeitsteuerung darstellen. B0-Werte wurden ausschließlich aus der vom Auftrag vorgegebenen Baseline und dem Development Journal übernommen; es wurde kein neuer Lauf erzeugt.

## 21. Executive Summary für die weitere Arbeit

KO-PLAN ist insgesamt als qualitativ starkes, aber architektonisch überladenes System zu bewerten. B0 zeigt, dass der Agent didaktische Spannungen präzise fokussieren, Entscheidungen der Lehrperson stabil fortführen, unnötige Rückfragen vermeiden und einen kohärenten Blog-/Reveal-Workflow kontrollieren kann. Diese Leistung ist plausibel auf eine kleine Gruppe besonders wirksamer Regeln zurückzuführen: menschliche Entscheidungsautonomie, eine führende begründete Verdichtung, begrenzte Alternativen, genau eine entscheidende Rückfrage, klare Gate-Disziplin, Blog-first, Quellenintegrität sowie die DQM-Heuristiken zu Kohärenz, Lernlogik, kognitiver Aktivierung, Reflexion und Adaptivität. Diese Elemente müssen in B1 sichtbar und dauerhaft erhalten bleiben.

Das Hauptproblem ist nicht schlechte Regelqualität, sondern fehlende Trennung der Verantwortlichkeiten. Der Contract ist zugleich Core, State-Machine-Beschreibung, Research-Spezifikation, Produktionshandbuch, OER-/Reveal-Profil, QA-Regelwerk und Antwortformat. Master, Plan, Check und Low-noise wiederholen anschließend zentrale Teile. Die erklärte kanonische Ownership existiert deshalb formal, aber nicht semantisch konsequent. Hinzu kommt, dass die State Machine nur in Markdown beschrieben ist: Der Agent muss Phase, Entscheidungen und Artefaktstatus aus Chat und Dateien rekonstruieren.

Der große Pflichtkontext ist strukturell gut erklärbar. Beim normalen PLAN-Start lädt der Codex-Adapter sechs Dateien einschließlich Adapter mit insgesamt rund 15.140 Wörtern beziehungsweise 130 KB. Contract und DQM stellen etwa drei Viertel dieses Wortumfangs. Darin liegen umfangreiche Forschungsdateischemata, Blog-/Reveal-/OER-Metadaten, Finalisierungslogik, Beispiele, theoretische Erläuterungen und Literatur, die der erste Planungszug meist nicht benötigt. Die B0-Tokenwerte bestätigen nicht die Wirkung einzelner Dateien, machen wiederkehrenden Inputkontext aber zum plausibel wichtigsten Optimierungshebel.

Künftig sollte ein kleiner Core nur Rolle, Autonomie, Auftragstreue, Gate-/Routinggrundsätze, Quellenintegrität, KDM und die DQM-Kernheuristiken enthalten. Planung bleibt zunächst ein zusammenhängender Task; eine Zerlegung in separate Goal-, Content-, Activity- und Assessment-Tasks wäre zu granular und gefährdete Kohärenz. Blog- und Reveal-Produktion sowie ihre Finalisierung sind eigene Tasks mit Artefaktprofilen. OER/OERSI ist ein Blog-/Publikationssubprofil. Forschung ist ein orthogonaler Adapter. Wissens- und Literaturbasis bleiben References. KBS, DJP und itslearning sollten erst modelliert werden, wenn reale Regeln und Fälle vorliegen.

Das DQM darf nicht pauschal gekürzt werden. Ein DQM-Core kann sieben Fragen dauerhaft präsent halten: Ziel-/Assessment-Passung, lernlogische Struktur, aktives Verstehen, kognitive Tiefe der Aufgaben, funktionale Reflexion/Transfer, Adaptivität ohne Scheindiagnose und Fach-/Kontextspezifik. Das vollständige heutige DQM bleibt als Reference für Modelle, Profile, Spezialkontexte, Reviewlisten und wissenschaftliche Begründung erhalten. Besonders riskant wäre es, Constructive Alignment, die Unterscheidung von Aktivität und kognitiver Aktivierung oder die Trennung von Lernverständnis und konkreter Lernqualität zu verlieren.

Ein KDM muss keine neue Wissensbasis werden. Seine Regeln sind bereits vorhanden und müssen zusammengeführt werden: Lehrperson entscheidet; wichtigste Spannung zuerst; begründete Empfehlung statt Variantenraum; nur entscheidungsrelevante Rückfragen; bestätigte Entscheidungen bleiben stabil; Review ist keine automatische Reparatur; aktueller Auftrag und Task begrenzen die Arbeit. Ein Planning State kann diese Stabilität später unterstützen. Zwingend wären Kontext, Ziele, bestätigte Entscheidungen mit kurzer Begründung, offene Entscheidungen, aktueller Task/Gate, Artefaktstatus und bewusste Overrides. Der State darf weder Chatlog noch Research Trace imitieren und sollte zunächst parallel zur vollständigen Historie erprobt werden.

Das beste Nutzen-Risiko-Verhältnis bieten vier unmittelbare Schritte: Erstens Research-Regeln aus dem normalen Pflichtkontext lösen. Zweitens Blog-, Reveal-, OER- und Finalisierungsdetails erst an ihren Gates laden. Drittens KDM und kanonische Regel-Ownership ohne semantische Neuerfindung festlegen. Viertens einen DQM-Core als kontrollierte Variante gegen das vollständige DQM testen. Erst nach erfolgreichem Nachweis sollten Master, Plan und Low-noise entdupliziert werden.

Vorerst ausdrücklich nicht empfohlen sind eine radikale DQM-Kürzung, ein sofortiger Ersatz der Chat-Historie durch State, eine Multi-Agent-Struktur, automatische Reparaturen nach Review, neue Plattformprofile ohne reale Grundlage und die gleichzeitige Veränderung mehrerer B0-Sicherheitsregeln. Solche Schritte würden den Forschungsgegenstand verändern und erschweren die Zuordnung von Qualitätsverlusten.

Der konkret nächste Schritt ist eine minimale B1-Variante: Single Agent, kleiner Core mit unveränderten Autonomie-/Gate-/Quellenregeln, kurzer KDM, sieben DQM-Heuristiken und echtes Lazy Loading für Research und Artefaktproduktion. Das vollständige DQM bleibt verfügbar. Diese Variante wird zunächst mit H01 unter möglichst gleichen Bedingungen gegen B0 geprüft. Maßstab sind nicht nur Tokens, sondern mindestens gleiche didaktische Qualität, Drift 0, keine zusätzlichen unnötigen Rückfragen, stabile Entscheidungen und korrekte Finalisierung. Erst danach folgt ein separater Shadow-State- und Learner-Lens-Test.
