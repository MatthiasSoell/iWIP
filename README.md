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

Der integrierte Agent unterstützt Lehrende und Studierende dabei, Lehrveranstaltungen klar zu planen, Inhalte schrittweise auszuarbeiten und daraus veröffentlichbare Materialien zu entwickeln.

Im Zentrum steht ein einfacher Zusammenhang: **Planung → Blog → Präsentation**. Die fachliche und didaktische Arbeit beginnt mit der Planung. Daraus entsteht ein Blogbeitrag als zentrales Arbeitsdokument. Wenn gewünscht, kann anschließend eine Präsentation aus diesem Blogbeitrag abgeleitet werden.

Der Agent ist dabei kein technisches Steuerinstrument, sondern ein didaktisches Werkzeug. Er hilft, Gedanken zu ordnen, Ziele zu schärfen, Lernwege zu strukturieren und Inhalte so aufzubereiten, dass sie für Lehre, Reflexion und Austausch nutzbar werden.

### Wofür der Agent gedacht ist

- zur Unterstützung bei der Planung von Lehrveranstaltungen
- zur strukturierten Entwicklung von Blogbeiträgen
- zur Ableitung von Präsentationen auf Grundlage des Blogbeitrags

### Zentrale Idee

Der Blog ist das Herzstück der Arbeit. Hier werden Inhalte gebündelt, ausgearbeitet und in eine Form gebracht, die sowohl für die Lehre als auch für die Veröffentlichung geeignet ist. Die Präsentation entsteht nicht unabhängig davon, sondern baut auf dem Blogbeitrag auf.

Das schafft Klarheit: Erst wird inhaltlich und didaktisch gearbeitet, dann kann aus dieser Grundlage eine Präsentation entwickelt werden.

### Nutzung

Der Einstieg erfolgt über `/create`. Von dort aus begleitet der Agent die Ausarbeitung im Dialog: ruhig, fokussiert und in enger Zusammenarbeit mit den Nutzenden.

Die Arbeit ist ko-kreativ angelegt. Der Agent macht Vorschläge, strukturiert Inhalte, unterstützt beim Formulieren und hilft dabei, didaktische Entscheidungen sichtbar zu machen. Er übernimmt nicht die Lehrplanung, sondern unterstützt sie.

Wenn aus dem Blogbeitrag zusätzlich eine Präsentation entstehen soll, kann diese anschließend aus der bereits erarbeiteten Grundlage abgeleitet werden.

### Didaktischer Mehrwert

- unterstützt eine strukturierte Planung von Lehrveranstaltungen
- stärkt die Entwicklung aktiver Lernformate
- fördert Reflexion, Diskussion und nachvollziehbare Begründungen
- orientiert sich an didaktischer Qualität statt an schneller Texterzeugung

### Charakter des Systems

Der Agent arbeitet zurückhaltend und unterstützend. Er ist auf didaktische Klärung ausgerichtet, nicht auf technische Komplexität. Dadurch bleibt die Zusammenarbeit verständlich, fokussiert und anschlussfähig für unterschiedliche Lehr- und Lernsituationen.

### Verbindung zum Blog und zu OER

Der SciBlog iWIP versteht den Blog als OER-Angebot. Inhalte können veröffentlicht, weiterverwendet und in neuen Lehrzusammenhängen erneut aufgegriffen werden. Der Agent unterstützt diese Erstellung, indem er die Ausarbeitung von der ersten Planung bis zum veröffentlichbaren Blogbeitrag begleitet.

### Beispielhafter Ablauf

1. Planung einer Lehrveranstaltung oder Lerneinheit
2. Ausarbeitung eines Blogbeitrags als zentrales Arbeitsdokument
3. optionale Ableitung einer Präsentation aus dem Blogbeitrag

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
