# CONTENT-EMOJIS IN BLOGARTIKELN

## Aufgabe
Bitte zeichne in Blogartikeln des SciBlog iWIP gezielt Inhalts-Emojis mit
`<span class="content-emoji">…</span>`
aus, damit sie über den bestehenden Emoji-Toggle (😄 / ⚪) ein- und ausgeblendet werden können.

## Bearbeitungsbereich
Bearbeite ausschließlich die aktuell im Workflow erzeugte Blogdatei `index.md`. Keine anderen Blogdateien ändern.

Die Bearbeitung beginnt unmittelbar nach:
`{{< oer-meta >}}`

Die Bearbeitung endet vor:
`<span id="literatur"></span>`

## Fail-closed-Vorbedingung

Vor jeder Mutation muss in der aktuell bearbeiteten `index.md` geprueft werden,
dass `{{< oer-meta >}}` und der kanonische Literaturanker jeweils genau einmal
vorkommen und der Anker nach dem OER-Meta-Shortcode liegt. Nur der Inhalt
zwischen diesen beiden eindeutigen Grenzen darf bearbeitet werden.

Fehlt der kanonische Literaturanker, kommt er mehrfach vor oder sind die
Grenzen nicht eindeutig bestimmbar, brich den Schritt vor jeder Mutation mit
einem klaren `BLOCKER` ab. Arbeite insbesondere nicht bis zum Dateiende weiter,
veraendere den Literaturbereich nicht und repariere den Fehler nicht
stillschweigend ausserhalb des aktuell bearbeiteten Artefakts.

## Nicht verändern
- Front Matter
- `.top-toggle`
- UI-Icons (📑, 📥, 🖥️, 😄, ⚪, ⓘ)
- `{{< oer-meta >}}`
- Literaturbereich
- Bilder und Shortcodes

## Sonderregel: Nummerierungs-Emojis
`1️⃣ 2️⃣ 3️⃣ ... 🔟` durch `1. 2. 3. ...` ersetzen.

## Qualitätssicherung
- eindeutige Bereichsgrenzen vor der Mutation bestaetigen
- pruefen, dass nur der Bereich nach `{{< oer-meta >}}` und vor
  `<span id="literatur"></span>` veraendert wurde
- pruefen, dass der Literaturbereich bytegleich blieb
- keinen Build starten; der einzige abschliessende Build gehoert `BLOG FINAL`
