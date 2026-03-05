# SciBlog iWIP – Offene Publikationsplattform für Wirtschaftsdidaktik

SciBlog iWIP ist eine offene Publikationsplattform für wirtschaftsdidaktische Lehr-Lern- und Forschungs-Materialien.  
Das Projekt verbindet Blog, Präsentationen und OER-Materialien in einer transparent dokumentierten technischen Infrastruktur.

**English:**  
SciBlog iWIP is an open publishing platform for teaching and research materials in business education and training.  
The project combines a blog, presentations, and OER resources within a transparently documented technical infrastructure.

---

## 🌐 Website

Der veröffentlichte Blog ist hier erreichbar:

https://matthiassoell.github.io/iWIP/

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

**Technologien**

- **Hugo** – Static Site Generator  
- **PaperMod** – Blog-Theme  
- **reveal-hugo / reveal.js** – Präsentationssystem  
- **GitHub Pages** – Hosting  
- **GitHub Actions** – automatisiertes Deployment  

Alle Inhalte werden in **Markdown** geschrieben und als **statische Webseiten** generiert.

---

## 🧱 Projektstruktur

Die wichtigsten Bereiche des Repositories:

```
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

```
Design Tokens
      ↓
Blog Komponenten
      ↓
Callout-Komponenten
```

Dateien:

```
00_design_tokens.css
10_custom.css
20_custom_callouts.css
custom_reveal.css
```

Reveal-CSS und Blog-CSS sind strikt getrennt.

Details sind dokumentiert in:

```
project_governance/css_architecture.md
```

---

## 📚 Dokumentation

Die technische Architektur des Projekts ist zusammen mit mit Entwicklungsregeln im Ordner `project_governance/` transparent dokumentiert.

Wichtige Dokumente:

```
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

```
project_governance/ai_copilot_instructions.md
```

---

## 📖 Lizenz

Die Inhalte des Blogs werden – sofern nicht anders angegeben – unter einer **Creative Commons Lizenz (CC BY-SA 4.0)** veröffentlicht.

https://creativecommons.org/licenses/by-sa/4.0/

---

## 👤 Autor

**Prof. Dr. Matthias Söll**  
Universität Rostock  
Institut für Wirtschaftspädagogik

https://matthiassoell.github.io/iWIP/

---

## ℹ️ Hinweis

Dieses Repository dient in erster Linie der **Dokumentation der technischen Infrastruktur** des SciBlog iWIP.  
Die Inhalte werden über den Blog selbst veröffentlicht.
