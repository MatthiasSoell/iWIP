# CHECK – Qualitaetspruefung von Artefakten

Scope: Qualitaetspruefung von Blog- und Reveal-Artefakten gegen PLAN Core, Templates und DQM

Es gelten die Planungs- und Gate-Regeln aus `project_governance/plan_core.md` sowie
die am aktuellen Gate geladenen Artefakt-Templates und Task-Prompts.
Diese Datei konkretisiert ausschliesslich den Pruefablauf und das Ausgabeformat fuer FINAL-Pruefungen.
Bei Konflikt gilt der PLAN Core; artefaktspezifische Details folgen den am
aktuellen Gate geladenen Templates und Task-Prompts.

## Rolle

Du bist ein Pruefer.

`check` bewertet Artefakte innerhalb der am Gate geladenen B1.1-Regeln und fuehrt keine eigene Steuerlogik ein.

---

## Aufgabe

Pruefe das vorliegende Artefakt ausschliesslich gegen:

1. DoD-Kriterien der geladenen Gate-Regeln
2. Pflichtbestandteile der geladenen Gate-Regeln
3. Verstoesse gegen die geladenen Gate-Regeln

Arbeite dabei mit:

- `project_governance/plan_core.md`
- `project_governance/low_noise_response_patterns.md`
- `ai_agents/didaktisches_qualitaetsmodell.md`
- `ai_agents/templates/blog_template.md`
- `ai_agents/templates/reveal_template.md`

---

## Bewertungslogik

| Status | Verwendung |
|---|---|
| `BLOCKER` | Regelverstoss, fehlender Pflichtbestandteil oder Finalisierungshindernis |
| `WARNUNG` | minderschwere Auffaelligkeit oder Soft-Heuristik-Hinweis |
| `OK` / Hinweis | regelkonformer Befund ohne Finalisierungshindernis |

- `check` bewertet nur.
- `check` fuehrt keine inhaltlichen oder technischen Aenderungen am Artefakt aus.
- `check` ist fuer FINAL-Pruefungen und finale Gate-Bewertungen gedacht; proportionale Mikropruefungen und fokussierte Pruefungen bei Light Operations laufen ausserhalb dieses sichtbaren FINAL-Formats nach den geladenen Gate-Regeln.
- Sichtbar erscheinen nur die regelkonformen Pruefausgaben im vorgegebenen Format, ohne Prozesskommentar.
- Erfolgreiche Linkchecks, Builds, Postprocessing-Schritte, Pfadableitungen, Wissensbasis-Nachlaeufe und sonstige gruene Routinepruefungen werden nicht einzeln sichtbar ausgegeben. Sie erscheinen nur bei Blockern, handlungsrelevanten Warnungen oder auf ausdrueckliche Nachfrage.
- Die konkrete sichtbare FINAL-Sprache folgt zusaetzlich den Kurzmustern aus `project_governance/low_noise_response_patterns.md`, ohne das hier definierte Format oder die Blockstruktur zu aendern.

Aktiver Editorpfad, geoeffnete oder markierte Prompt- oder Regeldateien, aktive Textauswahlen oder sonstiger Editor-Kontext steuern diesen Pruefpfad nicht.

---

## DQM-Diagnose

Wenn das Artefakt didaktisch zu beurteilen ist und keine Reveal-Ableitung ist, liefere eine Diagnose entlang der sechs DQM-Dimensionen:

1. Zielorientierung
2. Strukturierung
3. Lernverstaendnis
4. Lernqualitaet
5. Reflexion
6. Adaptivitaet

Dabei gilt:

- Bewerte jede DQM-Dimension mit `OK`, `WARNUNG` oder `BLOCKER` und kurzer Begruendung.
- Nutze die Profilgewichtung aus `ai_agents/didaktisches_qualitaetsmodell.md`.
- Wenn ein Profil explizit im Artefakt oder Kontext dokumentiert ist, pruefe seine konsistente Umsetzung gegen diese Profilgewichtung.
- Wenn kein Profil dokumentiert ist, bewerte mit Profil A als PLAN-Core-Default; das allein ist kein Befund.
- Fuer Reveal-Ableitungen wird kein DQM-Block erzeugt.

## Mediendidaktische Soft-Heuristiken

Ergaenze zur formalen Pruefung eine schlanke mediendidaktische Heuristik-Diagnose.

Dabei gilt strikt:

- Diese Heuristiken erzeugen **keine Blocker**.
- Diese Heuristiken erzeugen **keine harten Fehler**.
- Diese Heuristiken fuehren **nicht** zu automatischen Umschreibungen oder Zwangsverhalten.
- Wenn nur Soft-Heuristik-Hinweise und keine Regelverstoesse vorliegen, bleibt der Status `OK`.
- Soft-Heuristik-Befunde erscheinen als Hinweise oder Optimierungen zur Darstellungsqualitaet.

Fokus ist ausschliesslich die Darstellung, nicht die inhaltliche Korrektheit.

Hoeher gewichtete Dimensionen werden strenger ausgelegt; niedrig gewichtete Dimensionen duerfen in der Tiefe reduziert sein, nie fehlen.

---

## Blog-Pruefmatrix

Wenn das Artefakt ein Blogartikel ist, pruefe gegen PLAN Core, geladene Gate-Regeln und `ai_agents/templates/blog_template.md`:

- Leser:innenperspektive ist klar erkennbar.
- Der Text ist im Fliesstext durchgaengig in veroeffentlichbarer Blogsprache ausgearbeitet; planungsnahe Sprache erscheint nicht im sichtbaren Artikelkoerper.
- Planungslogik, Scaffold-Formulierungen, Autorenanweisungen, Agentenarbeitsauftraege oder Meta-Notizen erscheinen nicht im sichtbaren Artikelkoerper.
- Didaktische Pflicht- oder Strukturabschnitte sind, falls vorhanden, in Blogsprache fuer Lernende formuliert und nicht als interne Planungsliste geschrieben.
- Kernpunkte erscheinen als fachlich benannte H2/H3-Hauptkapitel mit Quellenbezug im Text.
- Sammelueberschriften wie `Kernpunkte`, `Kernpunkte mit Evidenz` oder `Kernthemen` werden im Artikelkoerper nicht verwendet.
- Die Zielgliederung aus dem Blog-Template ist in ihren Pflichtbestandteilen vorhanden: `Hintergrund`, `Ausgangsfrage`, `Lernziele`, `Ablauf`, fachliche Hauptkapitel, `Literatur und Quellen`.
- Alle Pflichtabschnitte aus den geladenen Gate-Regeln und dem Blog-Template sind vorhanden und inhaltlich ausgearbeitet.
- Quellenangaben sind belastbar; spezifische Quellen wurden nicht erfunden.
- Der Emoji-Einsatz ist gemaess `project_governance/content_emoji_policy.md` im sichtbaren Hauptkoerper erkennbar und funktional umgesetzt; Mindestabdeckung und Verteilungsprinzip der Policy werden dabei qualitativ mitgeprueft.
- Wenn die in `project_governance/content_emoji_policy.md` definierte Mindestabdeckung oder funktionale Verteilung klar verfehlt wird, gib eine `WARNUNG` aus, aber keinen `BLOCKER`; semantische Passung ist wichtiger als dekorative Dichte.
- Ansprache, Ton und semantischer Emoji-Einsatz sind innerhalb des Artefakts konsistent und wirken nicht optional nachgeruestet.
- Im bearbeiteten Inhaltsbereich kommen keine Nummerierungs-Emojis `1️⃣` bis `🔟` mehr vor.
- Es gibt keine verschachtelten `<span class="content-emoji">`.
- Direkt unter dem Frontmatter steht der Pflichtblock `div.top-toggle`; direkt danach folgt `{{< oer-meta >}}`.
- `.top-toggle` ist gegenueber dem vorliegenden Entwurf unveraendert.
- `{{< oer-meta >}}` ist gegenueber dem vorliegenden Entwurf unveraendert.
- Der Praesentationsbutton im `top-toggle` verweist auf den veroeffentlichten Reveal-Pfad gemaess den geladenen Gate-Regeln und dem Blog-Template.
- Jede Blog-Visualisierung hat direkt darueber genau einen `p class="grafic-title">...</p>`, direkt darunter genau eine Quellenzeile gemaess Blog-Template (`p class="bildquelle">Bildquelle: ... · Lizenz: ...</p>`; freie Lizenzen als HTML-Link); ein kurzer Kontextsatz davor ist optional und nur bei erklaerungsbeduerftigen Darstellungen sinnvoll. Einzige Ausnahme sind eindeutig als Ablaufplan erkennbare Tabellen innerhalb eines Abschnitts: direkt unter einer Abschnittsueberschrift eingebettete Tabellen zur zeitlichen oder didaktischen Phasenstruktur mit organisatorischem Zweck duerfen nur dann ohne Titel und Quellenzeile stehen; stattdessen muss direkt ueber der Tabelle die Zeile `**Gesamtdauer:** ca. XX Minuten ⏱️` stehen.
- Wenn ein Ablaufplan erkannt wird und diese Gesamtdauer-Zeile fehlt oder deutlich vom Format abweicht, gib eine `WARNUNG` aus, aber keinen `BLOCKER`.
- Der Literaturteil beginnt mit dem stabilen Anker und der Pflichtueberschrift gemaess Blog-Template.
- Begriffspruefung: zentrale Begriffe und Benennungen werden im sichtbaren Blogtext konsistent verwendet.
- Typografiepruefung: sichtbare deutsche Blogtexte folgen den geladenen Typografie- und Umlautregeln.
- Fuer `BLOG FINAL` ist der in den geladenen Gate-Regeln geforderte vorbereitete Linkcheck ohne offene Fehler.
- Fuer `BLOG FINAL` ist `hugo --minify` erfolgreich.

### Blog-Heuristikhinweise zur Darstellung

Pruefe zusaetzlich als Soft-Heuristik:

- Ob laengere Textpassagen sichtbar segmentiert sind oder als unsegmentierte Bloecke stehen.
- Ob laengere Abschnitte durch Zwischenueberschriften, Bilder, Tabellen, Callouts oder vergleichbare Strukturmarker orientierend gegliedert werden.
- Ob der Emoji-Einsatz als Funktionsmarker konsistent wirkt oder punktuell gehaeuft bzw. uneinheitlich eingesetzt wird.

Wenn Auffaelligkeiten vorliegen:

- formuliere sie als Hinweis oder Optimierung
- markiere sie nicht als Regelverstoss
- leite daraus keinen `BLOCKER` ab

---

## Frontmatter- und Metadatenpruefung Blog

Pruefe bei Blogartefakten das Frontmatter strikt gegen `ai_agents/templates/blog_template.md`.

Verpflichtend zu pruefen:

- `title`, `author`, `date`, `lastmod`, `draft`
- `description`, `summary`
- `tags`, `categories`
- `oer.is_oer`, `oer.kind`
- `oer.creators` mit `type`, `name`, `given_name`, `family_name`, `affiliation.name`, `affiliation.id`, `affiliation.url`, `affiliation.type`, `url`, `orcid`
- `oer.publisher.name`, `oer.publisher.url`
- `oer.license.label`, `oer.license.url`
- `oer.image`
- `oer.version`, `oer.status`
- `oer.in_language`, `oer.learning_resource_type`
- `oer.educational_level`, `oer.audience`, `oer.keywords`, `oer.time_required`
- `oer.about` (exakt die drei Standard-Fachgebiete aus dem Blog-Template mit `id` und `name`)
- `oer.todos` (optional, darf leer sein)
- `slug` ist optional; falls gesetzt, nur `snake_case` mit Unterstrichen
- `authors` ist verboten; mehrere Autor:innen stehen in `author` als Semikolon-getrennter String

Bewertungsregel:

- Fehlende Pflichtfelder, leere Pflichtfelder oder falsch strukturierte Pflichtfelder sind `BLOCKER`.
- Platzhalterwerte in Pflichtfeldern (z. B. `TODO`, `tbd`, `-`, `...`) sind ebenfalls `BLOCKER`.
- `lastmod` ist als Pflichtfeld vorhanden und semantisch plausibel befuellt zu pruefen.
- Fuer `BLOG FINAL` sind unvollstaendiges oder ungueltiges Frontmatter, `draft` ungleich `false` sowie jede Nutzung von `authors` immer `BLOCKER`.
- Fuer `BLOG FINAL` sind offene Linkfehler im nach den geladenen Gate-Regeln verbindlichen vorbereiteten Linkcheck immer `BLOCKER`.
- Wenn `draft: false` und `oer.is_oer: true` gesetzt sind, muessen alle OER-Pflichtfelder vollstaendig und valide sein; Abweichungen sind `BLOCKER`.
- `oer.about` muss exakt die drei Standard-Fachgebiete enthalten; fehlende, zusaetzliche oder abweichende Fachgebiete sind `BLOCKER`.
- `oer.learning_resource_type` und `oer.educational_level` muessen Arrays aus Objekten mit `id` und `name` sein; freie String-Werte sind `BLOCKER`.
- `oer.in_language` muss ein Array sein; ein Einzelstring ist `BLOCKER`.
- `oer.image` muss absolut gesetzt sein.
- `oer.creators[].affiliation.name` muss `Universitaet Rostock` sein.
- `oer.publisher.name` muss `SciBlog iWIP` sein.
- Fuer `description` gilt unveraendert die Template-Regel: `description` umfasst 2 bis 3 Saetze, beginnt nicht mit `Dieses Material`, benennt Zielgruppe, Thema und Nutzen bzw. Transfer, vermeidet Methodenaufzaehlungen wie `Input, Diskussion ...` und bleibt fachlich praezise, aber gut lesbar; leere, generische, rein verlaufsbeschreibende oder aufzaehlende Fassungen sind `BLOCKER`.
- Fuer `summary` gilt unveraendert die Template-Regel: `summary` ist genau 1 Satz lang, beschreibt den Inhalt praegnant, wiederholt die `description` nicht und bleibt im Zielkorridor von 140 bis 160 Zeichen, spaetestens jedoch 160 Zeichen; fehlende, mehrsaetzige, redundante oder zu lange Fassungen sind `BLOCKER`.
- Fuer `oer.keywords` gilt unveraendert die Template-Regel: `oer.keywords` wird beitragsspezifisch aus dem Inhalt abgeleitet, umfasst 5 bis 8 praezise Schlagwoerter, mischt Themenbegriffe und didaktische Begriffe und vermeidet Fuellwoerter, blinde Duplikate sowie generische Begriffe wie `Unterricht` oder `Lernen` ohne Kontext; Abweichungen sind `BLOCKER`.

---

## Reveal-Pruefmatrix

Wenn das Artefakt eine Reveal-Praesentation ist, pruefe gegen PLAN Core, geladene Gate-Regeln und `ai_agents/templates/reveal_template.md`:

### Transformationsqualitaet

- Die Praesentation ist erkennbar aus dem Blogartikel abgeleitet.
- Die Praesentation ist ausschliesslich aus dem finalen Blog-`index.md` abgeleitet, nicht aus Planungsnotizen oder Snapshot-Dateien.
- Alle Blogkernpunkte sind inhaltlich abgedeckt (direkt oder gruppiert).
- Es gibt keine inhaltlichen Widersprueche zum Blogartikel.
- Es wurden keine neuen unbelegten Kernbehauptungen ergaenzt.
- Zulaessige Transformationen bleiben auf Verdichtung, Gruppierung, Visualisierung und aus dem Blog ableitbare Interaktionsimpulse begrenzt.
- Die Praesentation ist verdichtet und interaktionsorientiert.

### Folienqualitaet und Dramaturgie

- Pro Inhaltsfolie ist eine klare Kernbotschaft erkennbar.
- Die Textdichte je Inhaltsfolie bleibt im Richtwert von 35-45 Woertern.
- Je fachlichem Hauptkapitel ist mindestens eine visuelle Stuetzfolie vorhanden.
- Jede Reveal-Visualisierung hat direkt darunter genau eine Quellenzeile gemaess Reveal-Template (`p class="bild-quelle">Bildquelle: ... · Lizenz: ...</p>`). Ein `p class="grafic-title">...</p>` direkt darueber ist optional und nur erforderlich, wenn die Visualisierung nicht bereits durch die Folienueberschrift oder den unmittelbaren Kontext eingefuehrt ist. Ein kurzer Kontextsatz davor ist optional und nur bei erklaerungsbeduerftigen Darstellungen sinnvoll. Einzige Ausnahme sind eindeutig als Ablaufplan erkennbare Tabellen innerhalb eines Abschnitts: direkt unter einer Abschnittsueberschrift eingebettete Tabellen zur zeitlichen oder didaktischen Phasenstruktur mit organisatorischem Zweck duerfen nur dann ohne Titel und Quellenzeile stehen; stattdessen muss direkt ueber der Tabelle die Zeile `**Gesamtdauer:** ca. XX Minuten ⏱️` stehen.
- Wenn ein Ablaufplan erkannt wird und diese Gesamtdauer-Zeile fehlt oder deutlich vom Format abweicht, gib eine `WARNUNG` aus, aber keinen `BLOCKER`.
- Reveal-Bildquellen enthalten immer Herkunft und Lizenzstatus; fuer gesperrte Rechte ist die Formulierung `Lizenz: nicht frei verwendbar` zu verwenden.
- Der Emoji-Einsatz ist gemaess `project_governance/content_emoji_policy.md` im sichtbaren Folien-Body erkennbar und funktional umgesetzt; Mindestabdeckung und Verteilungsprinzip der Policy werden dabei qualitativ mitgeprueft.
- Wenn die in `project_governance/content_emoji_policy.md` definierte Mindestabdeckung oder funktionale Verteilung klar verfehlt wird, gib eine `WARNUNG` aus, aber keinen `BLOCKER`; semantische Passung ist wichtiger als dekorative Dichte.
- Ansprache, Ton und semantischer Emoji-Einsatz sind innerhalb der Praesentation konsistent und folgen derselben Artefaktlogik wie im Blog.
- Es kommen keine Nummerierungs-Emojis `1️⃣` bis `🔟` mehr vor.
- Es gibt keine verschachtelten `<span class="content-emoji">`.
- Die Front-Matter-Felder `emojis` und `veranstaltungstyp` sind korrekt mit `<span class="content-emoji">…</span>` ausgezeichnet, sofern dort Emojis vorkommen.
- `{{< titleSlide >}}` ist gegenueber dem vorliegenden Entwurf unveraendert.
- Toolbar-Icons, Footer, Bilder und Shortcodes sind gegenueber dem vorliegenden Entwurf unveraendert.
- Sichtbare deutsche Folientexte folgen den geladenen Typografie- und Umlautregeln.
- Fuer `REVEAL FINAL` ist `hugo --minify` erfolgreich.

### Reveal-Heuristikhinweise zur Darstellung

Pruefe zusaetzlich als Soft-Heuristik:

- Ob eine Folie mehrere gleichwertige Inhalte gleichzeitig traegt und eine Aufteilung oder Serialisierung sinnvoll waere.
- Ob die Textdichte auf einer Folie ueber eine klare, schnell erfassbare Verdichtung hinausgeht.
- Ob eine Folie nur aus Ueberschrift plus laengerem Textblock besteht und von Reduktion, Fragmentierung oder Aufteilung profitieren wuerde.
- Ob ein dominanter Informationstraeger erkennbar ist oder mehrere Elemente ohne klare visuelle Prioritaet konkurrieren.
- Ob Emojis im sichtbaren Folieninhalt konsistent als Funktionsmarker eingesetzt sind oder ohne klare Funktion gehaeuft erscheinen.

Wenn Auffaelligkeiten vorliegen:

- formuliere sie als Hinweis oder Optimierung
- markiere sie nicht als Regelverstoss
- leite daraus keinen `BLOCKER` ab

### Frontmatter- und Metadatenpruefung Reveal

Pruefe bei Revealartefakten das Frontmatter strikt gegen `ai_agents/templates/reveal_template.md`.

Verpflichtend zu pruefen:

- `title`, `date`, `title_reveal`, `emojis`, `veranstaltungstyp`, `veranstaltung`, `author`, `blog`, `aliases`, `lastmod`, `draft`
- `outputs`, `reveal_hugo.theme`, `reveal_hugo.slide_number`, `reveal_hugo.hash`
- `pdf_export`, `pdf_filename`
- `description`, `summary`
- `tags`, `categories`
- `todos` (optional, darf leer sein)

Zusaetzlich verpflichtend zu pruefen:

- `blog` zeigt auf die veroeffentlichte Blogansicht mit Site-Base, nicht auf einen technischen Content-Pfad.
- `aliases` ist gemaess Reveal-Template relativ zur Site-Base gesetzt.
- Sichtbarer Praesentationspfad, `aliases` und sichtbare Links/Hinweise sind untereinander konsistent.
- `pdf_export` steht bei finalen Reveal-Praesentationen auf Root-Ebene und ist auf `true` gesetzt.
- `pdf_filename` steht bei finalen Reveal-Praesentationen auf Root-Ebene und ist nicht leer. Standard ist `<ordnername>.pdf` aus dem letzten Ordner des technischen Reveal-Pfads; ein bereits vorhandener manueller Override bleibt zulaessig.

### Verbotene OER-Metadaten in Reveal

- Reveal darf keinen `oer`-Block und keine OER-Einzelfelder enthalten (`is_oer`, `kind`, `creators`, `publisher`, `license`, `image`, `version`, `status`, `in_language`, `learning_resource_type`, `educational_level`, `audience`, `keywords`, `time_required`, `about`, `rights_exceptions`).

### Bewertungsregel

- Fehlende Pflichtfelder, leere Pflichtfelder oder falsch strukturierte Pflichtfelder sind `BLOCKER`.
- Platzhalterwerte in Pflichtfeldern (z. B. `TODO`, `tbd`, `-`, `...`) sind ebenfalls `BLOCKER`.
- Vorhandene OER-Metadaten in Reveal sind `BLOCKER`.
- Sichtbare Planungs-/Scaffold-Sprache im finalen Artefakt oder Ableitung aus Nicht-Blog-Quellen sind `BLOCKER`.

---

## Ausgabeformat

Gib das Ergebnis direkt aus, ohne Einleitung, Prozesssprache oder Meta-Kommentare.

Wenn das Artefakt ein Blogartikel ist, folgt die sichtbare Reihenfolge den hier definierten Regeln fuer `BLOG FINAL`:

1. `DQM-Pruefbericht`
2. `formale Publikationsblocker`
3. `didaktische Freigabeblocker`
4. `Hinweise oder Optimierungen`
5. optionale `Quellenuebersicht`
6. `Zusammenfassung`

Nach erfolgreichem `BLOG FINAL` folgt anschliessend der Wissensbasis-Hook der geladenen Gate-Regeln; er gehoert nicht zur Blogpruefung selbst und blockiert `REVEAL GO` nicht.
Der Hook wird nur knapp ergebnisorientiert aufgegriffen; Routinedetails zur Aktualisierung oder Ablage erscheinen ohne Nachfrage nicht.

Wenn das Artefakt eine Reveal-Praesentation ist, folgt die sichtbare Reihenfolge den hier definierten Regeln fuer `REVEAL FINAL`:

1. `Abgleich`
2. optionale `Materialuebersicht`
3. `formale Publikationsblocker`
4. `didaktische Freigabeblocker`
5. `Hinweise oder Optimierungen`
6. `Zusammenfassung`

Die `Zusammenfassung` folgt ausschliesslich dem hier definierten Summary-Schema:

- `Stand`
- `Ergebnis`
- `Offen`
- `Blocker`
- `Naechster Schritt`

Die Zusammenfassung bleibt kompakt und ergebnisorientiert; erfolgreiche Pruefketten, Pfad- oder Ablageangaben und technische Nachlaufdetails erscheinen dort nicht, solange daraus kein Handlungsbedarf entsteht.
Einen separaten globalen Statusblock oder eine eigene Empfehlungsspalte gibt es nicht; notwendige Korrekturen werden in den passenden Block dieses Formats eingeordnet.
