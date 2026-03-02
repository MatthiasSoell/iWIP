---
title: "Warum OER?"
date: 2025-06-12
lastmod: 2025-06-12
draft: false

description: >
  In diesem Beitrag wird der Hintergrund freier Bildungsmaterialien erläutert. Aus der Perspektive der beruflichen Bildung werden drei zentrale Argumentationsfiguren für die Nutzung von Open Educational Resources (OER) vorgestellt: emotional, rational und qualitativ.

summary: >
  Warum OER? Der Beitrag erläutert Herkunft, Zielsetzungen und zentrale Mehrwerte für die berufliche Bildung.

tags:
  - OER
  - Open Educational Resources
  - Offene Bildung
  - Berufliche Bildung
  - Wissenschaftskommunikation

categories:
  - OER

oer:
  is_oer: true
  kind: "article"

  # TULLU-Pflichtdaten (Frontend) + Basis für JSON-LD
  creators:
    - name: "Prof. Dr. Matthias Söll"
      given_name: "Matthias"
      family_name: "Söll"
      affiliation: "Universität Rostock · Institut für Wirtschaftspädagogik"
      url: ""
      orcid: ""

  publisher:
    name: "SciBlog iWIP – Universität Rostock"
    url: "https://matthiassoell.github.io/iWIP/"

  license:
    label: "CC BY-SA 4.0"
    url: "https://creativecommons.org/licenses/by-sa/4.0/"

  source:
    label: "SciBlog iWIP – Universität Rostock"
    url: "https://matthiassoell.github.io/iWIP/"

  # Version / Reifegrad
  version: "1.0"
  status: "stable"   # draft | pilot | stable | aligned

  # OERSI / schema.org-nahe Felder
  in_language: "de"
  learning_resource_type: "Article"
  educational_level:
    - "Hochschule"
    - "Berufliche Bildung"
  audience:
    - "Studierende"
    - "Lehrende"
    - "Interessierte an Open Education"
  time_required: "PT20M"

  about:
    - term: "Open Educational Resources"
    - term: "Offene Bildung"
    - term: "Creative Commons"
    - term: "OER-Strategien"
    - term: "Berufliche Bildung"

  todos: []
---

<script>
  function triggerPrint() {
    window.print(); // oder eine andere Funktion, je nach Zweck
  }
</script>

<script>
document.addEventListener("DOMContentLoaded", function () {
  if (window.location.search.includes("print-pdf")) {
    // Warten, bis Reveal "ready" ist
    Reveal.addEventListener("ready", function () {
      setTimeout(() => {
        window.print();
      }, 300); // etwas Spielraum lassen
    });
  }
});
</script>

<div class="top-toggle">
  <button id="md-copy-btn" title="Markdown kopieren (ohne Bilder)">📑</button>
  <button onclick="triggerPrint()" title="Blog speichern">📥</button>
  <button onclick="location.href='/iWIP/praesentation/oer/warum_oer/'" title="Zur Präsentationsansicht">🖥️</button>
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

## Was sind OER?
> [!IMPORTANT]
> OER = Open Educational Resources = freie Bildungsmaterialien  

OER sind stark, weil:
* Bildungsmaterialien in einem sehr weiten Verständnis (z. B. Konzepte oder Planungen, Texte, Zusammenfassungen oder Aufgaben, aber auch Online- oder Selbstlern-Kurse)
* frei über Online-Plattformen verfügbar (wie <a href="https://www.twillo.de" target="_blank" rel="noopener">twillo</a> oder <a href="https://hubbs.schule/"  target="_blank" rel="noopener">HubbS</a> geteilt)
* digital (da sich entsprechende Materialien gut teilen und bearbeiten lassen)
* gut bearbeitbar
* unter offener Lizenz veröffentlicht

## Woher kommen OER?
* Ausgangspunkt der OER-Initiativen ist die <a href="https://www.unesco.de/assets/dokumente/Deutsche_UNESCO-Kommission/02_Publikationen/Publikation_Bildungsagenda_2030_Aktionsrahmen.pdf" target="_blank" rel="noopener">Agenda Bildung 2030 (PDF)</a> der UNESCO aus dem Jahr 2015
* Die UNESCO zielt mit der Agenda auf eine inklusive, chancengerechte und hochwertige Bildung für alle Menschen weltweit ab
* Die UNESCO veröffentlichte 2019 <a href="https://www.unesco.de/assets/2019_Empfehlung_Open_Educational_Resources.pdf" target="_blank" rel="noopener"> Empfehlungen zu OER (PDF)</a>, in denen diese als geeignete Mittel zur Erreichung der Ziele der Agenda definiert werden
* Das Bundesministerium für Forschung, Technologie und Raumfahrt (BMFTR, ehemals Bundesministerium für Bildung und Forschung, BMBF) fördert in diesem Kontext seit 2016 folgende Maßnahmen:
  * <a href="https://open-educational-resources.de/" target="_blank" rel="noopener">OERInfo</a> (2016)
  * <a href="https://www.oer-strategie.de/foerdern/foerderrichtlinien/" target="_blank" rel="noopener">OE_COM</a> (2023)
  * <a href="https://www.oer-strategie.de/foerdern/foerderrichtlinien/" target="_blank" rel="noopener">OE_Struktur</a> (2024)
  
  Diese Maßnahmen dienen der Umsetzung der im Jahr 2022 ausgegebenen <a href="https://www.bmbf.de/SharedDocs/Publikationen/DE/3/691288_OER-Strategie.pdf?__blob=publicationFile&v=5" target="_blank" rel="noopener">OER-Strategie der Bundesregierung (PDF)</a>.

> [!TIPP]
  > Auf <a href="https://open-educational-resources.de/was-ist-oer-3-2/" target="_blank" rel="noopener">OERInfo.de</a> finden Sie weitere, anschaulich aufbereitete Informationen zu OER: bspw. ein 90s Erklärvideo, eine ausführliche Definition sowie Infos zu offenen Lizenzen und zum Mehrwert von OER.

## Warum OER? ❤️ Emotionale Begründung

> [!QUOTE]
> „Wissen ist das einzige Gut, das sich vermehrt, wenn man es teilt.“  
> — Marie von Ebner-Eschenbach (1830 – 1916)

Dieses Zitat bringt den Kern von OER auf den Punkt: Wissen entfaltet seinen Wert erst im Teilen.  
Wer Lehr-Lern-Materialien offen zur Verfügung stellt, stärkt das gemeinsame Lernen und trägt zur Bildungsgerechtigkeit bei.  
Ähnlich argumentiert <a href="https://www.bpb.de/shop/zeitschriften/apuz/33204/elinor-ostrom-und-die-wiederentdeckung-der-allmende/" target="_blank" rel="noopener">Elinor Ostrom</a>, die 2009 als erste Frau den Wirtschaftsnobelpreis erhielt.  
Sie beschreibt Wissen als *Allmende* — als gemeinsames Gut, das durch gemeinschaftliche Nutzung wächst, statt zu verknappen.  

---

## Warum OER? 📈 Rationale Begründung

OER steigern die **Effizienz** in Lehr-Lern-Prozessen:

* 22 638 neue Büromanagement-Auszubildende im Jahr 2023 👩‍💼  
* Durchschnittlich 22 Schüler:innen pro Klasse 👥  
* Ca. 1 029 Klassen allein im 1. Lehrjahr 🏫  
* Etwa 1 000 Lehrkräfte, die ähnliche Unterrichtsinhalte täglich neu aufbereiten 👩‍🏫  

> [!TIPP]
> Das Teilen und gemeinsame Bearbeiten von Materialien reduziert redundante Arbeit und ermöglicht eine bessere Nutzung gemeinsamer Ressourcen.  
> So kann mehr Zeit in die didaktische Gestaltung und Begleitung von Lernprozessen fließen.

---

## Warum OER? ✨ Qualitative Begründung

Neben Effizienzgewinnen kann OER die **Qualität** von Lehr-Lern-Arrangements erhöhen.  
Durch kooperative Entwicklung und kollegiale Begutachtung entstehen Materialien, die didaktisch reifer, aktueller und vielfältiger sind.

<img class="responsive-image" src="/iWIP/praesentation/warum_oer/OER_qualitaet.png" alt="Kooperative Entwicklung von OER">

<p class="bild-quelle"><i>Bildquelle: erstellt mit ChatGPT · Lizenz: CC BY 4.0</i></p>

Offene Zusammenarbeit führt so zu reflektierteren, anschlussfähigeren und lernförderlicheren Ergebnissen — und stärkt eine Kultur des Teilens, die weit über das einzelne Unterrichtsmaterial hinausgeht.

---

## Fazit

OER stehen für mehr als frei verfügbare Materialien:  
Sie verkörpern eine Haltung — die Bereitschaft, Wissen zu teilen, voneinander zu lernen und Bildung als gemeinsame Aufgabe zu verstehen.  
Ob emotional, rational oder qualitativ begründet:  
**OER sind ein Schlüssel zu einer offenen, kollaborativen und gerechten Bildungslandschaft.**