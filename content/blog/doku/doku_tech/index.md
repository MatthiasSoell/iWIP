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
  <button id="md-copy-btn" title="Markdown kopieren (ohne Bilder)">📑</button>
  <button onclick="triggerPrint()" title="Blog speichern">📥</button>
  <button class="iwip_help_btn"
        type="button"
        aria-haspopup="dialog"
        aria-controls="iwip_help_overlay"
        aria-expanded="false"
        title="Hinweise zur Nutzung">
  ⓘ
  </button>
</div>

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

---

## 7️⃣ Versionierung & Reifegrad von Lehr-Lern-Einheiten

**🛠️ Entwicklungslogik des SciBlog iWIP:** Neben der technischen Infrastruktur folgt der SciBlog iWIP einer transparenten Entwicklungslogik für Lehr-Lern-Einheiten.

Im SciBlog iWIP werden Lehr-Lern-Einheiten nicht nur veröffentlicht, sondern kontinuierlich weiterentwickelt.  
Um diesen Entwicklungsprozess transparent zu machen, werden zwei unterschiedliche Angaben ausgewiesen:

---

### 🧩 Version (X.Y)

Die Version beschreibt **Veränderungen an der Struktur oder am Inhalt** einer Einheit.

- **X (Hauptversion)**  
  Eine neue Hauptversion (z. B. 2.0) bedeutet eine grundlegende didaktische Überarbeitung, etwa eine neue Zielgruppe, eine veränderte Struktur oder eine konzeptionelle Neuausrichtung.

- **Y (Unterversion)**  
  Unterversionen (z. B. 1.1, 1.2) markieren inhaltliche Ergänzungen, Präzisierungen, sprachliche Überarbeitungen oder kleinere didaktische Anpassungen.

Die Version macht sichtbar, **was sich verändert hat**.

---

### 🚦 Reifegrad (Status)

Der Status beschreibt den **Entwicklungsstand** einer Lehr-Lern-Einheit.

Die Reifegrade sind:

| Symbol | Bezeichnung | Bedeutung |
|--------|------------|-----------|
| 🟡 | **Entwurf** | Die Einheit befindet sich noch im Aufbau. Struktur oder Inhalte können sich ändern. |
| 🟠 | **In Erprobung** | Die Einheit wird aktuell in der Lehre eingesetzt und weiterentwickelt. |
| 🔵 | **Stabil** | Die Einheit wurde mehrfach eingesetzt und ist zuverlässig nutzbar. |
| 🟢 | **Didaktisch abgestimmt** | Die Einheit ist didaktisch konsolidiert und reflektiert ausgearbeitet. |

### Wichtiger Hinweis

Der Reifegrad ist **kein Qualitätsranking**.  
Er stellt keine Wertung dar, sondern macht transparent, **in welcher Phase des Entwicklungsprozesses sich eine Einheit befindet**.

Eine Einheit im Status „In Erprobung“ ist nicht „schlechter“ als eine „Stabile“ Einheit – sie befindet sich lediglich in einer anderen Phase der didaktischen Weiterentwicklung.