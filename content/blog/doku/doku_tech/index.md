---
title: "Technische Dokumentation"
date: 2025-10-01
lastmod: 2025-10-01
draft: false

description: >
  Diese technische Dokumentation beschreibt die OER-kompatible, offene und frei verfügbare Softwarebasis des SciBlog iWIP sowie zentrale Design- und Infrastrukturentscheidungen.

summary: >
  Technische Dokumentation zur Infrastruktur des SciBlog iWIP: GitHub, Hugo, Themes, Präsentationsformate und kollaborative Workflows für offene Wissenschaftskommunikation.

tags:
  - Dokumentation
  - Technische Infrastruktur
  - GitHub
  - Hugo
  - Open Source
  - OER-Infrastruktur
  - Wissenschaftskommunikation

categories:
  - Doku

oer:
  is_oer: false
  kind: "documentation"
  note: "Technische Dokumentation zur Infrastruktur des SciBlog iWIP (keine Lehr-Lern-Einheit, kein einzelnes OER)"

  related_practices:
    - "Open Educational Practices (OEP)"
    - "Open Source Software"
    - "Open Science"
    - "Open Infrastructure"

  creators:
    - name: "Prof. Dr. Matthias Söll"
      affiliation: "Universität Rostock · Institut für Wirtschaftspädagogik"
      url: ""
      orcid: ""

  publisher:
    name: "SciBlog iWIP – Universität Rostock"
    url: "https://matthiassoell.github.io/iWIP/"

  license:
    label: "CC BY-SA 4.0"
    url: "https://creativecommons.org/licenses/by-sa/4.0/"

  in_language: "de"

  audience:
    - "Lehrende"
    - "Studierende"
    - "Co-Autor:innen"
    - "Interessierte an OER- und Blog-Infrastrukturen"

  about:
    - term: "Technische Dokumentation"
    - term: "Blog-Infrastruktur"
    - term: "GitHub Pages"
    - term: "Hugo"
    - term: "Open-Source-Software"
    - term: "OER-kompatible Webpublikation"

  todos:
    - "Erweiterung der Co-Autor:innen-Dokumentation"
    - "Dokumentation der Preview- und Review-Workflows"
---

<div class="top-toggle">
  <button onclick="triggerPrint()" title="Blog speichern">📥</button>
</div>
{{< oer-meta >}}

# 📚 Gegenstand  

Im Mittelpunkt dieses Beitrags steht die technische Infrastruktur hinter dem SciBlog iWIP. Ziel ist eine **offene**, **frei verfügbare** und **OER-kompatible Plattform** für Wissenschaftskommunikation und Lehre. Die eingesetzten Tools ermöglichen sowohl **effizientes Publizieren** als auch **kollaboratives Arbeiten** mit Co-Autor:innen.

---

## 1️⃣ Entwicklungsumgebung „GitHub“

- **🌐 GitHub als öffentliche Softwareentwicklungsplattform:** [`https://github.com`](https://github.com)  
  Ich nutze die Plattform GitHub, die eine benutzerfreundliche Umgebung für die **Entwicklung**, **Versionierung** und **Veröffentlichung** von Code bietet. Die Zusammenarbeit an Code wird durch die Versionsverwaltungs-Software Git transparent dokumentiert. GitHub ist für Open-Source-Projekte kostenfrei.
 
- **🚀 GitHub Pages als Host:** [`https://pages.github.com`](https://pages.github.com)  
  Der Blog wird direkt über GitHub Pages im Internet **veröffentlicht**.

---

## 2️⃣ Webseitengenerator „Hugo“

- **⚡ Hugo als Generator:** [`https://gohugo.io`](https://gohugo.io)  
  Hugo ist ein **schneller** und **vielseitiger** Webseitengenerator, der Markdown-Dateien in statische HTML-Seiten umwandelt. Er eignet sich besonders gut für die Veröffentlichung über GitHub Pages und unterstützt eine effiziente Automatisierung via GitHub Actions. ✅ Da rein **statische Seiten** generiert werden, ist die Ladegeschwindigkeit hoch, das Hosting einfach und die langfristige Archivierbarkeit ganz im Sinne von OER.

- **📦 Hugo Modules als Modulverwaltung:** [`https://gohugo.io/hugo-modules/`](https://gohugo.io/hugo-modules/)  
  Die Verwaltung von Themes und Erweiterungen erfolgt über Hugo Modules. Diese bieten gegenüber klassischen Git Submodules eine **einfachere**, **robustere** und **wartungsärmere** Lösung – besonders im Teamkontext.

- **🎨 PaperMod als Theme:** [`https://github.com/adityatelange/hugo-PaperMod`](https://github.com/adityatelange/hugo-PaperMod)  
  Das PaperMod-Theme überzeugt durch **minimalistisches Design**, **hohe Anpassbarkeit** über Custom CSS und **gute Dokumentation**.

- **🖥️ Reveal-Hugo als Präsentationserweiterung:** [`https://github.com/joshed-io/reveal-hugo`](https://github.com/joshed-io/reveal-hugo)  
  Mit Reveal-Hugo können Blogbeiträge auch als **interaktive Online-Präsentationen** (basierend auf reveal.js) dargestellt werden – ein Feature, das ich in meinen Lehrveranstaltungen aktiv nutze.

---

## 3️⃣ Quelltext-Editor Visual Studio Code  

Zur Programmierung der Webseiten nutze ich 📝 **Visual Studio Code** [`https://code.visualstudio.com`](https://code.visualstudio.com), der über zahlreiche Erweiterungen, z. B. **Markdown All in One** oder **Live Preview**, individuell erweitert und angepasst werden kann. 💡 Kleinere Änderungen nehme ich auch über **GitHub** selbst vor.

---

## 4️⃣ KI-Unterstützung

🤖 Für die Konzeption des SciBlogs iWIP sowie für die technische Umsetzung nutze ich die **KI ChatGPT**.  
Sie kommt insbesondere bei der **Ideensammlung**, der **Codeoptimierung**, der **Fehlersuche**, dem **Schreiben von Dokumentationen** sowie der **didaktischen Aufbereitung** von Inhalten zum Einsatz.

---

## 5️⃣ Struktur  

- 📂 **Repository:** [`https://github.com/MatthiasSoell/iWIP/`](https://github.com/MatthiasSoell/iWIP/)  
- 🌍 **Homepage:** [`https://matthiassoell.github.io/iWIP/`](https://matthiassoell.github.io/iWIP/)

---

## 6️⃣ Zusammenarbeit  

- 👥 Alle interessierten GitHub Nutzer:innen können über **Pull Requests** im Repository Beiträge oder Änderungen vorschlagen und so transparent dokumentiert als **Co-Autor:innen** am Projekt mitwirken.  
- 🤝 **Collaborator:innen** können direkt im **Fork** [`https://github.com/kiwip2025/iWIP`](https://github.com/kiwip2025/iWIP) arbeiten, Beiträge erstellen und live unter [`https://kiwip2025.github.io/iWIP/`](https://kiwip2025.github.io/iWIP/) testen, bevor sie ihre Inhalte über Pull Requests in das Hauptprojekt einbringen.
