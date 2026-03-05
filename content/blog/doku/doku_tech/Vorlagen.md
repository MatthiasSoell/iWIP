# Vorlagen – Copy & Paste (Blog / Präsentation)

Diese Sammlung enthält wiederkehrende Snippets aus `content/blog/**/index.md` und `content/praesentation/**/_index.md`.

---

## 1) Blog-Vorlagen (`index.md`)

### 1.1 Kopfbereich: Top-Toggle + OER-Meta

```html
<div class="top-toggle">
  <button id="md-copy-btn" title="Markdown kopieren (ohne Bilder)">📑</button>
  <button onclick="triggerPrint()" title="Blog speichern">📥</button>
  <button onclick="location.href='/iWIP/praesentation/oer/MEIN_BEITRAG/'" title="Zur Präsentationsansicht">🖥️</button>
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

### 1.2 Callouts (Markdown-Admonitions)

```markdown
> [!TIPP]
> TIPP

> [!QUOTE]
> Zitat

> [!IMPORTANT]
> Hinweis

> [!NOTE]
> Betonung
```

### 1.3 Literatur-Icons (UB / DOI / WorldCat)

```html
<a class="lit-ub" href="https://opac.lbs-rostock.gbv.de/DB=1/XMLPRS=N/PPN?PPN=123" target="_blank" rel="noopener noreferrer" aria-label="Universitätsbibliothek-Rostock-Link zur Publikation"></a>
<a class="lit-doi" href="https://doi.org/10.xxxx/xxxx" target="_blank" rel="noopener noreferrer" aria-label="DOI-Link zur Publikation"></a>
<a class="lit-worldcat" href="https://search.worldcat.org/de/title/123" target="_blank" rel="noopener noreferrer" aria-label="WorldCat-Link zur Publikation"></a>
```

### 1.4 DOI-Hinweis-Icon

```html
<span class="info_tip"
      title="Der DOI führt direkt zum Artikel."
      tabindex="0"
      aria-label="Hinweis: Der DOI führt direkt zum Artikel.">
  ⓘ
</span>
```

### 1.5 Abbildungsrahmen

```html
<figure class="figure-frame">
  <img src="bild.jpg"
       alt="Aussagekräftiger Alternativtext">
</figure>
```

### 1.6 Interne Verlinkung auf andere Beiträge

```markdown
[Warum OER?]({{< ref "blog/oer/warum_oer/index.md" >}})
```

---

## 2) Präsentations-Vorlagen (`_index.md`)

### 2.1 Grundgerüst Reveal

```markdown
---

{{< titleSlide >}}

---

## Folientitel

Inhalt

---

{{< endSlide >}}
```

### 2.2 Titelbereich mit `logoBox` + parametrisiertem `titleSlide`

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

### 2.3 Literatur-/Abschlussfolien (Shortcodes)

```markdown
{{< literatureSlide >}}

---

{{< endSlide >}}
```

### 2.4 Fragment: Absatz / Liste / Markdown-Kommentar

```html
<p class="fragment">Dieser Text erscheint später.</p>

<li class="fragment">Dieser Listenpunkt erscheint später.</li>
```

```markdown
- Ein Punkt, der später erscheint. <!-- .element: class="fragment" -->
```

### 2.5 Reveal-Callout (Shortcode)

```markdown
{{< callout type="tip" >}}
Dies ist ein Tipp.
{{< /callout >}}

{{< callout type="warning" >}}
Dies ist ein Hinweis.
{{< /callout >}}

{{< callout type="info" >}}
Dies ist eine neutrale Info.
{{< /callout >}}
```

### 2.6 Reveal-Callout (HTML, mit/ohne Fragment)

```html
<div class="callout callout--tipp fragment">
  <div class="callout-content">
    <p>
      Kernaussage für die Folie.
    </p>
  </div>
</div>
```

### 2.7 Hinweisbox in Präsentation

```html
<div class="hinweis-box fragment">
  ☝️ Kurzer Hinweistext.
</div>
```

### 2.8 `rawhtml`-Block für komplexes HTML

```markdown
{{< rawhtml >}}
<div class="k3-step fragment" data-fragment-index="1">
  Komplexes, eigenes HTML
</div>
{{< /rawhtml >}}
```

### 2.9 Bild + Bildquelle (Reveal)

```html
<img class="fragment responsive-image" data-fragment-index="1" src="bild.png" alt="Beschreibung">
<p class="fragment bild-quelle" data-fragment-index="1">Bildquelle: ...</p>
```

---

## 3) Mini-Workflow (für schnelles Arbeiten)

1. Blog mit Abschnittsstruktur + Callouts + Literatur-Icons schreiben.
2. Für Präsentation auf Kernaussagen kürzen, dann `titleSlide` + `fragment` + `callout` einsetzen.
3. Abschluss immer mit `{{< literatureSlide >}}` und `{{< endSlide >}}`.

---

## 4) Content Conventions – Emoji-Policy (Referenz)

Verbindliche Quelle:

- `project_governance/content_emoji_policy.md`

Kurzregeln für schnelles Arbeiten:

- Emojis semantisch einsetzen (nicht dekorativ).
- Maximal 1 Emoji pro Absatz/Bullet.
- Emoji-Bedeutungen konsistent halten.
- OER-Kennzeichnung: `🎓🌍🔓`

---

## 5) KI-Workflow-Prompts (Copy & Paste)

### 5.1 Didaktik glätten (aus Stichpunkten)

```text
Rolle: Du bist mein didaktischer Sparringspartner für wirtschaftsdidaktische Blogbeiträge.

Aufgabe:
- Überführe meine Stichpunkte in eine didaktisch konsistente Struktur.
- Behalte meine Aussagen vollständig bei, erfinde keine neuen Inhalte.
- Markiere fehlende Übergänge oder argumentative Lücken als kurze Hinweise.

Zielstruktur:
1) Ausgangsproblem
2) Zielperspektive
3) Didaktische Einordnung
4) Praktische Umsetzung
5) Reflexion / Ausblick

Ausgabeformat:
- Erst: strukturierter Entwurf mit Zwischenüberschriften
- Danach: 5 konkrete Verbesserungsvorschläge in Stichpunkten

Hier ist mein Rohtext:
<<<
[HIER EINFÜGEN]
>>>
```

### 5.2 Sprachlich finalisieren (wissenschaftsnah, klar)

```text
Rolle: Du bist mein wissenschaftsnaher Lektor (Deutsch).

Aufgabe:
- Formuliere den Text klar, präzise und gut lesbar.
- Erhalte meinen Stil (professionell, zugänglich, nicht überformal).
- Kürze Redundanzen und glätte lange Sätze.
- Keine inhaltlichen Ergänzungen.

Stilregeln:
- Aktive Formulierungen
- Kurze Absätze
- Fachbegriffe nur dort, wo sie wirklich nötig sind
- Gender- und Zeichensetzung konsistent lassen

Ausgabeformat:
1) Überarbeitete Fassung komplett
2) Kurzliste: wichtigste sprachliche Änderungen (max. 8 Punkte)

Text:
<<<
[HIER EINFÜGEN]
>>>
```

### 5.3 Emoji-Standard anwenden

```text
Rolle: Du bist mein Editor für konsistente Emoji-Annotation nach meinem Standard.

Aufgabe:
- Füge passende Emojis nur dort ein, wo sie semantisch unterstützen.
- Keine Emoji-Überladung: maximal 1 Emoji pro Satz bzw. Listenpunkt.
- Bestehende Emojis nur ersetzen, wenn sie unpassend oder inkonsistent sind.

Regeln:
- Überschriften: optional 1 Emoji
- Aufzählungen: höchstens 1 Emoji pro Bullet
- Fachlich neutrale Abschnitte: ggf. ganz ohne Emoji

Ausgabeformat:
1) Text mit Emoji-Anpassung
2) Liste der verwendeten Emoji-Regeln (kurz)

Text:
<<<
[HIER EINFÜGEN]
>>>
```

### 5.4 Blog → Präsentation reduzieren (Reveal-fähig)

```text
Rolle: Du bist mein Editor für die Reduktion eines Blogtexts auf eine Reveal-Präsentation.

Aufgabe:
- Reduziere den Text auf präsentationsrelevante Kernaussagen.
- Erzeuge prägnante Folientitel und kurze Bulletpoints.
- Kennzeichne Stellen, die als Fragment erscheinen sollen.
- Behalte zentrale Quellenhinweise bei (kurzform).

Ausgabeformat:
- Direkt als Hugo-Reveal-Markdown mit Folientrennern `---`
- Nutze bei Bedarf diese Muster:
  - `{{< titleSlide >}}`
  - `{{< literatureSlide >}}`
  - `{{< endSlide >}}`
  - `<!-- .element: class="fragment" -->`

Zusatz:
- Max. 5 Bullets pro Folie
- Möglichst 1 Kernaussage pro Folie

Blogtext:
<<<
[HIER EINFÜGEN]
>>>
```

### 5.5 Qualitätscheck vor Veröffentlichung

```text
Prüfe den finalen Blog-/Slide-Text auf folgende Punkte:

1) Inhalt
- Roter Faden erkennbar?
- Zielperspektive und Fazit konsistent?

2) Sprache
- Klar, präzise, ohne Redundanzen?
- Einheitlicher Stil?

3) Emojis
- Konsistent und sparsam?
- Keine dekorative Überladung?

4) Präsentationstauglichkeit
- Folien nicht überladen?
- Pro Folie klare Kernaussage?

Gib am Ende eine kurze Ampelbewertung:
- Grün = direkt veröffentlichbar
- Gelb = kleine Korrekturen
- Rot = größere Überarbeitung nötig
```

---

## 6) Ultra-Kurz (1-Minuten-Version)

### 6.1 Rohtext → didaktische Struktur

```text
Strukturiere meinen Rohtext didaktisch in 5 Abschnitte: Ausgangsproblem, Zielperspektive, Einordnung, Umsetzung, Ausblick. Keine neuen Inhalte ergänzen.

Text:
<<<
[HIER EINFÜGEN]
>>>
```

### 6.2 Struktur → sprachlich sauber

```text
Überarbeite den Text sprachlich klar und präzise (wissenschaftsnah, gut lesbar), ohne inhaltliche Ergänzungen. Kürze Redundanzen.

Text:
<<<
[HIER EINFÜGEN]
>>>
```

### 6.3 Emoji-Standard schnell anwenden

```text
Füge Emojis nach meinem Standard sparsam ein: max. 1 Emoji pro Satz/Bullet, nur semantisch passend, keine Überladung.

Text:
<<<
[HIER EINFÜGEN]
>>>
```

### 6.4 Blogtext → Reveal-Folien (kompakt)

```text
Reduziere den Text auf Reveal-Folien mit `---`, max. 5 Bullets pro Folie, 1 Kernaussage pro Folie, Fragmente markieren (`<!-- .element: class="fragment" -->`). Nutze bei Bedarf `{{< titleSlide >}}`, `{{< literatureSlide >}}`, `{{< endSlide >}}`.

Text:
<<<
[HIER EINFÜGEN]
>>>
```