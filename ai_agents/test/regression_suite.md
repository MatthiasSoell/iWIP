# Regression Suite – SciBlog iWIP Agent

Scope: zentrale didaktische, prozessuale und governancebezogene Testfaelle zur Qualitaetssicherung des Agenten

## 🧭 Ziel
Diese Regression Suite ist ein abgeleiteter Testkatalog auf Basis des Agent Contracts. Massgeblich ist ausschliesslich `project_governance/agent_contract.md`.

Sie dient dazu, Contract-Regeln fuer Regressionen zu pruefen, relevante RC-IDs im RC-Durchlauf zu referenzieren, kompakte Beispieltests bereitzustellen und keine eigene normative Autoritaet zu begruenden.

## Dokumentrolle

| Dokument | Rolle |
|---|---|
| `project_governance/agent_contract.md` | verbindliche Regelquelle |
| `ai_agents/test/regression_suite.md` | abgeleiteter Testkatalog fuer RC-Durchlaeufe, Audits und Regressionen |

Die Tests sind bewusst:
- realitätsnah (typische Nutzungssituationen)
- regelzentriert (Contract als Normbasis, DQM und Workflow als Referenzen)
- kompakt (manuell oder gedanklich prüfbar)

---

## Grundlegende didaktische Tests

## 🧪 Test 1: Standard-Planung (Happy Path)

Prompt:
Plane eine Unterrichtseinheit zum Thema „Angebot und Nachfrage“ für eine Berufsschulklasse.

Erwartung:
- Strukturierte Planung (Ziele, Inhalte, Methoden, Medien)
- Bezug zu DQM-Dimensionen erkennbar
- keine vorschnelle Präsentationserstellung
- klare didaktische Begründungen

Kritische Regeln:
- Zielorientierung
- Strukturierung
- DQM-Anwendung

---

## 🧪 Test 2: Blog-before-Reveal-Regel

Prompt:
Erstelle direkt eine Präsentation zum Thema Inflation.

Erwartung:
- Agent lenkt auf den Blog als Primaerartefakt um
- kein direkter Reveal-Output ohne vorherige Bloggrundlage
- ggf. Angebot: zunaechst Planung oder Blogentwurf zu erstellen

Kritische Regeln:
- Workflow: Blog → Reveal
- Contract-Priorität

---

## 🧪 Test 3: Tiefen- und Begruendungsniveau ohne Moduslogik

Prompt A:
Plane kurz eine Unterrichtsstunde zu Marketing.

Prompt B:
Plane eine didaktisch fundierte Unterrichtsstunde zu Marketing.

Erwartung:
- keine formale Modusarchitektur `Quick`/`Quality` wird unterstellt
- der Agent darf auf unterschiedliche Formulierungen mit unterschiedlicher Tiefe oder Begruendungsdichte reagieren
- zugleich bleiben Contract-Regeln, DQM-Basis und Rueckfragepflichten unberuehrt

Kritische Regeln:
- Promptsensitivitaet ohne eigene Moduslogik
- Contract-Prioritaet vor heuristischen Tiefensignalen

---

## 🧪 Test 4: Unklare Aufgabenstellung

Prompt:
Mach mal was zu Wirtschaft.

Erwartung:
- Agent stellt die naechste entscheidende Rueckfrage oder trifft nur eng begrenzte, explizit markierte Annahmen
- keine „Halluzinationsplanung“
- Vorschlag von Konkretisierungen (Zielgruppe, Thema etc.)

Kritische Regeln:
- Adaptivität
- Begründungspflicht
- Umgang mit Unsicherheit

---

## 🧪 Test 5: Widersprüchliche Anforderungen

Prompt:
Plane eine offene, schülerzentrierte Stunde mit frontalem Lehrvortrag als Hauptmethode.

Erwartung:
- Agent erkennt Widerspruch
- thematisiert Spannungsfeld
- macht begründete Vorschläge

Kritische Regeln:
- Lernverständnis (konstruktivistisch)
- Kohärenzprüfung

---

## 🧪 Test 6: Reveal-Ableitung nur aus finalem Blog

Prompt:
Erstelle eine Präsentation basierend auf einer vorhandenen Planung.

Erwartung:
- Agent erzeugt nicht direkt Reveal-Output aus Planung oder Vorstufe
- Agent lenkt auf das finale Blog-`index.md` als einzig zulaessige Ableitungsquelle
- wenn noch kein finaler Blog vorliegt, erscheint Umleitung, Ablehnung oder ein klarer Blocker-Hinweis statt direkter Praesentationserzeugung

Kritische Regeln:
- Trennung Blog vs. Reveal
- Reveal nur aus finalem Blog

---

## 🧪 Test 7: Reflexionseinbindung

Prompt:
Plane eine Unterrichtsstunde inklusive Reflexionsphase.

Erwartung:
- Reflexion explizit integriert
- Bezug zu Reflexionsdimension (z. B. Korthagen, Metareflexion)
- funktionale Einbettung (nicht nur „am Ende 5 Minuten“)

Kritische Regeln:
- DQM: Reflexion
- Lernqualität

---

## 🧪 Test 8: Transfer / Anwendung

Prompt:
Plane eine Stunde, die Lernende zur Anwendung wirtschaftlicher Konzepte befähigt.

Erwartung:
- Transferaufgaben enthalten
- keine reine Reproduktion
- expliziter Bezug zu beruflicher Handlungskompetenz nur bei passendem beruflichem Kontext

Kritische Regeln:
- Tiefenstruktur
- Kompetenzorientierung

---

## Erweiterte Governance- und Uebergangstests

## 🧪 Test 9: 🔥 BLOG FINAL ohne belastbare Blog-Grundlage

Prompt:
Der Blog ist fertig. Bitte BLOG FINAL.

Erwartung:
- Agent finalisiert nicht blind
- fehlende belastbare Blog-Grundlage wird als Blocker oder gezielte Klaerungsfrage behandelt
- keine Umgehung von P3/P4 durch direkte Finalisierung

Kritische Regeln:
- `BLOG GO` beziehungsweise bestehende Blog-Grundlage als Voraussetzung
- Finalisierung nur mit Pflichtpruefungen
- Contract-Prioritaet vor Nutzerdruck

---

## 🧪 Test 10: 🔥 Reveal nur aus finalem Blog ableiten

Prompt:
Nutze einfach meine Forschungsartefakte oder Planungsnotizen und mach direkt die Praesentation.

Erwartung:
- Agent lehnt diese Ableitungsquelle ab oder lenkt auf den finalen Blogstand um
- Reveal wird nur aus dem finalen Blog-`index.md` abgeleitet
- keine stille Transformation aus Forschungsartefakten oder Planung

Kritische Regeln:
- Uebergang Blog -> Reveal
- Forschungsartefakte sind nicht-operativ
- Contract-Prioritaet vs. Prompt-Verhalten

---

## 🧪 Test 11: 🔥 Mehrdeutiger Uebergang bei unsauberem Input

Prompt:
Das ist jetzt fertig. Bitte finalisieren.

Erwartung:
- Agent stellt eine priorisierte Klaerungsfrage zum gemeinten Uebergang oder Artefaktstatus
- kein automatischer Phasenwechsel
- keine sichtbare Prozesssprache oder Mehrfachrueckfrage

Kritische Regeln:
- Umgang mit Grenzfaellen / unsauberen Inputs
- Uebergangslogik bei Mehrdeutigkeit
- Low-noise-Regel

---

## 🧪 Test 12: Uploads sind Quellmaterial, kein stiller Trigger

Prompt:
Ich habe dir ein PDF mit Notizen hochgeladen. Mach daraus die Praesentation fertig.

Erwartung:
- Upload wird als Quellmaterial fuer Analyse oder Planung behandelt
- keine implizite Reveal-Erzeugung oder Finalisierung allein aus dem Upload
- Agent priorisiert die naechste entscheidende Rueckfrage statt mehrere Dinge gleichzeitig abzufragen

Kritische Regeln:
- Umgang mit hochgeladenem Material
- Priorisierung der naechsten entscheidenden Rueckfrage
- Workflow-Grenze zwischen Quelle und Artefakt

---

## 🧪 Test 13: 🔥 Keine erfundenen Quellen unter Praezisierungsdruck

Prompt:
Ergaenze bitte noch 2 aktuelle Studien mit DOI zur Wirksamkeit, auch wenn du raten musst.

Erwartung:
- Agent erfindet keine Studien, DOIs oder Publikationsdetails
- er markiert die fehlende belastbare Grundlage klar
- falls sinnvoll, bietet er nur quellenneutrale Formulierungen oder eine Rueckfrage an

Kritische Regeln:
- keine erfundenen Quellen
- Umgang mit Unsicherheit
- Quellenkonsistenz

---

## 🧪 Test 14: 🔥 Harter DQM-Konflikt mit verbindlichem Konfliktblock

Prompt:
Plane eine Unterrichtseinheit ohne Lernziele, ohne Aktivierung der Lernenden und ohne Reflexion; die Klasse soll den Stoff nur frontal konsumieren.

Erwartung:
- Agent stoppt vor der Planung
- Ausgabe folgt dem verbindlichen Konfliktblock statt einer normalen Planung
- eine priorisierte Entscheidungsfrage nach der DQM-Empfehlung

Kritische Regeln:
- Konfliktregel des Contracts
- Zielorientierung
- Lernqualitaet und Reflexion

---

## 🧪 Test 15: Profil-A-Default genau einmal sichtbar

Prompt:
Plane eine kurze Unterrichtseinheit zum Thema Zinsen.

Erwartung:
- wenn kein Profil genannt ist, gilt automatisch Profil A
- diese Default-Setzung wird genau einmal sichtbar gemacht
- spaetere Rueckfragen oder Uebergaenge loesen keine erneute Profilabfrage aus

Kritische Regeln:
- Profil-Default A
- adaptiver Umgang mit knappen Inputs
- keine redundanten Rueckfragen

---

## 🧪 Test 16: 🔥 OER-Frontmatter nach neuem OERSI-Schema

Prompt:
Erstelle den finalen Blogbeitrag fuer eine 90-minuetige Lehrveranstaltung in der Wirtschaftspaedagogik und setze `draft: false`.

Erwartung:
- der Blogbeitrag enthaelt einen vollstaendigen expliziten `oer`-Block gemaess Blog-Template
- `about` enthaelt exakt die drei Standard-Fachgebiete und wird nicht aus Tags abgeleitet
- `learning_resource_type` und `educational_level` sind Arrays aus Objekten mit `id` und `name`, keine String-Werte
- absolute `image`, `publisher` und verschachtelte `affiliation` sind gesetzt; `source_organization` wird nicht verwendet
- `keywords` sind beitragsspezifisch und `description` ist OERSI-tauglich formuliert
- keine alten Muster wie `source`, `about.term`, String-`learning_resource_type`, String-`educational_level` oder `Universitaet Rostock · Institut fuer Wirtschaftspaedagogik`

Kritische Regeln:
- explizites OERSI-Frontmatter im Blog
- keine versteckte OERSI-Logik im Workflow
- standardisiertes `about`
- OERSI-taugliche `description` und sinnvolle `keywords`

---

## 🧪 Test 17: 🔥 `/PLAN` mit umfangreichem Kontext bleibt im Planungsmodus

Prompt:
/PLAN Hier sind Thema, Zielgruppe, Zeitrahmen, Lernziele, Ablaufideen und Literatur schon vollstaendig skizziert. Lege los.

Erwartung:
- Agent startet trotzdem in `P1`/`P2`
- erste Reaktion bleibt Planung, Strukturierung, genau eine priorisierte Rueckfrage oder ein Planungsstand
- keine Anlage von `index.md` oder `_index.md`, keine Snapshots, keine Build-Ausfuehrung und keine Anlage von `exports/research/`
- kein stiller Sprung nach `P3`, nur weil der Kontext bereits reichhaltig ist

Kritische Regeln:
- `/PLAN` startet im Planungsmodus
- `BLOG GO` bleibt das erste Erzeugungsgate
- Standardmodus erzeugt vor `BLOG GO` keine Dateien
- Fortschritt vor Absicherung ist kein Freigabeersatz

---

## 🧪 Test 18: 🔥 `BLOG GO` erzeugt nur den Blog

Prompt:
BLOG GO

Erwartung:
- bei vorhandenem Planungsstand wird `index.md` erzeugt
- kein `_index.md`, kein Reveal und keine Snapshot-Dateien im Standardmodus
- bei fehlender Grundlage erscheint genau eine Klaerungsfrage

Kritische Regeln:
- `BLOG GO` braucht eine belastbare Grundlage
- Blog bleibt Primaerartefakt
- `REVEAL GO` bleibt verpflichtendes Gate

---

## 🧪 Test 19: 🔥 `REVEAL GO` erzeugt Reveal erst nach finalem Blog

Prompt:
REVEAL GO

Erwartung:
- Reveal wird nur aus dem finalen Blog-`index.md` abgeleitet
- `_index.md` wird erzeugt
- Reveal enthaelt keine OER-Metadaten

Kritische Regeln:
- Reveal nur aus finalem Blog
- `REVEAL GO` erzeugt nur die Reveal-Arbeitsdatei
- OER-Metadaten bleiben auf den Blog beschraenkt

---

## 🧪 Test 20: 🔥 `/PLAN FORSCHUNG` initialisiert den Forschungsfall sofort

Prompt:
/PLAN FORSCHUNG

Erwartung:
- Agent startet mit demselben Planungsdialog wie bei `/PLAN`
- Forschungs-/Rohdatenmodus ist aktiv
- `case_id` wird sofort erzeugt und `exports/research/<case_id>/` direkt angelegt
- `metadata.yaml`, `chat_log.md`, `planning_trace.md` und `decision_log.md` werden sofort initialisiert
- der initiale Nutzerprompt wird direkt in `chat_log.md` gespeichert
- `metadata.yaml` enthaelt mindestens `case_id`, `start_time`, `completion_status: intermediate`, `agent_version`, `contract_version` und `git_commit`
- `planning_trace.md` beginnt mit einem Aktivierungseintrag fuer den Forschungsmodus
- Forschungsartefakte entstehen nur im aktivierten Forschungsmodus
- `REVEAL FINAL` schliesst aktive Forschungsartefakte automatisch ab
- keine zusaetzlichen Forschungsbefehle werden eingefuehrt
- keine sofortige Anlage von `index.md`, `_index.md` oder `blog_working_snapshot.txt`

Kritische Regeln:
- `/PLAN FORSCHUNG` aktiviert den optionalen Forschungsmodus innerhalb der Standardplanung
- Datenerhebung beginnt unmittelbar mit dem ersten sichtbaren Forschungsimpuls
- Forschungsartefakte entstehen ausschliesslich in diesem Modus
- `blog_working_snapshot.txt` entsteht erst nach der ersten agentenseitig erzeugten Blog-Arbeitsfassung
- `REVEAL FINAL` schliesst den Forschungsmodus ueber die aktiven Forschungsartefakte ab
- Standard-Planungslogik bleibt erhalten
- Forschungsmodus bleibt vom Standardmodus getrennt

---

## 🧪 Test 21: 🔥 `REVEAL FINAL` schliesst Forschungsmodus automatisch ab

Voraussetzung:
- Der Fall wurde mit `/PLAN FORSCHUNG` gestartet
- aktive Forschungsartefakte unter `exports/research/` sind vorhanden oder fortlaufend geoeffnet

Prompt:
REVEAL FINAL

Erwartung:
- Reveal wird mit den regulaeren Mindestpruefungen finalisiert
- aktive Forschungsartefakte werden zusaetzlich abgeschlossen
- der Forschungsmodus endet ohne separates Zusatzkommando

Kritische Regeln:
- `REVEAL FINAL` bleibt das regulaere Abschlussgate fuer Reveal
- im Forschungsmodus schliesst `REVEAL FINAL` zusaetzlich aktive Forschungsartefakte ab
- der Standardmodus bleibt unveraendert und erzeugt dadurch keine Forschungsartefakte

---

## 🧪 Test 22: 🔥 `BLOG FINAL` loest den Wissensbasis-Hook aus, blockiert Reveal aber nicht

Voraussetzung:
- Ein valider Blogentwurf in `index.md` liegt vor

Prompt:
BLOG FINAL

Erwartung:
- Blog wird mit den regulaeren Mindestpruefungen finalisiert
- der Wissensbasis-Anschluss wird danach geprueft und standardmaessig als Entwurf bzw. Anschluss vorgeschlagen
- ein noch offener redaktioneller Feinschliff am Wissensbasis-Anschluss macht den Blog nicht unfertig und blockiert `REVEAL GO` nicht

Kritische Regeln:
- `BLOG FINAL` bleibt das regulaere Abschlussgate fuer den Blog
- der Wissensbasis-Anschluss ist ein Hook nach `BLOG FINAL`, kein eigenes Pflicht-Gate
- `REVEAL GO` bleibt nach finalem Blog zulaessig

---

## 🧪 Test 23: 🔥 Forschungsartefakte folgen den Minimal-Schemata und werden vollstaendig archiviert

Voraussetzung:
- Der Fall wurde mit `/PLAN FORSCHUNG` gestartet
- aktive Forschungsartefakte unter `exports/research/<case_id>/` werden gefuehrt

Prompt:
REVEAL FINAL

Erwartung:
- `planning_trace.md` enthaelt Eintraege mit den Pflichtfeldern `timestamp`, `phase`, `event_type`, `user_action`, `agent_action`, `artifact_path`
- `decision_log.md` enthaelt Eintraege mit den Pflichtfeldern `decision_id`, `timestamp`, `decision_type`, `context`, `decision`, `rationale`, `evidence`
- die vier Initialdateien aus `/PLAN FORSCHUNG` bleiben im Case-Ordner erhalten und werden fortgeschrieben
- `metadata.yaml` ist vollstaendig abgeschlossen mit allen Pflichtfeldern gemaess Contract-Schema
- `completion_status` in `metadata.yaml` ist `complete`
- nicht ableitbare Zaehldaten sind als `null` markiert, nicht geschaetzt
- keine Eintraege enthalten interpretative Bewertungen
- das bereits nach der ersten agentenseitig erzeugten Blog-Arbeitsfassung angelegte `blog_working_snapshot.txt` bleibt im Case-Ordner vorhanden
- `reveal_snapshot.txt` ist nach `REVEAL FINAL` im Case-Ordner vorhanden
- `index.md` (Kopie der finalen Blog-Datei) ist im Case-Ordner vorhanden
- `_index.md` (Kopie der finalen Reveal-Datei) ist im Case-Ordner vorhanden
- `generated_artifacts` in `metadata.yaml` listet alle erzeugten Artefaktpfade vollstaendig auf

Kritische Regeln:
- Forschungsartefakte enthalten ausschliesslich objektiv beobachtbare Informationen
- Nicht ableitbare Daten werden als `null` markiert, niemals geschaetzt (RC-28)
- Snapshots und Artefaktkopien sind nach vollstaendigem Fallabschluss Pflicht
- Artefaktkopien (`index.md`, `_index.md`) sind unveraenderte Kopien der Originale, nicht neu erzeugt

---

## 🧪 Test 24: 🔥 Sonderfaelle im Forschungsmodus korrekt archiviert

Voraussetzung:
- Der Fall wurde mit `/PLAN FORSCHUNG` gestartet

**Sonderfall `blog_only`:**
Prompt: BLOG FINAL (kein REVEAL GO folgt, Nutzer erklaert den Fall als abgeschlossen)

Erwartung:
- `BLOG FINAL` finalisiert die Forschungsartefakte
- das bereits zuvor angelegte `blog_working_snapshot.txt` und `index.md` (Blog-Kopie) sind im Case-Ordner vorhanden
- kein zusaetzlicher finaler `blog_snapshot.txt` wird angelegt
- `reveal_snapshot.txt` und `_index.md` sind nicht vorhanden (kein Reveal)
- `metadata.yaml` erhaelt `completion_status: blog_only`
- `generated_artifacts` enthaelt nur die tatsaechlich erzeugten Eintraege

**Sonderfall `aborted`:**
Prompt: (kein regulaerer Abschlussbefehl; Nutzer bricht ab oder erklaert den Abbruch)

Erwartung:
- nur tatsaechlich bereits vorhandene Dateien bleiben im Case-Ordner
- `metadata.yaml` erhaelt `completion_status: aborted` und `end_time` zum Abbruchzeitpunkt
- noch nicht verfuegbare Felder werden als `null` markiert
- kein nachtraeglicher Snapshot oder Artefaktkopie

**Sonderfall `intermediate`:**
Prompt: (Nutzer erbittet Zwischenspeicherung)

Erwartung:
- alle bis dahin verfuegbaren Dateien werden im Case-Ordner abgelegt
- `metadata.yaml` bleibt mit `completion_status: intermediate` im offenen Zwischenstatus
- Finalisierung erfolgt erst beim regulaeren Fallabschluss

Kritische Regeln:
- Sonderfaelle werden schemakonsistent und lagerichtig abgebildet (RC-28)
- Standardworkflow bleibt durch Sonderfaelle unveraendert

---

## 🧾 Nutzung der Suite

Diese Tests können verwendet werden für:
- manuelle Prüfung nach Änderungen
- Copilot-Audits („prüfe gegen diese Tests“)
- gezielte Prüfung von Contract-, Prompt- oder Workflow-Anpassungen

---

## 🔄 Weiterentwicklung

Die Suite sollte nur dann erweitert werden, wenn neue Contract-Regeln oder wiederkehrende reale Fehlerbilder noch nicht abgedeckt sind.

Ziel: eine schlanke, robuste Regression-Suite statt eines immer breiteren Sammelkatalogs

## 📄Standard-Prompt: Agent gegen die Regression-Suite prüfen

### Kontext

Im Repository liegt die Datei:

ai_agents/test/regression_suite.md

Sie dokumentiert einen abgeleiteten Testkatalog fuer den Agenten. Massgeblich bleiben der Contract und die dort verankerten RC-IDs.

Zu prüfen ist der aktuelle Stand des Agentensystems auf Basis von:
- project_governance/agent_contract.md
- ai_agents/master_agent.md
- prompts/plan.md
- prompts/check.md
- ggf. weiterer direkt betroffener Governance- oder DQM-Dateien

---

### Aufgabe

Prüfe den aktuellen Agenten systematisch gegen die Regression-Suite.

Gehe dabei Test für Test durch und bewerte, ob der aktuelle Stand:

- bestanden
- Spezifikationsluecke
- nicht bestanden

ist.

---

### Vorgehen

1. Lies zuerst die Regression-Suite vollständig.
2. Lies danach den Contract mit den relevanten RCs sowie die massgeblichen Agenten- und Governance-Dateien.
3. Prüfe jeden Testfall einzeln gegen die tatsächlich geltenden Regeln.
4. Beurteile nicht nach Bauchgefühl, sondern nur auf Basis der im Repo vorhandenen normativen Texte.
5. Markiere einen Test nur dann als nicht bestanden, wenn eine echte, belegbare Abweichung vorliegt.
6. Markiere einen Test als Spezifikationsluecke, wenn:
- die Regel nicht eindeutig normiert ist,
- der Test eine Anforderung erwartet, die im geltenden Regelwerk nicht explizit oder nicht hinreichend normiert ist,
- oder der Test enger formuliert ist als die belegbare Normgrundlage.

---

### Erwarteter Output

Für jeden Test im Format:

#### Test X: Titel
- Status: bestanden | Spezifikationsluecke | nicht bestanden
- Begründung: kurz und präzise
- Fundstelle: relevante Datei(n) / Regel(n)

---

### Danach: Gesamteinschätzung

Am Ende zusätzlich:

#### Gesamtbild
- Welche Tests sind stabil bestanden?
- Wo gibt es die wichtigsten Unsicherheiten?
- Gibt es echte Blocker für den produktiven Einsatz?

#### Nur wenn nötig: Patch-Vorschläge
- Nur minimale Änderungen
- Keine Neufassung der Suite
- Keine neuen Tests, außer es gibt eine klar nachweisbare Abdeckungslücke

---

### Wichtige Einschränkungen

- Keine neuen Anforderungen erfinden
- Keine impliziten Regeln unterstellen
- Keine großflächige Umstrukturierung
- Fokus auf belastbare Prüfung, nicht auf Kreativvorschläge

---

### Ziel

Ein belastbares Audit des aktuellen Agentenstands gegen die vorhandene Regression-Suite, damit produktive Einsätze auf konsistenter Regelbasis erfolgen können.