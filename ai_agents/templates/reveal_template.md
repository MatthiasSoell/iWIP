# Reveal Template — SciBlog iWIP

Dieses Template definiert die Standardstruktur
für Reveal-Präsentationen im SciBlog iWIP.

Die Präsentation wird aus dem Blogartikel abgeleitet.

Emojis werden gemäß **content_emoji_policy.md** verwendet.

Referenzstil (qualitatives Zielbild):

- `content/praesentation/oer/uplan_ki_oer/_index.md`
- `content/praesentation/widi/hosp_feed_refl/_index.md`

---

## Frontmatter (Pflichtstruktur Reveal)

```yaml
title: ""
title_reveal: ""
emojis: ""
veranstaltungstyp: ""
veranstaltung: ""
author: ""
blog: ""
source_lastmod: YYYY-MM-DD
date: YYYY-MM-DD
lastmod: YYYY-MM-DD
draft: false

outputs:
  - Reveal

reveal_hugo:
  theme: simple
  slide_number: true
  transition: slide
  custom_theme: /iWIP/css/custom_reveal.css

description: >
  

summary: >
  

tags: []
categories: []

oer:
  is_oer: true
  kind: "presentation"
  note: >
    

  creators:
    - name: ""
      given_name: ""
      family_name: ""
      affiliation: ""
      url: ""
      orcid: ""

  publisher:
    name: ""
    url: ""

  license:
    label: ""
    url: ""

  source:
    label: ""
    url: ""

  in_language: "de"
  learning_resource_type: "Presentation"
  educational_level: []
  audience: []
  time_required: ""

  about:
    - term: ""

  rights_exceptions: []
  todos: []
```

Regeln:

- Alle Felder sind verpflichtend, außer `oer.rights_exceptions` und `oer.todos`.
- `blog` soll auf den zugehörigen Blogbeitrag zeigen.
- `source_lastmod` muss den aktuellen `lastmod` des zugehörigen Blogbeitrags enthalten.
- Migrationsregel: Bei bestehenden Legacy-Reveals ohne `source_lastmod` ist der Nachtrag beim naechsten Reveal-Update verpflichtend.
- Metadaten müssen kontextspezifisch zur jeweiligen Präsentation ausgefüllt sein (keine Copy-Paste-Werte).
- Der Agent darf keine Reveal-Datei als final ausgeben,
  wenn Pflichtfelder fehlen oder leer geblieben sind.
- Pflichtfelder muessen semantisch gefuellt sein (keine Platzhalterwerte wie `TODO`, `tbd`, `-`, `...`).
- Ohne explizites Nutzer-OK darf keine Reveal-Datei erstellt, aktualisiert oder finalisiert werden.

---

## Folienstruktur

## Folie 1 — Titel

{{< titleSlide >}}

Hinweis:

- Nutze nach Möglichkeit `title_reveal` und `emojis` im Frontmatter,
  um die visuelle Tonalität der Präsentation zu schärfen.

---

## Folie 2 — Leitfrage / Problem 💭

Formuliere die zentrale Leitfrage.

Die Folie soll:

- Interesse wecken
- das Problem sichtbar machen
- den Einstieg strukturieren.

---

## Folie 3 — Ablauf 🧭

Überblick über den Ablauf der Sitzung.

Zum Beispiel:

1 Einstieg  
2 Problem / Leitfrage  
3 Arbeitsphase  
4 Diskussion  
5 Reflexion  
6 Transfer  

---

## Folie 4 — Lernziele 🎯

Formuliere die wichtigsten Lernziele der Veranstaltung.

---

## Folie 5 — Einordnung

Ordne das Thema kurz ein.

Zum Beispiel:

- fachliche Perspektive
- didaktische Perspektive
- Praxisbezug.

---

## Folie 6 — Arbeitsphase 🧩

Beschreibe die zentrale Lernaktivität.

Die Folie enthält:

- Arbeitsauftrag
- Arbeitsform
- ggf. Zeitrahmen.

---

## Folie 7 — Diskussion / Reflexion 🪞

Mögliche Diskussionsfragen.

Ziel:

- Argumentation
- Perspektivwechsel
- Reflexion.

---

## Folie 8 — Transfer / Erweiterung 🌱

Fragen zur Übertragung des Gelernten.

Zum Beispiel:

- Anwendung auf andere Kontexte
- Verbindung zu Praxis
- weiterführende Fragen.

---

## Adaptive Kernfolienregel

Die Anzahl der inhaltlichen Kernfolien wird dynamisch aus dem Blogartikel abgeleitet.

- Ermittle zuerst, wie viele Kernpunkte im Blogartikel fachlich ausgearbeitet wurden.
- Erzeuge daraus eine fachlich sinnvolle Themenfolienstruktur (1:1 oder gruppiert).
- Vermeide starre Folienanzahlen, wenn sie nicht zur inhaltlichen Dramaturgie passen.

Die Folienstruktur ist somit ein Gerüst,
das an die fachlich sinnvolle Gliederung angepasst wird.

### Transformations-Checks (verbindlich)

- Erzeuge ein kurzes Mapping: Blogkernpunkt -> Themenfolie.
- Übernimm nur Inhalte, die im Blogartikel fachlich ausgearbeitet sind.
- Ergänze keine neuen unbelegten Kernaussagen.
- Prüfe vor Abschluss die Konsistenz von Kernaussagen zwischen Blog und Reveal.
- Folientitel sollen als reine Themenüberschrift erscheinen
  (z. B. "Lerntypen") und keine sichtbaren Präfixe wie "Kernfolie" enthalten.
- Stelle sicher, dass alle Blogkernpunkte in den Folien inhaltlich abgedeckt sind.

## Gestaltungsstil (verbindlich)

Reveal-Folien sollen die Referenzqualität erkennbar treffen:

- klare Leitfrage- und Zielorientierung,
- hoher visueller Fokus, wenig Fließtext,
- gezielter Einsatz von `fragment`-Schritten,
- semantische Emojis als Navigationshilfe,
- praxisnahe Arbeitsaufträge statt Textwände.

Zusätzliche Qualitätsregeln (verbindlich):

- Pro Inhaltsfolie genau eine klare Kernbotschaft.
- Textdichte niedrig halten: Richtwert maximal 35-45 Wörter pro Inhaltsfolie.
- Keine kompakten Absatzblöcke; stattdessen kurze Aussagen, Listen, Callouts.
- Fachliche Verdichtung über mehrere Folien statt "alles auf eine Folie".
- Sichtbarer Medieneinsatz: pro fachlichem Hauptkapitel mindestens ein visuelles Element
  (z. B. Abbildung, Diagramm, Tabelle, Schema).
- Jede eingesetzte Grafik erhält eine kurze Quellenzeile auf der Folie.
- Reveal-Fragmente so nutzen, dass Argumentation schrittweise sichtbar wird
  (nicht dekorativ, sondern dramaturgisch).

Sprach-/Schreibregeln (verbindlich):

- Folientexte in natürlichem, präsentationsnahen Deutsch ausgeben.
- In sichtbaren deutschen Texten Umlaute normalisieren: `ae -> ä`, `oe -> ö`, `ue -> ü`.
- In sichtbaren deutschen Texten Gedankenstrich `–` als Satzzeichen verwenden (statt Bindestrich `-`).
- Externe Links im sichtbaren Folientext immer als HTML-Anker mit sichtbarem Linktext ausgeben: `<a href="..." target="_blank" rel="noopener noreferrer">LINKTEXT</a>`.
- Die Badge-Regeln fuer das Blog-Literaturverzeichnis (siehe `templates/blog_template.md`) bleiben davon unberuehrt.
- Die Umlaut-Normalisierung gilt nicht für technische Felder und Tokens,
  insbesondere nicht für URLs, Pfade, Dateinamen, Slugs, Alias-Pfade,
  Bildquellen (`src`) oder maschinenlesbare Schlüssel.
- Wenn Fachbegriffe, Eigennamen oder Zitate bewusst ASCII verwenden,
  bleibt die Originalschreibweise erhalten.

Nutze bei passenden Inhalten:

- Callout-Boxen für zentrale Take-aways,
- Bild- oder Medienfolien mit kurzer Quellenzeile,
- kurze Interaktionsfolien (Fragen, Abstimmung, Auftrag).

Bildpfad-Regel (verbindlich):

- Standard fuer aus dem Blog uebernommene Bilder: absolute Pfade auf den Blogbeitrag verwenden (`/iWIP/blog/<bereich>/<ordner>/...`).
- Reveal-spezifische Bilder (z. B. Schrittsequenzen oder Animationen) im Reveal-Ordner ablegen und relativ referenzieren.
- Relative Bildpfade duerfen nur verwendet werden, wenn die Datei im Reveal-Ordner tatsaechlich vorhanden ist.
- Wenn ein Bild nicht aufloesbar ist, vor Finalisierung Pfad korrigieren oder Datei gezielt in den Reveal-Ordner uebernehmen.

---

## Vorletzte Folie — Literatur

{{< literatureSlide >}}

---

## Letzte Folie — Abschluss

{{< endSlide >}}

---

## Gestaltungsregeln

Reveal-Folien sollen:

- wenig Text enthalten
- klare Arbeitsaufträge formulieren
- Diskussion und Interaktion fördern.
- Abstände zwischen Überschrift und Liste über Utility-Klassen in
  `static/css/custom_reveal.css` steuern (z. B. `.headline-list-gap`),
  nicht über Inline-Styles pro Folie.

Sprachregel:

- Folientexte sollen mündlich anschlussfähig sein,
- nicht wie komprimierte Blogabsätze wirken,
- und pro Folie eine klare Kernbotschaft tragen.

Der Fokus liegt auf:

- Leitfrage
- Aktivität
- Diskussion
- Reflexion.

## Definition of Done (Reveal-Layout)

Definition of Done: siehe master_agent.md (Definition of Done - Reveal-Ableitung).
