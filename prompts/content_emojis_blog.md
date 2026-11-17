# CONTENT-EMOJIS IN BLOGARTIKELN

## Aufgabe
Bitte zeichne in Blogartikeln des SciBlog iWIP gezielt Inhalts-Emojis mit
`<span class="content-emoji">…</span>`
aus, damit sie über den bestehenden Emoji-Toggle (😄 / ⚪) ein- und ausgeblendet werden können.

## Bearbeitungsbereich
Bearbeite ausschließlich die aktuell im Workflow erzeugte Blogdatei `index.md`. Keine anderen Blogdateien ändern.

Die Bearbeitung beginnt unmittelbar nach:
`{{< oer-meta >}}`

Bei vorhandenem Literaturabschnitt endet die Bearbeitung vor:
`<span id="literatur"></span>`

Nur wenn gemaess Blog-Template und buildfreier Vorpruefung ein Literaturabschnitt
zulaessigerweise nicht vorhanden ist, endet die Bearbeitung am Dateiende.

## Fail-closed-Vorbedingung

Vor jeder Mutation muss `{{< oer-meta >}}` in der aktuell bearbeiteten
`index.md` genau einmal als Einstiegs-Shortcode nach dem Frontmatter stehen.
Danach ist genau einer der folgenden Faelle eindeutig zu bestaetigen:

1. **Mit Literaturabschnitt:** Genau ein kanonischer Literaturanker liegt nach
   dem OER-Meta-Shortcode unmittelbar vor dem eindeutigen Literaturabschnitt.
   Nur der Inhalt zwischen Shortcode und Anker darf bearbeitet werden.
2. **Ohne Literaturabschnitt:** Dessen Entfallen ist gemaess Blog-Template
   zulaessig und durch die buildfreie Vorpruefung bestaetigt. Es existieren
   weder Literaturabschnitt noch Literaturanker (auch keine aelteren Formen)
   oder lokale Verweise auf einen fehlenden Literaturbereich, einschliesslich
   Markdown-, HTML- und Referenzlinks sowie aelterer Fragmentziele.
   Nur der Inhalt nach dem Shortcode bis Dateiende darf bearbeitet werden.

Die Bestimmung des Literaturbereichs erfolgt nach seiner Funktion und seinem
Inhalt, nicht allein nach einem bestimmten Ueberschriftentext.
Ein fehlender Anker allein erlaubt niemals den Wechsel zum Dateiende.
Fehlender oder mehrfacher Einstiegs-Shortcode, fehlender Anker bei vorhandenem
Literaturabschnitt, mehrfache, verwaiste oder falsch positionierte Anker,
verwaiste Literaturverweise sowie unklare oder widerspruechliche Bereichsgrenzen
sind vor jeder Mutation mit einem klaren `BLOCKER` abzubrechen.
Veraendere den Literaturbereich nicht und repariere Fehler nicht
stillschweigend ausserhalb des aktuell bearbeiteten Artefakts. Erzeuge keine
Dummy-Anker oder unsichtbaren Ersatzabschnitte.

## Nicht verändern
- Front Matter
- `.top-toggle`
- UI-Icons (📑, 📥, 🖥️, 😄, ⚪, ⓘ)
- `{{< oer-meta >}}`
- Literaturbereich
- Bilder und Shortcodes
- URLs, IDs und sonstige technische Steuersyntax

## Sonderregel: Nummerierungs-Emojis
`1️⃣ 2️⃣ 3️⃣ ... 🔟` durch `1. 2. 3. ...` ersetzen.

## Qualitätssicherung
- eindeutige Bereichsgrenzen vor der Mutation bestaetigen
- pruefen, dass nur der bestaetigte Bereich nach `{{< oer-meta >}}` bis vor
  den Literaturanker beziehungsweise im zulaessigen Fall bis Dateiende
  veraendert wurde und alle geschuetzten Bestandteile bytegleich blieben
- bei vorhandenem Literaturabschnitt pruefen, dass er einschliesslich Anker
  und gesamtem nachfolgendem Dateiteil bytegleich blieb
- vorhandene `content-emoji`-Spans erhalten; keine verschachtelten Spans
  erzeugen und bei erneutem Lauf keine weiteren Auszeichnungen hinzufuegen
- keinen Build starten; der einzige abschliessende Build gehoert `BLOG FINAL`
