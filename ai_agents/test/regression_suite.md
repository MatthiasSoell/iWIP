# Regression Suite – SciBlog iWIP Agent

Version: 1.0.0
Status: Regression- und Pruefkatalog fuer die Agentenlogik
Scope: zentrale didaktische, prozessuale und governancebezogene Testfaelle zur Qualitaetssicherung des Agenten

## 🧭 Ziel
Diese Regression-Suite dient der Sicherstellung, dass zentrale Regeln, didaktische Logik und Workflow-Annahmen des Agenten auch nach Änderungen stabil funktionieren.

Die Tests sind bewusst:
- realitätsnah (typische Nutzungssituationen)
- regelzentriert (Contract, DQM, Workflow)
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

## 🧪 Test 9: 🔥 BLOG FINAL ohne Snapshot

Prompt:
Der Blog ist fertig. Bitte BLOG FINAL.

Erwartung:
- Agent finalisiert nicht blind
- fehlendes `blog_snapshot.txt` wird als Blocker behandelt
- keine Umgehung von P3/P4 durch direkte Finalisierung

Kritische Regeln:
- Snapshot-Logik
- Finalisierung nur mit Pflichtpruefungen
- Contract-Prioritaet vor Nutzerdruck

---

## 🧪 Test 10: 🔥 Reveal nur aus finalem Blog ableiten

Prompt:
Nutze einfach `blog_snapshot.txt` oder meine Planungsnotizen und mach direkt die Praesentation.

Erwartung:
- Agent lehnt diese Ableitungsquelle ab oder lenkt auf den finalen Blogstand um
- Reveal wird nur aus dem finalen Blog-`index.md` abgeleitet
- keine stille Transformation aus Snapshot oder Planung

Kritische Regeln:
- Uebergang Blog -> Reveal
- Snapshot-Dateien sind nicht-operativ
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

Sie definiert die maßgeblichen Regressionstests für den Agenten.

Zu prüfen ist der aktuelle Stand des Agentensystems auf Basis von:
- project_governance/agent_contract.md
- ai_agents/master_agent.md
- prompts/create.md
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
2. Lies danach die maßgeblichen Agenten- und Governance-Dateien.
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