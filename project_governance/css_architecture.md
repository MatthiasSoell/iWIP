
# CSS Architecture – SciBlog iWIP

Version: 1.0.0
Scope: Blog (PaperMod) + Reveal (reveal-hugo)
Status: verbindliche Projektregel

---

# 1. Grundprinzipien

1. **Markdown-first, CSS minimal**
2. **Design Tokens sind die einzige Quelle für Farben, Abstände, Radius**
3. **Keine Doppeldefinitionen von Selektoren**
4. **Kein `!important` ohne dokumentierten Grund**
5. **Reveal strikt vom Blog getrennt**
6. **Jede CSS-Datei hat einen klar definierten Owner-Bereich**
7. **Keine spontane Regelergänzung ohne Einordnung in diese Struktur**

Ziel: Wartbarkeit, Verständlichkeit, Release-Stabilität.

---

# 2. Dateistruktur & Verantwortlichkeiten

## 00_design_tokens.css
**Owner:** Design-System

Enthält ausschließlich:

- `:root` Variablen
- Dark-/Light-Mode-Varianten
- Farbdefinitionen
- Radius-, Shadow-, Spacing-Variablen
- typografische Basisvariablen (z. B. Schriftfamilien, **keine Schriftgrößen**)

Enthält NICHT:

- Layout-Regeln
- Komponenten
- Blockquote- oder Callout-Styles
- `.reveal`-Regeln
- globale Selektoren wie `body`, `a`, `blockquote`

Zweck:
Zentrale visuelle Sprache des gesamten Projekts.

---

## 10_custom.css
**Owner:** Globales Layout & Komponenten (außer Callouts)

Enthält:

- Link-Styles
- Typografie-Anpassungen
- Footer
- OER-Metabox
- Overlay / UI-Elemente
- Tabellen & Agenda
- Buttons
- allgemeine Layout-Korrekturen

Enthält NICHT:

- Callouts / Blockquote-Spezialdesign
- `.reveal`-Regeln
- Design Tokens
- doppelte Definitionen aus anderen Dateien

Zweck:
Site-weite Strukturen und wiederkehrende Komponenten.

---

## 20_custom_callouts.css
**Owner:** Callouts & Zitat-Logik

Enthält:

- `[!quote]`
- `[!info]`
- `[!tip]`
- Blockquote-Design
- Callout-spezifische Typografie
- Callout-Hintergründe & Rahmen

Enthält NICHT:

- globale Typografie
- Layout-Regeln
- `.reveal`-Selektoren
- Design Tokens

Zweck:
Alle semantischen Hervorhebungen sind hier zentralisiert.

---

## static/css/custom_reveal.css
**Owner:** Präsentationsdesign

Enthält:

- `.reveal`-Selektoren
- Folien-Layout
- Präsentations-Typografie
- Reveal-spezifische Komponenten

Enthält NICHT:

- Blog-Layout
- OER-Metabox
- Callouts außerhalb von Reveal
- globale Typografie-Regeln

Zweck:
Strikte Trennung zwischen Blog und Präsentation.

---

# 3. Kaskadenreihenfolge (verbindlich)

Die Reihenfolge der Dateien im Ordner `assets/css/extended/` ist:

1. `00_design_tokens.css` – Designsystem
2. `10_custom.css` – globale Komponenten & Layout
3. `20_custom_callouts.css` – semantische Callouts

Reveal wird unabhängig davon geladen:

- `static/css/custom_reveal.css`

Regeln:

- Tokens stehen immer am Anfang der Cascade.
- Komponenten bauen auf Tokens auf.
- Callouts bauen auf Tokens und Komponenten auf.

---

# 4. Umgang mit `!important`

`!important` ist nur erlaubt, wenn:

- Drittanbieter-Styles überschrieben werden müssen
- Inline-Styles eines Themes nicht anders greifbar sind

Jede Nutzung wird kommentiert:

```css
/* !important required because PaperMod inline style overrides link color */
```

Ziel: `!important` als Ausnahme, nicht als Stilmittel.

---

# 5. Selektor-Scope-Regel

Selektoren müssen möglichst lokal sein.

Beispiele:

- `.reveal …` → nur Präsentation
- `.callout …` → nur Callouts
- `.footer …` → nur Footer-Komponente

Globale Selektoren wie:

- `body`
- `a`
- `blockquote`

dürfen nur in `10_custom.css` stehen.

Ziel:
Unbeabsichtigte CSS-Überschreibungen vermeiden.

---

# 6. Refactoring-Regel

Wenn ein Selektor in zwei Dateien auftaucht:

→ sofort konsolidieren
→ nur eine Datei darf Owner sein
→ Doppeldefinitionen sind nicht erlaubt

---

# 7. 1.0.0 Stabilitätsregeln

Vor Release:

- keine doppelten Selektoren
- keine ungenutzten Tokens
- keine Reveal-Regeln im Blog-CSS
- keine toten Klassen
- keine nicht kommentierten `!important`
- kein extern geladener CSS-Code ohne Dokumentation

---

# 8. Erweiterungsregel

Neue CSS-Regeln werden:

1. zunächst einer Owner-Datei zugeordnet
2. mit Tokens umgesetzt (keine Hardcoded-Farben)
3. getestet in:
   - Blogpost
   - OER-Seite
   - Präsentation (falls relevant)

Spontanes Einfügen „irgendwo dazwischen“ ist nicht zulässig.

---

# 9. Projektziel

Die CSS-Architektur soll:

- verständlich bleiben
- ohne Dokumentation lesbar sein
- manuell wartbar sein
- ohne externe Tools debugbar sein
- langfristig stabil bleiben

Sie ist Teil der Governance des SciBlog iWIP.