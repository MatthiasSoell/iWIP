
# CSS Architecture – SciBlog iWIP

Version: 1.0.0
Scope: Blog (PaperMod) + Reveal (reveal-hugo)
Status: verbindliche Projektregel

---

# 1. CSS Architecture Diagram

```mermaid
flowchart TD

A[CSS Entry Point (Blog)<br>Hugo Pipes: assets/css/extended] --> T[00_design_tokens.css<br>Tokens only]
T --> C[10_custom.css<br>Blog components + features]
C --> O[20_custom_callouts.css<br>Blog callouts only]

R[Reveal CSS (Presentation)<br>static/css/custom_reveal.css] --> RV[.reveal / reveal-hugo only]

subgraph RULES[Governance Rules]
  X1[No hardcoded colors outside tokens]
  X2[Owner principle: one file owns a selector]
  X3[No Reveal selectors in Blog CSS]
  X4[No Blog selectors in Reveal CSS]
end

T -.enforces.-> X1
C -.enforces.-> X2
O -.enforces.-> X2
R -.enforces.-> X3
R -.enforces.-> X4

```

**Legend**
- Solid arrows = load order / dependency
- Dashed arrows = governance constraints

Das Diagramm zeigt die Lade-Reihenfolge der Blog-CSS-Dateien sowie die
strikte Trennung zwischen Blog-CSS und Reveal-Präsentations-CSS.

---

# 2. Grundprinzipien

1. **Markdown-first, CSS minimal**
2. **Design Tokens sind die einzige Quelle für Farben, Abstände, Radius im Blog**
3. **Reveal verwendet für Farben eigene Variablen in custom_reveal.css**
4. **Keine Doppeldefinitionen von Selektoren**
5. **Kein `!important` ohne dokumentierten Grund**
6. **Reveal strikt vom Blog getrennt**
7. **Jede CSS-Datei hat einen klar definierten Owner-Bereich**
8. **Keine spontane Regelergänzung ohne Einordnung in diese Struktur**

Ziel: Wartbarkeit, Verständlichkeit, Release-Stabilität.

---

# 3. Dateistruktur & Verantwortlichkeiten

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

# 4. Kaskadenreihenfolge (verbindlich)

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

# 5. Umgang mit `!important`

`!important` ist nur erlaubt, wenn:

- Drittanbieter-Styles überschrieben werden müssen
- Inline-Styles eines Themes nicht anders greifbar sind

Jede Nutzung wird kommentiert:

```css
/* !important required because PaperMod inline style overrides link color */
```

Ziel: `!important` als Ausnahme, nicht als Stilmittel.

---

# 6. Selektor-Scope-Regel

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

# 7. Refactoring-Regel

Wenn ein Selektor in zwei Dateien auftaucht:

→ sofort konsolidieren
→ nur eine Datei darf Owner sein
→ Doppeldefinitionen sind nicht erlaubt

---

# 8. 1.0.0 Stabilitätsregeln

Vor Release:

- keine doppelten Selektoren
- keine ungenutzten Tokens
- keine Reveal-Regeln im Blog-CSS
- keine toten Klassen
- keine nicht kommentierten `!important`
- kein extern geladener CSS-Code ohne Dokumentation

---

# 9. Erweiterungsregel

Neue CSS-Regeln werden:

1. zunächst einer Owner-Datei zugeordnet
2. mit Tokens umgesetzt (keine Hardcoded-Farben)
3. getestet in:
   - Blogpost
   - OER-Seite
   - Präsentation (falls relevant)

Spontanes Einfügen „irgendwo dazwischen“ ist nicht zulässig.

---

# 10. Projektziel

Die CSS-Architektur soll:

- verständlich bleiben
- ohne Dokumentation lesbar sein
- manuell wartbar sein
- ohne externe Tools debugbar sein
- langfristig stabil bleiben

Sie ist Teil der Governance des SciBlog iWIP.

---

# 11. AI-Unterstützte Codebearbeitung

Für Änderungen mit KI-Tools (z. B. GitHub Copilot oder ChatGPT)
gelten zusätzliche Regeln.

Diese sind dokumentiert in:

ai_copilot_instructions.md

Die dort definierten Prinzipien (Modify-first, Framework-first,
No-hack) sind verbindlich für alle automatisierten Codevorschläge.