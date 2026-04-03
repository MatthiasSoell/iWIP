# SciBlog iWIP – Offene Publikationsplattform für Wirtschaftsdidaktik

SciBlog iWIP ist eine offene Publikationsplattform für wirtschaftsdidaktische Lehr-Lern- und Forschungs-Materialien.  
Das Projekt verbindet Blog, Präsentationen und OER-Materialien in einer transparent dokumentierten technischen Infrastruktur.

**English:**  
SciBlog iWIP is an open publishing platform for teaching and research materials in business education and training.  
The project combines a blog, presentations, and OER resources within a transparently documented technical infrastructure.

---

## 🌐 Website

Der veröffentlichte Blog ist hier erreichbar:

[https://matthiassoell.github.io/iWIP/](https://matthiassoell.github.io/iWIP/)

---

## 🎓 Ziel des Projekts

Der SciBlog iWIP verfolgt das Ziel, Lehr-Lern- und Forschungs-Materialien der Wirtschaftsdidaktik offen zugänglich zu machen und kontinuierlich weiterzuentwickeln.

Der Blog dient insbesondere dazu:

- Lehrmaterialien und Forschungsmaterialien als **Open Educational Resources (OER)** zu veröffentlichen  
- **Lehrveranstaltungen transparent zu dokumentieren**  
- Präsentationen direkt aus Markdown zu generieren  
- eine **offene, nachvollziehbare Infrastruktur** für wissenschaftliche Lehre und Forschung bereitzustellen

---

## ⚙️ Technische Grundlage

Der SciBlog iWIP basiert auf einer bewusst einfachen, offenen Web-Infrastruktur.

### Technologien

- **Hugo** – Static Site Generator  
- **PaperMod** – Blog-Theme  
- **reveal-hugo / reveal.js** – Präsentationssystem  
- **GitHub Pages** – Hosting  
- **GitHub Actions** – automatisiertes Deployment  

Alle Inhalte werden in **Markdown** geschrieben und als **statische Webseiten** generiert.

---

## 🧱 Projektstruktur

Die wichtigsten Bereiche des Repositories:

```text
content/
├─ blog/               → Blogartikel und OER-Materialien
├─ praesentation/      → Präsentationen (Reveal.js)
├─ impressum/
├─ datenschutz/
└─ hinweise/

assets/css/extended/
├─ 00_design_tokens.css
├─ 10_custom.css
└─ 20_custom_callouts.css

static/css/
└─ custom_reveal.css
```

---

## 🎨 CSS-Architektur

Das Projekt nutzt eine klar definierte CSS-Architektur:

```text
Design Tokens
      ↓
Blog Komponenten
      ↓
Callout-Komponenten
```

Dateien:

```text
00_design_tokens.css
10_custom.css
20_custom_callouts.css
custom_reveal.css
```

Reveal-CSS und Blog-CSS sind strikt getrennt.

Details sind dokumentiert in:

```text
project_governance/css_architecture.md
```

---

## 📚 Dokumentation

Die technische Architektur des Projekts ist zusammen mit mit Entwicklungsregeln im Ordner `project_governance/` transparent dokumentiert.

Wichtige Dokumente:

```text
project_governance/
├─ repo_architecture.md
├─ css_architecture.md
├─ development_workflow.md
├─ content_emoji_policy.md
├─ ai_project_context.md
└─ ai_copilot_instructions.md
```

Diese Dokumente beschreiben:

- Repository-Struktur  
- CSS-System  
- Content-Konventionen (Emoji-Policy)
- AI-Regeln für Codeänderungen  
- technischen Projektkontext

---

## 🤖 KI-Unterstützung

Bei der technischen Entwicklung des Projekts werden KI-Werkzeuge eingesetzt, u. a.:

- GitHub Copilot
- ChatGPT

Die Regeln für AI-gestützte Änderungen sind dokumentiert in:

```text
project_governance/ai_copilot_instructions.md
```

---

## 🤖 Didaktischer Planungsagent

Der SciBlog iWIP nutzt einen KI-Agenten (Version 1.0.0) zur Unterstützung der didaktischen Planung und Veröffentlichung von Lehr-Lern-Arrangements als OER.

Der Agent arbeitet dialogisch in **fünf Phasen** und verbindet Planung, Ausarbeitung und Publikation in einem konsistenten Workflow.

### Kerneigenschaften

- **44 Core Rules** regeln Modus, Qualität und Artefakterstellung verbindlich.
- **Didaktisches Qualitätsmodell (DQM)** mit sechs Leitdimensionen und kompakter Prüfmatrix.
- **Drei didaktische Profile**: (A) Integrativ-kompetenzorientiert (Default), (B) Handlungsorientiert-konstruktivistisch, (C) Instruktional-kognitivistisch.
- **Gate-basierter Rigor**: Während der Entwurfsarbeit gelten Minimal-Checks; bei Finalisierung (`BLOG FINAL`, `REVEAL GO`) greifen automatisch alle Hardchecks, Guardrails und Reportings.
- **Blog-Wissensbasis**: Kuratierter Index veröffentlichter Blogartikel für thematische Anschlussfähigkeit.
- **Ko-kreative Textarbeit**: Kapitelweise Zusammenarbeit (Nutzerinput → publizistischer Fließtext).

### Fünf-Phasen-Workflow

| Phase | Beschreibung |
|---|---|
| P1 – Klären | Kontext, Profil, Wissensbasis-Bezüge |
| P2 – Strukturieren | Didaktische Struktur, Kohärenzcheck |
| P3 – Entwerfen | `.index.md` anlegen, Querverweise markieren |
| P4 – Ko-kreativ ausarbeiten | Kapitelweise Fließtextentwicklung |
| P5 – Finalisieren | Hardchecks, DQM-Prüfbericht, Reporting |

### Agenten-Dateien

```text
ai_agents/
├─ master_agent.md                → Agentendefinition (44 Rules, Workflow, DoD)
├─ didaktisches_qualitaetsmodell.md → DQM (Dimensionen, Profile, Prüfmatrix)
├─ blog_wissensbasis.md           → Kuratierter Artikelindex
└─ templates/
   ├─ blog_template.md            → Pflichtstruktur Blogartikel
   └─ reveal_template.md          → Pflichtstruktur Reveal-Präsentation

prompts/
├─ create.md                      → /create – Neue Planung starten
├─ check.md                       → /check – Didaktischer Qualitätscheck
└─ literatur.md                   → /literatur – Literaturformatierung
```

---

## ⚡ Quickstart

1. `PLAN START: Thema | Zielgruppe | Zeit`
2. Profil wählen (A/B/C) oder Default (A) übernehmen
3. Entwurf dialogisch entwickeln (`.index.md`)
4. Blog finalisieren (`BLOG FINAL`)
5. Präsentation erzeugen (`REVEAL GO`)

---

## 🧠 Grundlogik

Der Agent arbeitet strikt sequenziell in fünf Phasen (P1–P5):

1. Kontext klären und Profil festlegen
2. Didaktisch strukturieren und Kohärenz prüfen
3. Blogentwurf entwickeln (`.index.md`)
4. Kapitelweise ko-kreativ ausarbeiten
5. Blog finalisieren (`index.md`) und Reveal ableiten

Die `.index.md` dient als nicht-rendernder Arbeitsstand:

- wird iterativ bearbeitet
- enthält den aktuellen Entwicklungsstand
- wird bei `BLOG FINAL` in den finalen Blogartikel (`index.md`) überführt
- ist nicht öffentlich sichtbar (`_build.render: false`, `_build.list: false`)

Wichtig:

- Der Blog ist das **Primärartefakt**
- Die Präsentation wird **immer daraus abgeleitet**
- Keine parallele Erstellung von Blog und Reveal

---

## ⚙️ Steuerung

### Signale

- `PLAN START: Thema | Zielgruppe | Zeit`
- `Kapitel <N> freigegeben`
- `BLOG FINAL`
- `REVEAL GO`

### Gate-basierter Rigor

Es gibt keine separaten Arbeitsmodi. Stattdessen:

- **Entwurfsphase** (`.index.md`): Drei Minimal-Checks (keine erfundenen Quellen, Pflicht-Frontmatter, Reihenfolge Blog vor Reveal).
- **Finalisierung** (`BLOG FINAL`, `REVEAL GO`): Alle Hardchecks, Guardrails und Reportings greifen automatisch.

### Konsistenzregeln

- Reveal-Dateien enthalten keine OER-Metadaten; OER-Metadaten stehen ausschließlich im Blog.
- Reveal-Erzeugung und -Finalisierung erfolgen ausschließlich nach dem Signal `REVEAL GO`.
- Die didaktische Bewertung folgt dem DQM als einzigem didaktischen Referenzmodell, inklusive profilabhängiger Gewichtung (A/B/C).

Verbindliche Governance und Tests:

- `project_governance/agent_contract.md`

---

## 🔁 Snapshot-Logik

Bei `REVEAL GO` wird automatisch erzeugt:

```text
reveal_snapshot.md
```

Eigenschaften:

- nicht-rendernd (`_build.render: false`, `_build.list: false`)
- gleicher fachlicher Stand zum Zeitpunkt der Finalisierung
- dient als Momentaufnahme

Für Blogartikel wird kein Snapshot erzeugt. Stattdessen dient die `.index.md` als Arbeitsstand und Referenz für die Reflexion.

Wichtig:

- Snapshots sind **nicht-operativ**
- keine Weiterverarbeitung oder Ableitung daraus
- Reveal wird immer aus dem finalen Blog (`index.md`) erzeugt

---

## 💡 Optionale Reflexion

Der Agent kann optional Reflexionen anstoßen:

Nach `BLOG FINAL`:

- Vergleich zwischen bearbeiteter `.index.md` und finalem `index.md`
- Einordnung von Änderungen (Korrekturen, Ergänzungen, Anpassungen)
- Ableitung von 2–4 Reflexionsfragen oder Hypothesen

Nach `REVEAL GO`:

- Vergleich zwischen `reveal_snapshot.md` und finalem Reveal-Stand
- Ableitung von 2–4 Reflexionsfragen oder Hypothesen

→ dient ausschließlich der Weiterentwicklung  
→ keine automatischen Regeländerungen

---

### 🎯 Ziel

Der Agent unterstützt dabei:

- didaktisch kohärente Lehrveranstaltungen zu planen  
- Inhalte effizient auszuarbeiten  
- Blogartikel als OER zu publizieren  
- Präsentationen konsistent daraus abzuleiten  

### 🔄 Agent-Workflow (Übersicht)

```text
PLAN START
    ↓
.index.md (Arbeitsstand, nicht öffentlich)
    ↓
Bearbeitung & Ergänzung (dialogisch)
    ↓
BLOG FINAL
    ↓
index.md (finaler Blogartikel)
    ↓
REVEAL GO
    ↓
_index.md (vom Agent erzeugte Reveal-Version)
    + reveal_snapshot.md (Momentaufnahme der ersten Reveal-Version)
    ↓
Bearbeitung & Feinschliff an _index.md
    ↓
finale _index.md
```

- Nach BLOG FINAL: 
      Vergleich .index.md ↔ index.md

- Nach Reveal-Feinschliff:
    Vergleich `reveal_snapshot.md` ↔ finale `_index.md`

---

## 📖 Lizenz

Die Inhalte des Blogs werden – sofern nicht anders angegeben – unter einer **Creative Commons Lizenz (CC BY-SA 4.0)** veröffentlicht.

[https://creativecommons.org/licenses/by-sa/4.0/](https://creativecommons.org/licenses/by-sa/4.0/)

---

## 👤 Autor

**Prof. Dr. Matthias Söll**  
Universität Rostock  
Institut für Wirtschaftspädagogik

[https://matthiassoell.github.io/iWIP/](https://matthiassoell.github.io/iWIP/)

---

## ℹ️ Hinweis

Dieses Repository dient in erster Linie der **Dokumentation der technischen Infrastruktur** des SciBlog iWIP.  
Die Inhalte werden über den Blog selbst veröffentlicht.
