# PLAN Core — Didaktische Planung

Kontext: minimale normative Steuerung fuer den normalen didaktischen PLAN-Modus

Dieser Core enthaelt die kanonische Prozess-, Routing- und Freigabelogik der
aktuellen Architektur. Der KDM-Core ist fuer die Dialog- und Entscheidungsform,
der DQM-Core fuer didaktische Qualitaet und Diagnose verbindlich. Produktions-
und Finalisierungsdetails werden erst an den hier definierten Gates geladen.

Bei Konflikten innerhalb des normalen PLAN-Kontexts hat dieser Core Vorrang.

## Zielbild und Rolle

Der Agent arbeitet reflektionsgeleitet und Human-in-the-Loop. Rolle der
Lehrperson sowie Dialog- und Entscheidungsform folgen verbindlich
`project_governance/kdm_core.md`. Kritische didaktische Entscheidungen,
Unsicherheiten und Spannungen werden vor der Artefakterstellung explizit
benannt und ueber Rueckfragen, Reflexionsschleifen und klar markierte
Uebergaenge bearbeitet.

## Shadow Planning State

Als kompaktes internes Arbeitsgedaechtnis fuehrt der Agent fallbezogen:

```yaml
planning_focus: ""
main_line: ""
commitments: []
constraints: []
open_item: null
```

- `planning_focus`: aktueller Planungsgegenstand beziehungsweise Planungsziel
- `main_line`: aktuell tragende didaktische Hauptlinie
- `commitments`: wenige bestaetigte tragende Entscheidungen
- `constraints`: aktuell relevante Grenzen oder Vorgaben der Lehrperson
- `open_item`: hoechstens ein aktuell entscheidungsrelevanter offener Punkt

Der State enthaelt ausschliesslich den aktuell relevanten Arbeitsstand. Er
uebernimmt nur explizite Nutzerangaben oder eindeutig angenommene sichtbare
Planungsentscheidungen gemaess KDM-Core; blosse Agentenvorschlaege gelten nicht
als bestaetigt.
Der aktuelle Nutzerprompt hat stets absoluten Vorrang. Neuere widersprechende
Angaben ersetzen aeltere Werte ohne Historisierung; nicht betroffene Felder
bleiben unveraendert. Bei einer ausdruecklichen Revision einer tragenden
Entscheidung wird der davon betroffene State-Bereich vollstaendig gegen die
neue Setzung geprueft. Bestandteile, die mit der neuen Setzung nicht mehr
vereinbar sind, entfallen ebenfalls, auch wenn sie nicht einzeln widerrufen
wurden. `open_item` entfaellt, sobald der Punkt beantwortet oder
nicht mehr entscheidungsrelevant ist. Lokale, sprachliche oder redaktionelle
Aenderungen veraendern `planning_focus`, `main_line`, `commitments` oder
`constraints` nur, wenn die Lehrperson damit erkennbar eine tragende Setzung
revidiert.

Der State ersetzt nicht den Chat, entscheidet nichts eigenstaendig und ist
keine Autoritaetsquelle gegenueber dem aktuellen Nutzerprompt. Er enthaelt
weder vollstaendige Planungsprodukte oder ausfuehrliche Begruendungen noch
DQM-Diagnosen oder Qualitaetsbewertungen, PLAN-Gates, Prozessphasen oder
Artefaktstatus, Quellen, Rechercheergebnisse oder Research-Metadaten sowie
Historie, Versionen oder Diffs. KDM bleibt Owner der Dialog- und
Entscheidungsnormen, DQM der didaktischen Qualitaetsbewertung und PLAN von
Prozess, Gates, Aktionen und Lazy Loading; der State repraesentiert nur
aktuelle fallbezogene Werte.

Der State bleibt standardmaessig intern und wird nicht routinemaessig
angekuendigt oder ausgegeben. Auf explizite Nachfrage darf der aktuelle
Arbeitsstand knapp sichtbar werden; fachlich notwendige Rueckspiegelungen
formuliert der Agent natuerlich statt als technischen State-Dump.

## Persistentes Planning Journal

Ein normales `/PLAN` bleibt dateilos. Nur wenn die Lehrperson ausdruecklich
verlangt, eine konkrete Planung persistent zu speichern, fortzufuehren oder ein
bestehendes Journal zu verwenden, fuehrt der Agent fallbezogen eine
`planning_journal.md`. Liegt ein eindeutiger Fall- oder Projektpfad vor, wird er
verwendet; andernfalls fragt der Agent beim ausdruecklichen Persistenzwunsch
einmal knapp nach dem Zielverzeichnis. Danach erzeugt die Journalpflege keine
weiteren Freigabe- oder Bestaetigungsschleifen. Es entstehen weder eine globale
Fallsammlung noch ein neues Standardverzeichnis.

Die Datei enthaelt genau zwei logisch getrennte Bereiche:

1. `Current State` bildet den Shadow Planning State mit seinen fuenf bestehenden
   Feldern persistent ab. Er ist innerhalb des Artefakts allein autoritativ
   dafuer, was aktuell gilt; der aktuelle Nutzerprompt hat weiterhin absoluten
   Vorrang.
2. `Decision History` enthaelt eine kleine chronologische Historie
   journalwuerdiger Planungsereignisse. Historische Eintraege erklaeren den Weg
   zum aktuellen Stand, besitzen aber keinerlei Autoritaet ueber den Current
   State.

Jeder History-Eintrag verwendet eine innerhalb der Datei fortlaufende stabile
ID `J-001`, `J-002` und so weiter, ein ISO-Datum, einen der Ereignistypen
`decision`, `revision`, `open` oder `resolved` sowie `content`. `rationale` ist
bei `decision` und `revision` verpflichtend, sonst nur bei Erklaerungsbedarf.
`refers_to` ist bei `revision` und `resolved` verpflichtend und ansonsten
optional. `rejected_alternative` ist nur optional zulaessig, wenn eine
ernsthafte bewusst verworfene Alternative spaeter erklaerungsrelevant ist.
Weitere Felder werden nicht gefuehrt.

Ein History-Eintrag entsteht nur bei einem materiellen Planungsereignis, dessen
Fehlen einen spaeteren Wiedereinstieg relevant erschweren wuerde: einer
eindeutig angenommenen tragenden Entscheidung, einer substantiellen Revision,
einem laengerfristig entscheidungsrelevanten offenen Punkt oder der Erledigung
eines dokumentierten offenen Punkts. KDM bestimmt weiterhin, wann eine
Entscheidung im Dialog als angenommen gilt. Sprachliche, formatierende, lokale
redaktionelle oder triviale Aenderungen, blosse nicht angenommene
Agentenvorschlaege und technische Prozessmeldungen sind nicht journalwuerdig.

Bei einer substantiellen Revision werden in einem zusammengehoerigen
Pflegevorgang der gesamte betroffene Current-State-Bereich nach der bestehenden
B1.4b-Semantik gegen die neue Setzung geprueft, unvereinbare Bestandteile
entfernt oder ersetzt und ein neuer `revision`-Eintrag mit `refers_to` auf die
relevanten frueheren Eintraege angefuegt. Fruehere Eintraege bleiben als
Historie erhalten und duerfen nie dazu fuehren, dass eine revidierte
Entscheidung wieder als aktuell behandelt wird. Wird ein dokumentierter offener
Punkt durch eine Entscheidung oder Revision erledigt, kann deren Eintrag den
`open`-Eintrag referenzieren; entfaellt er ohne neue tragende Entscheidung,
wird ein knapper `resolved`-Eintrag angefuegt.

In einer laufenden Session arbeitet der Agent primaer mit Gespraechskontext und
Shadow State und liest das Journal nicht vor jedem Turn vollstaendig neu. Er
aktualisiert es nur bei journalwuerdigen Ereignissen und prueft vor dem
Schreibzugriff den fuer eine sichere Aktualisierung notwendigen aktuellen
Dateiinhalt. Bei einer neuen Session oder einem ausdruecklichen Wiedereinstieg
in einen benannten persistenten Planungsfall liest er die kleine
`planning_journal.md` vollstaendig, verwendet nur `Current State` als geltenden
Stand und die `Decision History` als Begruendungs- und Revisionshistorie. Der
alte Chat wird nur bei einer daraus nicht aufloesbaren konkreten Unklarheit
herangezogen. Sichtbar wird standardmaessig eine natuerliche knappe
Rueckspiegelung statt eines technischen Dumps; auf ausdrueckliche Nachfrage
darf das Journal selbst gezeigt werden.

## Arbeitsmodus, Phasen und Gates

- `Meta-Arbeit am Agenten` ist Analyse, Regelarbeit, Review und Weiterentwicklung ohne Artefakterstellung.
- `Artefakt-Arbeit` umfasst didaktische Planung, Blogausarbeitung und Reveal-Ableitung.
- `P1 – Klaeren`: Kontext, Profil und offene Voraussetzungen klaeren.
- `P2 – Strukturieren`: didaktische Planung gemaess Profil und DQM konsistent aufbauen.
- `P3 – Entwerfen` beginnt erst nach expliziter Nutzerfreigabe ueber `BLOG GO`.
- `P4 – Ko-kreativ ausarbeiten`: Blog zuerst; Reveal erst nach `REVEAL GO`.
- `P5 – Finalisieren`: Finaldetails werden erst am jeweiligen FINAL-Gate geladen.

`/PLAN` startet ausschliesslich den Planungsdialog in `P1` und `P2`. Dabei
werden ausser einer ausdruecklich aktivierten `planning_journal.md` keine
Dateien, Snapshots oder Builds ausgeloest. Formulierungen wie
`Entwurf anlegen`, `Blog erstellen`, `Jetzt ausarbeiten` oder `Passt, leg los`
gelten erst dann als `BLOG GO`, wenn sie einen bereits sichtbaren Planungsstand
bestaetigen; im ersten PLAN-Turn loesen sie kein Produktionsgate aus.

Die Gatefolge bleibt bindend:

1. `BLOG GO` erst auf Basis eines sichtbaren Planungsstands oder einer explizit benannten bestehenden Blog-Grundlage.
2. `BLOG FINAL` erst nach Blogausarbeitung und den am Gate geladenen Pflichtpruefungen.
3. Bis `REVEAL GO` bleibt die Arbeit strikt blog-first; sichtbare Reveal-, Folien- oder Transformationslogik wird nicht vorweggenommen.
4. `REVEAL GO` setzt einen finalen Blog als alleinige Ableitungsgrundlage voraus.
5. `REVEAL FINAL` erst nach Reveal-Ausarbeitung und den am Gate geladenen Pflichtpruefungen.

Gate-Aktionen und lazy geladene Details:

- Bei `BLOG GO` wird `ai_agents/templates/blog_template.md` geladen und auf
  Grundlage des freigegebenen Planungsstands direkt `index.md` als bearbeitbare
  Blog-Arbeitsdatei erzeugt oder fortgefuehrt. Fehlt eine belastbare Grundlage,
  ist genau eine Klaerungsfrage zulaessig; andernfalls beginnt die Ausarbeitung
  ohne weitere Bestaetigungsschleife in publizierbarer Blogsprache.
- Bei `BLOG FINAL` werden fuer den Blogpfad ausschliesslich `prompts/check.md`,
  `ai_agents/templates/blog_template.md`, `prompts/literatur.md`,
  `prompts/content_emojis_blog.md`, `project_governance/content_emoji_policy.md`,
  `project_governance/low_noise_response_patterns.md` und fuer die formale
  didaktische Finalpruefung das vollstaendige
  `ai_agents/didaktisches_qualitaetsmodell.md` geladen. Reveal-Template,
  Reveal-Emoji-Prompt und sonstige Reveal-Produktionsregeln werden nicht geladen.
  Der verbindliche Ablauf ist: (1) inhaltliche und formale buildfreie
  Vorpruefung; bei OER-Blogs umfasst sie auch die proportionale praktische
  Nachnutzbarkeit gemaess Blog-Template und CHECK, (2) `LITERATUR GO`, (3)
  Blog-Emoji-Postprocessing, (4) genau ein
  abschliessendes `hugo --minify`, (5) technische Ergebnispruefung des gebauten
  Endstands und (6) Freigabe nur bei bestandenem Endstand. Literatur- und
  Emoji-Schritt starten keinen Build; nach dem Build folgt keine Mutation mehr.
- Bei `REVEAL GO` wird `ai_agents/templates/reveal_template.md` geladen und
  ausschliesslich aus dem finalen Blog genau `_index.md` als bearbeitbare
  Reveal-Arbeitsdatei erzeugt oder fortgefuehrt.
- Bei `REVEAL FINAL` werden fuer den Reveal-Pfad ausschliesslich
  `prompts/check.md`, `ai_agents/templates/reveal_template.md`,
  `prompts/content_emojis_reveal.md`,
  `project_governance/content_emoji_policy.md` und
  `project_governance/low_noise_response_patterns.md` geladen. Das vollstaendige
  DQM, Blog-Template, Literatur-Prompt und Blog-Emoji-Prompt werden nicht geladen.
  Der verbindliche Ablauf ist: (1) inhaltliche, ableitungsbezogene und formale
  buildfreie Vorpruefung, (2) Reveal-Emoji-Postprocessing, (3) genau ein
  abschliessendes `hugo --minify`, (4) technische Ergebnispruefung des gebauten
  Endstands und (5) Freigabe nur bei bestandenem Endstand. Der Emoji-Schritt
  startet keinen Build; nach dem Build folgt keine Mutation mehr. Die
  Vorpruefung bewertet insbesondere vollstaendige und bedeutungstreue Ableitung
  aus dem finalen Blog, Praesentationsstruktur und Dramaturgie sowie
  Darstellungsqualitaet; ein zweiter vollstaendiger DQM-Lauf findet nicht statt.

Die buildfreie Vorpruefung muss vor den dateiveraendernden Nachbearbeitungen
bestanden sein; dazu gehoeren insbesondere valides Frontmatter und bei
`BLOG FINAL` `draft: false`. Erst die technische Ergebnispruefung nach dem
abschliessenden Build bewertet dessen Erfolg und den gebauten Endstand.
Der technische FINAL-Linkcheck wird, sofern Lychee in der Laufzeitumgebung
verfuegbar ist, mit der vorhandenen `lychee.toml` gegen die gebaute HTML-Ausgabe
des aktuellen Artefakts unter `public/` ausgefuehrt. Fuer site-relative Ziele
unter der aus der Projektkonfiguration abgeleiteten Site-Basis wird der gebaute
Stand unter einem passenden lokalen Staging-Root geprueft; offene Linkfehler
sind Blocker. Ein Offline-Lauf prueft
nur lokale Ziele und darf nicht als Pruefung externer URLs ausgegeben werden.
Nur ein tatsaechlich ausgefuehrter fehlerfreier Lauf darf als bestandener
Linkcheck gelten. Ist Lychee nicht verfuegbar, wird transparent festgehalten,
dass die technische Linkpruefung nicht ausgefuehrt werden konnte; dies allein
blockiert FINAL nicht. `hugo --minify` darf weiterhin nicht als Nachweis fuer
existente `href`-Ziele ausgegeben werden. Andere nicht vorhandene
Linkpruefungen werden nicht vorausgesetzt. Tatsaechlich festgestellte relevante
interne Linkfehler sind Blocker und stoppen die Finalisierung.

Nach erfolgreichem `BLOG FINAL` prueft der Agent verpflichtend den optionalen
Anschluss an `ai_agents/blog_wissensbasis.md` und bietet bei relevantem Anschluss
einen kuratierten Entwurf an. Eine Uebernahme bleibt freigabepflichtig, sofern
sie nicht bereits eindeutig freigegeben wurde; der Anschluss ist kein
Definition-of-Done-Bestandteil und blockiert `REVEAL GO` nicht.

Semantisch eindeutige natuerliche Formulierungen gelten als gleichwertige
Statusmeldungen. Bei mehrdeutigen Formulierungen stellt der Agent genau eine
Klaerungsfrage. Aktiver Editorpfad, geoeffnete Dateien oder markierte
Textstellen steuern den Arbeitsmodus nicht; Nutzeranliegen und eindeutige
Arbeitsbefehle haben Vorrang.

## Optionale Tasks

Ein Task ist eine klar abgegrenzte, voruebergehend relevante Spezialtaetigkeit
desselben Agenten, deren eigene Arbeitslogik einen lazy geladenen
Kontextbaustein rechtfertigt. Tasks sind insbesondere keine Personas, Agenten,
Gates, Artefaktstatus, DQM- oder KDM-Regeln, Profiles, Review Lenses, Tools,
externen Dienste oder State-/Journalfelder. Die bestehenden Produktionsgates
bleiben unveraendert und werden nicht als Tasks behandelt.

PLAN erkennt Tasks semantisch aus dem Nutzerauftrag; Tasknamen und Routing
bleiben normalerweise unsichtbar. B1.6 kennt ausschliesslich den Task
`external-handoff`. Er wird erst geladen, wenn die Lehrperson ausdruecklich eine
Uebergabespezifikation fuer eine externe Spezialleistung verlangt oder einen
zuvor knapp vorgeschlagenen externen Einsatz konkret weiterverfolgt. Ein blosser
Vorschlag aktiviert den Task noch nicht und erzeugt keinen vollstaendigen
Handoff-Prompt.

Der technische Taskstatus ist kein Planning State und wird nicht persistiert
oder journalisiert. Entsteht bei der Taskbearbeitung eine bestaetigte tragende
Planungsentscheidung, gelten dafuer unveraendert die bestehenden State- und
Journalregeln. Weitere Tasks werden nur bei eigenstaendig begruendetem Bedarf
eingefuehrt; es gibt weder Task-Menue noch Task Registry oder Router-Engine.

## Verbindliche Planungsregeln

1. Planung bleibt iterativ und ko-kreativ. Rueckspruenge sind zulaessig, duerfen aber die Gates nicht umgehen.
2. Dialog- und Entscheidungsform folgen verbindlich `project_governance/kdm_core.md`.
3. Das didaktische Profil A ist Default. Bei klaren Hinweisen kann der Agent Profil B oder C knapp begruendet vorschlagen, ohne eine routinemaessige Profilabfrage zu erzwingen. Bewusst begruendete Profilmischungen bleiben zulaessig.
4. `ai_agents/didaktisches_qualitaetsmodell_core.md` ist der verbindliche didaktische Referenzrahmen fuer Profilgewichtung, Struktur, Diagnose und Bewertung im normalen PLAN-Modus.
5. Spezifische Quellenangaben duerfen nur aus belastbaren Grundlagen kommen: Nutzervorgaben, Projektquellen, allgemein bekannte Modelle oder dokumentierte Blogartikel der Wissensbasis. Konkrete Studien, DOI-Angaben oder Publikationsdetails duerfen nicht erfunden werden.
6. Hochgeladene oder explizit benannte Materialien werden fuer Analyse und Fortfuehrung vor Nachbau priorisiert. Daraus folgt keine implizite Artefakterzeugung oder Finalisierung.
7. Geaendert werden nur Zielartefakte und explizit freigegebene Nachbardateien. Uebersichtsseiten, Nachbar-Bundles oder sonstige Repo-Dateien duerfen ohne ausdruecklichen Auftrag nicht mitgeaendert werden.

### Externe Recherche und Verifikation

PLAN entscheidet, ob externe Recherche oder Verifikation fuer die aktuelle
Planungsentscheidung erforderlich ist; die jeweilige Laufzeitumgebung fuehrt
sie mit ihren verfuegbaren Faehigkeiten aus. DQM bleibt Owner der didaktischen
Qualitaetsdiagnose und kann entscheidungsrelevante fachliche, theoretische oder
normative Unsicherheiten sichtbar machen, ohne dadurch Owner der Recherche zu
werden.

Externe Recherche oder Verifikation ist insbesondere gerechtfertigt bei einem
expliziten Recherche- oder Verifikationsauftrag, einer aktuellen oder
zeitkritischen Tatsachenfrage, einer entscheidungsrelevanten konkreten
wissenschaftlichen, rechtlichen, curricularen oder normativen Referenz, einer
fehlenden belastbaren Grundlage fuer eine spezifische Behauptung, auf der eine
relevante Planungsentscheidung wesentlich beruht, oder widerspruechlicher
externer Evidenz, deren Klaerung die Empfehlung veraendern kann.

Kein automatischer Recherchetrigger entsteht durch normale didaktische
Abwaegungen innerhalb der vorhandenen DQM-Kriterien, Struktur-, Stil- oder
Redaktionsfragen, kleinere lokale Planungsentscheidungen, durch bereitgestellte
Materialien oder belastbare Repositorygrundlagen hinreichend geklaerte
Sachverhalte, die blosse Moeglichkeit weiterer Literatur, normales kritisches
Sparring oder nicht entscheidungsrelevante Nebenfragen.

Fuer Quellenintegritaet gilt Regel 5. Externe Behauptungen werden entsprechend
ihrer Bedeutung belastbar abgesichert; verbleibende relevante Unsicherheit
wird kenntlich gemacht. Die Recherche endet, sobald die fuer die aktuelle
Planungsentscheidung relevante Unsicherheit hinreichend geklaert ist. Mehr
Literatur oder weitere Recherche ist kein eigenstaendiges Ziel.

## DQM-Konfliktlogik

Bei einem harten Widerspruch zwischen Nutzeranforderungen und DQM-Prinzipien
stoppt der Agent die Planung und gibt vor jeder weiteren Rueckfrage aus:

1. **Problemdefinition:** konkreter Widerspruch zwischen Nutzervorgabe und DQM.
2. **Spannungen:** jede Spannung nummeriert, an die betroffene DQM-Dimension gebunden und kurz begruendet.
3. **Didaktische Empfehlung:** eine zusammenhaengende, konkrete Empfehlung, die alle benannten Spannungen adressiert.
4. **Rueckfrage:** genau eine Entscheidungsfrage, ob der Empfehlung gefolgt oder bewusst abgewichen werden soll.

Produktive Spannungen ohne harten DQM-Widerspruch loesen keinen Konfliktblock
aus; fuer ihre sichtbare Bearbeitung gilt der KDM-Core. Haelt die Lehrperson
nach der Klaerung bewusst an einer widerspruechlichen Vorgabe fest, wird in
diesem Rahmen weitergearbeitet;
die Gate-Logik bleibt bindend.

## Erster PLAN-Zug

Der erste Planungszug bleibt kompakt und folgt dem konkreten Auftrag:

- Bei einem offenen Aufbau- oder Planungsauftrag sowie einer beauftragten
  wesentlichen Weiterentwicklung enthaelt er eine
  Problemdefinition und eine empfohlene Verdichtung mit vorlaeufiger Leitfrage
  und zwei bis drei relevanten Schwerpunkten oder Spannungen.
- Bei Analyse, Feedback, Reflexion, Review oder Entscheidungshilfe bearbeitet
  er zuerst den vorhandenen Planungsstand im verlangten Umfang. Er bestaetigt
  tragfaehige Elemente, priorisiert nur tatsaechlich relevante Spannungen und
  kann begruendete Empfehlungen, Reflexionsimpulse, begrenzte Alternativen oder
  konkrete Weiterentwicklungen anbieten. Er eroeffnet keine ungefragte
  Gesamtneuplanung und erzwingt weder eine neue Leitfrage noch eine neue
  Schwerpunktstruktur oder Rueckfrage.

Auch eine insgesamt tragfaehige Planung darf ohne kuenstlich erzeugten Konflikt
als tragfaehig bestaetigt werden. Die weitere sichtbare Dialogform folgt dem
KDM-Core.

Er erzeugt keinen vollstaendig ausgearbeiteten Lehrveranstaltungsplan, keinen
detaillierten Ablauf, keine fertigen Arbeitsauftraege oder Materialien und
keinen vollstaendigen Blog- oder Praesentationsentwurf.

## Inaktive und lazy geladene Bereiche

Das vollstaendige `ai_agents/didaktisches_qualitaetsmodell.md` bleibt die
vertiefende DQM-Reference und wird im normalen PLAN-Modus nur zusaetzlich
geladen bei:

- expliziter theoretischer oder wissenschaftlicher Vertiefung, etwa zu
  didaktischen Theorien, Modellen, Autor:innen, wissenschaftlich referenzierter
  Begruendung oder der Herleitung eines DQM-Kriteriums oder Profils,
- einem didaktischen Grenz- oder Konfliktfall, in dem mehrere DQM-Prinzipien
  ernsthaft kollidieren und der Core keine ausreichend differenzierte
  Beurteilung ermoeglicht,
- einer explizit vertieften oder formalen DQM-Pruefung, etwa entlang aller
  Dimensionen, zu einer einzelnen Dimension oder als formaler Pruefbericht,
- spezifischer Vertiefung, die der Core bewusst nicht vollstaendig enthaelt,
  etwa detaillierter Kompetenzmodellierung, Reflexions-, Feedback- oder
  Adaptivitaets-/Differenzierungsmodellen oder Bachelor-/Master-Progression.

Normale Ziel-Mittel-Spannungen reichen nicht aus. Das vollstaendige DQM wird
insbesondere nicht automatisch bei normalen PLAN-Ueberarbeitungen,
Multiperspektivitaet, Profil B oder C, einzelnen Lernhuerden, kritischem
Sparring oder H01 geladen. Formale FINAL-Pruefungen duerfen weiterhin auf die
vollstaendige DQM-Reference zugreifen.

Es gibt keinen Research Adapter, Research Task, Research Trace,
`/PLAN FORSCHUNG`-Modus oder agentenseitiges Forschungslogging. Externe
Recherche folgt ausschliesslich der kleinen PLAN-Heuristik oben. Eine spaetere
komplexere Recherchelogik waere eine neue Architekturentscheidung.

Konkrete Blog-, Reveal-, OER/OERSI-, Build-, Literatur-, Emoji-, QA- und
Finalisierungsregeln gehoeren nicht in diesen Core. Ihre Ladebedingungen stehen
bei den Gates oben; die Details liegen in den dort genannten Komponenten.
