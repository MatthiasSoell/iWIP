---
title: "Warum SciBlog iWIP? – Motivation, Funktionen, Learnings"
author: "Prof. Dr. Matthias Söll"
date: 2025-12-17
lastmod: 2025-12-17
draft: false
permalink: "/blog/oer/warum_sciblog/"

description: >
  Der Beitrag beschreibt die Entwicklung des SciBlog iWIP als integrierte Lehr-Lern-Umgebung.
  Ausgehend von der persönlichen Lehrpraxis werden Herausforderungen der Tool-Akkumulation,
  der OER-Arbeit und der digitalen Lehrplanung reflektiert und didaktisch begründete
  Gestaltungsentscheidungen erläutert.

summary: >
  Der Beitrag erläutert Motivation, Funktionen und zentrale Learnings aus der Entwicklung
  des SciBlog iWIP als integrierte, offen lizenzierte Lehr-Lern-Umgebung für Hochschule
  und berufliche Bildung.

tags:
  - OER
  - Open Educational Resources
  - Offene Bildung
  - Hochschullehre
  - Berufliche Bildung
  - Lehrplanung
  - Digitale Lehre
  - Künstliche Intelligenz
  - Wissenschaftskommunikation

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
        name: "Universität Rostock · Institut für Wirtschaftspädagogik"
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
  status: "pilot"   # draft | pilot | stable | aligned

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
    - "Studierende"
    - "Lehrende"
    - "Hochschuldidaktiker:innen"
    - "Interessierte an Open Education"

  keywords:
    - "Open Educational Resources"
    - "Offene Bildung"
    - "Digitale Lehr-Lern-Umgebungen"
    - "Lehrplanung"
    - "Hochschuldidaktik"
    - "Berufliche Bildung"
    - "Künstliche Intelligenz in der Lehre"
    - "Open Educational Practices"

  time_required: "PT20M"

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
  <button onclick="location.href='/iWIP/praesentation/oer/warum_sciblog/'" title="Zur Präsentationsansicht">🖥️</button>
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

## 1. Motivation: Wie es zur Idee kam <span class="content-emoji">🧭</span>

### Die 2010er-Jahre: Lehre als gut beherrschbares Handwerk <span class="content-emoji">🧩😄</span>

Ich habe meine Lehre schon immer gerne vorbereitet <span class="content-emoji">👨‍🏫</span>. Besonders reizvoll fand ich dabei weniger das „Abarbeiten von Stoff“, sondern das Nachdenken darüber, **wer meine Zielgruppe ist**, was sie mitbringt – und wie Inhalte so aufbereitet werden können, dass sie verständlich, anschlussfähig und **lernförderlich** [(Wernke & Zierer 2017)](/iWIP/blog/oer/warum_sciblog/#-literatur) sind <span class="content-emoji">🧠</span><span class="content-emoji">🎯</span>. Um die Lernendenperspektive zu fokussieren, habe ich bspw. auch die Methode *Unterrichtsplanung in Drehbuchform* entwickelt [(Söll & Klusmeyer 2022)](/iWIP/blog/oer/warum_sciblog/#-literatur).

In den 2010er-Jahren sah diese Vorbereitung noch vergleichsweise überschaubar aus:  
Konzepte entstanden in **Word**, Präsentationen in **PowerPoint**, Bilder wurden mit **GIMP** bearbeitet <span class="content-emoji">🎨</span>. Die Materialien lagen sauber sortiert auf **Netzlaufwerken** <span class="content-emoji">💻</span><span class="content-emoji">🌐</span>.

---

### Mitte der 2010er-Jahre: Digitale Lehr-Lern-Arrangements und wachsende Komplexität <span class="content-emoji">⚙️</span><span class="content-emoji">🙂</span>

Mit dem Aufkommen der ersten **Learning-Management-Systeme** <span class="content-emoji">🌐</span> veränderte sich die Lehrvorbereitung spürbar. Präsentationen wurden als **PDF** exportiert, in **ILIAS**, **Moodle** oder **Stud.IP** eingepflegt und mit **Metadaten** versehen <span class="content-emoji">🏷️</span>. Lehrmaterialien wurden versioniert, aktualisiert und erneut hochgeladen <span class="content-emoji">🔁</span>.

Ab etwa der Mitte der 2010er-Jahre gestaltete ich zunehmend **parallele Online-Lehr-Lern-Arrangements** <span class="content-emoji">👥</span><span class="content-emoji">💻</span>. **Videos** und **interaktive Elemente** hielten zusätzlich Einzug <span class="content-emoji">🎬</span><span class="content-emoji">🧩</span>. Die Datenmengen wuchsen, die Anzahl der zu pflegenden **Metadaten** ebenfalls <span class="content-emoji">🗂️</span>. Was zunächst nach Fortschritt aussah, fühlte sich in meinem Alltag immer häufiger nach **Redundanz** an <span class="content-emoji">🤹‍♂️</span><span class="content-emoji">💭</span>.

---

### Die 2020er-Jahre: OER, Metadaten und der Kipppunkt <span class="content-emoji">📈</span><span class="content-emoji">😖</span>

Spätestens in den 2020er-Jahren, mit meiner Beschäftigung mit **<span class="content-emoji">🎓</span><span class="content-emoji">🌍</span><span class="content-emoji">🔓</span> Open Educational Resources (OER)**, erreichte diese Entwicklung einen Kipppunkt <span class="content-emoji">🪞</span>.  
Zu den bestehenden Systemen kamen neue Werkzeuge hinzu: OER-Autorentools wie **Lumi** oder **H5P** <span class="content-emoji">🧩</span><span class="content-emoji">💻</span> sowie Repositorien wie **twillo** oder **HUBBS** <span class="content-emoji">🌐</span>.

Die Anforderungen an **Lizenzierung**, **Dokumentation** und **Metadatenpflege** wurden berechtigterweise höher 📑<span class="content-emoji">🏷️</span> – der organisatorische Aufwand aber ebenfalls. Meine Stimmung in der Lehrvorbereitung: angespannt <span class="content-emoji">😕</span>.

An diesem Punkt stellte sich für mich eine einfache, aber grundlegende Frage <span class="content-emoji">💭</span><span class="content-emoji">🧭</span>: **Muss das wirklich so kleinteilig, redundant und fragmentiert sein?**

---

## 2. Vom Tool-Zoo zur integrierten Umgebung <span class="content-emoji">🧭</span><span class="content-emoji">🧩</span>

Rückblickend lässt sich meine Lehrvorbereitung über viele Jahre gut als ein wachsender **Tool-Zoo** beschreiben <span class="content-emoji">🦒</span><span class="content-emoji">🦉</span><span class="content-emoji">🐘</span>.  
Jedes neue Werkzeug hatte für sich genommen seine Berechtigung – oft sogar klare didaktische Vorteile. Das Problem war nicht das einzelne Tool, sondern die **Summe**.

### Immer mehr Werkzeuge – und immer mehr Brüche <span class="content-emoji">🧩</span><span class="content-emoji">⚙️</span>

Über die Jahre kamen zahlreiche Programme, Plattformen und Formate zusammen:

- **Textverarbeitung**, **Präsentationssoftware** und **Bildbearbeitung**
- **Learning-Management-Systeme** für Organisation und Verteilung <span class="content-emoji">🌐</span>
- **Videoformate**, **interaktive Elemente** und **Online-Aktivitäten** <span class="content-emoji">🎬</span>
- **OER-Autorentools**, **Repositorien** und **Lizenzmodelle** <span class="content-emoji">🎓</span><span class="content-emoji">🌍</span><span class="content-emoji">🔓</span>
- unterschiedliche **Metadatenstandards**, **Exporte** und **Versionen** <span class="content-emoji">🏷️</span><span class="content-emoji">📄</span>

Jedes dieser Elemente erfüllte eine Funktion.  
Gemeinsam erzeugten sie jedoch **Brüche im Arbeitsprozess**: Medienbrüche, Systembrüche – und nicht zuletzt **Denkbrüche** <span class="content-emoji">🪞</span>.

Didaktische Planung, technische Umsetzung und Veröffentlichung fielen zunehmend auseinander. Inhalte mussten mehrfach angepasst, konvertiert und dokumentiert werden. Änderungen an einer Stelle zogen neue Arbeit an anderer Stelle nach sich <span class="content-emoji">🔁</span>.

---

### Komplexität als didaktisches Problem <span class="content-emoji">🧠</span><span class="content-emoji">⚠️</span>

Irgendwann wurde klar:  
Diese Komplexität war **nicht nur ein organisatorisches**, sondern auch ein **didaktisches Problem**.

Statt mich auf Fragen zu konzentrieren wie:

- *Was sollen die Studierenden hier eigentlich lernen?* <span class="content-emoji">🎯</span>  
- *Wie greifen Inhalte, Aufgaben und Reflexion ineinander?* <span class="content-emoji">🧠</span>  
- *Was ist zentral – und was kann vertiefend angeboten werden?* <span class="content-emoji">🧭</span>  

banden technische Fragen immer mehr Aufmerksamkeit:

- *In welchem System liegt was?*  
- *Welche Daten muss ich konvertieren?*  
- *Wo müssen Metadaten nachgepflegt werden?*  

Die Gefahr war spürbar: **Lehre wird verwaltet statt gestaltet**.

---

### Die Schlüsselfrage: Integration statt Addition <span class="content-emoji">🔄</span><span class="content-emoji">🎯</span>

Der Wendepunkt war keine neue Software, sondern eine **konzeptionelle Entscheidung** <span class="content-emoji">💭</span><span class="content-emoji">🧭</span>:

> [!TIPP]
> **Was wäre, wenn Lehre nicht aus vielen verbundenen Tools besteht,  
> sondern aus einer integrierten Umgebung, die didaktische Logik abbildet?**

Statt Inhalte immer wieder neu zu exportieren, hochzuladen und anzupassen, sollte es einen **zentralen Ort** geben:

- für **didaktische Planung** <span class="content-emoji">🧭</span>  
- für **Materialerstellung** <span class="content-emoji">🎨</span>  
- für **Veröffentlichung** <span class="content-emoji">🌐</span>  
- für **Offenheit und Nachnutzung** <span class="content-emoji">🎓</span><span class="content-emoji">🌍</span><span class="content-emoji">🔓</span>  

Nicht als starres System, sondern als **flexible Struktur**, die sich an der Logik von Lehre orientiert – nicht umgekehrt.

---

### Reduktion als Gewinn <span class="content-emoji">🌱</span>

Der entscheidende Schritt bestand daher nicht darin, *noch mehr* zu integrieren,  
sondern **konsequent zu reduzieren** <span class="content-emoji">✂️</span><span class="content-emoji">🧩</span>:

- weniger Formate  
- weniger Konvertierungen  
- weniger doppelte Pflege  
- weniger Orte, an denen Inhalte „leben“
- Automatisierung zur Entlastung für wiederkehrende Funktionen

Was blieb, waren nur die Werkzeuge, die **wirklich gebraucht** werden – eingebettet in eine Umgebung, die **Kohärenz** statt Fragmentierung erzeugt <span class="content-emoji">🤝</span><span class="content-emoji">🧠</span>.

Aus dieser Reduktion heraus wurde der Weg frei für das, was mir in der Lehre eigentlich wichtig ist:  
**Die Perspektive der Studierenden – und Lernprozesse, Inhalte, Reflexion** <span class="content-emoji">👥</span><span class="content-emoji">🎯</span>.



### Der Perspektivwechsel: Der Perspektivwechsel: Integration statt Tool-Logik <span class="content-emoji">🎯</span><span class="content-emoji">😁</span>

> [!TIPP]
> Die entscheidende Idee war, nicht noch ein weiteres Tool zu suchen, sondern die **Perspektive zu wechseln**: weg von einzelnen Anwendungen – hin zu einer integrierten **Software-Umgebung für die Lehre** <span class="content-emoji">💻</span><span class="content-emoji">🎯</span>.

Inspiriert durch meine Kollegin **Silvia Retzlaff** sowie durch die Arbeit der [oer.community](https://oer.community) im OE_COM-Projekt **FOERBICO** <span class="content-emoji">🤝</span><span class="content-emoji">🌱</span>, erinnerte ich mich – unter leichtem sozialem Druck <span class="content-emoji">😉</span> – an meine eigenen Programmieranfänge in der Jugend <span class="content-emoji">👨‍💻</span>.

Als ich mich intensiver mit dem Gedanken beschäftigte, dass das **Web selbst** – und insbesondere **HTML** – eine ausgesprochen **OER-freundliche Umgebung** ist <span class="content-emoji">🌍</span><span class="content-emoji">🔓</span>, fiel meine Entscheidung:  

Ich baue mir eine **eigene, internetbasierte Lehr-Lern-Umgebung**, in der sich **didaktische Planung** <span class="content-emoji">🧭</span>, **Veröffentlichung** <span class="content-emoji">🌐</span>, **Offenheit** <span class="content-emoji">🎓</span><span class="content-emoji">🌍</span><span class="content-emoji">🔓</span> und **Nachhaltigkeit** <span class="content-emoji">🌱</span> sinnvoll miteinander verbinden lassen <span class="content-emoji">🤝</span>.

Zeitgleich begann ich, **Künstliche Intelligenz** systematisch in meine Arbeitsprozesse einzubeziehen <span class="content-emoji">🤖</span><span class="content-emoji">🧠</span> – sowohl als **technische Unterstützung** <span class="content-emoji">⚙️</span> als auch als **didaktisches Gegenüber** <span class="content-emoji">🪞</span>. Aus dieser Kombination heraus entstand im SoSe 2025 Schritt für Schritt der **SciBlog iWIP** <span class="content-emoji">🌐</span><span class="content-emoji">🎯</span>, den ich seit dem WiSe 2025/2026 einsetze.

## 3. Funktionen des SciBlog iWIP <span class="content-emoji">💻</span><span class="content-emoji">🎯</span>

Der **SciBlog iWIP** ist kein weiteres Tool im bestehenden Systemgefüge, sondern eine **integrierte Lehr-Lern-Umgebung**, die sich an der Logik von Lehre orientiert <span class="content-emoji">🧭</span> – nicht an der Logik einzelner Plattformen.

Die zentralen Funktionen lassen sich in vier miteinander verbundene Bereiche bündeln.

---

### Lernendenperspektive zuerst: Zugang und Nutzung <span class="content-emoji">👥</span><span class="content-emoji">🧠</span>

Ein zentrales Gestaltungsprinzip des SciBlog iWIP ist die konsequente **Ausrichtung auf die Perspektive der Lernenden** <span class="content-emoji">👥</span>.

- **Responsives Design** ermöglicht eine sinnvolle Nutzung auf Smartphone, Tablet und Desktop <span class="content-emoji">📱</span><span class="content-emoji">💻</span>  
- Inhalte sind **klar strukturiert**, gut lesbar und niedrigschwellig zugänglich  
- Studierende entscheiden selbst, **wie tief** sie einsteigen möchten <span class="content-emoji">🧭</span>
- Für Aufgaben, die in Präsenz in Partner- oder Gruppenarbeit durchgeführt werden, erfolgt im Blog ein Prompt-basierter Vorschlag für **eine interaktive Aufgabenbearbeitung mit KI**

Lehre wird damit nicht nur bereitgestellt, sondern **nutzbar gemacht** <span class="content-emoji">🧠</span>.

---

### Unterschiedliche Zugänge – ein Inhalt <span class="content-emoji">🌐</span><span class="content-emoji">🧩</span>

Didaktisch sinnvoll ist selten *ein* Darstellungsformat.  
Der SciBlog iWIP erlaubt daher **verschiedene Zugänge zu denselben Inhalten**:

- als **Blogbeitrag** zur vertieften Auseinandersetzung <span class="content-emoji">📖</span>  
- als **Präsentation** für die Präsenzlehre oder synchrone Online-Formate <span class="content-emoji">👥</span><span class="content-emoji">💬</span>  
- als **PDF** oder **Markdown** für Download, Archivierung und Offline-Nutzung <span class="content-emoji">📄</span>  

Alle Formate basieren auf **einer gemeinsamen inhaltlichen Quelle**.  
Redundante Pflege entfällt – **Kohärenz entsteht automatisch** <span class="content-emoji">🤝</span>.

---

### Nachhaltige Speicherformen statt flüchtiger Formate <span class="content-emoji">🌱</span><span class="content-emoji">📄</span>

Technisch setzt der SciBlog iWIP bewusst auf **nachhaltige, offene Speicherformate**:

- Inhalte werden primär in **Markdown** verfasst <span class="content-emoji">✍️</span>  
- **PDFs** entstehen automatisiert aus derselben Quelle  
- Änderungen bleiben nachvollziehbar, versionierbar und langfristig nutzbar <span class="content-emoji">🔁</span>

Das reduziert Abhängigkeiten von Softwareversionen und erhöht die **Zukunftsfähigkeit** der Materialien <span class="content-emoji">🌱</span>.

---

### Vertiefung, Transparenz und Offenheit <span class="content-emoji">🎓</span><span class="content-emoji">🌍</span><span class="content-emoji">🔓</span>

Ein weiterer zentraler Funktionsbereich betrifft die **didaktische Dokumentation und Offenheit**:

- **Direkte Verlinkungen** zu Quellen, Studien und Materialien ermöglichen Vertiefung <span class="content-emoji">📚</span>  
- Lehr-Lern-Arrangements werden **didaktisch transparent dokumentiert** (z. B. über **TULLU**) <span class="content-emoji">🧭</span>  
- Alle Inhalte sind i. d. R.  **offen lizenziert** (CC BY-SA 4.0) <span class="content-emoji">🎓</span><span class="content-emoji">🌍</span><span class="content-emoji">🔓</span>  

Lehre wird damit nicht nur genutzt, sondern **teilbar, überprüfbar und weiterentwickelbar** <span class="content-emoji">🤝</span>.

---

### Systemanschluss statt Insellösung <span class="content-emoji">🌐</span><span class="content-emoji">🔗</span>

Der SciBlog iWIP ist bewusst so angelegt, dass er **anschlussfähig** bleibt:

- geplante automatische **Anbindung an Repositorien** (z. B. **OERSI**, beantragt) <span class="content-emoji">🌐</span>  
- **klare Metadatenstrukturen** ohne Mehrfachpflege <span class="content-emoji">🏷️</span>  
- Nutzung **unabhängig** von bzw. integriert in **LMS-Instanzen**  

Damit bleibt die Lehr-Lern-Umgebung **offen für institutionelle Kontexte**, ohne von ihnen abhängig zu sein <span class="content-emoji">🔗</span>.

---

### Zusammengefasst <span class="content-emoji">🧭</span>

Der SciBlog iWIP…

- reduziert technische Komplexität <span class="content-emoji">✂️</span>  
- erhöht didaktische Kohärenz <span class="content-emoji">🤝</span>  
- stärkt die Perspektive der Lernenden <span class="content-emoji">👥</span><span class="content-emoji">🧠</span>  
- und macht Lehre **nachhaltig, offen und anschlussfähig** <span class="content-emoji">🎓</span><span class="content-emoji">🌍</span><span class="content-emoji">🔓</span>  

Nicht als Selbstzweck – sondern als **Arbeitsumgebung für gute Lehre** <span class="content-emoji">👩‍🏫</span><span class="content-emoji">🎯</span>.

## 4. Zentrale Learnings <span class="content-emoji">🪞</span><span class="content-emoji">🧠</span>

Die Arbeit mit dem SciBlog iWIP hat für mich nicht nur technische Abläufe verändert, sondern vor allem meine **Sicht auf Lehre** geschärft. Einige dieser Lernprozesse waren erwartet – andere eher überraschend.

---

### Veröffentlichen verändert Vorbereitung <span class="content-emoji">🧭</span><span class="content-emoji">🌐</span>

Ein zentrales Learning war für mich:  
**Ich bereite Lehre anders – und besser – vor, wenn ich weiß, dass ich sie veröffentliche.**

Die Entscheidung für Offenheit erzeugt einen produktiven Druck:
- Inhalte müssen **klarer strukturiert** und **mit Quellen belegt** sein  
- Argumentationen müssen **begründbar** sein  
- didaktische Entscheidungen werden **bewusster reflektiert** <span class="content-emoji">🪞</span>  

Lehre wird damit weniger situativ und stärker **konzeptionell durchdacht** [(Wiley & Hilton 2018)](/iWIP/blog/oer/warum_sciblog/#-literatur).

---

### KI als didaktisches Gegenüber <span class="content-emoji">🤖</span><span class="content-emoji">🧠</span>

Ein weiteres zentrales Learning betrifft die Arbeit mit **Künstlicher Intelligenz**.  
KI nutze ich nicht zur Automatisierung, sondern als **Reflexions- und Feedbackinstanz** <span class="content-emoji">🪞</span>.

- zur Prüfung von **didaktischer Stringenz**  
- zur Rückmeldung auf **Aufgabenstellungen und Struktur**  
- zur Unterstützung bei Sprache, Reduktion und Zuspitzung 
- zur [technischen Umsetzung](/iWIP/content/blog/doku/doku_tech/) des Blogs 

KI ersetzt dabei keine didaktische Verantwortung – sie **verstärkt Reflexion**, wenn sie bewusst eingesetzt wird <span class="content-emoji">🧠</span>.

[Dietrich & Zug (2025)](/iWIP/blog/oer/warum_sciblog/#-literatur), die Entwickler von LiaSkript, beschreiben in Ihrem Blogbeitrag ein ähnliches Konzept der KI-unterstützten Gestaltung von Lehre.

---

### Reduktion schafft didaktischen Raum <span class="content-emoji">✂️</span><span class="content-emoji">🧭</span>

Die konsequente Reduktion von Tools, Formaten und Abläufen hat einen unerwarteten Effekt:  
Sie schafft **mentalen Raum**.

Weniger technische Entscheidungen bedeuten:
- mehr Fokus auf **Lernziele** <span class="content-emoji">🎯</span>  
- mehr Aufmerksamkeit für **Lernprozesse** <span class="content-emoji">🧠</span>  
- mehr Zeit für **didaktische Feinjustierung** <span class="content-emoji">🧭</span>  

Komplexitätsreduktion ist damit kein technisches, sondern ein **didaktisches Qualitätsmerkmal**.

---

### Lehre rückt (wieder) ins Zentrum <span class="content-emoji">👩‍🏫</span><span class="content-emoji">🎯</span>

Vielleicht das wichtigste Learning:  
Durch den SciBlog iWIP rückt **Lehre selbst** – und ein entsprechender Austausch, auch über das Web – wieder stärker in den Fokus.

Nicht als Nebenprodukt von Organisation, Verwaltung oder Toolpflege – sondern als **professionelle Gestaltungsaufgabe** <span class="content-emoji">👩‍🏫</span>.

Der SciBlog ist dabei kein Selbstzweck, sondern ein **Arbeitsmittel**, das mir erlaubt, mich auf das zu konzentrieren, was Lehre im Kern ausmacht:  
**Lernende, Inhalte, Prozesse und Reflexion** <span class="content-emoji">👥</span><span class="content-emoji">🧠</span><span class="content-emoji">🪞</span>.

# <span class="content-emoji">📚</span> Literatur

Dietrich, A., & Zug, S. (2025). AI-assisted course creation: From Markdown to interactive learning in 3 hours [Blogbeitrag]. LiaScript. <a class="lit-online" href="https://liascript.github.io/blog/ai-assisted-course-creation-buchstabensuppe-tutorial/" target="_blank" rel="noopener noreferrer"></a>

Söll, M., & Klusmeyer, J. (2022). Akademisches Lernen und Reflexion bei der Förderung von Unterrichtsplanungskompetenz in der Wirtschaftsdidaktik. In J. Klusmeyer & D. Bosse (Hrsg.), *Konzepte reflexiver Praxisstudien in der Lehrer*innenbildun* (S. 73–114). Springer VS. <a class="lit-ub" href="https://opac.lbs-rostock.gbv.de/DB=1/XMLPRS=N/PPN?PPN=1799310981" target="_blank" rel="noopener noreferrer" aria-label="Universitätsbibliothek-Rostock-Link zur Publikation"></a>
<a class="lit-doi" href="https://doi.org/10.1007/978-3-658-35483-1" target="_blank" rel="noopener noreferrer" aria-label="DOI-Link zur Publikation"></a>
<a class="lit-worldcat" href="https://search.worldcat.org/de/title/1311485961" target="_blank" rel="noopener noreferrer" aria-label="WorldCat-Link zur Publikation"></a>

Wernke, S.; Zierer, K. (2017). Die Unterrichtsplanung - ein in Vergessenheit geratener Kompetenzbereich?!. In: S. Wernke & K. Zierer (Hrsg.), *Die Unterrichtsplanung: ein in Vergessenheit geratener Kompetenzbereich?! Status Quo und Perspektiven aus Sicht der empirischen Forschung.* (S. 7-16). Julius Klinkhardt. <a class="lit-ub" href="https://opac.lbs-rostock.gbv.de/DB=1/XMLPRS=N/PPN?PPN=1009887009" target="_blank" rel="noopener noreferrer" aria-label="Universitätsbibliothek-Rostock-Link zur Publikation"></a> <a class="lit-worldcat" href="https://search.worldcat.org/de/title/1015854043" target="_blank" rel="noopener noreferrer" aria-label="WorldCat-Link zur Publikation"></a>

Wiley, D., & Hilton, J. (2018). Defining OER-enabled pedagogy. *International Review of Research in Open and Distributed Learning*, 19(4), 133–147. <a class="lit-doi" href="https://doi.org/10.19173/irrodl.v19i4.3601" target="_blank" rel="noopener noreferrer" aria-label="DOI-Link zur Publikation"></a> <a class="lit-worldcat" href="https://search.worldcat.org/de/title/8214655664" target="_blank" rel="noopener noreferrer" aria-label="WorldCat-Link zur Publikation"></a>