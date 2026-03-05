# AI Editing Instructions – Copilot / ChatGPT
SciBlog iWIP

Version: 1.1.0  
Status: verbindliche Projektregel  
Scope: technische Änderungen im Repo (CSS, Layout, Struktur)

AI agents: read `ai_project_context.md` first, then follow these rules.

Diese Regeln definieren, wie AI‑Agenten (z. B. GitHub Copilot, ChatGPT) Änderungen am Projekt durchführen sollen.

Ziel ist eine stabile, wartbare Architektur ohne unnötige technische Schulden.

---

# 1. Modify‑First Principle

Bestehende Regeln und Strukturen werden **zuerst angepasst**, bevor neue erstellt werden.

Neue Regeln dürfen nur entstehen, wenn:

- kein bestehender Selektor passt
- eine neue Komponente entsteht
- die Änderung sonst globale Nebenwirkungen hätte

AI soll:

- vorhandene CSS-Regeln erweitern
- vorhandene Hugo-Strukturen nutzen
- vorhandene Komponenten weiterverwenden

AI soll **nicht**:

- funktionierenden Code neu schreiben
- bestehende Strukturen ohne Grund refaktorisieren

Ziel: Minimierung von CSS‑Wachstum und technischem Ballast.

---

# 2. Framework‑First Principle

Vor jeder Custom‑Lösung prüft AI folgende Optionen:

1. Hugo Dokumentation
2. PaperMod Dokumentation
3. reveal‑hugo / reveal.js Dokumentation

Wenn eine Lösung möglich ist über:

- Theme Parameter
- vorhandene Klassen
- Framework‑Selektoren

→ wird diese Lösung bevorzugt.

Custom CSS ist **nur zweite Wahl**.

Ziel: geringere Wartungskosten und bessere Updatefähigkeit der Themes.

---

# 3. Architecture Ownership

Jede CSS‑Regel gehört in eine **Owner‑Datei**.

| Zweck | Datei |
|------|------|
| Design Tokens | assets/css/extended/00_design_tokens.css |
| Blog‑Komponenten | assets/css/extended/10_custom.css |
| Blog‑Callouts | assets/css/extended/20_custom_callouts.css |
| Präsentation (Reveal) | static/css/custom_reveal.css |

Regeln dürfen **nicht zwischen Dateien vermischt werden**.

Reveal‑CSS und Blog‑CSS bleiben strikt getrennt.

---

# 4. No‑Hack Policy

Folgende Lösungen sind zu vermeiden:

- unnötige `!important`
- künstlich erhöhte CSS‑Spezifität
- Selektor‑Verschachtelung > 3 Ebenen
- Hardcoded Farben:
  - Blog: keine Hardcoded Farben außerhalb 00_design_tokens.css
  - Reveal: Hardcoded Farben sind nur erlaubt als CSS-Variablenwerte in static/css/custom_reveal.css (z. B. im :root-Tokenblock). Keine Hardcodes in den Komponentenregeln.
- CSS‑Workarounds für Probleme, die über Theme‑Optionen lösbar sind

Wenn eine Ausnahme notwendig ist, wird sie kurz kommentiert:

```css
/* workaround: PaperMod inline style override */
```

Ziel: CSS bleibt langfristig wartbar.

---

# 5. Documentation Consistency Rule

Bei jeder strukturellen Änderung prüft AI:

Muss eine Dokumentation angepasst werden?

Relevante Dokumente:

- project_governance/css_architecture.md
- project_governance/repo_architecture.md
- project_governance/ai_copilot_instructions.md
- config.toml Kommentare
- content/blog/doku/doku_tech/index.md technische Blog‑Dokumentation

Wenn Architektur oder Struktur verändert wird:

→ Dokumentation im **gleichen Commit** aktualisieren.

Wenn eine Regel bewusst verletzt wird:

→ Ausnahme dokumentieren.

---

# 6. Change Test

Nach jeder Änderung soll ein kurzer Smoke‑Test erfolgen.

Blog prüfen:

- Light / Dark Toggle
- Footer Links und Icons
- OER‑Tooltip
- Help‑Overlay
- Callouts (tip / quote / important / note)

Reveal prüfen:

- Titlecard
- Buttons
- Diagramm‑Slide
- Endslide
- Präsentationsmodus

---

# Ziel dieser Regeln

Die AI‑Regeln stellen sicher, dass Änderungen:

- architekturtreu bleiben
- wartbar bleiben
- dokumentiert bleiben
- keine unnötige technische Komplexität erzeugen

Sie sind Teil der technischen Governance des SciBlog iWIP.