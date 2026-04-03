# Agent Contract — Didaktische Planung und Publikation

Version: 1.2.0
Status: verbindliche Verhaltensspezifikation
Scope: Planungsmodus, Blogmodus, Reveal-Transformationsmodus

---

## 1. Zielbild

Der Agent erzeugt aus einer didaktischen Planung zwei konsistente Artefakte:

1. Blogartikel (Primärartefakt)
2. Reveal-Präsentation (abgeleitetes Artefakt)

Die Präsentation wird ausschließlich aus dem finalen Blogartikel abgeleitet.
OER-Metadaten werden im Blogartikel geführt; Reveal bleibt OER-metadatenfrei.

---

## 2. Moduslogik

### Planungsmodus

- Kontext klären
- didaktische Struktur entwickeln
- Lernziele, Aktivitäten, Methoden, Medien, Zeitrahmen abstimmen

### Blogmodus

- Planung in leser:innenorientierten Fließtext transformieren
- inhaltliche Kernpunkte argumentativ ausarbeiten
- Quellen im Text sichtbar integrieren

### Reveal-Transformationsmodus

- Blogstruktur in Folienlogik verdichten
- Blogkernpunkte in Themenfolien überführen (1:1 oder gruppiert)
- keine neuen inhaltlichen Behauptungen hinzufügen

---

## 3. Verbindliche Regeln

1. Kein Überspringen der Modusreihenfolge.
2. Kein finales Blogartefakt in planungsnaher Sprache.
3. Dynamische Kernpunktzahl je Thema, nicht fixe Anzahl.
4. Reveal muss alle Blogkernpunkte inhaltlich abdecken (direkt oder gruppiert).
5. Quellenkonsistenz zwischen Blogtext und Literaturteil.
6. Keine erfundenen spezifischen Quellenangaben (Studien, DOI, Publikationsdetails).
7. Bei fehlenden Kerninformationen oder Regelkonflikten: eine klärende Rückfrage, dann Stopp vor Artefakterstellung.
8. Blog-Frontmatter vollständig gemäß ai_agents/templates/blog_template.md, inklusive vollständigem OER-/TULLU-/OERSI-Metadatenblock.
9. Reveal-Frontmatter vollständig gemäß ai_agents/templates/reveal_template.md; Reveal enthält keine OER-Metadaten.
10. Bei `REVEAL GO` wird im Reveal-Zielordner zusätzlich `reveal_snapshot.md` als nicht-rendernde Momentaufnahme erzeugt. Der Snapshot enthaelt denselben inhaltlichen Stand wie die zum Zeitpunkt von `REVEAL GO` erzeugte Reveal-Datei und ergaenzt ausschliesslich den Frontmatter-Block `_build: { render: false, list: false }`.
11. Snapshot-Dateien im Reveal-Kontext sind nicht-operativ: keine automatische Bearbeitung und keine Ableitung aus Snapshot-Dateien; Reveal wird stets aus dem finalen Blog-`index.md` abgeleitet.

---

## 4. Definition of Done — Blog

Ein Blogartikel ist nur final, wenn:

1. Leser:innenperspektive klar erkennbar.
2. Ablauf unterstützend, nicht dominierend.
3. Kernpunkte als Fließtextabschnitte ausgearbeitet.
4. Kernpunkte mit Quellenbezug im Text.
5. Literaturverzeichnis vollständig vorhanden.
6. Pflicht-Frontmatter vollständig ausgefüllt (inkl. `oer.creators`, `publisher`, `license`, `source`, `version`, `status`, `in_language`, `learning_resource_type`, `educational_level`, `audience`, `time_required`, `about`).
7. Die bearbeitete `.index.md` bleibt als nicht-rendernder Arbeitsstand erhalten und enthält `_build.render: false` sowie `_build.list: false`; der finale Blogartikel (`index.md`) wurde konsistent daraus abgeleitet.

---

## 5. Definition of Done — Reveal

Eine Reveal-Ableitung ist nur final, wenn:

1. Alle Blogkernpunkte sind in den Themenfolien inhaltlich abgedeckt (1:1 oder gruppiert).
2. Keine inhaltlichen Widersprüche zum Blogartikel.
3. Keine neuen unbelegten Kernbehauptungen.
4. Folien sind verdichtet und interaktionsorientiert.
5. Literaturfolie basiert auf der Blog-Literatur.
6. Pflicht-Frontmatter vollständig ausgefüllt (inkl. `title_reveal`, `emojis`, `veranstaltungstyp`, `veranstaltung`, `author`, `blog`, `outputs`, `reveal_hugo`, `description`, `summary`, `tags`, `categories`); OER-Metadaten sind in Reveal-Dateien verboten.
7. Pro Inhaltsfolie ist eine klare Kernbotschaft erkennbar.
8. Textdichte ist foliengerecht verdichtet (Richtwert maximal 35-45 Wörter je Inhaltsfolie).
9. Je fachlichem Hauptkapitel ist mindestens eine visuelle Stützfolie mit kurzer Quellenzeile enthalten.
10. Fragment-Einsatz unterstützt einen schrittweisen Argumentationsaufbau.
11. Emoji-Einsatz ist semantisch konsistent zur Emoji-Policy des Projekts.
12. Sichtbare deutsche Folientexte enthalten korrekte Umlaute;
   Normalisierung `ae/oe/ue -> ä/ö/ü` gilt verpflichtend außerhalb technischer Felder
   (URLs, Pfade, Dateinamen, Slugs, Alias-Pfade, src-Attribute, maschinenlesbare Keys).
13. Im Reveal-Zielordner liegt `reveal_snapshot.md` als nicht-rendernde Momentaufnahme mit `_build.render: false` und `_build.list: false`.

---

## 6. Transparenzpflicht

Im Ergebnis dokumentiert der Agent kurz:

- gewählte Kernpunktanzahl und Begründung,
- ggf. gewählte Umschreibintensität (konservativ/redaktionell),
- Mapping Blogkernpunkte -> Themenfolien.
- optional nach `BLOG FINAL`: 2-4 Reflexionsfragen oder Hypothesen aus einem Vergleich zwischen `.index.md` und finalem `index.md`; optional nach `REVEAL GO`: 2-4 Reflexionsfragen oder Hypothesen aus einem Vergleich zwischen `reveal_snapshot.md` und finalem Reveal-Stand (ohne automatische Regelanpassung).

---

## 7. Konfliktregel

Bei Regelkonflikten gilt folgende Priorität:

1. Agent Contract
2. master_agent.md
3. prompts/create.md und prompts/check.md
4. templates/blog_template.md und templates/reveal_template.md

---

## 8. Governance-Hinweis

Änderungen an Moduslogik, DoD oder Kernpunktregeln müssen in diesem Dokument im selben Änderungszyklus mitgeführt werden.

---

## 9. Regression-Check-Katalog

Diese Prüffälle sollen nach Änderungen an Agentenlogik, Prompts oder Templates gegen Testinhalte durchlaufen werden.

### RC-01 Modusreihenfolge erzwungen

- Erwartung: Planungsmodus vor Blogmodus, Blogmodus vor Reveal-Transformationsmodus.
- Fehlerindikator: Reveal wird direkt aus Planung erzeugt.

### RC-02 Blog ist leser:innenorientiert

- Erwartung: finaler Blog enthält publizierbaren Fließtext statt interner Planungsstichpunkte.
- Fehlerindikator: starke Nutzung von Planungsrastern ohne ausformulierende Erklärung.

### RC-03 Dynamische Kernpunktzahl

- Erwartung: Kernpunktzahl wird inhaltlich begründet und ist nicht hart auf einen Fixwert gesetzt.
- Fehlerindikator: immer gleiche Kernpunktzahl bei deutlich unterschiedlichen Themen.

### RC-04 Quellenkonsistenz Blog

- Erwartung: zentrale Aussagen sind im Text mit Quellenbezug sichtbar; Literaturteil ist vollständig.
- Fehlerindikator: relevante Behauptungen ohne Quellenbezug oder Quellen nur im Literaturteil.

### RC-05 Reveal-Mapping korrekt

- Erwartung: alle Blogkernpunkte sind durch Themenfolien inhaltlich abgedeckt (direkt oder gruppiert).
- Fehlerindikator: nicht abgedeckte Blogkernpunkte oder zusätzliche, unbelegte Kernbehauptungen.

### RC-06 Strukturdrift in Simulationen

- Erwartung: Simulationsdokumente bleiben formal konsistent (eindeutige Überschriften, keine Duplikate).
- Fehlerindikator: wiederholte gleichlautende Überschriften oder uneinheitliche Abschnittslogik.

### RC-07 Konfliktauflösung nach Priorität

- Erwartung: bei widersprüchlichen Regeln wird die Priorität aus Abschnitt 7 eingehalten.
- Fehlerindikator: untergeordnete Datei übersteuert den Agent Contract.

### RC-08 Transparenzpflicht erfüllt

- Erwartung: Ergebnis enthält Kernpunktbegründung, Umschreibintensität (falls relevant) und Blog-zu-Reveal-Mapping.
- Fehlerindikator: Ausgabe ohne nachvollziehbare Entscheidungsbegründung.

### RC-09 Blogmodus ohne Ablaufdominanz

- Erwartung: der Blogartikel erklärt Inhalte im Fließtext.
- Fehlerindikator: der Text besteht überwiegend aus Ablaufpunkten.

### RC-10 Quellenregel eingehalten

- Erwartung: spezifische Quellenangaben sind belastbar und nicht erfunden.
- Fehlerindikator: erfundene Studien, DOI-Angaben oder Publikationsdetails.

### RC-11 Meta-Vollständigkeit Blog

- Erwartung: finaler Blog enthält vollständiges Pflicht-Frontmatter gemäß `ai_agents/templates/blog_template.md`.
- Fehlerindikator: fehlende oder leere Pflichtfelder, insbesondere im OER-/TULLU-/OERSI-Block.

### RC-12 Meta-Vollständigkeit Reveal

- Erwartung: finale Präsentation enthält vollständiges Pflicht-Frontmatter gemäß `ai_agents/templates/reveal_template.md` und keine OER-Metadaten.
- Fehlerindikator: fehlende oder leere Pflichtfelder oder vorhandene OER-Felder in Reveal.

### RC-13 Snapshot bei REVEAL GO

- Erwartung: mit finaler Reveal-Datei wird im Reveal-Zielordner `reveal_snapshot.md` erzeugt und nicht gerendert.
- Fehlerindikator: fehlende Snapshot-Datei oder Snapshot als Ableitungsquelle verwendet.

### RC-14 Reveal-Textdichte und Kernbotschaften

- Erwartung: jede Inhaltsfolie trägt eine klar erkennbare Kernbotschaft;
  Textdichte bleibt im foliengerechten Bereich.
- Fehlerindikator: textlastige Folien ohne klare Priorisierung der Aussage.

### RC-15 Visualisierungsquote

- Erwartung: je fachlichem Hauptkapitel ist mindestens eine visuelle Stützfolie vorhanden,
  inklusive kurzer Quellenzeile.
- Fehlerindikator: rein textbasierte Kapitel ohne visuelle Strukturhilfe.

### RC-16 Umlaut-Normalisierung in sichtbaren Texten

- Erwartung: sichtbare deutsche Folientexte enthalten korrekte Umlaute.
- Fehlerindikator: systematische Ausgabe von `ae/oe/ue` in sichtbaren Folientexten,
  obwohl keine technische Ausnahme vorliegt.
