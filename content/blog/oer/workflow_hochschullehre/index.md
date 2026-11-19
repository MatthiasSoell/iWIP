---
title: "Vor lauter Tools keine Zeit zum Planen? Mein neuer Workflow für die Hochschullehre"
author: "Prof. Dr. Matthias Söll"
date: 2026-11-17
lastmod: 2026-11-17
draft: false
permalink: "/blog/oer/workflow_hochschullehre/"

description: >
  Der Beitrag zeigt Hochschullehrenden, wie ein integrierter Workflow didaktische Planung mit einem KI-Agenten, Bloginhalte, Präsentationen und OER verbindet.
  Die persönliche Erfahrung regt dazu an, Mehrfacharbeit zu reduzieren und mehr Zeit für didaktische Reflexion zu gewinnen.

summary: >
  Ein persönlicher Workflow verbindet didaktische Planung im KI-Dialog, Blog, Präsentationen und OER und schafft mehr Raum für die Gestaltung der Hochschullehre.

tags:
  - OER
  - SciBlog iWIP
  - Hochschullehre
  - Hochschuldidaktik
  - Künstliche Intelligenz
  - Agentensysteme
  - Lehrplanung
  - Open Educational Practices

categories:
  - OER
  - Lehre
  - Hochschuldidaktik

oer:
  is_oer: true
  kind: "article"

  creators:
    - type: "Person"
      name: "Prof. Dr. Matthias Söll"
      given_name: "Matthias"
      family_name: "Söll"
      affiliation:
        name: "Universität Rostock"
        id: "https://ror.org/03zdwsf69"
        url: "https://www.uni-rostock.de/"
        type: "Organization"
      url: "https://www.iwip.uni-rostock.de/institut/iwip/team/prof-dr-matthias-soell/"
      orcid: "https://orcid.org/0000-0002-9717-3017"

  publisher:
    name: "SciBlog iWIP"
    url: "https://matthiassoell.github.io/iWIP/"

  license:
    label: "CC BY-SA 4.0"
    url: "https://creativecommons.org/licenses/by-sa/4.0/"

  image: "https://matthiassoell.github.io/iWIP/images/og/og_sciblog_default.jpg"

  version: "1.0"
  status: "pilot"

  in_language:
    - "de"

  learning_resource_type:
    - id: "https://w3id.org/kim/hcrt/text"
      name: "Text"

  educational_level:
    - id: "https://w3id.org/kim/educationalLevel/level_A"
      name: "Hochschule"

  audience:
    - "Hochschullehrende"

  keywords:
    - "Didaktische Lehrplanung"
    - "KI-gestützte Reflexion"
    - "Hochschullehre"
    - "SciBlog iWIP"
    - "Open Educational Resources"
    - "Mehrfachnutzung von Lehrmaterialien"
    - "Integrierter Workflow"

  time_required: "PT2M"

  about:
    - id: "https://w3id.org/kim/hochschulfaechersystematik/n270"
      name: "Berufs- und Wirtschaftspädagogik"
    - id: "https://w3id.org/kim/hochschulfaechersystematik/n181"
      name: "Wirtschaftspädagogik"
    - id: "https://w3id.org/kim/hochschulfaechersystematik/n33"
      name: "Erziehungswissenschaften"

  todos: []
---

<div class="top-toggle">
  <button id="md-copy-btn" title="Markdown kopieren (ohne Bilder)">📑</button>
  <button onclick="triggerPrint()" title="Blog speichern">📥</button>
  <button onclick="location.href='/iWIP/praesentation/oer/workflow_hochschullehre/'" title="Zur Präsentationsansicht">🖥️</button>
  <button class="iwip_help_btn"
        type="button"
        aria-haspopup="dialog"
        aria-controls="iwip_help_overlay"
        aria-expanded="false"
        title="Hinweise zur Nutzung">
  ⓘ
  </button>
</div>

{{< oer-meta >}}

Digitale Werkzeuge sollen uns die Lehre erleichtern. Aber was passiert, wenn wir irgendwann mehr Zeit mit ihrer Bedienung als mit der eigentlichen didaktischen Planung verbringen? Genau diese Frage hat mich dazu gebracht, meinen bisherigen Workflow grundlegend zu überdenken.

## <span class="content-emoji">💻</span> Mein Ausgangspunkt: Zu viele Tools!

Word für die Planung, PowerPoint für Präsentationen, verschiedene Programme für Materialien und Stud.IP für die Bereitstellung. Dazu noch KI und die Veröffentlichung als Open Educational Resources (OER).

Irgendwann hatte ich den Eindruck, mehr Zeit mit der Bedienung unterschiedlicher Werkzeuge als mit der eigentlichen didaktischen Planung zu verbringen.

**Das wollte ich ändern! 🔄**

<p class="grafic-title">Vor lauter Tools keine Zeit zum Planen!</p>
{{< blog_image_overlay src="tool_chaos.png" alt="Comic: Ein überforderter Lehrender zwischen zahlreichen digitalen Werkzeugen und Dateiformaten; KI kommt als weiteres Werkzeug hinzu." id="iwip_workflow_tool_chaos_overlay" >}}
<p class="bildquelle">Bildquelle: Eigene Darstellung (erstellt mit ChatGPT) · Lizenz: <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener noreferrer">CC BY-SA 4.0</a></p>

## <span class="content-emoji">🤖</span> Meine Lösung: Ein integrierter Workflow

Statt immer neue Werkzeuge in meinen bisherigen Arbeitsprozess einzubauen, habe ich versucht, diesen grundsätzlich anders zu organisieren. Entstanden ist ein Workflow, in dem vier Schritte ineinandergreifen:

- <span class="content-emoji">💬</span> **Dialogisch planen:** Ein eigens konfigurierter KI-Agent hinterfragt meine didaktischen Entscheidungen, liefert Ideen und unterstützt meine Reflexion. Die Entscheidungen treffe weiterhin ich.
- <span class="content-emoji">🎨</span> **Inhalte entwickeln:** Die Ergebnisse veröffentliche ich in meinem Lehreblog in Markdown auf einer Hugo Umgebung. Texte, Bilder und weitere Medien bilden dort eine gemeinsame Inhaltsbasis.
- <span class="content-emoji">💻</span> **Präsentationen ableiten:** Aus den Bloginhalten entstehen teilautomatisiert Reveal-Präsentationen. So muss ich die Inhalte nicht mehrfach entwickeln.
- <span class="content-emoji">🎓🌍🔓</span> **Offen veröffentlichen:** Die Materialien veröffentliche ich unter einer offenen Lizenz, sodass sie als OER nachgenutzt und weiterentwickelt werden können.

<p class="grafic-title">Mein Workflow vom didaktischen Dialog zur Veröffentlichung</p>
{{< blog_image_overlay src="workflow.png" alt="Vier aufeinanderfolgende Schritte: dialogische und reflexive Planung mit KI bei menschlicher Entscheidungshoheit, Blog aus Markdown und Medien, teilautomatisch abgeleitete Reveal-Präsentation sowie Veröffentlichung und Nachnutzung als OER." id="iwip_workflow_workflow_overlay" >}}
<p class="bildquelle">Bildquelle: Eigene Darstellung (erstellt mit ChatGPT) · Lizenz: <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener noreferrer">CC BY-SA 4.0</a></p>

Der entscheidende Unterschied liegt für mich nicht allein in der technischen Integration. <span class="content-emoji">🪞</span> **Ich plane inzwischen anders:** Im Dialog mit dem KI-Agenten hinterfrage ich meine Überlegungen bewusster, während die technische Verarbeitung der Materialien weniger Aufmerksamkeit beansprucht.

Wie mein [didaktischer KI-Agent](https://matthiassoell.github.io/iWIP/blog/oer/blog_agent/) funktioniert und [warum ich den SciBlog entwickelt habe](https://matthiassoell.github.io/iWIP/blog/oer/warum_sciblog/), habe ich an anderer Stelle ausführlicher beschrieben.

## <span class="content-emoji">🎓</span> Und was haben die Studierenden davon?

Die gemeinsame Inhaltsbasis bietet auch in der Lehrveranstaltung Vorteile: Während die Präsentation über den Beamer läuft, können Studierende die Inhalte gleichzeitig auf Laptop, Tablet oder Smartphone aufrufen und beispielsweise in ihre persönlichen Notizsysteme übernehmen.

Die Materialien bleiben außerdem über die Lehrveranstaltung hinaus zugänglich 🔓.

<p class="grafic-title">Mein Workflow im Seminarraum</p>
{{< blog_image_overlay src="seminarraum.png" alt="Comic eines Seminars: Der Lehrende zeigt den vierstufigen Workflow auf der Leinwand; Studierende nutzen die Bloginhalte parallel auf Laptops, Tablets und Smartphones." id="iwip_workflow_seminarraum_overlay" >}}
<p class="bildquelle">Bildquelle: Eigene Darstellung (erstellt mit ChatGPT) · Lizenz: <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener noreferrer">CC BY-SA 4.0</a></p>

## <span class="content-emoji">💡</span> Mein Fazit: Mehr Raum für Didaktik

Natürlich erfordert ein solcher Workflow zunächst Zeit und technisches Know-how 🛠️. Aber für mich hat sich der Aufwand gelohnt: Ich muss weniger Inhalte doppelt bearbeiten und gewinne mehr Raum für die didaktische Gestaltung.

Vor allem hat sich meine Planung verändert. Der kritische Dialog mit dem KI-Agenten eröffnet zusätzliche Möglichkeiten, didaktische Entscheidungen zu reflektieren und weiterzuentwickeln.

Dafür braucht es nicht zwingend dieselben Werkzeuge. <span class="content-emoji">🌱</span> **Die Grundidee ist übertragbar: Inhalte einmal entwickeln, vielfältig nutzen und die gewonnene Zeit in die Qualität der Lehre investieren.**

Denn am Ende geht es nicht darum, möglichst viele digitale Tools einzusetzen, sondern darum, sie so einzusetzen, dass wieder mehr Zeit für gute Didaktik bleibt.
