---
title: "Technische Dokumentation"
date: 2025-10-01
draft: false
description: "In dieser technischen Dokumentation stelle ich die möglichst OER-kompatible und frei verfügbare Software vor, mit deren Hilfe ich meinen Blog betreibe."
summary: "In dieser technischen Dokumentation stelle ich die möglichst OER-kompatible und frei verfügbare Software vor, mit deren Hilfe ich meinen Blog betreibe."
tags: ["GitHub", "GitHub Pages", "Hugo", "PaperMod", "reveal-hugo"]
categories: ["Doku"]
---

# Mitarbeit am SciBlog iWIP

Diese Anleitung richtet sich an Co-Autor:innen des SciBlog iWIP. Sie beschreibt das technische Setup, das Repository-Konzept und wie eigene Beiträge mit Live-Vorschau verfasst und zur Veröffentlichung vorgeschlagen werden können – inklusive kurzer Markdown-Einführung.

---

## 1. Projektübersicht

- **Blog-Adresse (öffentlich):**  
  [`https://matthiassoell.github.io/iWIP/`](https://matthiassoell.github.io/iWIP/)

- **Haupt-Repository (admin-only):**  
  [`https://github.com/MatthiasSoell/iWIP`](https://github.com/MatthiasSoell/iWIP)

- **Co-Autor:innen-Arbeitsumgebung (Fork):**  
  [`https://github.com/kiwip2025/iWIP`](https://github.com/kiwip2025/iWIP)  
  [`https://kiwip2025.github.io/iWIP/`](https://kiwip2025.github.io/iWIP/) (Live-Vorschau!)

- **Generator:** [Hugo](https://gohugo.io) (v0.147.7 extended)  
- **Themes:** [PaperMod](https://github.com/adityatelange/hugo-PaperMod), [Reveal-Hugo](https://github.com/joshed-io/reveal-hugo)  
- **Modulverwaltung:** Hugo Modules  
- **Hosting:** GitHub Pages  
- **Deployment:** GitHub Actions (automatisch bei Push auf `main`)  
- **Struktur:**
  - Seiten: `/content/…`
  - Bilder: `/static/iWIP/bilder/…` → Online erreichbar unter `/iWIP/bilder/…`

---

## 2. Mitarbeit über Fork & Pull Requests

### Schritt 1: Zugang
- Du erhältst Zugriff auf den Fork unter [`https://github.com/kiwip2025/iWIP`](https://github.com/kiwip2025/iWIP) als **Collaborator**.
- Du kannst dort direkt Änderungen vornehmen und live unter [`https://kiwip2025.github.io/iWIP/`](https://kiwip2025.github.io/iWIP/) testen.

### Schritt 2: Beitrag verfassen
- Lege eine neue Datei im Verzeichnis `/content/<dein-thema>/` an, z. B.:
