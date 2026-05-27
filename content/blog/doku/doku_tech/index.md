---
title: "Technische Dokumentation"
author: "Prof. Dr. Matthias Söll"
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

  creators:
    - name: "Prof. Dr. Matthias Söll"
      given_name: "Matthias"
      family_name: "Söll"
      affiliation: "Universität Rostock · Institut für Wirtschaftspädagogik"
      url: "https://www.iwip.uni-rostock.de/institut/iwip/team/prof-dr-matthias-soell/"
      orcid: "https://orcid.org/0000-0002-9717-3017"

  publisher:
    name: "Prof. Dr. Matthias Söll"
    url: "https://www.iwip.uni-rostock.de/institut/iwip/team/prof-dr-matthias-soell/"

  license:
    label: "CC BY-SA 4.0"
    url: "https://creativecommons.org/licenses/by-sa/4.0/"

  source:
    label: "SciBlog iWIP – Universität Rostock"
    url: "https://matthiassoell.github.io/iWIP/"

  version: "1.0"
  status: "pilot"

  note: "Technische Dokumentation als offen lizenzierter Blog-Beitrag; keine klassische Lehr-Lern-Einheit"

  related_practices:
    - "Open Educational Practices (OEP)"
    - "Open Source Software"
    - "Open Science"
    - "Open Infrastructure"

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

# <span class="content-emoji">📚</span> Gegenstand  

<!-- Test -->

Im Mittelpunkt dieses Beitrags steht die technische Infrastruktur hinter dem SciBlog iWIP. Ziel ist eine **offene**, **frei verfügbare** und **OER-kompatible Plattform** für Wissenschaftskommunikation und Lehre.

Die eingesetzten Tools ermöglichen sowohl **effizientes Publizieren** als auch **kollaboratives Arbeiten** mit Co-Autor:innen.

Der SciBlog iWIP ist jedoch kein rein technisches Projekt, sondern folgt einem **didaktischen Primat**: Die **technische Infrastruktur** dient der **Unterstützung von Lehr-Lern-Prozessen**, deren **Planung**, **Reflexion** und **Veröffentlichung**.

Die Technik wird daher bewusst einfach gehalten und an didaktischen Anforderungen ausgerichtet – nicht umgekehrt.

---

## 1. Entwicklungsumgebung „GitHub“

- **<span class="content-emoji">🌐</span> GitHub als öffentliche Softwareentwicklungsplattform:** <a href="https://github.com" target="_blank" rel="noopener noreferrer"><code>https://github.com</code></a>  
  Ich nutze die Plattform GitHub, die eine benutzerfreundliche Umgebung für die **Entwicklung**, **Versionierung** und **Veröffentlichung** von Code bietet. Die Zusammenarbeit an Code wird durch die Versionsverwaltungs-Software Git transparent dokumentiert. GitHub ist für Open-Source-Projekte kostenfrei.
 
- **<span class="content-emoji">🚀</span> GitHub Pages als Host:** <a href="https://pages.github.com" target="_blank" rel="noopener noreferrer"><code>https://pages.github.com</code></a>  
  Der Blog wird direkt über GitHub Pages im Internet **veröffentlicht**.

---

## 2. Webseitengenerator „Hugo“

- **<span class="content-emoji">⚡</span> Hugo als Generator:** <a href="https://gohugo.io" target="_blank" rel="noopener noreferrer"><code>https://gohugo.io</code></a>  
  Hugo ist ein **schneller** und **vielseitiger** Webseitengenerator, der Markdown-Dateien in statische HTML-Seiten umwandelt. Er eignet sich besonders gut für die Veröffentlichung über GitHub Pages und unterstützt eine effiziente Automatisierung via GitHub Actions. <span class="content-emoji">✅</span> Da rein **statische Seiten** generiert werden, ist die Ladegeschwindigkeit hoch, das Hosting einfach und die langfristige Archivierbarkeit ganz im Sinne von OER.

- **<span class="content-emoji">📦</span> Hugo Modules als Modulverwaltung:** <a href="https://gohugo.io/hugo-modules/" target="_blank" rel="noopener noreferrer"><code>https://gohugo.io/hugo-modules/</code></a>  
  Die Verwaltung von Themes und Erweiterungen erfolgt über Hugo Modules. Diese bieten gegenüber klassischen Git Submodules eine **einfachere**, **robustere** und **wartungsärmere** Lösung – besonders im Teamkontext.

- **<span class="content-emoji">🎨</span> PaperMod als Theme:** <a href="https://github.com/adityatelange/hugo-PaperMod" target="_blank" rel="noopener noreferrer"><code>https://github.com/adityatelange/hugo-PaperMod</code></a>  
  Das PaperMod-Theme überzeugt durch **minimalistisches Design**, **hohe Anpassbarkeit** über Custom CSS und **gute Dokumentation**.

- **<span class="content-emoji">🖥️</span> Reveal-Hugo als Präsentationserweiterung:** <a href="https://github.com/joshed-io/reveal-hugo" target="_blank" rel="noopener noreferrer"><code>https://github.com/joshed-io/reveal-hugo</code></a>  
  Mit Reveal-Hugo können Blogbeiträge auch als **interaktive Online-Präsentationen** (basierend auf reveal.js) dargestellt werden – ein Feature, das ich in meinen Lehrveranstaltungen aktiv nutze.

- **<span class="content-emoji">🎇</span> GitHub Actions für automatisiertes Deployment:** <a href="https://github.com/astefanutti/decktape" target="_blank" rel="noopener noreferrer"><code>https://github.com/astefanutti/decktape</code></a> Es werden erweiterte Build-Prozesse genutzt, z. B. der PDF-Export für Präsentationen über DeckTape.
---

## 3. Quelltext-Editor Visual Studio Code  

Zur Programmierung der Webseiten nutze ich <span class="content-emoji">📝</span> **Visual Studio Code** <a href="https://code.visualstudio.com" target="_blank" rel="noopener noreferrer"><code>https://code.visualstudio.com</code></a>, der über zahlreiche Erweiterungen, z. B. **Markdown All in One** oder **Live Preview**, individuell erweitert und angepasst werden kann. <span class="content-emoji">💡</span> Kleinere Änderungen nehme ich auch über **GitHub** selbst vor.

---

## 4. KI-Unterstützung

<span class="content-emoji">🤖</span> Für die Konzeption des SciBlogs iWIP sowie für die technische Umsetzung nutze ich die **KI ChatGPT**.  
Sie kommt insbesondere bei der **Ideensammlung**, der **Codeoptimierung**, der **Fehlersuche**, dem **Schreiben von Dokumentationen** sowie der **didaktischen Aufbereitung** von Inhalten zum Einsatz.

---

## 5. Didaktischer Planungsagent

Ein zentrales Element des SciBlog iWIP ist ein didaktischer Planungsagent, der die Entwicklung von Lehr-Lern-Inhalten unterstützt.

Der Agent verbindet den Arbeitszusammenhang:

**Planung → Blog → Präsentation**

Er arbeitet dialogisch und strukturierend und unterstützt insbesondere die didaktische Ausarbeitung von Inhalten. Der Blog dient dabei als zentrales Arbeitsdokument.

Weitere Informationen finden sich in der Agentendokumentation:  
→ [ai_agents/README.md](../../../../ai_agents/README.md)

---

## 6. Automatisierte Metadatenpflege

Zur Verbesserung der Auffindbarkeit und Interoperabilität werden Metadaten automatisiert gepflegt und aktualisiert.

Dies erfolgt über GitHub Actions, die Änderungen an Metadaten im Repository automatisiert committen können.

Dadurch können auch ohne manuelle Eingriffe Aktualisierungen im Repository entstehen.

Diese Automatisierung ist insbesondere für die Anbindung an OER-Infrastrukturen wie OERSI relevant.

---

## 7. Struktur  

- <span class="content-emoji">📂</span> **Repository:** <a href="https://github.com/MatthiasSoell/iWIP/" target="_blank" rel="noopener noreferrer"><code>https://github.com/MatthiasSoell/iWIP/</code></a>  
- <span class="content-emoji">🌍</span> **Homepage:** <a href="https://matthiassoell.github.io/iWIP/" target="_blank" rel="noopener noreferrer"><code>https://matthiassoell.github.io/iWIP/</code></a>

---

## 8. Zusammenarbeit  

- <span class="content-emoji">👥</span> Alle interessierten GitHub Nutzer:innen können über **Pull Requests** im Repository Beiträge oder Änderungen vorschlagen und so transparent dokumentiert als **Co-Autor:innen** am Projekt mitwirken.  
- <span class="content-emoji">🤝</span> **Collaborator:innen** können direkt im **Fork** <a href="https://github.com/kiwip2025/iWIP" target="_blank" rel="noopener noreferrer"><code>https://github.com/kiwip2025/iWIP</code></a> arbeiten, Beiträge erstellen und live unter <a href="https://kiwip2025.github.io/iWIP/" target="_blank" rel="noopener noreferrer"><code>https://kiwip2025.github.io/iWIP/</code></a> testen, bevor sie ihre Inhalte über Pull Requests in das Hauptprojekt einbringen.

---

<span id="versionierung-reifegrad-blogbeitraege"></span>

## 9. Versionierung & Reifegrad von Blogbeiträgen

**<span class="content-emoji">🛠️</span> Entwicklungslogik des SciBlog iWIP:** Neben der technischen Infrastruktur folgt der SciBlog iWIP einer transparenten Entwicklungslogik für Lehr-Lern-Einheiten.

Im SciBlog iWIP werden Lehr-Lern-Einheiten nicht nur veröffentlicht, sondern kontinuierlich weiterentwickelt.  
Um diesen Entwicklungsprozess transparent zu machen, werden zwei unterschiedliche Angaben ausgewiesen:

---

### <span class="content-emoji">🧩</span> Version (X.Y)

Die Version beschreibt **Veränderungen an der Struktur oder am Inhalt** einer Einheit.

- **X (Hauptversion)**  
  Eine neue Hauptversion (z. B. 2.0) bedeutet eine grundlegende didaktische Überarbeitung, etwa eine neue Zielgruppe, eine veränderte Struktur oder eine konzeptionelle Neuausrichtung.

- **Y (Unterversion)**  
  Unterversionen (z. B. 1.1, 1.2) markieren inhaltliche Ergänzungen, Präzisierungen, sprachliche Überarbeitungen oder kleinere didaktische Anpassungen.

Die Version macht sichtbar, **was sich verändert hat**.

---

### <span class="content-emoji">🚦</span> Reifegrad (Status)

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

## 10. Versionierung der Plattform und des didaktischen Planungsagenten

Die Versionierung erfolgt auf mehreren Ebenen:

- **Lehr-Lern-Einheiten (OER):** eigene Versionierung und Reifegrad (z. B. 1.0, „In Erprobung“), siehe [oben](#versionierung-reifegrad-blogbeitraege)
- **Plattform (SciBlog iWIP):** markiert größere Entwicklungsschritte (Version 1.1)
- **Agent:** eigenständige Versionierung (Version 1.0)

Kleinere technische Änderungen werden nicht versioniert.
