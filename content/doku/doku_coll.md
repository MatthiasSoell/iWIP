---
title: "Anleitungen für Co-Autor:innen"
date: 2025-10-01
draft: false
description: "Diese Anleitung richtet sich an Co-Autor:innen des SciBlog iWIP. Schritt für Schritt wird erklärt, wie eigene Seiten mit Markdown und grundlegenden Webtechniken erstellt werden können."
summary: "Diese Anleitung richtet sich an Co-Autor:innen des SciBlog iWIP. Schritt für Schritt wird erklärt, wie eigene Seiten mit Markdown und grundlegenden Webtechniken erstellt werden können."
tags: ["GitHub", "GitHub Pages", "Hugo", "PaperMod", "reveal-hugo", "Markdown", "HTML", "CSS", "JavaScript", "Co-Autor:innen"]
categories: ["Doku"]
---

---

## title: "Dokumentation und Anleitung für Co-Autor\:innen" date: 2025-10-01

# 🔧 SciBlog iWIP – Technisches Setup und Anleitung für Co-Autor\:innen

## ✍️ Zielsetzung

Diese Dokumentation erklärt das Setup des Lehr-/Wissenschaftsblogs **SciBlog iWIP** mit GitHub Pages, Hugo, PaperMod, Reveal-Hugo und einer Preview-Umgebung für Co-Autor\:innen. Sie richtet sich an Mitwirkende, die Inhalte erstellen, überarbeiten oder als Open Educational Resources (OER) veröffentlichen möchten.

---

## ♻️ A. Technisches Setup (für Admins)

### 1. Repositories

- **Hauptprojekt:**\
  GitHub: [github.com/MatthiasSoell/iWIP](https://github.com/MatthiasSoell/iWIP)\
  Online: [matthiassoell.github.io/iWIP/](https://matthiassoell.github.io/iWIP/)

- **Preview-/Fork-Umgebung für Co-Autor\:innen:**\
  Fork: [github.com/kiwip2025/iWIP](https://github.com/kiwip2025/iWIP)\
  Online: [kiwip2025.github.io/iWIP/](https://kiwip2025.github.io/iWIP/)

### 2. Technologiestack

- **Static Site Generator:** [Hugo](https://gohugo.io/) (v0.147.7 extended)
- **Themes:**
  - [PaperMod](https://github.com/adityatelange/hugo-PaperMod) (Blog)
  - [reveal-hugo](https://github.com/joshed-io/reveal-hugo) (Präsentationen)
- **Hosting:** GitHub Pages
- **CI/CD:** GitHub Actions (Deploy über `hugo.yml`)
- **Bildverzeichnisse:** `/static/bilder/<unterordner>/`
- **Contentverzeichnisse:** `/content/<unterordner>/`

### 3. GitHub Konfiguration

- Co-Autor\:innen arbeiten im Fork `kiwip2025/iWIP` (mit Schreibrechten als Collaborators)
- Vorschau-URL: `https://kiwip2025.github.io/iWIP/`
- Pull Requests möglich gegen Hauptrepo `MatthiasSoell/iWIP`
- Keine Vorschauüberschneidungen, da getrenntes Deployment

---

## 📄 B. Anleitung für Co-Autor\:innen

### 1. Voraussetzungen

- GitHub-Account
- Schreibzugriff auf [github.com/kiwip2025/iWIP](https://github.com/kiwip2025/iWIP) (als Collaborator eingeladen)
- Online-Bearbeitung oder optional VS Code mit GitHub Desktop

### 2. Neue Seite erstellen

1. Navigiere im Repository zu `content/<unterordner>/`
2. Erstelle dort eine neue Datei, z. B. `mein-beitrag.md`
3. Beginne mit folgendem **Front Matter** (YAML-Format):

```markdown
---
title: "Titel der Seite"
date: 2025-10-01
draft: false
---

Hier folgt der Inhalt ...
```

4. Speichere die Datei. Nach wenigen Minuten ist sie unter [https://kiwip2025.github.io/iWIP/](https://kiwip2025.github.io/iWIP/) sichtbar.

### 3. Bilder einbinden

- Lege Bilder in folgendes Verzeichnis: `static/bilder/<unterordner>/Bild1.png`

- Verwende folgenden Markdown-Befehl:

```markdown
![Alternativtext](/iWIP/bilder/<unterordner>/Bild1.png)
```

Beispiel:

```markdown
![Diagramm zur OER-Nutzung](/iWIP/bilder/oer/oer-uebersicht.png)
```

### 4. Präsentation erstellen (Reveal-Hugo)

1. Erstelle einen Beitrag mit `.md` wie oben, aber mit `output: Reveal` im Front Matter:

```markdown
---
title: "Meine Präsentation"
date: 2025-10-01
outputs: ["Reveal"]
draft: false
---
```

2. Verwende `##` als Slide-Trenner:

```markdown
## Titel der Folie

Inhalt der Folie

## Nächste Folie
```

3. Online-Vorschau unter z. B.: `https://kiwip2025.github.io/iWIP/mein-vortrag/reveal`

### 5. Markdown Basics

| Zweck              | Markdown Syntax              |
| ------------------ | ---------------------------- |
| **Überschrift H1** | `# Haupttitel`               |
| **Fett**           | `**Text**`                   |
| **Kursiv**         | `*Text*`                     |
| **Liste**          | `- Punkt 1`                  |
| **Link**           | `[Text](https://adresse.de)` |
| **Bild**           | `![Alt](/pfad/zum/bild.png)` |
| **Code inline**    | `` `code` ``                 |
| **Codeblock**      | ` `\ncode\`\`\`              |

---

## 📈 Weitere Hinweise

- Vorschau dauert 1–5 Minuten nach Commit
- Bitte keine Änderungen direkt im Hauptrepo vornehmen
- Bei Fragen oder Pull Request bitte [Prof. Söll](https://github.com/MatthiasSoell) kontaktieren

---

## ✔️ Lizenzhinweis

Alle Inhalte werden als Open Educational Resources unter CC BY-SA 4.0 veröffentlicht, sofern nicht anders angegeben.

---

*Letzte Aktualisierung: 01.10.2025*
