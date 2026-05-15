# CONTENT-EMOJIS IN REVEAL-PRÄSENTATIONEN

## Aufgabe
Bitte zeichne in Reveal-Präsentationen des SciBlog iWIP gezielt Inhalts-Emojis mit
`<span class="content-emoji">…</span>`
aus, damit sie über den bestehenden Emoji-Toggle (😄 / ⚪) ein- und ausgeblendet werden können.

## Bearbeitungsbereich
Bearbeite ausschließlich die aktuell im Workflow erzeugte Präsentationsdatei `_index.md`. Keine anderen Präsentationsdateien ändern.

## Front Matter zusätzlich prüfen
Bitte in den Feldern `emojis` und `veranstaltungstyp` enthaltene Emojis mit
`<span class="content-emoji">…</span>`
auszeichnen.

### Beispiel
```yaml
emojis: '<span class="content-emoji">🎓</span> <span class="content-emoji">🏛️</span> <span class="content-emoji">⚖️</span>'
veranstaltungstyp: '<span class="content-emoji">🎓</span> Vorlesung'
```

## Inhaltsbereich
Die Bearbeitung im Markdown beginnt erst nach:

```markdown
todos: []
---

{{< titleSlide >}}

---
```

## Nicht verändern
- andere Front-Matter-Felder
- `{{< titleSlide >}}`
- Toolbar-Icons (📥, 📄, 😄, ⚪, QR)
- Fußzeile, Bilder, Shortcodes

## Sonderregel: Nummerierungs-Emojis
`1️⃣ 2️⃣ 3️⃣ ... 🔟` durch `1. 2. 3. ...` ersetzen.

## Qualitätssicherung
- `hugo --minify`
- mindestens eine Präsentation testen
- prüfen, dass auch Emojis aus `emojis:` und `veranstaltungstyp:` ausgeblendet werden
