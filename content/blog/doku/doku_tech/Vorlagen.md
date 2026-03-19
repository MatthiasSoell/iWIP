# Vorlagen – Quickstart, Copy & Paste, Qualitätschecks

Diese Seite ist als öffentliche Arbeitsvorlage gedacht: schnell im Alltag nutzbar, aber mit klaren Qualitätsleitplanken.

Sie ist bewusst getrennt nach:

- Blog (`index.md`)
- Reveal-Präsentation (`_index.md`)

---

## 1) Quickstart (2 Minuten)

1. Nutze unten ein passendes Snippet aus den Top 10.
2. Schreibe erst die inhaltliche Struktur, dann Feinschliff (Sprache, Emojis, Quellen).
3. Prüfe vor Veröffentlichung mit den jeweiligen Qualitätschecks für Blog oder Reveal.

---

## 2) Top 10 Copy-Paste Snippets

### 2.1 Blog: Top-Toggle + OER-Meta

```html
<div class="top-toggle">
  <button id="md-copy-btn" title="Markdown kopieren (ohne Bilder)">📑</button>
  <button onclick="triggerPrint()" title="Blog speichern">📥</button>
  <button onclick="location.href='/iWIP/praesentation/<BEREICH>/<ORDNER>/'" title="Zur Präsentationsansicht">🖥️</button>
  <button class="iwip_help_btn"
        type="button"
        aria-haspopup="dialog"
        aria-controls="iwip_help_overlay"
        aria-expanded="false"
        title="Hinweise zur Nutzung">
  ⓘ
  </button>
</div>

{{< oer-meta >}}
```

Pfadregel: `content/blog/<BEREICH>/<ORDNER>/index.md` -> `/iWIP/praesentation/<BEREICH>/<ORDNER>/`

### 2.2 Blog: Callouts

```markdown
> [!TIPP]
> Kurzer Tipp.

> [!IMPORTANT]
> Wichtiger Hinweis.
```

### 2.3 Blog: Figure + Bildquelle

```html
<figure class="figure-frame">
  <img src="bild.jpg" alt="Aussagekräftiger Alternativtext">
</figure>

<p class="bildquelle">Bildquelle: Eigene Darstellung · Illustration: erstellt mit Unterstützung von ChatGPT · Lizenz: <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener">CC BY-SA 4.0</a></p>
```

### 2.4 Blog: Interner Hugo-Link

```markdown
[Warum OER?]({{< ref "blog/oer/warum_oer/index.md" >}})
```

### 2.5 Blog: Agenda-Tabelle (Standard)

```markdown
<div class="agenda">

| Phase | Inhalt | Ziel | Zeit |
|---|---|---|---|
| 1 | Einstieg | Orientierung | 5<br>Min |
| 2 | Arbeitsphase | Vertiefung | 25<br>Min |

</div>
```

### 2.6 Blog: Agenda-Tabelle (Varianten)

```markdown
<div class="agenda compact"> ... </div>
<div class="agenda roomy"> ... </div>
```

### 2.7 Reveal: Minimalgerüst

```markdown
---

{{< titleSlide >}}

---

## Folientitel

Kernaussage

---

{{< endSlide >}}
```

### 2.8 Reveal: Fragmente

```markdown
- Erster Punkt
- Zweiter Punkt <!-- .element: class="fragment" -->
```

### 2.9 Reveal: Literatur-/Abschlussfolie

```markdown
{{< literatureSlide >}}

---

{{< endSlide >}}
```

### 2.10 Reveal: Callout

```markdown
{{< callout type="tip" >}}
Kernaussage für die Folie.
{{< /callout >}}
```

### 2.11 Reveal: Abstand Headline -> Liste

```markdown
###### Beitrag evidenzinformierter<br>Unterrichts- und Schulentwicklung:

<div class="headline-list-gap">

- Weiterentwicklung von **Unterrichtspraxis** 🧠
- Unterstützung der **Lehrkräfteprofessionalisierung** 👩‍🏫
- Stärkung einer innovativen, kooperativen **Schulkultur** 🤝

</div>
```

Hinweis: Für solche Abstände bevorzugt Klassen in
`static/css/custom_reveal.css` (z. B. `.headline-list-gap`)
statt Inline-Styles.

---

## 3) Blog-Bereich (`index.md`)

### 3.1 Markdown-Grundlagen (Blog)

````markdown
## Abschnitt

Kurzer Einleitungsabsatz mit klarer Leitidee.

- Punkt 1
- Punkt 2

> [!QUOTE]
> Pointierte Aussage.

`Inline-Code` und

  Codeblock
````

### 3.2 Tabellen-Patterns (Blog)

Wichtig:

- Normale Markdown-Tabellen erhalten automatisch den universellen Tabellenstil.
- Für breite Prozess-/Vergleichstabellen immer `agenda` als Wrapper nutzen.
- Optional Dichte steuern mit `agenda compact` oder `agenda roomy`.
- Für eine Tabellenüberschrift vor der Tabelle: `table-title` nutzen (fett + zentriert).
- Optional für eine zweite, nicht-fette Zeile direkt darunter: `<span class="table-title-note">...</span>` innerhalb von `table-title` nutzen.
- Für Überschriften direkt vor Grafiken/Bildern: `grafic-title` nutzen (gleiche Typografie, enger Abstand zur Grafik).
- In der Zeitspalte standardmäßig Format `Zahl<br>Min` verwenden (z. B. `25<br>Min`).

Tabellenüberschrift (empfohlen):

```markdown
<p class="table-title">Methoden und Medien in Abhängigkeit von Aktions- und Sozialform (Euler & Hahn, 2014, 319)</p>

<p class="table-title">Taxonomie nach Anderson & Krathwohl (2001)<span class="table-title-note">(Mouseover zeigt die Tabelleneinträge)</span></p>

<p class="grafic-title">Lerntypen</p>
```

Beispiel (5 Spalten):

```markdown
<div class="agenda">

| Aktionsform | Plenum | Gruppe | Partner | Einzeln |
|---|---|---|---|---|
| Darbieten | Vortrag / Vorführung | Instruktion | Instruktion | Instruktion |
| Im Dialog entwickeln | Lehrgespräch | Beratung / Moderation | Beratung / Moderation | Beratung / Moderation |
| Erarbeiten & entdecken lassen | angeleitete Einzelarbeit | Gruppenarbeit | Partnerarbeit | Einzelarbeit |

</div>
```

### 3.3 Häufige Bausteine (Blog)

- Literatur-Icons: `lit-ub`, `lit-doi`, `lit-worldcat`
- DOI-Hinweis: `info_tip`
- Bildrahmen + Bildquelle: `figure-frame`, `bildquelle`

### 3.4 Qualitätscheck (Blog)

1. Struktur: Leitfrage, roter Faden, nachvollziehbarer Abschluss.
2. Evidenz: Kernaussagen mit Quellenbezug im Fließtext.
3. Sprache: klar, präzise, wenig Redundanz.
4. Emojis: semantisch, sparsam, konsistent.
5. Technik: interne Links funktionieren, Tabellen sinnvoll gesetzt, Bilder mit Alt-Text.

---

## 4) Reveal-Bereich (`_index.md`)

### 4.1 Markdown-Grundlagen (Reveal)

```markdown
---

## Folie 1

- Max. 3-5 Bullets

---

## Folie 2

Ein Punkt pro Folie als Kernaussage.
```

### 4.2 Typische Reveal-Bausteine

Titelbereich:

```markdown
{{< logoBox src="/iWIP/bilder/logo_siblog_iwip.png" text="SciBlog iWIP" show="true" >}}

{{< titleSlide
  title="Mein Titel"
  emojis="🤖 🎓🌍🔓"
  veranstaltung="Meine Veranstaltung"
  author="Prof. Dr. Matthias Söll"
  blog="/iWIP/blog/oer/mein_beitrag/"
>}}
```

Fragment + rawhtml:

```markdown
{{< rawhtml >}}
<div class="k3-step fragment" data-fragment-index="1">Kernaussage</div>
{{< /rawhtml >}}
```

### 4.3 Qualitätscheck (Reveal)

1. Pro Folie genau eine Hauptaussage.
2. Maximal 5 Bullets pro Folie.
3. Fragmente gezielt, nicht inflationär.
4. Lesbarkeit: ausreichend Kontrast, Schrift nicht zu klein, keine Textwände.
5. Abschluss immer mit Literatur/Endfolie.

---

## 5) KI-Workflow-Prompts (Kurzfassung)

### 5.1 Rohtext didaktisch strukturieren

```text
Strukturiere meinen Rohtext in 5 Abschnitte: Ausgangsproblem, Zielperspektive, Einordnung, Umsetzung, Ausblick. Keine neuen Inhalte ergänzen.

Text:
<<<
[HIER EINFÜGEN]
>>>
```

### 5.2 Sprachlich finalisieren

```text
Überarbeite den Text sprachlich klar und präzise (wissenschaftsnah, gut lesbar), ohne inhaltliche Ergänzungen. Kürze Redundanzen.

Text:
<<<
[HIER EINFÜGEN]
>>>
```

### 5.3 Blog zu Reveal reduzieren

```text
Reduziere den Text auf Reveal-Folien mit `---`, max. 5 Bullets pro Folie, 1 Kernaussage pro Folie, Fragmente markieren (`<!-- .element: class="fragment" -->`).

Text:
<<<
[HIER EINFÜGEN]
>>>
```

---

## 6) Verbindliche Referenzen

- `project_governance/css_architecture.md`
- `project_governance/content_emoji_policy.md`
- `project_governance/ai_copilot_instructions.md`
- `ai_agents/templates/blog_template.md`
- `ai_agents/templates/reveal_template.md`

---

## 7) Reveal-Baukasten (Geruest fuer die naechste Ueberarbeitung)

Ziel:

- wiederkehrende Layoutaufgaben ueber feste Klassen loesen,
- Inline-Styles reduzieren,
- neue Praesentationen schneller bauen.

### 7.1 Einsatzprinzip

1. Erst Inhalt bauen, danach Layout.
2. Pro Folie nur vorhandene Baustein-Klassen kombinieren.
3. Neue Klasse nur dann aufnehmen, wenn sie mindestens 2x genutzt wurde.

### 7.2 Kern-Bausteine (V1)

Layout/Spacing:

- `layout-compact` (enge Vertikalabstaende)
- `headline-list-gap` (mehr Luft zwischen Ueberschrift und Liste)
- `list-tight` (kompakte Listen)

Bilder/Diagramme:

- `figure-frame figure-frame-sm`
- `figure-frame figure-frame-ssm` (supersmall, platzkritische Folien)
- `methoden-bonz-diagram` (Overlay-Frames Bonz)
- `methoden-euler-hahn-diagram` (Overlay-Frames Euler/Hahn)

Quellenzeilen:

- `bild-quelle` (Standard)
- `bild-quelle is-tight` (enger Abstand)

Callouts:

- `callout--tipp`
- `callout--important`
- `callout--note`
- `callout--quote`

### 7.3 Entscheidungslogik (Wenn-Dann)

- Wenn eine Grafik in den Footer ragt -> `figure-frame-ssm` nutzen.
- Wenn mehrere Frame-Bilder ueberlagert werden sollen -> Overlay-Container nutzen (`...-diagram`), nicht `figure-frame`.
- Wenn Headline + Grafik zu weit auseinander stehen -> erst Container-Margins pruefen, nicht Bildbreite.
- Wenn Quelle zu tief sitzt -> Abstand ueber `bild-quelle`-Variante steuern, nicht ueber globale Paragraph-Regeln.

### 7.4 Copy-Paste Muster (Overlay)

```markdown
**Untertitel / Bildtitel**

{{< rawhtml >}}
<div class="methoden-bonz-diagram">
  <img src="pfad/frame_1.png" class="fragment plain" alt="">
  <img src="pfad/frame_2.png" class="fragment plain" alt="">
  <img src="pfad/frame_3.png" class="fragment plain" alt="">
</div>
{{< /rawhtml >}}

<p class="bild-quelle is-tight">Bildquelle: ... · Lizenz: CC BY-SA 4.0</p>
```

### 7.5 QA-Check vor Freigabe (Reveal)

1. Keine Elemente ueberlagern den Footer.
2. Quellenzeile ist auf 100% Zoom lesbar.
3. Max. eine Hauptaussage pro Folie.
4. Fragmente erscheinen in sinnvoller Reihenfolge.
5. Keine unnoetigen Inline-Styles, wenn Baustein-Klasse existiert.
6. Diagrammklassen sind sprechend und folienuebergreifend wiederverwendbar.

### 7.6 Kandidatenliste fuer neue Klassen

Hier waehrend der naechsten Praesentationen sammeln:

- Kandidat:
  Einsatzfall:
  Bereits genutzt in:
  In Baukasten uebernehmen (ja/nein):

