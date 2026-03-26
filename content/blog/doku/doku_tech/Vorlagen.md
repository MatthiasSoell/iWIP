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

<!-- Alias-Klassen (gleiches Styling): -->
<div class="agenda agenda-sm"> ... </div>
<div class="agenda agenda-lg"> ... </div>
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

{{< callout type="info" >}}
Zusatzinformation in ruhigem Ton.
{{< /callout >}}

{{< callout type="warning" >}}
Wichtiger Hinweis / Stolperstelle.
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

## 7) CSS-Baukasten (Konsistent und schnell)

Ziel:

- wiederkehrende Layoutaufgaben ueber feste Klassen loesen,
- Inline-Styles reduzieren,
- dieselben Modifier in Blog und Reveal nutzen.

### 7.1 Einheitliche Modifier (neu)

Blog (Agenda):

- `agenda-sm` als Alias zu `compact`
- `agenda-lg` als Alias zu `roomy`

Reveal (Figure/Spacing):

- `is-sm`, `is-ssm`, `is-lg` als Alias zu den bestehenden Figure-Groessen
- `spacer is-sm`, `spacer is-lg` als Alias zu `spacer-sm`, `spacer-lg`

Callouts (Blog + Reveal):

- `tip` als Alias zu `tipp`
- `info` als Alias zu `note`
- `warn`/`warning` als Alias zu `important`

### 7.2 Copy-Paste: Blog (Agenda)

```markdown
<div class="agenda agenda-sm">

| Phase | Inhalt | Ziel | Zeit |
|---|---|---|---|
| 1 | Einstieg | Orientierung | 5<br>Min |
| 2 | Arbeitsphase | Vertiefung | 25<br>Min |

</div>
```

```markdown
<div class="agenda agenda-lg">

| Phase | Inhalt | Ziel | Zeit |
|---|---|---|---|
| 1 | Einstieg | Orientierung | 5<br>Min |
| 2 | Arbeitsphase | Vertiefung | 25<br>Min |

</div>
```

### 7.3 Copy-Paste: Reveal (Figure + Spacer)

```markdown
<figure class="figure-frame is-sm">
  <img src="/iWIP/bilder/beispiel.png" alt="Kurzbeschreibung">
</figure>

<div class="spacer is-sm"></div>
```

```markdown
<figure class="figure-frame is-lg">
  <img src="/iWIP/bilder/beispiel.png" alt="Kurzbeschreibung">
</figure>

<div class="spacer is-lg"></div>
```

### 7.4 Copy-Paste: Callouts (einheitliche Namen)

Blog-Callout (Markdown):

```markdown
> [!TIPP]
> Didaktischer Hinweis.

> [!IMPORTANT]
> Kritischer Hinweis.
```

Reveal-Callout (Shortcode):

```markdown
{{< callout type="tip" >}}Kernaussage{{< /callout >}}
{{< callout type="info" >}}Ergaenzung{{< /callout >}}
{{< callout type="warning" >}}Stolperstelle{{< /callout >}}
```

### 7.5 Schrittweise Konsistenzpruefung (empfohlen)

1. Inventar: nur Klassen/IDs erfassen und Dubletten markieren.
2. Alias-Stufe: zusaetzliche Namen (`sm/lg/info/warning`) einfuehren, ohne alte Namen zu brechen.
3. Vorlagen-Stufe: nur Klassen verwenden, die im CSS wirklich existieren.
4. Cleanup-Stufe: doppelte Regelbloecke zusammenziehen, Reihenfolge klar nach Owner-Datei.
5. Migrations-Stufe: alte Namen optional in Content schrittweise auf die neuen Alias-Namen umstellen.

### 7.6 Aufraeumen ohne Werteaenderung

Sinnvoll:

- doppelte Definitionen zusammenziehen (z. B. identische Rahmen-/QR-Regeln),
- uneinheitliche Benennung vereinheitlichen (z. B. `tipp`/`tip`),
- Altmuster bei Dark-Mode (`body.dark` vs `[data-theme="dark"]`) als geplante Migration markieren.

Nicht in dieser Stufe:

- keine Farb-/Spacing-Werte aendern,
- keine visuelle Umgestaltung,
- keine Cross-Owner-Verschiebung zwischen Blog- und Reveal-CSS.

### 7.7 Youtube Videos einbetten

{{< rawhtml >}}
<iframe
  class="video-embed"
  width="700"
  height="394"
  src="https://www.youtube-nocookie.com/embed/1DlSMQr4D6g"
  title="Wirksam Feedback geben"
  loading="lazy"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen>
</iframe>
{{< /rawhtml >}}
<p class="bild-quelle" style="margin-top:-3px;">
Quelle: <a href="https://www.youtube.com/watch?v=1DlSMQr4D6g" target="_blank" rel="noopener">
YouTube: Die Feedbackformel WWW – Mit WWW erfolgreich Feedback geben
</a>
</p>