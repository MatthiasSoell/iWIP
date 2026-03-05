# Repository Architecture – SciBlog iWIP

Version: 1.0.0  
Scope: Gesamte Projektstruktur des SciBlog iWIP (Blog + Präsentationen)  
Status: verbindliche Projekt-Governance

---

## 1. Ziel der Dokumentation

Diese Datei beschreibt die **technische Architektur des GitHub-Repositories** des SciBlog iWIP.  
Sie dient als Orientierung für:

- Maintainer
- Co-Autor:innen
- zukünftige Weiterentwicklungen

Ziel ist eine **klare, stabile und nachvollziehbare Struktur**, die langfristig wartbar bleibt.

---

## 2. Systemübersicht

Der SciBlog iWIP basiert auf folgenden Kerntechnologien:

| Ebene | Technologie | Zweck |
|---|---|---|
| Versionsverwaltung | Git / GitHub | Entwicklung & Kollaboration |
| Hosting | GitHub Pages | Veröffentlichung |
| Static Site Generator | Hugo | Generierung statischer Seiten |
| Blog-Theme | PaperMod | Layout und Blogstruktur |
| Präsentationen | reveal-hugo / reveal.js | Präsentationsmodus |
| Styles | Custom CSS | Design und UI-Komponenten |

---

## 3. Architekturdiagramm

```mermaid
flowchart TD
  A[GitHub Repository iWIP] --> B[GitHub Actions Build]
  B --> C[Hugo Build]
  C --> D[public/ (Build Output)]
  D --> E[GitHub Pages Deploy]

  subgraph CONTENT[Inhalte (content/)]
    F1[blog/ … PaperMod HTML] 
    F2[praesentation/ … Reveal Output]
    F3[impressum/ datenschutz/ hinweise/ …]
  end

  subgraph STYLING[Styles]
    S1[assets/css/extended/<br/>00_design_tokens.css<br/>10_custom.css<br/>20_custom_callouts.css]
    S2[static/css/custom_reveal.css]
  end

  subgraph THEMES[Themes / Modules]
    T1[PaperMod (Hugo Module)]
    T2[reveal-hugo (Hugo Module)]
  end

  C --> CONTENT
  C --> THEMES
  C --> STYLING

  F1 -->|nutzt| T1
  F2 -->|nutzt| T2
  F1 -->|lädt via Hugo Pipes| S1
  F2 -->|lädt direkt| S2
```

---

## 4. Repository-Struktur

Die zentrale Projektstruktur (vereinfacht):

```text
iWIP/
│
├─ content/                # Markdown-Inhalte (Blog + Präsentationen)
│  ├─ blog/                # Blog-Bereiche (PaperMod)
│  │  ├─ oer/
│  │  ├─ widi/
│  │  └─ doku/
│  ├─ praesentation/     # Präsentationsbereiche (Reveal)
│  │  ├─ oer/
│  │  └─ widi/
│  ├─ impressum/
│  ├─ datenschutz/
│  └─ hinweise/
│
├─ assets/                 # Hugo Asset Pipeline (Hugo Pipes)
│  └─ css/
│     └─ extended/
│        ├─ 00_design_tokens.css
│        ├─ 10_custom.css
│        └─ 20_custom_callouts.css
│
├─ static/                 # Statische Dateien (ohne Hugo-Verarbeitung)
│  ├─ css/
│  │   └─ custom_reveal.css
│  ├─ bilder/
│  └─ favicon.ico
│
├─ layouts/                # Hugo Layout-Anpassungen / Overrides
│
├─ project_governance/                   # Projekt-Dokumentation (Governance)
│  ├─ css_architecture.md
│  ├─ ai_copilot_instructions.md
│  ├─ content_emoji_policy.md
│  └─ repo_architecture.md
│
├─ config.toml             # zentrale Hugo-Konfiguration
│
└─ .github/
   └─ workflows/           # GitHub Actions Deployment
```

---

## 5. Content-Struktur (Hauptordner)

Alle Inhalte liegen unter:

```text
content/
```

### 5.1 Blog

```text
content/blog/
```
Zweck: Blogartikel (PaperMod), inkl. OER-Seiten und technischer Dokumentation.

### 5.2 Präsentationen

```text
content/praesentation/
```
Zweck: Präsentationsansichten (Reveal-Hugo / reveal.js).  
Diese sind **bewusst getrennt** vom Blog: ein Wechsel erfolgt z. B. über einen Button-Link vom Blog zur Präsentation.

### 5.3 Weitere Site-Pages

```text
content/impressum/
content/datenschutz/
content/hinweise/
```
Zweck: rechtliche und organisatorische Seiten.

---

## 6. CSS-Architektur (Kurzfassung)

Das Styling folgt einer klaren, modularen Struktur (Blog):

| Datei | Zweck |
|---|---|
| `assets/css/extended/00_design_tokens.css` | zentrale Designvariablen |
| `assets/css/extended/10_custom.css` | Blog-Komponenten & globale Features (ohne Callouts) |
| `assets/css/extended/20_custom_callouts.css` | Callout-System im Blog |

Reveal-Präsentationen nutzen ein eigenes Stylesheet:

```text
static/css/custom_reveal.css
```

Details sind dokumentiert in:

- `project_governance/css_architecture.md`

---

## 7. Präsentationssystem (Reveal)

Der Blog nutzt zusätzlich **reveal-hugo**, um Inhalte als Präsentation zu rendern.

Konfiguration erfolgt in:

- `config.toml` (OutputFormat `Reveal` und `params.reveal_hugo.custom_theme`)

Custom Styling liegt bewusst in:

- `static/css/custom_reveal.css`

Begründung: Reveal-Hugo bindet das Theme zuverlässig über `custom_theme` aus `static/` ein.

---

## 8. Modulverwaltung (Hugo Modules)

Themes werden über **Hugo Modules** geladen:

- PaperMod
- reveal-hugo

Definition in:

- `config.toml` → `[module.imports]`

Vorteile:

- robuste Theme-Einbindung ohne Git-Submodules
- einfachere Updates
- bessere Teamtauglichkeit

---

## 9. Deployment

Die Veröffentlichung erfolgt über:

- GitHub Pages
- GitHub Actions (`.github/workflows/`)

Workflow:

```text
Commit → GitHub Action → Hugo Build → Deploy → GitHub Pages
```

---

## 10. Kollaboration

Beiträge können über **Pull Requests** eingebracht werden.

Typischer Workflow:

```text
Fork → Änderung → Pull Request → Review → Merge
```

---

## 11. Architekturprinzipien

1. **Markdown-first** (Inhalte bleiben in Markdown)
2. **statische Webseiten** (DSGVO-freundlich, schnell, archivfähig)
3. **minimale externe Abhängigkeiten**
4. **strikte Trennung Blog ↔ Präsentation**
5. **Owner-Prinzip bei CSS-Dateien**
6. **Dokumentation ist Teil der Architektur**

---

## 12. Wartungsprinzip

Änderungen an der Infrastruktur erfolgen nur, wenn:

- Wartbarkeit verbessert wird
- neue Funktionen benötigt werden
- Sicherheits-/Kompatibilitätsupdates notwendig sind

Stabile Lösungen werden **nicht ohne Grund refaktoriert**.

---

## 13. Projektziel

Der SciBlog iWIP soll langfristig als:

- offene Infrastruktur für Wissenschaftskommunikation
- OER-Plattform 🎓🌍🔓
- Lehr- und Lernumgebung

genutzt werden – mit Fokus auf Stabilität, Transparenz und Offenheit.