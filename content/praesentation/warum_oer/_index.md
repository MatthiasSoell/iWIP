---
title: "Warum OER?"
outputs:
  - Reveal
---

{{< logoBox src="/iWIP/bilder/logo_siblog_iwip.png" text="SciBlog iWIP" >}}

<script>
  function triggerPrint() {
    window.print(); // oder eine andere Funktion, je nach Zweck
  }
</script>

<div class="top-toggle">
  <button onclick="triggerPrint()" title="Präsentation speichern">💾</button>
  <button onclick="location.href='/iWIP/oer/warum_oer'" title="Zur Blogansicht">📄</button>
</div>

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

# Was sind OER?
> OER =  
> 
> Open Educational Resources =  
> 
> freie Bildungsmaterialien  

---

# OER sind:
* Bildungsmaterialien in einem sehr weiten Verständnis (von einer Definition über eine Grafik bis hin zu einem Selbstlernkurse)
* frei über Online-Plattformen verfügbar (bspw. <a href="https://www.twillo.de" target="_blank" rel="noopener">twillo</a> oder <a href="https://hubbs.schule/"  target="_blank" rel="noopener">HubbS</a> geteilt)
* digital (so lässt sich das Material gut teilen)
* leicht bearbeitbar
* unter offener Lizenz veröffentlicht (siehe <a href="https://creativecommons.org" target="_blank" rel="noopener">Creative Commons</a>)

---

# OER & UNESCO
* Ausgangspunkt der OER-Initiativen ist die <a href="https://www.unesco.de/assets/dokumente/Deutsche_UNESCO-Kommission/02_Publikationen/Publikation_Bildungsagenda_2030_Aktionsrahmen.pdf" target="_blank" rel="noopener">Agenda Bildung 2030 (PDF)</a> der UNESCO aus dem Jahr 2015
* Ziel der Agenda (u. a.): inklusive, chancengerechte und hochwertige Bildung für alle Menschen weltweit
* UNESCO (2009) <a href="https://www.unesco.de/assets/2019_Empfehlung_Open_Educational_Resources.pdf" target="_blank" rel="noopener"> Empfehlungen zu OER (PDF)</a>: OER als geeignete Mittel zur Zielerreichung

---

# OER & Deutschland
* Das BMFTR (Bundesministerium für Forschung, Technologie und Raumfahrt, ehemals BMBF: Bundesministerium für Bildung und Forschung) fördert OER seit 2016:
  * <a href="https://open-educational-resources.de/" target="_blank" rel="noopener">OERInfo</a> (2016)
  * <a href="https://www.oer-strategie.de/foerdern/foerderrichtlinien/" target="_blank" rel="noopener">OE_COM</a> (2023)
  * <a href="https://www.oer-strategie.de/foerdern/foerderrichtlinien/" target="_blank" rel="noopener">OE_Struktur</a> (2024)
* Fördermaßnahmen setzen <a href="https://www.bmbf.de/SharedDocs/Publikationen/DE/3/691288_OER-Strategie.pdf?__blob=publicationFile&v=5" target="_blank" rel="noopener">OER-Strategie der Bundesregierung (PDF)</a> um
  
---

  > Auf <a href="https://open-educational-resources.de/was-ist-oer-3-2/" target="_blank" rel="noopener">OERInfo.de</a> finden Sie weitere, anschaulich aufbereitete Informationen zu OER: bspw. ein 90s Erklärvideo, eine ausführliche Definition sowie Infos zu offenen Lizenzen und zum Mehrwert von OER.

---

<div class="zitat-wrapper">
  <div class="zitat-container">
    <blockquote class="zitat-box">
      Wissen ist das einzige Gut, das sich vermehrt, wenn man es teilt.
    </blockquote>
    <p class="zitat-quelle">Marie von Ebner-Eschenbach (1830 – 1916)</p>
  </div>
</div>

Ähnlich argumentiert Elinor Ostrom in in „Was mehr wird, wenn wir teilen“. Sie ist die erste weibliche Nobelpreisträgerin in den Wirtschaftswissenschaften (2009).
