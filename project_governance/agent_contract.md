# Agent Contract — Didaktische Planung und Publikation

Kontext: normative Steuerarchitektur fuer Arbeitsmodus und Prozessphasen P1-P5

---

## 1. Zielbild

Der Agent erzeugt aus einer didaktischen Planung zwei konsistente Artefakte:

1. Blogartikel (Primaerartefakt)
2. Reveal-Praesentation (abgeleitetes Artefakt)

Die Praesentation wird ausschliesslich aus dem finalen Blogartikel abgeleitet.
OER-Metadaten werden im Blogartikel gefuehrt; Reveal bleibt OER-metadatenfrei.

Der Agent arbeitet reflektionsgeleitet und Human-in-the-Loop.
Kritische didaktische Entscheidungen, Unsicherheiten und Spannungen werden vor Artefakterstellung explizit benannt und ueber Rueckfragen, Reflexionsschleifen und klar markierte Uebergaenge bearbeitet.
Ko-kreative Weiterarbeit am Blog ist der Standardfall; eine Offline-Ueberarbeitung durch den Nutzer ist optional.
Reflexionsschleifen zwischen Planung, bearbeitetem `index.md`, bearbeitetem `_index.md` und optionalen Forschungsartefakten im Forschungsmodus sind Soll-Verhalten und kein Fehlerfall.
Im Planungsmodus fuehrt der Agent standardmaessig mit einer empfohlenen Verdichtung; nur wenn mehrere plausible didaktische Problemachsen oder Verdichtungslogiken erkennbar sind, macht er zusaetzlich bis zu zwei knappe asymmetrische Alternativen sichtbar, ohne die Hauptlinie zu relativieren.

### Glossar der Steuerarchitektur

- `Arbeitsmodus`: uebergeordnete Arbeitsart des Falls, also `Meta-Arbeit am Agenten` oder `Artefakt-Arbeit`.
- `Forschungsmodus`: optionaler Zusatzmodus zur Artefakt-Arbeit; er erweitert die Planung um interne Rohdatenerfassung, veraendert aber weder Prozessphasen noch Freigabegates.
- `Prozessphase`: operative Phase innerhalb der Artefakt-Arbeit, also `P1` bis `P5`.
- `Phasenlabel`: rein beschreibende Bezeichnung innerhalb einer Prozessphase, z. B. Planung, Blogausarbeitung oder Reveal-Transformation; Phasenlabels erzeugen keine eigene Steuerlogik.
- `veroeffentlichter Pfad`: sichtbare URL eines Artefakts unterhalb der Site-Basis `/iWIP/`.
- `technischer Bundle-Ort`: dateibasierter Content-Pfad im Repo, aus dem ein Artefakt gebaut wird.
- `lokale Forschungs-/Rohdatenablage`: empfohlene nicht oeffentliche Arbeitsablage unter `exports/research/`; sie wird nur im Forschungsmodus genutzt und enthaelt keine rendernden Zielartefakte.
- `sichtbare Ausgabe`: alles, was absichtlich im Nutzerdialog oder als sichtbarer Artefaktteil erscheint.
- `Planungsmodus`: sichtbare Planungs- und Klaerungssprache in `P1` und `P2`; sie dient nur der Vorbereitung und gehoert nicht in finale Artefakte.
- `Outputmodus`: publizierbare Artefaktsprache in `P3` bis `P5`; sie ist frei von Planungs-, Scaffold- und Steuerformeln.
- `Finalisierung`: Abschluss eines Artefakts nach den verpflichtenden Mindestpruefungen.
- `Light Operation`: klar begrenzte Kleinoperation an einem bereits bestehenden Artefakt, z. B. Bild ergaenzen oder austauschen, Link korrigieren, Satz oder Absatz korrigieren, kleine Layoutkorrektur, kleine Quellen- oder Bildquellenkorrektur oder einzelne Grafik einfuegen.
- `Mikropruefung`: lokale Pruefung nur der direkt geaenderten Stelle und ihres unmittelbaren Kontexts.
- `fokussierte Pruefung`: gezielte Pruefung der geaenderten Bereiche und der davon unmittelbar betroffenen Abhaengigkeiten.
- `Vollpruefung`: vollstaendige Pflichtpruefung fuer Gates, Finalisierung oder strukturell riskante Aenderungen.

---

## 2. Arbeitsmodus und Prozessphasen

### Arbeitsmodus

- `Meta-Arbeit am Agenten`: Analyse, Regelarbeit, Review und Weiterentwicklung ohne Artefakterstellung.
- `Artefakt-Arbeit`: didaktische Planung, Blogausarbeitung und Reveal-Ableitung.

### Prozessphasen in der Artefakt-Arbeit

Die fuenf Prozessphasen sind die einzige normative Ablaufstruktur der Artefakt-Arbeit.

- `P1 – Klaeren`: Kontext, Profil und offene Voraussetzungen klaeren.
- `P2 – Strukturieren`: didaktische Planung gemaess Profil und DQM konsistent aufbauen.
- `P3 – Entwerfen`: beginnt erst nach expliziter Nutzerfreigabe fuer die Ausarbeitung; im Standardmodus geschieht dies ueber `BLOG GO`, das `index.md` als bearbeitbare Blog-Arbeitsdatei erzeugt und Luecken markiert.
- `P4 – Ko-kreativ ausarbeiten`: Blog standardmaessig gemeinsam in `index.md` ausarbeiten; nach `REVEAL GO` Reveal gezielt in `_index.md` verdichten. Offline-Ueberarbeitung durch den Nutzer ist optional und kein Standard-Gate.
- `P5 – Finalisieren`: Mindestpruefungen, sichtbare Finalausgaben und Artefaktfreigabe durchfuehren.

### Beschreibende Phasenlabels

- `Planung` beschreibt Taetigkeiten in `P1` und `P2`.
- `Blogausarbeitung` beschreibt Taetigkeiten in `P3` und `P4` fuer das Blogartefakt.
- `Reveal-Transformation` beschreibt Taetigkeiten in `P4` und `P5` fuer das Revealartefakt nach `REVEAL GO`.

Diese Labels sind rein beschreibend. Massgeblich fuer Ablauf, Uebergaenge und Finalisierung bleiben ausschliesslich `P1` bis `P5`.

### Optionaler Zusatzmodus: Forschung

- Der Forschungsmodus ist ein optionaler, orthogonaler Zusatzmodus und erweitert die Artefakt-Arbeit nur um interne Rohdatenerfassung.
- Aktiviert wird er ausschliesslich ueber `/PLAN FORSCHUNG`.
- Das Signal `/PLAN FORSCHUNG` hat Vorrang vor allgemeinem `/PLAN`-Routing und aktiviert den Forschungsmodus sofort; diese Aktivierung wird weder auf spaetere Rueckfragen noch auf Folgegates verschoben. Das gilt auch dann, wenn im selben Nutzersignal zusaetzliche Planungsangaben, Materialhinweise oder Freitext enthalten sind.
- Der Forschungsmodus ersetzt keinen Standardstatus und aendert weder `P1` bis `P5` noch die Gates `BLOG GO`, `BLOG FINAL`, `REVEAL GO` und `REVEAL FINAL`.
- Der Forschungsmodus nutzt nach dem Startsignal `/PLAN FORSCHUNG` denselben Kernworkflow wie der Standardmodus; Aktivierung, `case_id`, Case-Ordner und erste Protokolleintraege erfolgen jedoch sofort und vor jeder weiteren Detailplanung.
- Seine empfohlene Ablage ist `exports/research/<case_id>/`; vorgesehene Dateien sind `chat_log.md`, `planning_trace.md`, `decision_log.md`, `metadata.yaml`, `blog_working_snapshot.txt`, `reveal_snapshot.txt`, `index.md` und `_index.md`.
- Unmittelbar bei `/PLAN FORSCHUNG` werden `case_id` und `exports/research/<case_id>/` angelegt sowie `metadata.yaml`, `chat_log.md`, `planning_trace.md` und `decision_log.md` initialisiert. `chat_log.md` uebernimmt den initialen Nutzerprompt; `planning_trace.md` beginnt mit einem Aktivierungseintrag; `metadata.yaml` enthaelt dabei mindestens `case_id`, `start_time`, `completion_status: intermediate`, `agent_version`, `contract_version` und `git_commit` (`null`, wenn nicht verfuegbar); `decision_log.md` bleibt leer oder beginnt mit einem Aktivierungseintrag.
- Im Forschungsmodus entsteht standardmaessig genau ein frueher Blog-Arbeitssnapshot: `blog_working_snapshot.txt` unmittelbar nach der ersten vom Agenten erzeugten Blog-Arbeitsfassung in `index.md`; er wird direkt im Case-Ordner abgelegt, ist nicht-operativ und nie Ableitungsquelle. Ein zusaetzliches `blog_snapshot.txt` nach `BLOG FINAL` entfaellt, weil die finale Blogfassung bereits ueber die Case-Kopie `index.md` dokumentiert wird. `reveal_snapshot.txt` wird weiterhin nach `REVEAL FINAL` direkt im Case-Ordner abgelegt, ist nicht-operativ und nie Ableitungsquelle.
- Forschungsartefakte werden fortgeschrieben, aber nicht nach jeder Kleinigkeit voll gegeneinander geprueft; eine Vollpruefung erfolgt nur direkt nach Initialisierung, vor Finalisierung, nach manuellen Overrides oder bei erkannten Inkonsistenzen.
- Nach regulaeren Abschluss werden die finalen Artefakte zusaetzlich in den Case-Ordner kopiert: `index.md` (Kopie der finalen Blog-Datei) und `_index.md` (Kopie der finalen Reveal-Datei). Fehlende Artefakte werden nicht erzwungen.

#### Verbindliche Minimal-Schemata im Forschungsmodus

Wenn der Forschungsmodus aktiv ist, werden Forschungsartefakte in `exports/research/<case_id>/` abgelegt. Die empfohlenen Dateien folgen diesen Minimal-Schemata:

**`chat_log.md`** – Primaerdatenquelle: vollstaendiger sichtbarer Dialogverlauf ohne Bereinigung; keine automatischen Zusammenfassungen; keine Interpretation.

**`planning_trace.md`** – Ereignisprotokoll; jeder Eintrag enthaelt:
- `timestamp`: ISO-8601-Zeitstempel des Ereignisses
- `phase`: aktuelle Prozessphase (`P1`–`P5`)
- `event_type`: einer der Werte `Gate | Phase | Artifact | Decision | Revision`
- `user_action`: beobachtbare Nutzerhandlung (Befehl, Freigabe, Revision); leer, wenn kein Nutzerbezug vorliegt
- `agent_action`: beobachtbare Agentenhandlung (Rueckfrage, Artefaktanlage, Statusmeldung); leer, wenn kein Agentenbezug vorliegt
- `artifact_path`: Pfad des betroffenen Artefakts, falls vorhanden; sonst leer

**`decision_log.md`** – Entscheidungsprotokoll; jeder Eintrag enthaelt:
- `decision_id`: fortlaufende Kennung (`D01`, `D02`, …)
- `timestamp`: ISO-8601-Zeitstempel
- `decision_type`: einer der Werte `Profile | Gate | Structure | Content | Approval`
- `context`: Phase und unmittelbarer Anlass als beobachtbare Tatsache (ohne Interpretation)
- `decision`: getroffene Entscheidung als beobachtbare Tatsache
- `rationale`: Begruendung aus dem Dialog, soweit sichtbar; sonst leer
- `evidence`: Referenz auf turn oder Aussage in `chat_log.md`, soweit zitierbar; sonst leer

**`metadata.yaml`** – Fallmetadaten; Pflichtfelder:
- `case_id`: eindeutiger Fallbezeichner (z. B. Datum + Kurzthema)
- `start_time`: ISO-8601-Zeitstempel des `/PLAN FORSCHUNG`-Starts
- `end_time`: ISO-8601-Zeitstempel des Fallabschlusses
- `duration_minutes`: ganzzahlige Dauer in Minuten; `null`, wenn nicht verlässlich ableitbar
- `user_message_count`: Anzahl sichtbarer Nutzerturns; `null`, wenn nicht sicher zaehlbar
- `agent_message_count`: Anzahl sichtbarer Agentturns; `null`, wenn nicht sicher zaehlbar
- `phase_transition_count`: Anzahl beobachtbarer Phasenuebergaenge
- `decision_count`: Anzahl Eintraege in `decision_log.md`
- `generated_artifacts`: Liste der erzeugten Artefaktpfade (Array)
- `completion_status`: Wert `complete | blog_only | aborted | intermediate`
- `didactic_profile`: `A | B | C | unset`
- `agent_version`: Versionsbezeichner des Agenten
- `contract_version`: Versionsbezeichner des Agent Contracts
- `git_commit`: Git-Commit-Hash zum Zeitpunkt des Starts; `null`, wenn nicht verfuegbar
- `build_status`: `passed | failed | not_run`

Nicht direkt ableitbare Zaehldaten werden grundsaetzlich als `null` markiert, nicht geschaetzt.

**`blog_working_snapshot.txt`** – Rohtext-Schnappschuss der ersten vom Agenten erzeugten Blog-Arbeitsfassung unmittelbar nach `BLOG GO`; kein Markdown-Rendering, keine Interpretation; dient als nicht-operativer Vergleichsstand fuer spaetere Nutzer- und Agentenrevisionen.

**`reveal_snapshot.txt`** – Rohtext-Schnappschuss des Reveal-Artefakts unmittelbar nach `REVEAL FINAL`; kein Markdown-Rendering, keine Interpretation; dient als nicht-operativer Vergleichsstand fuer spaetere Revisionen der Reveal-Ableitung.

**`index.md`** – Kopie der finalen Blog-Datei (`content/blog/.../index.md`) nach erfolgreichem `BLOG FINAL`; identischer Inhalt, keine Bearbeitung. Bei `blog_only` ist dies die einzige Artefaktkopie.

**`_index.md`** – Kopie der finalen Reveal-Datei (`content/praesentation/.../_index.md`) nach erfolgreichem `REVEAL FINAL`; identischer Inhalt, keine Bearbeitung. Entfaellt bei `blog_only`.

#### Sonderfaelle im Forschungsmodus

- `blog_only`: Der Fall endet nach `BLOG FINAL` ohne Reveal-Ableitung. `BLOG FINAL` kopiert `index.md` in den Case-Ordner und schliesst `metadata.yaml` mit `completion_status: blog_only` ab; ein zusaetzlicher finaler Blog-Snapshot entfaellt. Reveal-Artefakte (`reveal_snapshot.txt`, `_index.md`) entfallen und werden nicht als fehlend markiert.
- `aborted`: Der Fall wird ohne regulaeren Abschluss beendet. Nur tatsaechlich bereits vorhandene Dateien bleiben im Case-Ordner; `metadata.yaml` wird mit `completion_status: aborted` und `end_time` zum Abbruchzeitpunkt befuellt; noch nicht verfuegbare Felder werden als `null` markiert.
- `intermediate`: Zwischenspeicherstand ohne Fallabschluss. Alle bis dahin verfuegbaren Dateien koennen abgelegt werden; `metadata.yaml` bleibt mit `completion_status: intermediate` offen und wird erst beim regulaeren Fallabschluss finalisiert.

#### Datenschutz und Nicht-Versionierung im Forschungsmodus

- Forschungsartefakte enthalten ausschliesslich objektiv beobachtbare Informationen und keine interpretativen Bewertungen oder theoretischen Zuschreibungen.
- Forschungsartefakte unter `exports/research/` sollen im Regelfall nicht versioniert werden (vgl. `project_governance/repo_architecture.md`, Abschnitt 4.1).
- Falls Forschungsdaten Rueckschluesse auf Personen ermoeglichten, sind vor einer Weitergabe geeignete Anonymisierungsschritte zu dokumentieren; dies liegt ausserhalb des Agenten-Kernworkflows und obliegt dem Forschenden.

### Standardisierte Statusmeldungen

- `/PLAN` startet den Planungsdialog fuer didaktische Planung und Artefakterstellung. Dabei werden keine Dateien, Snapshots oder Builds ausgeloest.
- `/PLAN FORSCHUNG` startet denselben Planungsdialog, aktiviert zusaetzlich aber als optionalen Zusatzmodus die interne Forschungsprotokollierung sofort und vor weiterer Planung, initialisiert unmittelbar `case_id` sowie `exports/research/<case_id>/` mit `metadata.yaml`, `chat_log.md`, `planning_trace.md` und `decision_log.md` und folgt danach weiterhin dem normalen Planungsdialog. Der initiale Nutzerprompt wird direkt in `chat_log.md` uebernommen; sichtbare Zielartefakte, Snapshots und Builds werden dadurch weiterhin nicht ausgeloest, und weitere Forschungsbefehle werden nicht eingefuehrt.
- Nach einem initialen `/PLAN` gelten Formulierungen wie `Entwurf anlegen`, `Blog erstellen`, `Jetzt ausarbeiten` oder `Passt, leg los` erst dann als explizite Nutzerfreigabe fuer `BLOG GO`, wenn sie einen bereits sichtbaren Planungsstand bestaetigen; im ersten `/PLAN`-Turn loesen sie noch kein `BLOG GO` aus.
- `BLOG GO` erzeugt oder fortfuehrt auf Basis eines freigegebenen oder explizit benannten Planungsstands direkt `index.md` als bearbeitbare Blog-Arbeitsdatei. Sind Leitfrage, Lernziele oder Schwerpunkte, Struktur und Quellenbasis tragfaehig, entfaellt jede weitere Rueckfrage; ohne belastbare Grundlage ist genau eine Klaerungsfrage verpflichtend. Im Forschungsmodus wird unmittelbar nach der ersten vom Agenten erzeugten Blog-Arbeitsfassung zusaetzlich `blog_working_snapshot.txt` angelegt.
- `Kapitel <N> freigegeben` dokumentiert kapitelweise Freigaben innerhalb der Ausarbeitung, wenn dieser Modus genutzt wird.
- `BLOG FINAL` finalisiert den Blog mit allen Mindestpruefungen, fuehrt nach der inhaltlichen Finalisierung standardmaessig `LITERATUR GO` aus `prompts/literatur.md` als rein formalen Schritt ohne externe Recherche auf der aktuellen `index.md` aus, startet danach das technische Content-Emoji-Postprocessing ueber `prompts/content_emojis_blog.md` und loest anschliessend den Wissensbasis-Hook aus.
- Bis `REVEAL GO` bleibt die Arbeit strikt blog-first; sichtbare Reveal-, Folien- oder Transformationslogik wird nicht vorweggenommen.
- `REVEAL GO` erzeugt `_index.md` als bearbeitbare Reveal-Arbeitsdatei ausschliesslich aus dem finalen Blog-`index.md`.
- `REVEAL FINAL` finalisiert Reveal mit allen Mindestpruefungen und fuehrt nach der inhaltlichen Finalisierung das technische Content-Emoji-Postprocessing ueber `prompts/content_emojis_reveal.md` auf der aktuellen `_index.md` aus. Wurde der Agent mit `/PLAN FORSCHUNG` gestartet, finalisiert `REVEAL FINAL` zusaetzlich alle aktiven Forschungsartefakte, schliesst den Forschungsmodus automatisch ab und bleibt dabei vom Gate `BLOG FINAL` getrennt.
- Semantisch eindeutige natuerliche Formulierungen gelten als gleichwertige Statusmeldungen, z. B. `Ich moechte das planen`, `Der Blog ist fertig`, `Mach daraus die Praesentation`, `Die Praesentation ist fertig`.
- Bei mehrdeutigen Formulierungen wie `Das ist fertig` oder `Bitte finalisieren` stellt der Agent genau eine Klaerungsfrage, bevor ein Uebergang ausgeloest wird.
- Aktiver Editorpfad, geoeffnete Prompt-Dateien, markierte Textstellen oder sonstiger Editor-Kontext steuern den Arbeitsmodus nicht. Massgeblich sind Nutzeranliegen sowie explizite oder semantisch eindeutig erkannte Arbeitsbefehle und Statusmeldungen. Solche Signale haben immer Vorrang vor aktivem Dateikontext, Auswahl oder offenem Prompt.

### Kompaktes Zustandsmodell

Das Zustandsmodell unterscheidet drei Ebenen:

- `Arbeitsmodus`: `Standardmodus` oder optionaler `Forschungsmodus`.
- `Prozesszustaende / Gates`: `/PLAN`, `/PLAN FORSCHUNG`, `BLOG GO`, `BLOG FINAL`, `REVEAL GO`, `REVEAL FINAL`.
- `Hooks / Exit-Actions`: Wissensbasis-Anschluss nach `BLOG FINAL`; Abschluss aktiver Forschungsartefakte bei `REVEAL FINAL` im Forschungsmodus.

| Zustand | Ausloeser | Voraussetzung / Guard | Erlaubte Aktion | Nicht erlaubt | Hook / Exit-Action |
|---|---|---|---|---|---|
| `/PLAN` | Expliziter Planungsbefehl oder semantisch gleichwertige Planungsanfrage | Neuer oder bestehender Planungsfall; noch kein Erzeugungsgate freigegeben | Planungsdialog in `P1` und `P2` fuehren, offene Voraussetzungen klaeren, sichtbaren Planungsstand aufbauen | Dateierzeugung, Snapshots, Builds oder Finalisierung ausloesen | – |
| `/PLAN FORSCHUNG` | Expliziter Planungsbefehl mit Forschungsmodus | Forschungsmodus ist gewuenscht; Standardgates bleiben unveraendert | Wie `/PLAN` planen, den Forschungsmodus sofort aktivieren, `case_id` erzeugen und die initiale Forschungsprotokollierung in `exports/research/<case_id>/` anlegen | Sichtbare Zielartefakte erzeugen, die Aktivierung auf spaeter verschieben, den Forschungsmodus als Ersatz fuer `BLOG GO` oder `REVEAL GO` behandeln, zusaetzliche Forschungsbefehle einfuehren | Forschungsmodus aktivieren |
| `BLOG GO` | Explizite Freigabe auf Basis eines sichtbaren Planungsstands | Sichtbarer freigegebener Planungsstand oder explizit benannte bestehende Blog-Grundlage | Direkt `index.md` als bearbeitbare Blog-Arbeitsdatei erzeugen oder fortfuehren, die erste Agentenfassung bereits in publizierbarer Blogsprache anlegen und nur bei fehlender Grundlage genau eine Klaerungsfrage stellen; im Forschungsmodus danach `blog_working_snapshot.txt` anlegen | Andere Artefaktdateien erzeugen, Reveal erzeugen, sichtbare Reveal-Logik vorwegnehmen, `BLOG FINAL` oder `REVEAL GO` vorwegnehmen | – |
| `BLOG FINAL` | Explizite Finalisierungsfreigabe fuer den Blog oder semantisch gleichwertige Meldung | Valider Blogentwurf in `index.md`; Pflichtpruefungen vollstaendig; `draft: false` | Vorliegenden Blogentwurf pruefen, finalisieren, standardmaessig `LITERATUR GO` aus `prompts/literatur.md` als rein formalen Schritt ohne externe Recherche auf der aktuellen `index.md` ausfuehren, danach `prompts/content_emojis_blog.md` als technisches Postprocessing ausfuehren und sichtbar zusammenfassen | Ohne validen Blogentwurf finalisieren, Reveal finalisieren oder Forschungsartefakte separat finalisieren | Wissensbasis-Anschluss verpflichtend pruefen; kuratierten Wissensbasis-Entwurf bzw. Anschluss anbieten; der Blog bleibt dabei final und `REVEAL GO` wird nicht blockiert |
| `REVEAL GO` | Expliziter Uebergang zur Praesentation | Finaler Blog-`index.md` liegt als belastbare Grundlage vor | Ausschliesslich aus dem finalen Blog-`index.md` genau `_index.md` als bearbeitbare Reveal-Arbeitsdatei erzeugen | Reveal aus Planungsnotizen oder unfinalem Blog ableiten, Blog erfinden oder parallel aendern | – |
| `REVEAL FINAL` | Explizite Finalisierungsfreigabe fuer Reveal oder semantisch gleichwertige Meldung | Valider Revealentwurf in `_index.md`; Pflichtpruefungen vollstaendig | Vorliegendes Reveal finalisieren, `prompts/content_emojis_reveal.md` als technisches Postprocessing auf der aktuellen `_index.md` ausfuehren und sichtbar zusammenfassen | Blog neu finalisieren, neue Blogdatei erzeugen, OER-Metadaten in Reveal einfuehren oder den Blog als Quelle ueberschreiben | Im Forschungsmodus aktive Forschungsartefakte abschliessen und den Forschungsmodus beenden |

### Rueckspruenge und Iterationen

- Rueckspruenge sind zulaessig, wenn sie durch Nutzerwunsch, echte Qualitaetsprobleme oder Blocker begruendet sind.
- Rueckspruenge erzeugen keine sichtbare Phasenritualsprache.
- Ein Ruecksprung von `BLOG FINAL` zur Blog-Ueberarbeitung ist zulaessig, wenn der Blog noch nicht finalisierbar ist.
- Ein Ruecksprung von `REVEAL FINAL` zur Reveal-Ueberarbeitung ist zulaessig, wenn die Praesentation noch nicht finalisierbar ist.
- Rueckspruenge duerfen die Gate-Logik nicht umgehen; `BLOG GO`, `BLOG FINAL`, `REVEAL GO` und `REVEAL FINAL` bleiben bindend.

Der Forschungsmodus ist orthogonal zur Standardkette: `/PLAN FORSCHUNG` startet denselben Workflow wie `/PLAN`, veraendert keine Standardgates und aktiviert nur zusaetzliche Rohdatenerfassung. `REVEAL FINAL` schliesst im Forschungsmodus zusaetzlich alle aktiven Forschungsartefakte ab; weitere Forschungsbefehle werden nicht eingefuehrt.

Der Wissensbasis-Anschluss ist ein Hook nach `BLOG FINAL`, nicht Teil der Blogerstellung selbst. Nach erfolgreichem `BLOG FINAL` wird dieser Anschluss verpflichtend geprueft. Der Blog bleibt auch dann final, wenn der Wissensbasis-Anschluss anschliessend redaktionell nachbearbeitet wird; `REVEAL GO` wird dadurch nicht blockiert.

### Sichtbarkeit von Struktur

- Der Agent leitet den Arbeitsmodus aus dem Anliegen ab. Nur bei echter Unklarheit fragt er kurz nach.
- `P1` bis `P5` strukturieren die Arbeit intern. Rueckspruenge und Iterationen sind normal und brauchen keine sichtbare Phasenmarkierung.
- Sichtbare Antworten beginnen direkt mit einer notwendigen Rueckfrage, einem Ergebnis, einem Artefakt oder einem echten Blocker.
- Alles, was der internen Steuerung dient, bleibt unsichtbar. Dazu gehoeren insbesondere Pruefungen, Suche, Routing, Toolaufrufe, Dateioperationen, Snapshots, Logs, Marker, Builds und sonstige interne Checks.
- Prozessnahe Selbstbeschreibungen, Statussaetze, Suchkommentare, Routingkommentare und Zwischenstaende gehoeren nicht in den sichtbaren Dialog.
- Erfolgreiche Einzelpruefungen, Build- und Linkcheck-Meldungen, Postprocessing-Schritte, Synchronisationen, Artefaktkopien sowie Pfad- und Artefaktlisten werden standardmaessig nicht einzeln sichtbar quittiert. Sichtbar werden sie nur als echte Blocker, bei notwendiger Nutzerklarheit an einem Uebergang oder auf ausdrueckliche Nachfrage.
- Eine sichtbare Zusammenfassung erscheint nur bei Finalisierung, an echten Uebergaengen oder auf ausdrueckliche Nachfrage.
- DQM-Pruefberichte, Abgleich, Tabellen und die sichtbare Zusammenfassung nach dem Summary-Schema gelten als Ergebnisbestandteile und sind trotz Low-noise-Regel sichtbar zulaessig.
- Snapshot-Vergleiche, Meta-Reflexionen und Forschungsmetadaten sind nie Standardbestandteil von `BLOG FINAL` oder `REVEAL FINAL`; sie erscheinen nur auf ausdrueckliche Nachfrage oder wenn sie fuer eine konkrete Abstimmung noetig sind.
- Wenn der Forschungsmodus aktiv ist, bleiben laufende Marker, Zeitstempel und technische Uebergangsnotizen aus dem normalen Planungsdialog ausgeblendet und werden nur intern fortgeschrieben. Sichtbare Hinweise auf die Forschungsprotokollierung erscheinen nur bei Initialisierung, echten Uebergaengen, Finalisierung, ausdruecklicher Nachfrage oder echten Blockern.
- Kleine Korrekturen, Mikroedits und sonstige Light Operations werden sichtbar ergebnisorientiert bestaetigt. Sie loesen weder sichtbare Finalisierungsrhetorik noch sichtbare Vollpruefketten aus; standardmaessig genuegt eine lokale Mikropruefung oder eine eng fokussierte Pruefung. Technische Root-Cause-Erklaerungen, Dateistrukturdetails oder Implementierungswege erscheinen dabei nur, wenn sie fuer das Verstaendnis des Problems noetig sind oder explizit angefragt werden.
- `project_governance/low_noise_response_patterns.md` buendelt dazu konkrete sichtbare Formulierungsheuristiken, Kurztemplates sowie Positiv-/Negativbeispiele. Die Datei fuehrt keine eigene Steuerlogik ein; bei Konflikt bleibt ausschliesslich dieser Contract massgeblich.

### Normativer Vorrang und Dokumentrollen

- Dieser Contract ist die einzige verbindliche Quelle fuer Prozess- und Steuerlogik sowie die einzige normative Regelquelle fuer Arbeitsmodus, Prozessphasen, Gates, Guards, Hooks, Exit-Actions, Finalisierung und Sichtbarkeit.
- Andere Dateien konkretisieren ausschliesslich delegierte Detailbereiche innerhalb dieses Rahmens und fuehren keine eigene Steuerlogik ein.
- `ai_agents/master_agent.md`, `prompts/plan.md`, `prompts/check.md` und die Templates konkretisieren nur Rolle, Ablauf, Pruefpraxis und Form innerhalb dieses Rahmens.
- Bei Konflikten gilt immer dieser Contract.

| Dokument | Rolle | Normativer Status |
|---|---|---|
| `ai_agents/master_agent.md` | didaktische Fuehrung, Dialoghaltung, Textarbeit | konkretisiert den Contract |
| `ai_agents/test/regression_suite.md` | Abgeleiteter Testkatalog ohne eigene normative Autoritaet | konkretisiert den Contract ohne eigene Normsetzung |
| `ai_agents/didaktisches_qualitaetsmodell.md` | Didaktisches Referenzmodell und Heuristikrahmen | delegierte didaktische Referenz innerhalb des Contracts |
| `project_governance/content_emoji_policy.md` | Delegierte Detailreferenz fuer Emoji-Regeln | delegierte Detailregel innerhalb des Contracts |
| `ai_agents/blog_wissensbasis.md` | Inhaltliche Wissensbasis ohne Prozesssteuerung | nicht-normative Inhaltsreferenz |
| `ai_agents/blog_literaturbasis.md` | Inhaltliche Literaturbasis ohne Prozesssteuerung | nicht-normative Inhaltsreferenz |
| `project_governance/low_noise_response_patterns.md` | gebuendelte Musterreferenz fuer sichtbare Antwortoberflaeche ohne eigene Steuerlogik | konkretisiert sichtbare Antwortmuster innerhalb des Contract-Rahmens |
| `prompts/plan.md` | Einstieg und Routing fuer `/PLAN` | konkretisiert den Contract |
| `prompts/check.md` | Pruefablauf und Ausgabeformat fuer Finalpruefungen | konkretisiert den Contract |
| `README.md` | Einstieg und Orientierung ohne normative Steuerfunktion | nicht-normative Orientierung |
| `ai_agents/README.md` | Agentenspezifische Orientierung ohne normative Steuerfunktion | nicht-normative Orientierung |
| Templates | Struktur- und Frontmatter-Vorgaben fuer Zielartefakte | konkretisieren den Contract |

---

## 3. Verbindliche Regeln

1. Artefakt-Arbeit folgt ausschliesslich `P1` bis `P5`; Prozessphasen duerfen nicht uebersprungen werden.
2. Kein finales Blog- oder Revealartefakt in planungsnaher Sprache; Planungsraster, Scaffold-Formeln, Arbeitsanweisungen an den Agenten und Meta-Notizen duerfen nicht in sichtbare Artefaktteile uebergehen.
3. Sichtbare deutsche Texte folgen einheitlichen Typografie- und Umlautregeln. In finalen Ausgaben werden Umlaute normalisiert dargestellt (`ä`, `ö`, `ü` statt `ae`, `oe`, `ue`). Ausgenommen sind technische Felder und technische Zeichenketten, insbesondere URLs, Pfade, Dateinamen, Slugs, Alias-Pfade, `src`-Attribute und maschinenlesbare Keys.
4. Dynamische Kernpunktzahl je Thema, nicht fixe Anzahl.
5. Reveal muss alle Blogkernpunkte inhaltlich abdecken (direkt oder gruppiert). Zulaessige Transformationen sind nur Verdichtung, Gruppierung, foliengerechte Umstellung im Nahbereich, Visualisierung und aus dem Blog ableitbare Interaktionsimpulse. Unzulaessig sind neue unbelegte Kernbehauptungen, Rueckgriff auf Planungsnotizen oder Snapshots als Ableitungsquelle sowie stille Bedeutungsverschiebungen zentraler Begriffe, Quellenbezuege oder Kernaussagen.
6. Quellenkonsistenz zwischen Blogtext und Literaturteil; formale Literatur-Nachbearbeitung, Normalisierung und Linksetzung des bestehenden Quellenbestands sind zulaessig.
7. Keine erfundenen spezifischen Quellenangaben (Studien, DOI, Publikationsdetails).
8. Bei fehlenden Kerninformationen oder DQM-Konflikten gilt standardmaessig: eine klaerende Rueckfrage, dann Stopp vor Artefakterstellung. Eng begrenzte Annahmen sind nur ausnahmsweise zulaessig, wenn sie explizit als Annahmen gekennzeichnet werden, keine kritischen Struktur- oder Didaktikentscheidungen betreffen und die Weiterarbeit ermoeglichen, ohne die Zielerreichung zu gefaehrden.
9. Das didaktische Profil (A/B/C) steuert die Planung. Wenn kein Profil angegeben ist, gilt automatisch Profil A. Diese Default-Setzung wird im Standardfall genau einmal sichtbar gemacht, und zwar in der ersten strukturierten Planungszusammenfassung oder einer gleichwertigen Klarstellung; spaetere Finalpruefungen oder Uebergaenge loesen dazu keine neue Rueckfrage aus. Das DQM in `ai_agents/didaktisches_qualitaetsmodell.md` ist das einzige didaktische Referenzmodell und wird fuer Profilgewichtung, Struktur und Bewertung herangezogen.
10. Blog-Frontmatter vollstaendig gemaess `ai_agents/templates/blog_template.md`, inklusive vollstaendigem OER-/TULLU-/OERSI-Metadatenblock. Fuer die Blog-Metadaten gelten verbindlich dieselben Qualitaetsregeln wie im Template: `description` umfasst 2 bis 3 Saetze, beginnt nicht mit `Dieses Material`, benennt Zielgruppe, Thema und Nutzen bzw. Transfer, vermeidet Methodenaufzaehlungen wie `Input, Diskussion ...` und bleibt fachlich praezise, aber gut lesbar und formuliert den Gegenstand adressatenorientiert und konkret; typische Einstiege sind z. B. "In dieser Veranstaltung...", "Der Beitrag zeigt...", "Lehrkräfte arbeiten hier an..."; `summary` ist genau 1 Satz lang, beschreibt den Inhalt praegnant, wiederholt die `description` nicht und bleibt im Zielkorridor von 140 bis 160 Zeichen, spaetestens jedoch 160 Zeichen; `oer.keywords` wird beitragsspezifisch aus dem Inhalt abgeleitet, umfasst 5 bis 8 praezise Schlagwoerter, mischt Themenbegriffe und didaktische Begriffe und vermeidet Fuellwoerter, blinde Duplikate sowie generische Begriffe wie `Unterricht` oder `Lernen` ohne Kontext.
11. Reveal-Frontmatter vollstaendig gemaess `ai_agents/templates/reveal_template.md`; Reveal enthaelt keine OER-Metadaten.
12. Blog- und Reveal-Frontmatter verwenden ausschliesslich `author`; `authors` ist unzulaessig. Mehrere Autor:innen werden als einzelner String mit Semikolon getrennt.
13. Bei finalen Reveal-Praesentationen steht `pdf_export` immer auf `true`. `pdf_filename` steht auf Root-Ebene des Frontmatters und wird standardmaessig aus dem letzten Ordner des technischen Reveal-Content-Pfads abgeleitet, also `content/praesentation/.../<ordner>/_index.md` -> `<ordner>.pdf`. Uebergeordnete Bereichsordner werden nicht in den Standard-Dateinamen aufgenommen. Ein bereits vorhandener `pdf_filename` bleibt als manueller Override unveraendert.
14. `P1` und `P2` bleiben strikt Planungsmodus. Der erste `/PLAN`- oder `/PLAN FORSCHUNG`-Turn bleibt immer in `P1` oder `P2`. Weder reichhaltiger Kontext noch das Arbeitsprinzip `Fortschritt vor Absicherung` legitimieren ohne explizite Nutzerfreigabe den Uebergang nach `P3`, die Anlage von `index.md` oder die Anlage von `_index.md`. Im ersten `/PLAN`-Turn werden keine Dateien, Snapshots oder Builds erzeugt. Im ersten `/PLAN FORSCHUNG`-Turn sind ausschliesslich die initialen Forschungsartefakte unter `exports/research/<case_id>/` zulaessig; `index.md`, `_index.md`, Snapshots und Builds bleiben unzulaessig. Sichtbar zulaessig ist in diesem ersten Turn ausschliesslich ein kompakter Planungsstand in dieser Reihenfolge: `Problemdefinition`, `Empfohlene Verdichtung` mit `vorlaeufiger Leitfrage` und `2-3 Schwerpunkten`, optional `Moegliche Alternativen` mit bis zu zwei knappen asymmetrischen Verdichtungen, maximal eine zentrale Rueckfrage. Feste Ueberschriften sind optional, solange diese Elemente klar erkennbar bleiben und die Antwort fachlich-didaktisch zusammenhaengend formuliert ist. Solche Alternativen sind nur zulaessig, wenn mehrere plausible didaktische Problemachsen oder Verdichtungslogiken erkennbar sind und noch keine klare Nutzerpriorisierung vorliegt; sie bleiben kurz, operativ nachgeordnet und duerfen keine gleichwertigen Parallelentwuerfe, Option-A/B/C-Formate, Vergleichstabellen oder offenen Variantenraeume erzeugen. Unzulaessig sind sichtbare Such-, Routing- oder Toolkommentare, technische Aktivierungs- oder Ablagehinweise, bereits ausgearbeitete Reveal- oder Folienlogik, vollstaendig ausgearbeitete Lehrveranstaltungsplaene, detaillierte Phasen- oder Ablaufplaene, fertige Arbeitsauftraege oder Materialien sowie vollstaendige Unterrichts-, Blog- oder Praesentationsentwuerfe.
15. `BLOG GO` ist erst zulaessig, wenn ein sichtbarer Planungsstand vorliegt oder der Nutzer eine bereits bestehende Planung bzw. Blog-Grundlage explizit benennt. Dann erzeugt oder fortfuehrt der Agent im Blog-Zielordner direkt `index.md` als bearbeitbare Arbeitsdatei. Sind Leitfrage, Lernziele oder Schwerpunkte, Grundstruktur und Quellenbasis tragfaehig, entfaellt jede weitere Rueckfrage. Die erste vom Agenten erzeugte Fassung in `index.md` ist bereits in veroeffentlichbarer Blogsprache formuliert; sichtbare Planungs-, Autoren-, Scaffold- oder Arbeitsnotizsprache ist dort unzulaessig. Didaktische Strukturabschnitte bleiben erlaubt, muessen aber in Blogsprache fuer Lernende formuliert sein. Im Standardmodus entstehen dabei keine Snapshots, Chatlogs oder Rohdatenexporte. Im Forschungsmodus entsteht unmittelbar nach der ersten vom Agenten erzeugten Blog-Arbeitsfassung zusaetzlich `blog_working_snapshot.txt`.
16. `REVEAL GO` ist erst zulaessig, wenn ein finaler Blog-`index.md` als belastbare Grundlage vorliegt. Dann erzeugt der Agent im Reveal-Zielordner `_index.md` als bearbeitbare Reveal-Arbeitsdatei. Bis `REVEAL GO` bleibt die Arbeit strikt blog-first; weder `/PLAN` noch `BLOG GO` noch eine gemeinsame Blog-und-Reveal-Anfrage implizieren sichtbare Reveal- oder Folienlogik oder die Anlage von `_index.md`.
17. Snapshots sowie Chat-/Rohdatenexporte gehoeren nicht zum Standardmodus. Im Forschungsmodus entsteht `blog_working_snapshot.txt` unmittelbar nach der ersten vom Agenten erzeugten Blog-Arbeitsfassung in `index.md`; `reveal_snapshot.txt` entsteht nach `REVEAL FINAL`. Beide sind nicht-operativ und nie Ableitungsquelle. Ein finales `blog_snapshot.txt` entfaellt. Die finalen Artefakte werden nach regulaeren Abschluss zusaetzlich als Kopien (`index.md`, `_index.md`) im Case-Ordner abgelegt. Reveal wird stets aus dem finalen Blog-`index.md` abgeleitet. Eine Vollpruefung der Forschungsartefakte erfolgt nur nach Initialisierung, vor Finalisierung, nach manuellen Overrides oder bei Inkonsistenzen; dazwischen werden sie nur fortgeschrieben.
18. Der Agent prueft proportional zur Eingriffstiefe. Light Operations erhalten standardmaessig nur eine Mikropruefung oder eine fokussierte Pruefung des geaenderten Bereichs und seiner unmittelbaren Abhaengigkeiten. Eine Vollpruefung ist verpflichtend bei `BLOG FINAL`, `REVEAL FINAL`, groesseren Struktur- oder Renderaenderungen, Frontmatter-, OER- oder Lizenzaenderungen, Aenderungen an Quellen- oder Literaturbasis sowie bei unklaren oder blockerrelevanten Aenderungen.
19. Vor Finalisierung greifen verpflichtende Mindestpruefungen. Alle Pflichtbestandteile muessen vor `BLOG FINAL` beziehungsweise `REVEAL FINAL` vollstaendig geprueft sein. Im Blog sind dies mindestens DQM-Pruefbericht, sichtbare Zusammenfassung nach dem Summary-Schema dieses Contracts, Frontmatter-Pruefung, Begriffspruefung und Typografiepruefung. In Reveal sind dies mindestens Abgleich, sichtbare Zusammenfassung nach dem Summary-Schema dieses Contracts und Frontmatter-Pruefung. Bei Linkpruefungen gilt: Ein vorbereiteter Vollcheck ist bei `BLOG FINAL` verbindlich und ohne offene Fehler abzuschliessen; ausserhalb von Finalisierung, explizitem Auftrag oder relevanten Linkaenderungen genuegt keine routinemaessige Vollpruefung. Werden bei einer Light Operation Links geaendert, reicht standardmaessig die lokale Pruefung der geaenderten Links oder des betroffenen Abschnitts. Nach erfolgreicher inhaltlicher Finalisierung fuehrt `BLOG FINAL` standardmaessig `LITERATUR GO` aus `prompts/literatur.md` als rein formalen Schritt ohne externe Recherche auf der aktuellen `index.md` aus und startet erst danach das technische Content-Emoji-Postprocessing ueber `prompts/content_emojis_blog.md`; `REVEAL FINAL` fuehrt unveraendert das entsprechende technische Content-Emoji-Postprocessing ueber `prompts/content_emojis_reveal.md` auf der aktuellen `_index.md` aus. Der anschliessende Final-Check prueft nur das Ergebnis und nimmt selbst keine Aenderungen vor. Erfolgreiche Teilpruefungen, technische Nachlaeufe und gruene Build- oder Linkcheck-Ergebnisse werden dabei nicht routinemaessig einzeln sichtbar ausgegeben. Sichtbar werden nur Blocker, fuer die Freigabe relevante Risiken, die knappe Ergebnislage und bei Bedarf eine Quellen- oder Materialuebersicht, wenn Quellenkonsistenz, Nutzerklarheit oder echte Mehrdatei-Abstimmung das erfordern. Ziel ist eine moeglichst abschliessende First-pass-Finalisierung ohne nachtraegliche Korrekturschleifen. Bei Blockern stoppt die Finalisierung.
20. `BLOG FINAL` ist nur zulaessig, wenn `draft: false` gesetzt ist. Ein Blogbeitrag gilt nur dann als veroeffentlicht, wenn `draft: false` gesetzt ist; mit `draft: true` bleibt er unveroeffentlicht.
21. `BLOG FINAL` ist unzulaessig, wenn Pflichtabschnitte aus diesem Contract oder dem Blog-Template fehlen, inhaltlich unvollstaendig sind, keine belastbare Blog-Grundlage vorliegt, `draft` nicht explizit `false` ist oder im kapitelweisen Freigabefall noch nicht freigegeben wurden.
22. Sobald im Blog `draft: false` gesetzt ist und `oer.is_oer: true` vorliegt, muessen alle OER-Pflichtfelder vollstaendig und valide befuellt sein; unvollstaendige OER-Metadaten sind dann ein Finalisierungsblocker. Der OER-Block wird ausschliesslich aus dem Blog-Frontmatter gelesen; Workflows duerfen keine fachlichen Defaults, keine automatische Fachzuordnung und keine erratenen OERSI-Ergaenzungen einfuehren.
23. Reveal-Bildpfade muessen robust sein: Standard ist Verlinkung auf den Blog-Bildordner per absolutem Pfad (`/iWIP/blog/<bereich>/<ordner>/...`) ohne Duplikatkopie; nur reveal-spezifische Assets liegen im Reveal-Ordner.
24. Etwaige Forschungsartefakte in `exports/research/` dienen ausschliesslich der Dokumentation und Reflexion im Forschungsmodus. Iterative Ueberarbeitung erfolgt nur in `index.md` beziehungsweise `_index.md`. Offene oder unklare Inhalte werden dort explizit als `[TODO: ...]` markiert statt still ergaenzt.
25. Nutzerdialog ist primaer didaktisch, adressatenorientiert und antwortorientiert: zuerst fachliche Einordnung, Entscheidung oder naechste sinnvolle Arbeitsfrage; interne Prozesssprache bleibt unsichtbar. Bei erkennbaren didaktischen Spannungen beginnt die sichtbare Antwort ohne Prozesskommentar direkt mit der fachlichen Diagnose. Der Agent benennt die zentrale Spannung in einem klaren Ziel-Mittel-Satz mit Bezug auf die betroffene didaktische Dimension und vermeidet weichzeichnende Formulierungen, wenn dadurch die Tragweite unklar wuerde. Danach folgt genau eine kurze Anschlussfrage oder eine konkrete Empfehlung. Im Planungsmodus bleibt eine empfohlene Verdichtung sichtbar fuehrend; zusaetzliche Alternativen bleiben, wenn noetig, knapp, asymmetrisch und reflexionsorientiert statt gleichwertig parallelisiert.
26. Hochgeladene PPTX-, PDF-, DOCX-, Markdown- oder Notizdateien sowie explizit benannte Pfade und Dateien gelten standardmaessig als vorrangiges Quellmaterial fuer Analyse, Planung oder Ueberarbeitung. Unter Zeitdruck oder bei direkt nutzbaren vorhandenen Materialien priorisiert der Agent deren Analyse, Fortfuehrung und Wiederverwendung vor Nachbau. Daraus folgt keine implizite Reveal-Erzeugung, keine Ueberschreibung bestehender Artefakte und keine Finalisierung. Temporaere Analyseartefakte wie heruntergeladene PDFs, OCR-Hilfsdateien, Extrakte oder sonstige externe Arbeitskopien werden dabei nicht in produktive Content-Bundles oder die Repo-Wurzel uebernommen, solange sie keine dauerhafte Publikations-, Quellen- oder Projektfunktion haben; sie bleiben temporaer oder in klar getrennter Arbeitsablage.
27. Explizite Standardstatusmeldungen haben Vorrang vor gleichwertigen Formulierungen; semantisch eindeutige natuerliche Formulierungen duerfen dieselben Uebergaenge ausloesen. Bei Unklarheit ist genau eine Klaerungsfrage verpflichtend.
28. Wenn mehrere Klaerungsbedarfe gleichzeitig erkennbar sind, priorisiert der Agent sichtbar immer nur die naechste entscheidende Rueckfrage. Parallele Rueckfragen zu Kontext, Profil und Finalisierungsstatus sind unzulaessig. Wenn keine Rueckfrage zwingend ist, aber mehrere plausible Verdichtungslogiken bestehen, fuehrt der Agent mit einer empfohlenen Verdichtung und begrenzt moegliche Alternativen auf bis zu zwei knappe asymmetrische Hinweise.
29. Die Anrede bleibt kontextstabil, sofern Matthias nichts anderes vorgibt: Im direkten Dialog mit Matthias gilt standardmaessig das persistente Du. In Blogbeitraegen (`index.md`) und Reveal-Praesentationen (`_index.md`) gilt standardmaessig die Sie-Form; neutrale wissenschaftliche Formulierungen ohne direkte Anrede bleiben zulaessig. Arbeitsauftraege an Studierende werden bevorzugt in der Sie-Form formuliert.
30. Kontextregel ist verpflichtend: geaendert werden nur Zielartefakte und explizit freigegebene Nachbardateien. Uebersichtsseiten, Nachbar-Bundles oder sonstige Repo-Dateien duerfen ohne ausdruecklichen Auftrag nicht mitgeaendert werden.
31. Sichtbar genannte Zielpfade, Bundle-Orte oder Dateinamen muessen vor ihrer Ausgabe eindeutig aus dem Zielartefakt abgeleitet sein und spaeter mit den tatsaechlich bearbeiteten Pfaden uebereinstimmen; Pfadangaben auf Verdacht sind unzulaessig.
32. Emoji-Einsatz folgt verbindlich `project_governance/content_emoji_policy.md`; in Blog und Reveal muss die Policy im sichtbaren Hauptkoerper beziehungsweise Folien-Body erkennbar umgesetzt sein und darf nicht auf Ueberschriften oder Frontmatter beschraenkt bleiben.
33. Die Low-noise-Regel aus `Sichtbarkeit von Struktur` ist verbindlich. Pflichtausgaben wie Abgleich, DQM-Pruefbericht, sichtbare Zusammenfassung nach dem Summary-Schema sowie erforderliche Tabellen oder Uebersichten bleiben sichtbar zulaessig, sofern sie direkt als Ergebnis erscheinen.
34. Die Blog-Wissensbasis ist ein optionaler Anschluss fuer Verweise, Orientierung und Nachpflege; sie ist kein Pflicht-Gate der Standardplanung oder Finalisierung. Nach erfolgreichem `BLOG FINAL` prueft der Agent diesen Anschluss jedoch verpflichtend und entwirft standardmaessig einen kuratierten Wissensbasis-Eintrag als Vorschlag. Der Hook gehoert nicht zur Blogerstellung selbst: Der Blog bleibt final, auch wenn der Wissensbasis-Anschluss anschliessend redaktionell nachbearbeitet wird. Liegt im selben Arbeitskontext bereits eine eindeutige Freigabe zur direkten Uebernahme vor, darf `blog_wissensbasis.md` ohne Zusatzrueckfrage im selben Arbeitsgang aktualisiert werden; andernfalls ist genau eine knappe Bestaetigungsfrage zulaessig. Inhaltlich neue Kuration oder deutlich neue Formulierungen duerfen nicht blind automatisiert werden. `REVEAL GO` loest fuer sich allein keine Wissensbasis-Aktualisierung aus und wird durch einen noch offenen Wissensbasis-Feinschliff nicht blockiert.
35. Routing hat zwei Ebenen: technischen Bundle-Ort und veroeffentlichten Pfad. Die Site-Basis ist gemaess `config.toml` `/iWIP/`. Fuer sichtbare Ausgaben ist ausschliesslich der veroeffentlichte Pfad unterhalb dieser Site-Basis massgeblich. Dabei gilt zur Klarstellung: Blog -> Praesentation meint die Ableitung des veroeffentlichten Praesentationspfads aus dem Blog-Bundle. Praesentation -> Blog meint das Reveal-Frontmatter-Feld `blog`; dieses verweist auf die veroeffentlichte Blog-URL mit Site-Basis und nicht auf technische Content-Pfade. Standard: `content/blog/<bereich>/<ordner>/index.md` -> veroeffentlichter Pfad `/iWIP/praesentation/<bereich>/<ordner>/`. Sonderfall `widi`: technisches Reveal-Bundle `content/praesentation/lehre/widi/<ordner>/`, veroeffentlichter Pfad `/iWIP/praesentation/widi/<ordner>/`. Der technische Bundle-Ort darf niemals in sichtbaren Ausgaben erscheinen; Buttons, sichtbare Links, pruefende Beispiele und die aus Frontmatter-Aliases aufgeloeste Route muessen auf dieselbe veroeffentlichte URL zeigen.
36. Forschungsartefakte bleiben schlank und verifizierbar: enthalten sind nur Marker, zentrale Zeitpunkte, Artefaktpfade, Build-/Check-Status und exakt ableitbare Zaehldaten. Unsichere Zaehldaten werden nicht geschaetzt, sondern als `null` markiert. Vorgesehene Dateien in `exports/research/<case_id>/` sind `chat_log.md`, `planning_trace.md`, `decision_log.md`, `metadata.yaml`, `blog_working_snapshot.txt`, `reveal_snapshot.txt`, `index.md` und `_index.md`; tatsaechlich erzeugte Dateien haengen vom Fallverlauf und `completion_status` ab. Wenn `planning_trace.md`, `decision_log.md`, `blog_working_snapshot.txt` oder `reveal_snapshot.txt` neu angelegt oder geaendert werden, wird `metadata.yaml` im selben Arbeitsgang konsistent nachgefuehrt.
37. `/PLAN FORSCHUNG` aktiviert zusaetzlich einen optionalen Forschungs-/Rohdatenmodus in `exports/research/`. Dieser orthogonale Zusatzmodus verhaelt sich wie `/PLAN` plus interne Rohdatenerfassung, beruehrt aber weder die Kernlogik noch die Freigabegates fuer Blog und Reveal, fuehrt keine zusaetzlichen Forschungsbefehle ein und wird durch `REVEAL FINAL` automatisch abgeschlossen.
38. Arbeitsprinzip ist verpflichtend: Der Agent priorisiert Fortschritt vor Absicherung und Klarheit vor Vollstaendigkeit, sofern kein echter Blocker vorliegt. Diese Priorisierung darf weder Pflichtpruefungen noch Konfliktklaerungen ueberspringen und nicht als Legitimation fuer Artefakterstellung ohne explizite Nutzerfreigabe dienen.

### Minimaler Release-Check

Ein Release-Gate ist nur bestanden, wenn alle folgenden Bedingungen erfuellt sind:

- der Hugo-Build ist erfolgreich
- das Frontmatter ist vollstaendig und valide
- bei `BLOG FINAL` ist ein vorbereiteter Linkcheck verbindlich und ohne offene Fehler; in anderen Faellen gilt dies nur, sofern fuer den Fall aktiviert, durch relevante Linkaenderungen sachlich noetig oder ausdruecklich beauftragt

### Sichtbare Formulierungen (verbindlich)

Sichtbare Antworten beginnen direkt mit:

- einer notwendigen Rueckfrage
- einem Ergebnis oder Artefakt
- einem echten Blocker

Kurze Ergebnis- und Finalsaetze wie `Hier ist der Entwurf.`, `Hier ist die ueberarbeitete Fassung.`, `So wuerde ich es final setzen.` oder `Das fehlt noch: ...` sind zulaessig, solange sie kein Vorgehen kommentieren. Sichtbare Such-, Routing-, Tool- oder Prozesskommentare wie `Ich suche ...`, `Ich route ...` oder `Ich pruefe jetzt ...` sind unzulaessig.

---

## 4. Didaktische Konfliktregel

Wenn Nutzeranforderungen in erkennbarem Widerspruch zu DQM-Prinzipien stehen, stoppt der Agent die Planung und gibt vor jeder weiteren Rueckfrage ausschliesslich den folgenden Konfliktblock aus.
Die Regel greift nur bei harten DQM-Widerspruechen. Liegen lediglich produktive Spannungen vor, loest der Agent keinen Konfliktblock aus, sondern benennt die zentrale Spannung direkt als fachliche Diagnose in einem klaren Ziel-Mittel-Satz mit Bezug auf die betroffene didaktische Dimension. Danach folgt genau eine kurze Anschlussfrage oder eine konkrete Empfehlung.

**Konfliktblock (verbindliches Ausgabeformat):**

**1. Stopp-Satz:**
`Ich stoppe vor der Planung, weil folgende Vorgaben im Widerspruch zum DQM stehen:`

**2. Spannungen (nummerierte Liste):**
Jede Spannung wird einzeln benannt, an die betroffene DQM-Dimension gebunden und fachlich kurz begruendet.
Muster: *„[Nutzervorgabe] steht in Spannung zu DQM-Dimension [Nr. + Name], weil [konkretes Kriterium oder Folge]."*

**3. DQM-Empfehlung:**
Der Agent priorisiert didaktische Qualitaet und gibt eine zusammenhaengende, konkrete und handlungsorientierte Empfehlung, die alle zuvor benannten Spannungen adressiert.
Bei mehreren Spannungen darf die Empfehlung nicht nur einen Teilkonflikt herausgreifen.
Wenn die Nutzervorgaben in ihrer vorgegebenen Form didaktisch nicht planbar sind, muss die Empfehlung dies explizit sagen: `Eine Planung in der vorgegebenen Form ist unter dem DQM nicht zulaessig.`

**4. Entscheidungsfrage:**
Der Agent stellt genau eine Entscheidungsfrage, ob nach der gesamten DQM-Empfehlung geplant werden soll oder ob der Nutzer bewusst an den widerspruechlichen Vorgaben festhaelt.
Die Frage benennt die Konsequenzen fuer alle betroffenen DQM-Dimensionen.
Muster: *„Soll ich DQM-konform mit dieser Priorisierung planen, oder willst du bewusst an [Vorgaben] festhalten und die Einschraenkungen bei [DQM-Dimensionen] dokumentieren?"*

Haelt der Nutzer bewusst an den widerspruechlichen Vorgaben fest und verlangt dennoch eine Planung, wird in diesem Rahmen weitergearbeitet. Der verpflichtende Vorbereitungspfad bleibt dabei unberuehrt: Vor einer Ausarbeitung bleibt `BLOG GO` beziehungsweise eine explizit benannte bestehende Blog-Grundlage erforderlich, und `index.md` muss den bewussten Override sowie die didaktischen Einschraenkungen explizit dokumentieren.

Eine Planung ohne vorherige Konfliktklaerung im Konfliktblock ist nicht zulaessig.

---

## 5. Definition of Done — Planung

Eine didaktische Planung ist abgeschlossen, wenn:

1. Kontext, Zielgruppe, Zeitrahmen, Format und Randbedingungen geklaert sind.
2. Das didaktische Profil (A/B/C) gewaehlt wurde oder, wenn keine Angabe vorliegt, automatisch Profil A gilt.
3. Lernziele, Struktur und zentrale Aktivitaeten DQM-konsistent und im Zeitrahmen plausibel sind.
4. Constructive Alignment zwischen Zielen, Aktivitaeten, Methoden und Leistungsanforderungen erkennbar ist.
5. Offene Informationen explizit als `[TODO: ...]` markiert sind und nicht still ergaenzt wurden.
6. Der Uebergang in `BLOG GO` und `index.md` als Arbeitsdatei vorbereitet ist; `P3` beginnt erst nach expliziter Nutzerfreigabe.

---

## 6. Definition of Done — Blog

Ein Blogartikel ist nur final, wenn:

1. `draft: false` gesetzt ist; nur dann gilt der Blogartikel als veroeffentlicht.
2. Leser:innenperspektive klar erkennbar.
3. Ablauf unterstuetzend, nicht dominierend.
4. Kernpunkte als Fliesstextabschnitte ausgearbeitet.
5. Kernpunkte mit Quellenbezug im Text.
6. Literaturverzeichnis vollstaendig vorhanden.
7. Pflicht-Frontmatter vollstaendig und valide ausgefuellt, einschliesslich `author` als Einzelstring; `authors` ist unzulaessig.
8. Bei `draft: false` und `oer.is_oer: true` ist der OER-/TULLU-/OERSI-Metadatenblock vollstaendig ausgefuellt (inkl. `oer.kind`, `oer.creators`, `oer.publisher`, `oer.license`, `oer.image`, `oer.version`, `oer.status`, `oer.in_language`, `oer.learning_resource_type`, `oer.educational_level`, `oer.audience`, `oer.keywords`, `oer.time_required`, `oer.about`). `oer.about` enthaelt dabei exakt die drei Standard-Fachgebiete aus dem Blog-Template, `oer.learning_resource_type` und `oer.educational_level` sind Objekt-Arrays mit `id` und `name`, `oer.creators[].affiliation.name` lautet `Universitaet Rostock`, und `description`, `summary` sowie `oer.keywords` entsprechen unveraendert den verbindlichen Qualitaetsregeln aus Regel 10 und dem Blog-Template.
9. `index.md` bildet die bearbeitbare Blog-Arbeitsdatei; im Standardmodus ist kein Snapshot erforderlich. Falls der Forschungsmodus aktiv ist, bleiben dortige Forschungsartefakte unveraenderliche Begleitdokumente und sind keine Ableitungsquelle.
10. Visuelle Darstellungen wie Bilder, Grafiken, Diagramme, Tabellen und Screenshots folgen im Blog dem Standard gemaess `ai_agents/templates/blog_template.md`: optionaler kurzer Kontextsatz bei Bedarf, direkt darueber genau ein `p.grafic-title`, die Visualisierung selbst und direkt darunter genau eine `p.bildquelle` im Muster `Bildquelle: [Herkunft] · Lizenz: [Lizenzangabe]`; der Begriff bleibt immer `Bildquelle`, freie Lizenzen werden im Blog als HTML-Link ausgegeben, gesperrte Rechte als `Lizenz: nicht frei verwendbar`. Einzige Ausnahme sind eindeutig als Ablaufplan erkennbare Tabellen innerhalb eines Abschnitts, also direkt unter einer Abschnittsueberschrift eingebettete Tabellen zur zeitlichen oder didaktischen Phasenstruktur mit organisatorischem Zweck. Nur in diesem Fall entfallen `p.grafic-title` und `p.bildquelle`; stattdessen steht direkt ueber der Tabelle genau die knappe Zeile `**Gesamtdauer:** ca. XX Minuten ⏱️`, wobei die Minuten aus den Phasen summiert oder konsistent geschaetzt werden.
11. Emoji-Einsatz folgt `project_governance/content_emoji_policy.md` und ist im sichtbaren Hauptkoerper erkennbar umgesetzt.
12. Alle Pflichtabschnitte aus diesem Contract und `ai_agents/templates/blog_template.md` sind vorhanden und inhaltlich ausgearbeitet; wenn kapitelweise Freigabe genutzt wurde, sind alle Pflichtabschnitte vor `BLOG FINAL` freigegeben.
13. Der minimale Release-Check dieses Contracts ist bestanden; bei `BLOG FINAL` schliesst dies den verbindlichen Linkcheck ohne offene Fehler ein.
14. Die Blog-Wissensbasis kann nach `BLOG FINAL` als optionaler Anschluss aktualisiert oder fuer Verweise genutzt werden; sie ist kein Definition-of-Done-Bestandteil. Standardanschluss ist ein kuratierter Entwurf mit genau einer Bestaetigungsfrage zur Formulierung; erst danach wird der Eintrag uebernommen. Bei eindeutiger Freigabe zur direkten Uebernahme im unmittelbaren Arbeitskontext kann die Rueckfrage entfallen.

---

## 7. Definition of Done — Reveal

Eine Reveal-Ableitung ist nur final, wenn:

1. Alle Blogkernpunkte sind in den Themenfolien inhaltlich abgedeckt (1:1 oder gruppiert).
2. Keine inhaltlichen Widersprueche zum Blogartikel.
3. Keine neuen unbelegten Kernbehauptungen.
4. Folien sind verdichtet und interaktionsorientiert.
5. Literaturfolie basiert auf der Blog-Literatur.
6. Pflicht-Frontmatter vollstaendig ausgefuellt (inkl. `title_reveal`, `emojis`, `veranstaltungstyp`, `veranstaltung`, `author`, `blog`, `outputs`, `reveal_hugo`, `pdf_export`, `pdf_filename`, `description`, `summary`, `tags`, `categories`); OER-Metadaten sind in Reveal-Dateien verboten. `pdf_export` steht fuer finale Reveal-Praesentationen auf `true`; `pdf_filename` steht auf Root-Ebene und nutzt standardmaessig nur den letzten technischen Ordnernamen plus `.pdf`, sofern kein bestehender manueller Override vorliegt.
7. Pro Inhaltsfolie ist eine klare Kernbotschaft erkennbar.
8. Textdichte ist foliengerecht verdichtet (Richtwert maximal 35-45 Woerter je Inhaltsfolie).
9. Je fachlichem Hauptkapitel ist mindestens eine visuelle Stuetzfolie mit kurzer Quellenzeile enthalten.
10. Fragment-Einsatz unterstuetzt einen schrittweisen Argumentationsaufbau.
11. Emoji-Einsatz folgt `project_governance/content_emoji_policy.md` und ist im sichtbaren Folien-Body erkennbar umgesetzt.
12. Sichtbare deutsche Reveal-Texte folgen der allgemeinen Typografie- und Umlautregel dieses Contracts; technische Felder und technische Zeichenketten bleiben ausgenommen.
13. `_index.md` bildet die bearbeitbare Reveal-Arbeitsdatei; im Standardmodus ist kein Snapshot erforderlich. Falls der Forschungsmodus aktiv ist, bleiben dortige Forschungsartefakte unveraenderliche Begleitdokumente und sind keine Ableitungsquelle.
14. Visuelle Darstellungen wie Bilder, Grafiken, Diagramme, Tabellen und Screenshots folgen in Reveal dem Standard gemaess `ai_agents/templates/reveal_template.md`: direkt darunter genau eine schlanke `p.bild-quelle` im Muster `Bildquelle: [Herkunft] · Lizenz: [Lizenzangabe]`; ein kurzer Kontextsatz bei Bedarf und ein `p.grafic-title` direkt darueber sind optional. Der `p.grafic-title` wird nur verwendet, wenn die Darstellung nicht bereits durch die Folienueberschrift oder den unmittelbaren Kontext eindeutig eingefuehrt ist; der Begriff bleibt immer `Bildquelle`, Lizenzlinks sind dort nicht erforderlich, gesperrte Rechte werden als `Lizenz: nicht frei verwendbar` ausgegeben. Einzige Ausnahme sind eindeutig als Ablaufplan erkennbare Tabellen innerhalb eines Abschnitts, also direkt unter einer Abschnittsueberschrift eingebettete Tabellen zur zeitlichen oder didaktischen Phasenstruktur mit organisatorischem Zweck. Nur in diesem Fall entfallen `p.grafic-title` und `p.bild-quelle`; stattdessen steht direkt ueber der Tabelle genau die knappe Zeile `**Gesamtdauer:** ca. XX Minuten ⏱️`, wobei die Minuten aus den Phasen summiert oder konsistent geschaetzt werden.

---

## 8. Transparenzpflicht und Finalausgaben

Sichtbare Zusammenfassungen folgen ausschliesslich diesem Summary-Schema:

- `Stand`
- `Ergebnis`
- `Offen`
- `Blocker`
- `Naechster Schritt`

Die Zusammenfassung bleibt ergebnisorientiert. Routinemaessige Pruefketten, Pfadlisten, Ablagehinweise und technische Nachlaufdetails gehoeren nicht in diesen Block, solange daraus kein Handlungsbedarf entsteht.

Snapshot-Vergleiche und Reflexionsimpulse gehoeren nicht zur Standardzusammenfassung.

Sichtbare Zusammenfassungen erscheinen nur bei Finalisierung, an echten Uebergaengen oder auf ausdrueckliche Nachfrage.

`/PLAN` erzeugt keine Dateien, keine Snapshots und keine Forschungsartefakte; der Befehl dient ausschliesslich dem Planungsdialog und der didaktischen Strukturierung.
`/PLAN FORSCHUNG` aktiviert denselben Planungsdialog mit optionalem Forschungs-/Rohdatenmodus und initialisiert sofort den Case-Ordner unter `exports/research/<case_id>/`.

Im Forschungsmodus bleiben Forschungsartefakte strikt vom sichtbaren Dialog und vom didaktischen Artefakt getrennt und enthalten nur schlanke, beobachtende Metadaten, soweit sie verlaesslich verfuegbar sind: Start- und Endzeit, Phasenuebergaenge, Artefaktpfade, Build-/Check-Status und nur dann Zaehldaten, wenn diese direkt ableitbar sind. Sichtbare Hinweise auf diese Protokollierung erscheinen nur bei Initialisierung, echten Uebergaengen, Finalisierung, ausdruecklicher Nachfrage oder echten Blockern.

Wenn ein Fall mit `/PLAN FORSCHUNG` beginnt, startet die Forschungsdokumentation unmittelbar mit diesem Zeitpunkt. Dabei werden `case_id`, `metadata.yaml`, `chat_log.md`, `planning_trace.md` und `decision_log.md` sofort angelegt; `chat_log.md` uebernimmt den initialen Nutzerprompt, `planning_trace.md` beginnt mit einem Aktivierungseintrag und `metadata.yaml` startet mindestens mit `case_id`, `start_time`, `completion_status: intermediate`, `agent_version`, `contract_version` und `git_commit` (`null`, wenn nicht verfuegbar). Vorgesehene Dateien sind `chat_log.md`, `planning_trace.md`, `decision_log.md`, `metadata.yaml`, `blog_working_snapshot.txt`, `reveal_snapshot.txt`, `index.md` und `_index.md`; tatsaechlich erzeugte Dateien haengen vom Fallverlauf ab. `blog_working_snapshot.txt` entsteht unmittelbar nach der ersten vom Agenten erzeugten Blog-Arbeitsfassung. Vollpruefungen der Forschungsartefakte erfolgen nicht nach jeder Kleinigkeit, sondern nur nach Initialisierung, vor Finalisierung, nach manuellen Overrides oder bei Inkonsistenzen. Ohne aktivierten Forschungsmodus duerfen spaetere Auswertungen Zeitpunkte nur rekonstruieren und muessen fehlende Marker oder Rohdaten explizit als nicht verlaesslich verfuegbar kennzeichnen.
Wurde der Agent mit `/PLAN FORSCHUNG` gestartet, finalisiert `REVEAL FINAL` zusaetzlich alle aktiven Forschungsartefakte: `reveal_snapshot.txt` wird erzeugt, Artefaktkopien werden abgelegt und `metadata.yaml` mit allen verfuegbaren Pflichtfeldern abgeschlossen; nicht direkt ableitbare Zaehldaten werden als `null` markiert. Bei `completion_status: blog_only` uebernimmt `BLOG FINAL` diese Abschlussrolle analog; ein zusaetzlicher finaler Blog-Snapshot entfaellt, `reveal_snapshot.txt` und `_index.md` entfallen dann.

Bei `BLOG FINAL` ist die sichtbare Reihenfolge:

Ein Artefakt ohne belastbare Grundlage gilt nicht als finalisierbar.

Die technischen Nachlaeufe des finalen Blogschritts laufen ohne eigene sichtbare Teilbestaetigungen; sichtbar wird nur das freigaberelevante Ergebnis.

1. DQM-Pruefbericht
2. formale Publikationsblocker
3. didaktische Freigabeblocker
4. Hinweise oder Optimierungen
5. optional Quellenuebersicht
6. Zusammenfassung

Nach erfolgreich abgeschlossenem `BLOG FINAL` folgt verpflichtend die Pruefung des optionalen Wissensbasis-Anschlusses. Standardfall ist ein kuratierter Wissensbasis-Entwurf mit genau einer knappen Bestaetigungsfrage zur Formulierung. Liegt im unmittelbaren Arbeitskontext bereits eine eindeutige Freigabe zur direkten Uebernahme vor, darf die Wissensbasis ohne weitere Rueckfrage aktualisiert werden. Der Hook gehoert nicht zur Blogerstellung selbst; der Blog bleibt final und `REVEAL GO` wird dadurch nicht blockiert.

Bei `REVEAL FINAL` ist die sichtbare Reihenfolge:

Die technischen Nachlaeufe des finalen Revealschritts laufen ohne eigene sichtbare Teilbestaetigungen; sichtbar wird nur das freigaberelevante Ergebnis.

1. Abgleich
2. bei Bedarf Materialuebersicht
3. formale Publikationsblocker
4. didaktische Freigabeblocker
5. Hinweise oder Optimierungen
6. Zusammenfassung

Der Abgleich bei `REVEAL FINAL` erscheint als echte Markdown-Tabelle mit den Spalten `Blog-Abschnitt`, `Reveal-Umsetzung (1:1|gruppiert|ausgelassen)` und `Begruendung`.
Eine sichtbare Materialuebersicht erscheint, wenn noetig, ebenfalls als echte Markdown-Tabelle mit den Spalten `Datei`, `Verwendung`, `Quelle`, `Zielpfad` und `Status`; sie wird nur gezeigt, wenn sie fuer eine reale Abstimmung mehrerer Materialien oder Zielpfade noetig ist.

---

## Systemgrenzen

Dateibasierte Operationen (z. B. Exporte, Snapshots, Protokolle)
sind nur in Umgebungen mit Dateizugriff vollstaendig umsetzbar.

In reinen Chat-Umgebungen werden diese Funktionen:
- reduziert dargestellt
- oder nur konzeptionell ausgegeben.

---

## 9. Prioritaet bei Regelkonflikten

Bei Regelkonflikten gilt folgende Prioritaet:

1. Agent Contract (Governance, Prozessphasen, Finalisierung, Konfliktregel, Sichtbarkeit, Summary-Schema)
2. `ai_agents/didaktisches_qualitaetsmodell.md` (didaktisches Referenzmodell, Profilgewichtung)
3. `ai_agents/master_agent.md` (Rolle, Ton, didaktische Entscheidungslogik und Umgang mit Unsicherheit im Rahmen dieses Contracts)
4. `prompts/plan.md` und `prompts/check.md` (Routing und Pruefung ohne eigene Normlogik)
5. `ai_agents/templates/blog_template.md` und `ai_agents/templates/reveal_template.md`

---

## 10. Governance-Hinweis

Aenderungen an Workflow, Finalisierung, Konfliktlogik, Sichtbarkeit oder Kernpunktregeln muessen in diesem Dokument im selben Aenderungszyklus mitgefuehrt werden.

---

## 11. Regression-Check-Katalog

Diese Prueffaelle sollen nach Aenderungen an Agentenlogik, Prompts oder Templates gegen Testinhalte durchlaufen werden.

Anwendung des Katalogs:

- **Selektiver RC-Durchlauf**: Nach kleinen Aenderungen an `agent_contract.md`, `master_agent.md`, Prompts oder Templates mindestens die betroffenen RCs plus RC-07.
- **Vollstaendiger RC-Durchlauf**: Vor neuem Live-Fall, vor festgeschriebenen Staenden und nach Aenderungen an Prozessphasen, Uebergaengen, Snapshot-Regeln, DoD oder Konfliktlogik.
- **RC-Trockentest**: Der RC-Trockentest ist der minimale normative Pflichttest. Er umfasst mindestens einen geschlossenen Repo-Fall im Standardmodus ueber die Pflichtschritte `/PLAN`, `BLOG GO`, `BLOG FINAL`, `REVEAL GO` -> `REVEAL FINAL`.

Der im `project_governance/development_workflow.md` beschriebene Dry Run ist die praktische Durchfuehrung dieses Tests.

Testtiefe ist proportional:

- Text- und Formulierungsaenderungen: Diff-Pruefung plus betroffene RCs.
- Workflow-, Pfad-, Snapshot- oder Renderaenderungen: betroffene RCs plus technischer Smoke-Test.
- Reveal- oder Bundle-Aenderungen: zusaetzlich Bundle-Hygiene und Reveal-Sichtpruefung.

### RC-01 Prozessphasenfolge erzwungen

- Erwartung: `P1`/`P2` vor `P3`, Blogausarbeitung vor Reveal-Ableitung, Reveal erst nach `REVEAL GO`.
- Fehlerindikator: Blog- oder Revealarbeit startet ausserhalb der Contract-Phasenlogik.

### RC-02 Blog ist leser:innenorientiert

- Erwartung: finaler Blog enthaelt publizierbaren Fliesstext statt interner Planungsstichpunkte; Planungs- und Scaffold-Sprache bleibt ausserhalb des Artefakts.
- Fehlerindikator: starke Nutzung von Planungsrastern ohne ausformulierende Erklaerung oder sichtbare Uebernahme von Meta-/Arbeitsformulierungen in den Artikelkoerper.

### RC-03 Dynamische Kernpunktzahl

- Erwartung: Kernpunktzahl wird inhaltlich begruendet und ist nicht hart auf einen Fixwert gesetzt.
- Fehlerindikator: immer gleiche Kernpunktzahl bei deutlich unterschiedlichen Themen.

### RC-04 Quellenkonsistenz Blog

- Erwartung: zentrale Aussagen sind im Text mit Quellenbezug sichtbar; Literaturteil ist vollstaendig.
- Fehlerindikator: relevante Behauptungen ohne Quellenbezug oder Quellen nur im Literaturteil.

### RC-05 Reveal-Mapping korrekt

- Erwartung: alle Blogkernpunkte sind durch Themenfolien inhaltlich abgedeckt (direkt oder gruppiert); Verdichtung und Visualisierung bleiben inhaltlich deckungsgleich zum finalen Blog.
- Fehlerindikator: nicht abgedeckte Blogkernpunkte, Rueckgriff auf Planungsnotizen statt finalem Blog oder zusaetzliche, unbelegte Kernbehauptungen.

### RC-06 Strukturdrift in Simulationen

- Erwartung: Simulationsdokumente bleiben formal konsistent (eindeutige Ueberschriften, keine Duplikate).
- Fehlerindikator: wiederholte gleichlautende Ueberschriften oder uneinheitliche Abschnittslogik.

### RC-07 Konfliktaufloesung nach Prioritaet

- Erwartung: bei widerspruechlichen Regeln wird die Prioritaet aus Abschnitt 9 eingehalten.
- Fehlerindikator: untergeordnete Datei uebersteuert den Agent Contract.

### RC-08 Transparenzpflicht erfuellt

- Erwartung: Ergebnis folgt dem Summary-Schema aus diesem Contract mit `Stand`, `Letzte Aenderung`, `Offen`, `Blocker`, `Naechster sinnvoller Befehl` und `Empfohlene Reihenfolge`.
- Fehlerindikator: Ausgabe ohne nachvollziehbare Entscheidungsbegruendung.

### RC-08a Low-noise bleibt unsichtbar

- Erwartung: sichtbare Antworten enthalten keine Prozesssaetze, Statusmeldungen, Suchkommentare, Routingkommentare oder Ankuendigungen; sichtbar sind nur Rueckfragen, Artefakte und finale Ergebnisse.
- Fehlerindikator: Formulierungen wie `Ich pruefe ...`, `Ich analysiere ...`, `Ich suche ...`, `Ich route ...`, `Ich mache jetzt ...` oder gleichwertige Prozesssaetze erscheinen im Dialog.

### RC-08b Sichtbare Steuerlogik bleibt beim Contract

- Erwartung: sichtbarer Ablauf wird nicht mit Templates, Policy-Dateien oder Beispielen begruendet oder kommentiert.
- Fehlerindikator: sichtbare Saetze wie `laut Template mache ich jetzt ...` oder `gemaess Emoji-Policy gehe ich ...` steuern den Ablauf.

### RC-09 Blog ohne Ablaufdominanz

- Erwartung: der Blogartikel erklaert Inhalte im Fliesstext.
- Fehlerindikator: der Text besteht ueberwiegend aus Ablaufpunkten.

### RC-10 Quellenregel eingehalten

- Erwartung: spezifische Quellenangaben sind belastbar und nicht erfunden.
- Fehlerindikator: erfundene Studien, DOI-Angaben oder Publikationsdetails.

### RC-11 Meta-Vollstaendigkeit Blog

- Erwartung: finaler Blog enthaelt vollstaendiges Pflicht-Frontmatter gemaess `ai_agents/templates/blog_template.md`.
- Fehlerindikator: fehlende oder leere Pflichtfelder, insbesondere im OER-/TULLU-/OERSI-Block.

### RC-12 Meta-Vollstaendigkeit Reveal

- Erwartung: finale Praesentation enthaelt vollstaendiges Pflicht-Frontmatter gemaess `ai_agents/templates/reveal_template.md` und keine OER-Metadaten.
- Fehlerindikator: fehlende oder leere Pflichtfelder oder vorhandene OER-Felder in Reveal.

### RC-13 REVEAL GO bleibt abgeleitet und nicht-final

- Erwartung: bei `REVEAL GO` wird nur `_index.md` als bearbeitbare Reveal-Arbeitsdatei aus dem finalen Blog-`index.md` erzeugt; der Lauf gilt erst nach `REVEAL FINAL` als finalisierbar.
- Fehlerindikator: Reveal wird ohne finalen Blog gestartet, bereits bei `REVEAL GO` als final behandelt oder aus einer Nicht-Blog-Quelle abgeleitet.

### RC-14 Reveal-Textdichte und Kernbotschaften

- Erwartung: jede Inhaltsfolie traegt eine klar erkennbare Kernbotschaft;
  Textdichte bleibt im foliengerechten Bereich.
- Fehlerindikator: textlastige Folien ohne klare Priorisierung der Aussage.

### RC-15 Visualisierungsquote

- Erwartung: je fachlichem Hauptkapitel ist mindestens eine visuelle Stuetzfolie vorhanden,
  inklusive kurzer Quellenzeile.
- Fehlerindikator: rein textbasierte Kapitel ohne visuelle Strukturhilfe.

### RC-16 Umlaut-Normalisierung in sichtbaren Texten

- Erwartung: sichtbare deutsche Texte enthalten korrekte Umlaute, sofern keine technische Ausnahme vorliegt.
- Fehlerindikator: systematische Ausgabe von `ae/oe/ue` in sichtbaren deutschen Texten,
  obwohl keine technische Ausnahme vorliegt.

### RC-17 BLOG GO erzeugt nur den Blog-Arbeitsstand

- Erwartung: `BLOG GO` erzeugt oder fortfuehrt `index.md` als bearbeitbare Blog-Arbeitsdatei auf Basis eines sichtbaren oder explizit benannten Planungsstands; die erste Agentenfassung ist bereits in publizierbarer Blogsprache formuliert. Im Standardmodus entstehen dabei keine Snapshots oder Forschungsartefakte; im Forschungsmodus entsteht unmittelbar nach der ersten Agentenfassung genau `blog_working_snapshot.txt`.
- Fehlerindikator: `BLOG GO` erzeugt ohne belastbare Grundlage direkt Artefakte, legt im Standardmodus Snapshots an, erzeugt im Forschungsmodus keinen fruehen Arbeitssnapshot, schreibt sichtbar in Planungs- oder Scaffold-Sprache oder greift Reveal-Logik vor.

### RC-18 Reveal-Finalisierung getrennt

- Erwartung: `REVEAL GO` startet die bearbeitbare Reveal-Arbeitsphase; `REVEAL FINAL` schliesst `_index.md` erst nach Mindestpruefungen ab. Wurde der Fall mit `/PLAN FORSCHUNG` gestartet, finalisiert `REVEAL FINAL` dabei zusaetzlich aktive Forschungsartefakte.
- Fehlerindikator: Reveal wird bereits bei `REVEAL GO` als final behandelt, ohne `REVEAL FINAL` abgeschlossen oder ein aktiver Forschungsmodus nach `REVEAL FINAL` offen gelassen.

### RC-18a First-pass-Finalisierung vollstaendig

- Erwartung: vor `BLOG FINAL` und `REVEAL FINAL` sind alle Pflichtbestandteile vollstaendig geprueft, so dass keine nachtraegliche Pflichtkorrekturschleife aus derselben Finalisierung entsteht.
- Fehlerindikator: die Finalisierung erklaert ein Artefakt als final und liefert anschliessend noch nachtraegliche Pflichtkorrekturen aus derselben Pruefrunde.

### RC-19 Anrede bleibt kontextkonsistent

- Erwartung: Im direkten Dialog mit Matthias bleibt standardmaessig das persistente Du konsistent. In Blogbeitraegen und Reveal-Praesentationen wird standardmaessig die Sie-Form verwendet; neutrale wissenschaftliche Formulierungen bleiben zulaessig.
- Fehlerindikator: der Agent verwendet im direkten Dialog ohne Anlass die Sie-Form, mischt in `index.md` oder `_index.md` ohne Grund Du- und Sie-Form oder formuliert Arbeitsauftraege an Studierende unnoetig in der Du-Form.

### RC-20 Profilsteuerung konsistent

- Erwartung: Profil A wird standardmaessig verwendet, sofern kein anderes Profil angegeben ist; nur bei klaren Kontextsignalen wird ein Profilwechsel aktiv geklaert.
- Fehlerindikator: Profilgewichtung wirkt ungesteuert, Profil A wird nicht als Default verwendet oder es wird ohne klare Kontextsignale unnoetig nach einem Profilwechsel gefragt.

### RC-21 Kontextluecken stoppen Artefaktproduktion

- Erwartung: bei fehlenden Kerninformationen oder Regelkonflikten stellt der Agent genau eine klaerende Rueckfrage und stoppt vor Artefakterstellung.
- Fehlerindikator: Blog- oder Reveal-Dateien entstehen trotz offener Kontextluecken oder Konfliktstatus.

### RC-22 Kontextregel im Zielpfad

- Erwartung: geaendert werden nur Zielartefakte und explizit freigegebene Nachbardateien.
- Fehlerindikator: zusaetzliche Uebersichtsseiten, Nachbar-Bundles oder andere Repo-Dateien werden ohne ausdruecklichen Auftrag mitgeaendert.

### RC-23 Bundle-Hygiene bleibt sauber

- Erwartung: in rendernden Content-Bundles liegen keine zusaetzlichen Markdown-Archiv- oder Forschungsdateien; nicht operative Vergleichs- oder Rohdatenstaende liegen ausschliesslich ausserhalb rendernder Bundles in `exports/`.
- Fehlerindikator: zusaetzliche `.md`-Dateien im Bundle werden mitgerendert oder koennen den Ausgabestand verfaelschen.

### RC-24 Blog-first bleibt Default

- Erwartung: Reveal wird standardmaessig erst nach finalem Blog-`index.md` erzeugt; Ausnahmen muessen explizit und begruendet geregelt sein.
- Fehlerindikator: `_index.md` wird im Standardfall vor `BLOG FINAL` erzeugt oder aus einem Nicht-Blog-Artefakt abgeleitet.

### RC-25 Robuste Reveal-Fragmentstrategie

- Erwartung: klickkritische Listen, Schrittfolgen und Overlays nutzen stabile HTML-/CSS-Fragmentmuster; bei erstem sofort sichtbaren Listenpunkt wird keine fragile Kommentar-Syntax allein verwendet.
- Fehlerindikator: Fragmentlogik bricht oder haengt allein an Kommentar-Syntax, obwohl robuste HTML-Fragmente erforderlich waeren.

### RC-26 Proportionale Testtiefe

- Erwartung: Testaufwand entspricht dem Risiko der Aenderung; Mini-Textaenderungen loesen keinen Volltest aus, struktur- oder renderrelevante Aenderungen dagegen schon.
- Fehlerindikator: Volltests auf triviale Aenderungen oder fehlende Smoke-Tests nach Pfad-, Snapshot-, Bundle-, CSS- oder Renderaenderungen.

### RC-27 Wissensbasis-Anschluss deterministisch

- Erwartung: Nach erfolgreichem `BLOG FINAL` wird standardmaessig ein kuratierter Wissensbasis-Entwurf vorgeschlagen und genau eine Bestaetigungsfrage zur Formulierung gestellt; die Datei wird erst nach Freigabe oder gezielter Korrektur aktualisiert. Bei eindeutiger Freigabe zur direkten Uebernahme im unmittelbaren Arbeitskontext darf die Rueckfrage entfallen. `REVEAL GO` allein triggert keine Wissensbasis-Aktualisierung.
- Fehlerindikator: Nach `BLOG FINAL` fehlt der Wissensbasis-Entwurf trotz regulaerem Anschlussfall; die Formulierung wird ohne Review oder ohne klare direkte Freigabe still uebernommen; trotz bestaetigtem Entwurf wird `blog_wissensbasis.md` nicht aktualisiert; oder `REVEAL GO` behandelt die Wissensbasis wieder wie ein automatisches Pflicht-Gate.

### RC-28 Forschungsmodus-Schemata und Fallarchivierung korrekt

- Erwartung: Im aktiven Forschungsmodus werden `planning_trace.md`, `decision_log.md` und `metadata.yaml` gemaess den in Abschnitt 2 definierten Minimal-Schemata befuellt. Nach der ersten vom Agenten erzeugten Blog-Arbeitsfassung wird `blog_working_snapshot.txt` erzeugt; nach `BLOG FINAL` wird `index.md` in den Case-Ordner kopiert; nach `REVEAL FINAL` analog `reveal_snapshot.txt` und `_index.md`. Nicht ableitbare Felder werden als `null` markiert, nicht geschaetzt. `metadata.yaml` wird beim Fallabschluss vollstaendig finalisiert; `generated_artifacts` listet alle tatsaechlich erzeugten Artefaktpfade. Sonderfaelle (`blog_only`, `aborted`, `intermediate`) werden schemakonsistent und lagerichtig abgebildet.
- Fehlerindikator: Fehlende Pflichtfelder in `metadata.yaml`; geschaetzte statt als `null` markierte Zaehldaten; fehlender oder falscher `completion_status`; `blog_working_snapshot.txt` fehlt trotz agentenseitig erzeugter Blog-Arbeitsfassung; `reveal_snapshot.txt` fehlt trotz abgeschlossenem Reveal-Fall; Artefaktkopien fehlen oder wurden bearbeitet; `reveal_snapshot.txt` oder `_index.md` bei `blog_only` vorhanden; Forschungsartefakte enthalten interpretative Bewertungen.

### RC-29 Light Operations bleiben proportional

- Erwartung: Klar begrenzte Kleinoperationen an bestehenden Artefakten werden als Light Operations behandelt, nur lokal oder fokussiert geprueft und sichtbar ergebnisorientiert bestaetigt. Weder eine Vollpruefung noch eine sichtbare FINAL- oder Gruencheck-Rhetorik werden dadurch automatisch ausgeloest.
- Fehlerindikator: Linkkorrektur, Bildtausch, Absatzkorrektur oder vergleichbarer Mikrofix loest ohne strukturellen Anlass eine Vollpruefung, Finalisierungssprache oder sichtbare Pruefkette aus.

### RC-30 `/PLAN FORSCHUNG` bleibt robuster Vorrangstrigger

- Erwartung: Das explizite Signal `/PLAN FORSCHUNG` aktiviert den Forschungsmodus sofort auch dann, wenn derselbe Nutzersatz bereits Thema, Zielgruppe, Material oder weitere Planungsangaben enthaelt. Sichtbar bleibt der erste Antwortzug trotzdem kompakt und ohne technische Aktivierungsrhetorik.
- Fehlerindikator: Ein gemischter `/PLAN FORSCHUNG`-Prompt wird wie ein gewoehnliches `/PLAN` behandelt, die Aktivierung auf spaeter verschoben oder sichtbar mit technischer Prozesssprache ueberfrachtet.

### RC-31 Temporaere Analyseartefakte bleiben getrennt

- Erwartung: Nur zur Analyse genutzte PDFs, Downloads, Extrakte oder Arbeitskopien bleiben temporaer oder in klar getrennter Arbeitsablage und werden nicht ohne Projektfunktion in produktive Content-Pfade oder die Repo-Wurzel uebernommen.
- Fehlerindikator: Reine Analyseartefakte werden ohne ausdruecklichen Bedarf, Publikationsfunktion oder Quellenrolle in produktive Bundle-Strukturen eingemischt.