---
title: "Doku – Technik, Struktur & Offenheit"
date: 2025-10-01
draft: false
description: >
  Technische Dokumentation zur offenen, OER-kompatiblen Infrastruktur
  des SciBlog iWIP sowie zu zentralen Design- und Infrastrukturentscheidungen.
summary: >
  Diese Dokumentation beschreibt die technische Basis des SciBlog iWIP
  und richtet sich an technisch Interessierte und Co-Autor:innen.
---

## 📥 Doku – Technik, Struktur & Offenheit

Diese Dokumentation beschreibt die **OER-kompatible, offene und frei verfügbare Softwarebasis** des SciBlog iWIP sowie zentrale **Design- und Infrastrukturentscheidungen**.

Sie richtet sich an **technisch Interessierte**, **Co-Autor:innen** und alle, die nachvollziehen möchten, **wie und warum der Blog technisch so umgesetzt ist**.  

Die **inhaltliche Nutzung** des Blogs (z. B. Lesen, PDF, Präsentation) wird bewusst **nicht hier**, sondern kontextnah auf den jeweiligen Seiten sowie im **Überblick 🧭** erläutert.

---

## 📚 Gegenstand

Im Mittelpunkt dieses Beitrags steht die **technische Infrastruktur** hinter dem SciBlog iWIP. Ziel ist eine **offene, frei verfügbare und OER-kompatible Plattform** für Wissenschaftskommunikation und Lehre.

Die eingesetzten Werkzeuge ermöglichen:
- effizientes Publizieren,
- transparente Versionierung,
- kollaboratives Arbeiten mit Co-Autor:innen.

---

## 1️⃣ Entwicklungsumgebung „GitHub“

- **🌐 GitHub als Entwicklungsplattform**  
  <https://github.com>  
  GitHub dient als zentrale Plattform für Entwicklung, Versionierung und Veröffentlichung.  
  Die Zusammenarbeit wird durch die Versionsverwaltung mit Git transparent dokumentiert.  
  Für Open-Source-Projekte ist GitHub kostenfrei nutzbar.

- **🚀 GitHub Pages als Hosting**  
  <https://pages.github.com>  
  Der SciBlog iWIP wird direkt über GitHub Pages veröffentlicht.

---

## 2️⃣ Webseitengenerator „Hugo“

- **⚡ Hugo**  
  <https://gohugo.io>  
  Hugo ist ein schneller, statischer Webseitengenerator, der Markdown-Dateien in HTML-Seiten umwandelt.  
  Die rein statische Generierung ermöglicht hohe Ladegeschwindigkeit, einfaches Hosting  
  und langfristige Archivierbarkeit – ganz im Sinne von OER.

- **📦 Hugo Modules**  
  <https://gohugo.io/hugo-modules/>  
  Themes und Erweiterungen werden über Hugo Modules verwaltet.  
  Diese Lösung ist robuster und wartungsärmer als klassische Git-Submodules,  
  insbesondere im Teamkontext.

- **🎨 Theme: PaperMod**  
  <https://github.com/adityatelange/hugo-PaperMod>  
  PaperMod bietet ein minimalistisches Design, hohe Anpassbarkeit über Custom CSS  
  und eine gute Dokumentation.

- **🖥️ Präsentationen mit Reveal-Hugo**  
  <https://github.com/joshed-io/reveal-hugo>  
  Mit Reveal-Hugo können Blogbeiträge zusätzlich als interaktive Online-Präsentationen  
  (auf Basis von reveal.js) dargestellt werden – ein Feature, das aktiv in der Lehre genutzt wird.

---

## 3️⃣ Quelltext-Editor

- **📝 Visual Studio Code**  
  <https://code.visualstudio.com>  
  Visual Studio Code dient als primärer Editor für die Arbeit am Blog.  
  Er kann über Erweiterungen (z. B. Markdown-Unterstützung, Vorschau) angepasst werden.  
  Kleinere Änderungen erfolgen teilweise direkt über GitHub.

---

## 4️⃣ KI-Unterstützung

- **🤖 KI-Einsatz**  
  Für Konzeption, technische Umsetzung und Dokumentation des SciBlog iWIP  
  wird KI (u. a. ChatGPT) unterstützend eingesetzt.

  Der Einsatz erfolgt insbesondere bei:
  - Ideensammlung,
  - Codeoptimierung und Fehlersuche,
  - dem Schreiben von Dokumentationen,
  - der didaktischen Aufbereitung von Inhalten.

---

## 5️⃣ Struktur

- **📂 Repository**  
  <https://github.com/MatthiasSoell/iWIP/>

- **🌍 Öffentliche Website**  
  <https://matthiassoell.github.io/iWIP/>

Die **inhaltliche Nutzung** des Blogs (z. B. PDF-Erstellung, Präsentationsansicht)  
wird bewusst **nicht** in dieser technischen Dokumentation erläutert,  
sondern kontextnah auf den jeweiligen Seiten sowie im **Überblick 🧭**.

---

## 6️⃣ Zusammenarbeit

- **👥 Mitarbeit über Pull Requests**  
  Alle interessierten GitHub-Nutzer:innen können Beiträge oder Änderungen  
  über Pull Requests vorschlagen und so transparent als Co-Autor:innen mitwirken.

- **🤝 Arbeiten mit Forks**  
  Collaborator:innen können im Fork  
  <https://github.com/kiwip2025/iWIP>  
  Inhalte erstellen und unter  
  <https://kiwip2025.github.io/iWIP/>  
  testen, bevor sie Änderungen in das Hauptprojekt einbringen.

Die Mitarbeit setzt **keine tiefgehenden technischen Vorkenntnisse** voraus;  
Beiträge können auch in Form von **reinen Markdown-Dateien** eingebracht werden.

---

## 🪞 OER-Versionierung und Zitierfähigkeit

Die im SciBlog iWIP veröffentlichten Lehr- und Lernmaterialien werden als  
**Open Educational Resources (OER)** versioniert, um **Transparenz, Nachvollziehbarkeit  
und Zitierfähigkeit** sicherzustellen.

Die Versionierung bezieht sich **ausschließlich auf das jeweilige Material**,  
nicht auf die technische Plattform oder den Blog als Ganzes.

### Grundprinzipien der OER-Versionierung

- Jede OER-Seite besitzt eine **eigene Versionsangabe**.
- Die Version kennzeichnet **inhaltlich relevante Änderungen**  
  (z. B. Überarbeitungen, Ergänzungen, strukturelle Anpassungen).
- Kleinere redaktionelle Korrekturen (z. B. Tippfehler, Layout)  
  führen nicht zwingend zu einer neuen Version.
- Zu jeder Version werden **Erstellungs- bzw. Aktualisierungsdatum**,  
  **Lizenzangaben** und ein **Zitiervorschlag** ausgewiesen.

### Zweck der Versionierung

Die OER-Versionierung dient insbesondere:
- der **wissenschaftlich sauberen Zitierbarkeit**,
- der **Nachvollziehbarkeit von Weiterentwicklungen**,
- der **verantwortungsvollen Nachnutzung** offener Materialien.

Nutzende können dadurch erkennen,  
**welche inhaltliche Fassung eines Materials** verwendet oder zitiert wurde.

### Abgrenzung

Die Versionierung der OER-Materialien ist **unabhängig** von der fortlaufenden  
technischen Weiterentwicklung des SciBlog iWIP.  
Änderungen an Darstellung, Navigation oder Infrastruktur  
haben keinen Einfluss auf die inhaltliche Version eines OER-Materials.
