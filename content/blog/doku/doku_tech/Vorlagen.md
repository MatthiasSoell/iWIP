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