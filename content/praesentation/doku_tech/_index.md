---
title: "Technische Dokumentation"
date: 2025-10-01
draft: false
description: "Diese Präsentation beschreibt die OER-kompatible und frei verfügbare Softwarebasis des SciBlog iWIP."
outputs:
  - Reveal
reveal_hugo:
  theme: simple
  slide_number: true
  transition: fade
  custom_theme: /iWIP/css/custom_reveal.css
---

{{< logoBox src="/iWIP/bilder/logo_siblog_iwip.png" text="SciBlog iWIP" show="true" >}}

# 📚 Technische Dokumentation

Im Mittelpunkt dieser Präsentation steht die technische Infrastruktur hinter dem **SciBlog iWIP**.  
Ziel ist eine **offene**, **frei verfügbare** und **OER-kompatible Plattform** für Wissenschaftskommunikation und Lehre.  
Die eingesetzten Tools ermöglichen sowohl **effizientes Publizieren** als auch **kollaboratives Arbeiten** mit Co-Autor:innen.

---

## 1️⃣ Entwicklungsumgebung „GitHub“

- 🌐 **GitHub** als Plattform für **Entwicklung**, **Versionierung** und **Veröffentlichung**  
  → [github.com](https://github.com)

- 🗂️ **Versionsverwaltung** über Git  
  → ermöglicht transparente Nachvollziehbarkeit von Änderungen

- 🚀 **GitHub Pages** als Host  
  → [pages.github.com](https://pages.github.com)  
  → kostenfrei für Open-Source-Projekte

---

## 2️⃣ Webseitengenerator „Hugo“

- ⚡ **Hugo** wandelt Markdown-Dateien in statische HTML-Seiten  
  → [gohugo.io](https://gohugo.io)  
  → hohe **Geschwindigkeit**, einfache **Automatisierung** mit GitHub Actions  
  → ideal für langfristig **archivierbare OER**

---

## 📦 Hugo Modules

- Verwaltung von Themes & Erweiterungen über **Hugo Modules**  
  → [Hugo Modules](https://gohugo.io/hugo-modules/)

✅ Vorteile gegenüber Git Submodules:
- einfacher in der Anwendung
- stabiler im Teamkontext
- besser wartbar bei Updates

---

## 🎨 PaperMod & 🖥️ Reveal-Hugo

- **PaperMod Theme** für minimalistisches, responsives Design  
  → [PaperMod](https://github.com/adityatelange/hugo-PaperMod)

- **Reveal-Hugo** zur Erstellung von Präsentationen im Blog  
  → basiert auf reveal.js  
  → [Reveal-Hugo](https://github.com/joshed-io/reveal-hugo)

💡 Ideal für **didaktische Visualisierung** von Inhalten direkt im Blog.

---

## 3️⃣ Visual Studio Code

- 📝 **VS Code** als Quelltexteditor  
  → [code.visualstudio.com](https://code.visualstudio.com)

🔌 Nützliche Erweiterungen:
- **Markdown All in One**
- **Live Preview**
- **GitLens**

🛠️ Auch kleinere Änderungen direkt auf GitHub möglich.

---

## 4️⃣ Projektstruktur

📂 **Repository:**  
[github.com/MatthiasSoell/iWIP](https://github.com/MatthiasSoell/iWIP)

🌍 **Live-Blog:**  
[matthiassoell.github.io/iWIP](https://matthiassoell.github.io/iWIP)

🗂️ Verzeichnisse:
- `/content/` → Seiten
- `/iWIP/bilder/` → Bilder
- `/static/css/` → eigene Styles

---

## 5️⃣ Kollaboration mit Co-Autor:innen

👥 **Pull Requests:**  
Alle GitHub-Nutzer:innen können Beiträge vorschlagen und versioniert einreichen.

🤝 **Fork-Collaboration:**  
- Mitarbeit über Fork [`kiwip2025/iWIP`](https://github.com/kiwip2025/iWIP)  
- Live-Test auf [`kiwip2025.github.io/iWIP`](https://kiwip2025.github.io/iWIP/)  
- Änderungen via Pull Request ins Hauptprojekt

---

## 🚀 Fazit

✅ Der SciBlog iWIP basiert auf einer **OER-freundlichen**, **Open-Source-basierten** Infrastruktur  
✅ Die verwendeten Tools sind **nachhaltig**, **kollaborativ** und **pädagogisch einsetzbar**  
✅ Co-Autor:innen können ohne lokale Installation live mitarbeiten

🧑‍🏫 *Ein digitales Wissenschafts- und Lehrprojekt zum Mitmachen!*

---

## 🙏 Danke für Ihre Aufmerksamkeit!

🧠 [https://matthiassoell.github.io/iWIP](https://matthiassoell.github.io/iWIP)  
📧 [matthias.soell@uni-rostock.de](mailto:matthias.soell@uni-rostock.de)

📂 [GitHub Repo](https://github.com/MatthiasSoell/iWIP)  
📑 [Anleitungen für Co-Autor:innen](/iWIP/doku/doku_coll/)
