# SciBlog iWIP – Offene Publikationsplattform für Wirtschaftspädagogik und -didaktik

SciBlog iWIP ist eine offene Publikationsplattform für wirtschaftspädagogische und -didaktische Lehr-, Lern- und Forschungsinhalte. 

Das Repository vereint Blog, OER, Präsentationen und didaktische Entwicklungsarbeit in einer gemeinsamen, transparent dokumentierten Infrastruktur.

Das Repository enthält:

- eine technische Plattform auf Basis von Hugo, GitHub Pages und GitHub Actions
- Blogartikel und Open Educational Resources (OER) in Markdown
- Präsentationen auf Basis von reveal-hugo und reveal.js
- einen didaktischen Planungsagenten für die Entwicklung von Lehr- und Publikationsmaterialien
- technische und didaktische Dokumentation zur Struktur und Weiterentwicklung des Projekts

## Website

Der veröffentlichte Blog ist hier erreichbar:

[https://matthiassoell.github.io/iWIP/](https://matthiassoell.github.io/iWIP/)

## Ziel des Projekts

- Lehr-Lern- und Forschungsmaterialien der Wirtschaftspädagogik und -didaktik offen zugänglich machen
- Materialien als Open Educational Resources veröffentlichen und weiterentwickeln
- Lehrveranstaltungen und Entwicklungsprozesse transparent dokumentieren
- Präsentationen direkt aus Markdown ableiten
- eine nachvollziehbare, offene, moderne Infrastruktur für wissenschaftliche Lehre und Forschung bereitstellen

## Komponenten der Plattform

### Blog & OER

Der Blog bildet das publizistische Zentrum des Projekts. Hier entstehen Blogartikel, OER-Materialien und fachbezogene Dokumentationen, die in Markdown gepflegt und als statische Seiten veröffentlicht werden.

### Präsentationen

Präsentationen werden mit reveal-hugo und reveal.js bereitgestellt. Sie sind bewusst als eigener Ausgabekanal organisiert und können aus vorhandenen Inhalten abgeleitet werden.

### Didaktischer Planungsagent

Der integrierte didaktische Planungsagent (WiDi) unterstützt die Planung und strukturierte Ausarbeitung von Lehr-Lern-Inhalten. Er verbindet den Arbeitszusammenhang Planung → Blog → Präsentation und macht Entwicklungsprozesse nachvollziehbar und reflektierbar. Der Agent arbeitet dialogisch, strukturierend und ko-kreativ; der Blog dient dabei als zentrales Arbeitsdokument, aus dem bei Bedarf Präsentationen abgeleitet werden können. Er ist als unterstützendes Werkzeug konzipiert und ersetzt keine didaktischen Entscheidungen. Weitere Details, zentrale Dateien und die Nutzung sind in [ai_agents/README.md](ai_agents/README.md) dokumentiert.

### Technische Infrastruktur

Die Plattform basiert auf einer bewusst einfachen, offenen Web-Infrastruktur:

- Hugo als Static Site Generator
- PaperMod als Blog-Theme
- reveal-hugo / reveal.js für Präsentationen
- GitHub Pages für Hosting
- GitHub Actions für automatisiertes Deployment

Alle Inhalte werden in Markdown gepflegt und als statische Webseiten generiert.

## Projektstruktur

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

## Dokumentation

Die technische und organisatorische Dokumentation liegt im Ordner `project_governance/`.

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

Dokumentiert sind dort insbesondere Repository-Struktur, CSS-System, Content-Konventionen, AI-Regeln und der technische Projektkontext.

## Versionierung

Die Versionierung markiert bewusst größere Entwicklungsschritte der Plattform und des Agenten (keine feingranulare Software-Versionierung).

Plattform SciBlog iWIP: 1.0

Kleinere Anpassungen an Layout, Formulierungen oder CSS werden nicht separat versioniert.

## Lizenz

Die Inhalte des Blogs werden, sofern nicht anders angegeben, unter der Lizenz **CC BY-SA 4.0** veröffentlicht.

[https://creativecommons.org/licenses/by-sa/4.0/](https://creativecommons.org/licenses/by-sa/4.0/)

## Autor

**Prof. Dr. Matthias Söll**  
Universität Rostock  
Institut für Wirtschaftspädagogik  
Lehrstuhl für Wirtschaftsdidaktik mit dem Schwerpunkt digitales Lehren und Lernen in der beruflichen Bildung

[https://www.iwip.uni-rostock.de/institut/iwip/team/prof-dr-matthias-soell/](https://www.iwip.uni-rostock.de/institut/iwip/team/prof-dr-matthias-soell/)