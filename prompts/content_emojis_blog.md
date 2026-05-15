# CONTENT-EMOJIS IN BLOGARTIKELN

## Aufgabe
Bitte zeichne in Blogartikeln des SciBlog iWIP gezielt Inhalts-Emojis mit
`<span class="content-emoji">…</span>`
aus, damit sie über den bestehenden Emoji-Toggle (😄 / ⚪) ein- und ausgeblendet werden können.

## Bearbeitungsbereich
- Bearbeite ausschließlich die aktuell im Workflow erzeugte Blogdatei index.md

Die Bearbeitung beginnt unmittelbar nach:
`{{< oer-meta >}}`

Die Bearbeitung endet vor:
`<div id="literatur"></div>`

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
- `hugo --minify`
- mindestens einen Blogartikel testen
- prüfen, dass nur Content-Emojis verschwinden
