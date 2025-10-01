---
title: "Technische Dokumentation"
date: 2025-10-01
draft: false
description: "Diese technische Dokumentation beschreibt die OER-kompatible und frei verfügbare Softwarebasis des SciBlog iWIP."
summary: "Diese technische Dokumentation beschreibt die OER-kompatible und frei verfügbare Softwarebasis des SciBlog iWIP."
tags: ["GitHub", "GitHub Pages", "Hugo", "PaperMod", "reveal-hugo"]
categories: ["Doku"]
---

# Zielgruppe

Diese Dokumentation richtet sich an Interessierte an einer OER-kompatiblen, frei verfügbaren Softwarebasis für Webseiten.

---

## 1. Entwicklungsumgebung "GitHub"

- **GitHub als öffentliche Softwareentwicklungsplattform:** [`https://github.com`](https://github.com)  
  Ich nutze die Plattform GitHub, in deren Zentrum die Nutzer:innen und deren Projekte stehen. Die Zusammenarbeit an Code wird durch die Versionsverwaltungs-Software Git transparent dokumentiert.
 
- **GitHub Pages als Host:** [`https://pages.github.com`](https://pages.github.com)  
  Der Blog wird direkt über GitHub Pages im Internet veröffentlicht.

## 2. Webseitengenerator "Hugo"

- **Hugo als Generator:** [`https://gohugo.io`](https://gohugo.io)
  Die Webseiten werden mit dem Webseitengenerator Hugo gebaut. Der Generator arbeitet mit GitHub Actions gut auf GitHub und GitHub Pages, ist umfassend dokumentiert und schnell. 

- **Hugo Modules als Modulverwaltung:** [`https://gohugo.io/hugo-modules/`](https://gohugo.io/hugo-modules/)  
  Die Verwaltung von Themes und Erweiterungen erfolgt bei meinem Blog über Hugo Modules. Diese ermöglichen eine einfachere und robustere Einbindung als ältere Methoden wie Git Submodules.

- **PaperMod als Theme:** [PaperMod](https://github.com/adityatelange/hugo-PaperMod)   
  Das PaperMod Theme nutze ich aufgrund des einfachen, ansprechenden Aufbaus und der Möglichkeit, es meinen Bedürfnissen v. a. über CSS anpassen zu können.

- **Reveal-Hugo als Erweiterung:** [Reveal-Hugo](https://github.com/joshed-io/reveal-hugo) 
  Reveal-Hugo nutze ich als Erweiterung, um meine Blogbeiträge als Online-Präsentationen aufzubereiten und in meinen Lehrveranstaltungen zeigen zu können.
  
- **Co-Autor:innen-Arbeitsumgebung (Fork):**  
  [`https://github.com/kiwip2025/iWIP`](https://github.com/kiwip2025/iWIP)  
  [`https://kiwip2025.github.io/iWIP/`](https://kiwip2025.github.io/iWIP/) (Live-Vorschau!)

## 3. Quelltext-Editor Visual Studio Code

Zur Programmierung der Webseiten nutze ich **Visual Studio Code** [`https://code.visualstudio.com`](https://code.visualstudio.com), der über zahlreiche Erweiterungen an die persönlichen Bedürfnisse angepasst werden kann. Kleinere Änderungen nehme ich auch über **GitHub** selbst vor.

## 4. Struktur

- Repository: [`https://github.com/MatthiasSoell/iWIP/`](https://github.com/MatthiasSoell/iWIP/)
- Homepage: [`https://matthiassoell.github.io/iWIP/`](https://matthiassoell.github.io/iWIP/)

## 5. Zusammenarbeit

- Alle GitHub Nutzer:innen können über Pull Requests Änderungen über das Repository vorschlagen.
- Mit Co-Autor:innen arbeite ich über einen Fork auf [`https://github.com/kiwip2025/iWIP`](https://github.com/kiwip2025/iWIP) zusammen. Als Collaborator:innen können sie dort Änderungen direkt vornehmen und live unter [`https://kiwip2025.github.io/iWIP/`](https://kiwip2025.github.io/iWIP/) testen.
