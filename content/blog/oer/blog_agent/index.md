---
title: "SciBlog iWIP und didaktischer Agent: Orientierung statt Tool Zoo"
author: "Prof. Dr. Matthias Söll"
date: 2026-06-03
lastmod: 2026-06-03
draft: false
permalink: "/blog/oer/blog_agent/"

description: >
  Der Beitrag zeigt Lehrenden, Hochschuldidaktiker:innen und Bildungswissenschaftler:innen, wie SciBlog iWIP und das dazugehörige didaktisch spezialisierte, dialogische und reflexive Agentensystem als zusammenhängende Infrastruktur für Lehre, Präsentationen und OER gedacht sind. Ausgehend von Erfahrungen mit einem wachsenden "Tool Zoo" in der Lehre erläutert er die Funktionen des Blogs, den Mehrwert eines blog-first-Workflows und die Rolle eines spezialisierten Agenten für didaktisch konsistente OER.

summary: >
  Der Beitrag erläutert, wie SciBlog iWIP und ein didaktisch spezialisierter Agent blog-first OER, Präsentationen und Reflexion konsistent zusammenführen.

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
  kind: "lesson"

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
    - id: "https://w3id.org/kim/educationalLevel/level_4"
      name: "Postsekundarer nicht-tertiärer Bereich"

  audience:
    - "Lehrende"
    - "Hochschuldidaktiker:innen"
    - "Bildungswissenschaftler:innen"
    - "Interessierte an Open Education und KI in der Lehre"

  keywords:
    - "SciBlog iWIP"
    - "didaktischer Agent"
    - "OER-Infrastruktur"
    - "blog-first-Workflow"
    - "Hochschuldidaktik"
    - "digitale Lehrplanung"
    - "Open Educational Practices"

  time_required: "PT25M"

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
  <button onclick="location.href='/iWIP/praesentation/oer/blog_agent/'" title="Zur Präsentationsansicht">🖥️</button>
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

## <span class="content-emoji">🧭</span> Hintergrund

In der Lehre erlebe ich seit einiger Zeit etwas, das viele Kolleg:innen vermutlich gut kennen: Die Zahl digitaler Werkzeuge wächst stetig. Neben **Word, PowerPoint, Excel, Bildbearbeitungstools und QR-Generatoren** <span class="content-emoji">💻</span> treten **Lernplattformen, Autorentools, KI-Anwendungen und OER-Werkzeuge** <span class="content-emoji">🌐</span>. Jedes einzelne Tool hat seine Berechtigung. Im Alltag entsteht jedoch schnell eher ein unübersichtlicher **"Tool Zoo"** <span class="content-emoji">🧭</span> als ein konsistenter Arbeitszusammenhang. Dabei trat mir der **didaktische Fokus** <span class="content-emoji">🎯</span> zu stark in den Hintergrund.

Der **SciBlog iWIP** ist aus genau dieser Erfahrung entstanden. Ziel war, einen **strukturierten Ort** <span class="content-emoji">🧩</span> zu schaffen, an dem sich **Lehrmaterialien, Visualisierungen, Reflexionen, Präsentationen und Automatisierungen** zusammenführen lassen. Gemeint sind dabei ausdrücklich auch wiederkehrende Arbeitsschritte wie **QR-Generierung, PDF-Generierung und Metadatenpflege** <span class="content-emoji">⚙️</span>, die in separaten Werkzeugketten sonst zusätzlichen Aufwand erzeugen (vgl. <a href="#literatur">SciBlog iWIP: Technische Infrastruktur</a>).

Die Vorstellung richtet sich an **Lehrende, Hochschuldidaktiker:innen und Bildungswissenschaftler:innen** <span class="content-emoji">👥</span> mit ersten KI-Vorkenntnissen, aber ohne Vorwissen zum **SciBlog iWIP** oder zum **Agentensystem**. Im Zentrum steht die Frage, wie eine offene, **Blog und Präsentation verbindende Infrastruktur** <span class="content-emoji">🤝</span> didaktische **Kohärenz**, **Transparenz** und **OER-Fähigkeit** unterstützen kann.

## <span class="content-emoji">💭</span> Ausgangsfrage

> [!TIPP]
> Wie lässt sich die **Kombination** aus **Blog** und **Präsentation** als **OER** sowie **didaktisch spezialisiertem, dialogischem und reflexivem KI-Agenten** so nutzen, dass Lehrmaterialien **didaktisch konsistent**, **transparent** und **anschlussfähig** bleiben?

## <span class="content-emoji">🎯</span> Lernziele

Die Teilnehmenden sollen nach der Vorstellung ...

- <span class="content-emoji">🧭</span> die **Entstehungsidee** des SciBlogs als Reaktion auf einen wachsenden "Tool Zoo" einordnen können.
- <span class="content-emoji">🌐</span> **zentrale Funktionen** des SciBlogs für Strukturierung, Selbststudium, OER und Präsentationsverknüpfung benennen können.
- <span class="content-emoji">🤖</span> den **didaktischen Mehrwert** eines **spezialisierten Agenten** gegenüber einem allgemeinen Chatbot oder einem Megaprompt nachvollziehen können.
- <span class="content-emoji">🪞</span> **Chancen** und **Grenzen** einer solchen Infrastruktur für die eigene Lehrpraxis reflektieren können.

## Ablauf

**Gesamtdauer:** ca. 25 Minuten ⏱️

<div class="agenda">

| Phase | Inhalt | Ziel | Zeit |
|:------|:--------|:------|:------:|
| **1. Einstieg <span class="content-emoji">💭</span>** | Persönlicher Zugang über den "Tool Zoo" und die Entstehungsidee des SciBlogs | Problem- und Praxisbezug herstellen | <span class="content-emoji">⏱️</span> 5 Min |
| **2. Blog zeigen <span class="content-emoji">🌐</span>** | Grundfunktionen des SciBlogs an einer Beispielseite demonstrieren | Struktur, OER-Mehrwert und Transparenz sichtbar machen | <span class="content-emoji">⏱️</span> 5 Min |
| **3. Agent erklären <span class="content-emoji">🤖</span>** | Komponenten des Agentensystems und impliziter Vergleich zu Chatbot und Megaprompt | didaktische Spezialisierung verständlich machen | <span class="content-emoji">⏱️</span> 5 Min |
| **4. Diskussion öffnen <span class="content-emoji">💬</span>** | Fragen, Kontroversen, Chancen und Risiken gemeinsam reflektieren | Anschluss an Hochschuldidaktik und Bildungswissenschaft herstellen | <span class="content-emoji">⏱️</span> 10 Min |

</div>

## Warum der SciBlog entstanden ist <span class="content-emoji">🧩</span>

Die **Ausgangsbeobachtung** <span class="content-emoji">🧭</span> ist alltagsnah: Lehrende arbeiten heute selten mit nur einem System. **Materialien** <span class="content-emoji">🧩</span> entstehen an unterschiedlichen Orten, werden in verschiedene Formate überführt, auf Lernplattformen verteilt, als OER nachgenutzt, mit Metadaten versehen und in Präsentationen oder PDFs transformiert. Diese **Vielfalt** <span class="content-emoji">🌐</span> kann produktiv sein, erhöht aber zugleich die Wahrscheinlichkeit für **Redundanz, Medienbrüche und organisatorische Überlastung** <span class="content-emoji">⚠️</span>.

Für mich lag das **Problem** <span class="content-emoji">💭</span> daher nicht in einem einzelnen Tool, sondern in der **Summe unverbundener Werkzeuge**. Die folgende Grafik illustriert diesen Ausgangspunkt. Aus **hochschuldidaktischer Sicht** <span class="content-emoji">🎯</span> verschiebt ein solcher Werkzeugüberschuss Aufmerksamkeit: Statt zuerst nach **Lernzielen, Struktur und Anschlussfähigkeit** zu fragen, dominiert schnell die operative Verwaltung von **Formaten, Plattformen und Übergängen** <span class="content-emoji">⚙️</span>.

<p class="grafic-title"><span class="content-emoji">🧭</span> Vom Tool Zoo zur integrierten Lehrumgebung</p>

{{< blog_image_overlay src="warum_blog.png" alt="Comicgrafik zum wachsenden Tool Zoo in der Lehre als Ausgangspunkt für den SciBlog iWIP" id="iwip_warum_blog_overlay" >}}

<p class="bildquelle">Bildquelle: Eigene Darstellung (erstellt mit ChatGPT) · Lizenz: <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener noreferrer">CC BY-SA 4.0</a></p>

Der **SciBlog iWIP** <span class="content-emoji">🧩</span> ist als Gegenentwurf dazu entstanden. Er ist kein weiteres isoliertes Tool, sondern ein **strukturierter Ort** zur Orientierung, Dokumentation und Weiterentwicklung von Lehre. Die **Leitidee** <span class="content-emoji">🤝</span> ist eine Umgebung, in der **Inhalte, Reflexion, Offenheit, Weiterverarbeitung und Automation** zusammenlaufen (vgl. <a href="#literatur">Warum SciBlog iWIP?</a>).

## Was der SciBlog leistet <span class="content-emoji">🌐</span>

An der **Beispielseite zur Hochschulbildung** (vgl. <a href="#literatur">Hochschulbildung</a>) lässt sich die **Grundfunktion** des SciBlogs gut zeigen. Die Seite ist kein digital abgelegtes Skript, sondern eine **strukturierte Lernressource** mit Leitfrage, Lernzielen, Ablauf, fachlichen Vertiefungen, Visualisierungen und transparenten Quellenbezügen. Gerade diese Kombination macht den Blog für Lehrpraxis und Selbststudium interessant.

Seine Funktionen lassen sich in sieben Punkten bündeln:

- <span class="content-emoji">🧭</span> **Strukturierte Aufbereitung von Inhalten:** Themen erscheinen nicht als lose Materialsammlung, sondern als nachvollziehbar gegliederte Lernressource mit Leitfrage, Lernzielen und Aufbau.
- <span class="content-emoji">🎨</span> **Verbindung von Text, Grafiken und Reflexion:** Fachliche Inhalte werden nicht nur beschrieben, sondern mit Visualisierungen und reflexiven Übergängen erschlossen.
- <span class="content-emoji">🧠</span> **Unterstützung des Selbststudiums:** Die Seiten sind so angelegt, dass auch ohne unmittelbare Lehrperson Orientierung möglich bleibt.
- <span class="content-emoji">🎓</span><span class="content-emoji">🌍</span><span class="content-emoji">🔓</span> **Bereitstellung als OER:** Materialien sollen nicht nur in einer Sitzung funktionieren, sondern offen nachnutzbar, bearbeitbar und weitergabefähig sein.
- <span class="content-emoji">🖥️</span> **Verknüpfung mit Präsentationen:** Aus dem Blog heraus können Präsentationsansichten abgeleitet werden; Lesen und Zeigen stehen damit nicht unverbunden nebeneinander.
- <span class="content-emoji">🪞</span> **Transparenz von Lehr-Lern-Prozessen:** Sichtbar wird nicht nur, *was* ein Thema ist, sondern auch, wie es didaktisch aufgebaut wurde.
- <span class="content-emoji">👨‍🔧</span> **Technische Nutzbarkeit:** Auf der Seite sind Funktionen wie Darkmode, Emoji-Ausblendung sowie Download als Markdown oder PDF eingebunden. Hinzu kommen übliche Browserfunktionen wie Zoom, Übersetzung und die Nutzung auf Computer, Beamer, Tablet oder Smartphone.

Pointiert lässt sich der SciBlog so beschreiben:

> [!QUOTE]
> Der **SciBlog iWIP** <span class="content-emoji">🧩</span> ist für mich kein digitales Regal, in dem ich Materialien ablege. Er ist ein **Arbeits- und Publikationsraum** <span class="content-emoji">🌐</span>, in dem Inhalte **strukturiert, visualisiert, reflektiert, offen bereitgestellt** und bei Bedarf direkt in **Präsentationen** <span class="content-emoji">🖥️</span> überführt werden können.

## Warum der Agent kein allgemeiner Chatbot ist <span class="content-emoji">🤖</span>

Aus diesem **Grundverständnis des Blogs** <span class="content-emoji">🧩</span> ergibt sich die Frage, wie die Entwicklung meiner Materialien **konsistent unterstützt** <span class="content-emoji">🤝</span> werden kann. An dieser Stelle kommt das **Agentensystem** <span class="content-emoji">🤖</span> ins Spiel. Inspiriert wurde ich dabei vom <a href="https://github.com/LiaScript/teaching-agent" target="_blank" rel="noopener noreferrer">**Teaching-Agent 🎓**</a> von **LiaScript** <span class="content-emoji">🌐</span> von **André Dietrich**.

Die entscheidende **Pointe** <span class="content-emoji">💡</span> lautet: Der Agent ist kein **allgemeiner Chatbot** <span class="content-emoji">💬</span> für beliebige Anfragen, sondern ein **didaktisch spezialisierter Arbeitsraum** <span class="content-emoji">🎓</span>. Seine Aufgabe besteht darin, **dialogisch und reflexiv** <span class="content-emoji">🪞</span> Planung, Wissensbasis, Vorlagen und Kontext so zu verbinden, dass daraus **konsistente Blogbeiträge** <span class="content-emoji">🌐</span> und ableitbare **Reveal-Präsentationen** <span class="content-emoji">🖥️</span> entstehen.

<p class="grafic-title">Grundfunktion des didaktischen Agentensystems</p>

{{< blog_image_overlay src="grundfunktionen_agent.png" alt="Grafik zur Grundfunktion des didaktischen Agentensystems mit Eingaben, Verarbeitung und Ausgabe für Blog und Präsentation" id="iwip_grundfunktion_agent_overlay" >}}

<p class="bildquelle">Bildquelle: Eigene Darstellung (erstellt mit ChatGPT) · Lizenz: <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener noreferrer">CC BY-SA 4.0</a></p>

Die Grafik macht sichtbar, dass der Agent nicht einfach "Text generiert", sondern mehrere Ebenen koordiniert:

- <span class="content-emoji">🧭</span> **Didaktische Orientierungen:** Sie sorgen dafür, dass Lernziele, Struktur, Aktivität und Reflexion nicht zufällig zusammengewürfelt werden.
- <span class="content-emoji">📚</span> **Wissensdatenbank:** Sie hält fachliche und projektspezifische Bezugspunkte verfügbar, damit Inhalte nicht jedes Mal neu aus dem Nichts formuliert werden müssen.
- <span class="content-emoji">🧩</span> **Vorlagen:** Sie geben Formate, Metadaten und Strukturen vor, damit Blog und Präsentation nicht nur sprachlich, sondern auch formal konsistent bleiben.
- <span class="content-emoji">📌</span> **Kontext:** Dazu gehören Zielgruppe, Thema, Material, Pfade und Arbeitsstand. Erst dieser Kontext macht aus abstrakten Regeln eine passende Ausarbeitung.

Aus dieser Verbindung entstehen dann nicht beliebige Texte, sondern konkrete OER-Artefakte:

- <span class="content-emoji">🌐</span> Blogbeiträge als Primärartefakte
- <span class="content-emoji">🖥️</span> Reveal-Präsentationen als abgeleitete Sekundärartefakte
- <span class="content-emoji">🏷️</span> Metadatenvorschläge für Auffindbarkeit, Dokumentation und Weiterverarbeitung

Weiterführende Informationen zum Agentensystem finden Sie direkt im Repository:

- Die Agentendokumentation in der <a href="https://github.com/MatthiasSoell/iWIP/blob/main/ai_agents/README.md" target="_blank" rel="noopener noreferrer">README des Agentenbereichs</a>.
- Die didaktischen Orientierungen im <a href="https://github.com/MatthiasSoell/iWIP/blob/main/ai_agents/didaktisches_qualitaetsmodell.md" target="_blank" rel="noopener noreferrer">didaktischen Qualitätsmodell</a>.
- Die fortlaufend aktualisierte Wissensbasis in der <a href="https://github.com/MatthiasSoell/iWIP/blob/main/ai_agents/blog_wissensbasis.md" target="_blank" rel="noopener noreferrer">Wissensbasis des Blogs</a>.
- Die Vorlagen unter den <a href="https://github.com/MatthiasSoell/iWIP/tree/main/ai_agents/templates" target="_blank" rel="noopener noreferrer">Templates</a> und die Prompts im Ordner <a href="https://github.com/MatthiasSoell/iWIP/tree/main/prompts" target="_blank" rel="noopener noreferrer">prompts</a>; zentral ist dabei <a href="https://github.com/MatthiasSoell/iWIP/blob/main/prompts/plan.md" target="_blank" rel="noopener noreferrer">plan.md</a>.
- Das gesamte Projekt im <a href="https://github.com/MatthiasSoell/iWIP" target="_blank" rel="noopener noreferrer">Repository SciBlog iWIP</a> sowie die übergreifende <a href="https://github.com/MatthiasSoell/iWIP/blob/main/README.md" target="_blank" rel="noopener noreferrer">README des Repositories</a>.

## Chatbot, Megaprompt oder spezialisierter Agent? <span class="content-emoji">🧠</span>

Zur **Einordnung** <span class="content-emoji">🧭</span> ist ein Vergleich mit **Chatbots** <span class="content-emoji">💬</span> und **Megaprompts** <span class="content-emoji">🧾</span> hilfreich.

Ein **allgemeiner Chatbot** <span class="content-emoji">💬</span> ist stark, wenn schnell **Ideen, Formulierungen oder erste Strukturvorschläge** <span class="content-emoji">💡</span> gebraucht werden. Seine Stärke liegt in der **situativen Reaktion** <span class="content-emoji">⚡</span>. Ein **Megaprompt** <span class="content-emoji">🧾</span> bündelt mehr **Kontext** und **Vorgaben** in einer Eingabe. Das kann die **Qualität** <span class="content-emoji">📈</span> deutlich verbessern, bleibt im Vergleich zu **Agenten** <span class="content-emoji">🤖</span> aber fragil: Wenn sich Kontext ändert, muss viel neu zusammengesetzt werden; **Konsistenz über mehrere Artefakte hinweg** <span class="content-emoji">🧩</span> bleibt aufwändig.

Der hier genutzte **Agent** <span class="content-emoji">🤖</span> geht einen **Schritt weiter** <span class="content-emoji">🚶</span>. Er bindet nicht nur viel Kontext auf einmal, sondern organisiert wiederkehrend das Zusammenspiel von **didaktischen Regeln, Wissensbeständen, Vorlagen und Zielartefakten** <span class="content-emoji">🧠</span>. Dadurch verschiebt sich der **Nutzen** <span class="content-emoji">🎯</span>: Weg von bloßer **Textproduktion** <span class="content-emoji">📝</span>, hin zu **konsistenter Artefaktentwicklung** <span class="content-emoji">🧩</span>.

<p class="grafic-title">Drei Arbeitsweisen im Vergleich</p>

| Format | Primäre Stärke | Typische Grenze | Didaktischer Mehrwert für OER |
|:------|:---------------|:----------------|:------------------------------|
| **Allgemeiner Chatbot <span class="content-emoji">💬</span>** | schnelle Antworten, Ideen, Umformulierungen | Kontext bleibt oft situativ und flüchtig | hilfreich für Einzelschritte, aber begrenzt für konsistente Gesamtartefakte |
| **Megaprompt <span class="content-emoji">🧾</span>** | viel Kontext in einer Eingabe bündelbar | Pflege und Wiederverwendung werden schnell komplex | kann Qualität heben, bleibt aber oft schwer wartbar |
| **Spezialisierter Agent <span class="content-emoji">🤖</span>** | verbindet Regeln, Wissensbasis, Templates und Kontext dauerhaft | braucht vorbereitete Struktur und Pflege | unterstützt didaktisch konsistente Blog- und Präsentationsentwicklung |

<p class="bildquelle">Bildquelle: Eigene Darstellung · Lizenz: <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener noreferrer">CC BY-SA 4.0</a></p>

Die Differenz lässt sich so zuspitzen:

> [!TIPP]
> Der entscheidende Mehrwert des Agenten liegt darin, didaktisch konsistente OER entlang eines **blog-first-Workflows** <span class="content-emoji">🌐</span> strukturiert zu unterstützen.

## Wie der Agent didaktisch konsistente OER unterstützt <span class="content-emoji">🎓</span>

**Hochschuldidaktisch interessant** <span class="content-emoji">🎓</span> wird das System dort, wo es **Kohärenz** <span class="content-emoji">🧭</span> stützt. Ein **spezialisierter Agent** <span class="content-emoji">🤖</span> kann dazu beitragen, dass **Lernziele, Inhalte, Struktur, Visualisierung, Reflexion und Präsentationsüberführung** <span class="content-emoji">🧩</span> nicht unabhängig voneinander entstehen. Genau das ist für **OER** <span class="content-emoji">🌍</span> relevant, weil offene Materialien nicht nur **auffindbar, nachvollziehbar, anschlussfähig und bearbeitbar** <span class="content-emoji">🔓</span> sein sollten.

Der **blog-first-Workflow** <span class="content-emoji">🌐</span> ist dafür entscheidend. Zuerst entsteht ein **strukturiertes Primärartefakt im Blog** <span class="content-emoji">📝</span>, das **fachliche Ausarbeitung, didaktische Struktur, Visualisierungen, Quellen und Metadaten** <span class="content-emoji">🧠</span> bündelt. Erst danach wird daraus eine **Präsentation** <span class="content-emoji">🖥️</span> abgeleitet. So werden **Blog und Folien** <span class="content-emoji">🤝</span> nicht zu zwei lose verbundenen Parallelwelten.

Aus bildungswissenschaftlicher Sicht lassen sich daran mindestens vier Stärken hervorheben:

- <span class="content-emoji">🧭</span> **Kohärenz:** Ziele, Inhalte und Darstellung werden gemeinsam iterativ entwickelt.
- <span class="content-emoji">🪞</span> **Reflexivität:** Die Struktur des Materials bleibt sichtbar und damit diskutierbar.
- <span class="content-emoji">🌱</span> **Nachnutzbarkeit:** OER entsteht in einer Form, die Bearbeitung und Weitergabe unterstützt.
- <span class="content-emoji">🤝</span> **Entlastung:** Wiederkehrende formale und technische Anforderungen werden stärker systematisiert.

Zugleich bleiben **Grenzen** <span class="content-emoji">⚠️</span> wichtig:

> [!IMPORTANT]
> Ein **Agent** <span class="content-emoji">🤖</span> ersetzt weder **fachliche Verantwortung** noch **didaktisches Urteil** <span class="content-emoji">🪞</span>. Er kann **Struktur stabilisieren** <span class="content-emoji">🧭</span>, aber keine **pädagogische Verantwortung automatisieren** <span class="content-emoji">⚠️</span>. 
> 
> Genau deshalb ist die **Kombination aus Spezialisierung und menschlicher Entscheidung** <span class="content-emoji">🤝</span> hier zentral.

## Fragen und Diskussion <span class="content-emoji">💬</span>

Für die abschließende Diskussion ist vor allem interessant, welche Elemente einer solchen Infrastruktur in der eigenen Praxis tatsächlich entlasten, wo sie didaktisch überzeugen und an welchen Stellen bewusster Widerspruch nötig bleibt.

<a id="literatur"></a>
## Literatur und Quellen

Repository SciBlog iWIP auf github.com. Verfügbar unter: <a href="https://github.com/MatthiasSoell/iWIP" target="_blank" rel="noopener noreferrer">https://github.com/MatthiasSoell/iWIP</a>

LiaScript: Teaching-Agent. Verfügbar unter: <a href="https://github.com/LiaScript/teaching-agent" target="_blank" rel="noopener noreferrer">https://github.com/LiaScript/teaching-agent</a>

SciBlog iWIP: Beispielseite Hochschulbildung. Verfügbar unter: <a href="https://matthiassoell.github.io/iWIP/blog/lehre/bisy/hochschulbildung/" target="_blank" rel="noopener noreferrer">https://matthiassoell.github.io/iWIP/blog/lehre/bisy/hochschulbildung/</a>

SciBlog iWIP: Technische Infrastruktur. Verfügbar unter: <a href="https://matthiassoell.github.io/iWIP/blog/doku/doku_tech/" target="_blank" rel="noopener noreferrer">https://matthiassoell.github.io/iWIP/blog/doku/doku_tech/</a>

SciBlog iWIP: Warum SciBlog iWIP? – Motivation, Funktionen, Learnings. Verfügbar unter: <a href="https://matthiassoell.github.io/iWIP/blog/oer/warum_sciblog/" target="_blank" rel="noopener noreferrer">https://matthiassoell.github.io/iWIP/blog/oer/warum_sciblog/</a>
