# /check — Didaktischer Qualitätscheck

Dieser Prompt führt einen **didaktischen Qualitätscheck** für eine geplante Lehrveranstaltung oder Lehr-Lern-Einheit durch.

Arbeite strikt nach den Regeln aus:

ai_agents/master_agent.md

Der Fokus liegt auf der **didaktischen Kohärenz** der Planung.

Didaktische Prüflogik:

- Das DQM in `ai_agents/didaktisches_qualitaetsmodell.md` ist das einzige didaktische Referenzmodell.
- Die didaktische Bewertung erfolgt entlang der sechs DQM-Dimensionen.
- Die Bewertung erfolgt profilabhängig gewichtet (Profil A/B/C gemäß DQM), bei gleichzeitigem Mindeststandard: keine Dimension darf ❌ sein.
- Bei Abweichungen in hoch gewichteten Dimensionen ist die Bewertung strenger auszulegen als in niedrig gewichteten Dimensionen.


---

## Aufgabe

Analysiere den vorliegenden Blogartikel, Veranstaltungsentwurf oder Ablaufplan.

Prüfe systematisch die didaktische Stimmigkeit.

Berücksichtige insbesondere:

- Zielgruppe
- Art des Planungsgegenstands
- institutionellen Kontext der Veranstaltung
- Lernziele
- Inhalte
- Methoden
- Medien
- Interaktion
- Zeitstruktur
- wissenschaftliche Fundierung
- Förderung von Deep Learning

Priorisierung der Prüfung:

- Wenn das Artefakt ein Blogartikel ist, prüfe **zuerst** die Blogmodus-Qualität.
- Wenn das Artefakt eine Reveal-Präsentation ist, prüfe **zuerst** die Reveal-Transformationsqualität.
- Wenn das Artefakt ein reiner Veranstaltungsentwurf ist, beginne mit der didaktischen Kohärenz.

Gate-basierter Rigor (gemaess Core Rule 38):

- Waehrend der Entwurfsarbeit (`.index.md`) gelten die Minimal-Checks gemaess Core Rule 38 in `ai_agents/master_agent.md`.
- Bei Finalisierung (`BLOG FINAL`, `REVEAL GO`) greifen automatisch alle folgenden detaillierten Prüfkategorien, Reportings und Guardrails.

## Materialien ↔ Planung

- Werden vorhandene Materialien sinnvoll in die Planung eingebunden?
- Unterstützen sie die Lernziele und den Ablauf?
- Gibt es Material, das eher dekorativ als lernförderlich eingesetzt wird?

---

## Didaktische Pruefkategorien (DQM-Kern)

## 1 🎯 Zielorientierung (DQM)

- Sind die Lernziele kompetenzorientiert und als beobachtbare Handlungen formuliert?
- Passen die Lernziele zum Niveau und Kontext der Zielgruppe?
- Ist das Anforderungsniveau transparent und realistisch im Zeitrahmen?

---

## 2 🧭 Strukturierung (DQM)

- Ist der Lehr-Lern-Prozess didaktisch schluessig sequenziert?
- Ist der Ablauf realistisch umsetzbar (keine Ueberfrachtung)?
- Sind Uebergaenge zwischen den Phasen klar?

---

## 3 🧠 Lernverstaendnis (DQM)

- Ist das Verhaeltnis von Lehrenden- und Lernendenaktivitaet bewusst gestaltet?
- Werden Lernende aktiv eingebunden statt ueberwiegend rezeptiv gefuehrt?
- Ist die Lernlogik konsistent zum gewaehlten Profil (A/B/C)?

---

## 4 👥 Lernqualitaet (DQM)

- Gehen Aufgaben ueber Reproduktion hinaus (Erklaeren, Vergleichen, Begruenden, Bewerten)?
- Foerdern die Aktivitaeten Verstaendnis, Anwendung, Transfer und Deep Learning?
- Ist Constructive Alignment (Ziele ↔ Aktivitaeten ↔ Assessment) erkennbar?

---

## 5 🪞 Reflexion (DQM)

- Sind explizite Reflexionsanlaesse vorhanden?
- Gibt es formative Feedback-Elemente (Feed-up / Feed-back / Feed-forward)?
- Passt die Reflexionstiefe zum gewaehlten Profil und Lernzielniveau?

---

## 6 🌱 Adaptivitaet (DQM)

- Werden Zielgruppe, Voraussetzungen und Kontext angemessen beruecksichtigt?
- Gibt es sinnvolle Differenzierungsoptionen (Niveau, Tempo, Zugang)?
- Ist der Medieneinsatz lernfoerderlich begruendet statt nur praesentativ?

---

## DQM-Bewertungsregel (verbindlich)

- Bewerte jede DQM-Dimension mit ✅ / ⚠️ / ❌ und kurzer Begruendung.
- Nutze die profilabhaengige Gewichtung (A/B/C) aus `ai_agents/didaktisches_qualitaetsmodell.md`.
- Hoeher gewichtete Dimensionen werden strenger ausgelegt; niedrig gewichtete Dimensionen duerfen nur in der Tiefe reduziert sein, nie fehlen.
- Mindeststandard bleibt immer verbindlich: keine Dimension darf ❌ sein.
- Bei ❌ ist eine Rueckfrage verpflichtend, bevor ein Artefakt als final bewertet werden darf.

---

## 7 Blogmodus-Qualitaet (Erweiterung)

- Ist der Text klar leser:innenorientiert statt planungsintern formuliert?
- Wird die inhaltliche Argumentation im Fließtext entwickelt (statt nur im Ablauf)?
- Ist der Ablauf unterstützend, aber nicht dominierend?
- Sind die Kernpunkte als eigene inhaltliche Abschnitte sichtbar und mit Quellen belegt?
- Sind die fachlichen Hauptinhalte als fachlich benannte H2/H3-Kapitel strukturiert (z. B. Lerntypen, Lernformen, Prüfungsformen)?
- Wurde auf Sammelüberschriften wie `Kernpunkte` oder `Kernpunkte mit Evidenz` im Artikelkörper verzichtet?
- Entspricht die Kapitelreihenfolge weitgehend der Zielstruktur (Hintergrund -> Ausgangsfrage -> Lernziele -> Aufbau & Ablauf -> fachliche H2/H3-Hauptkapitel -> Literatur)?
- Sind Quellenangaben belastbar (keine erkennbar erfundenen Studien-/DOI-Details)?
- Wird bei unsicherer Quellenlage transparent argumentiert statt Literatur zu erfinden?
- Wirkt der Text stilistisch wie ein publizierter SciBlog-Beitrag (statt generischer KI-Prosa)?
- Wurden stichpunktartige Nutzerinhalte kapitelweise in leser:innenfreundlichen Fließtext mit klaren Übergängen überführt?
- Ist erkennbar, dass der Text kapitelweise ko-kreativ entwickelt wurde (inhaltstreu zur Nutzerbasis, sprachlich redaktionell verdichtet)?
- Ist der Emoji-Einsatz funktional, konsistent und als Strukturhilfe erkennbar?
- Ist direkt unter dem Frontmatter der Pflichtblock `div.top-toggle` enthalten?
- Steht direkt nach `div.top-toggle` der Shortcode `{{< oer-meta >}}`?
- Verweist der Präsentationsbutton im `top-toggle` auf `/iWIP/praesentation/<bereich>/<ordner>/`, wobei `<bereich>/<ordner>` exakt dem Blogpfad `content/blog/<bereich>/<ordner>/index.md` entspricht?
- Ist eine knappe Meta-Reflexion zu Methoden- und Medienlogik im Abschnitt `Hintergrund` integriert?
- Werden keine separaten Standardabschnitte `Methoden`, `Medien`, `Reflexion` verwendet, sofern sie keinen zusätzlichen Erkenntnisgewinn bringen?
- Sind Literaturerwähnungen im Fließtext auf den Literaturanker verlinkt (z. B. `#literatur`)?
- Sind Mehrfachzitate als getrennte Links formatiert (Semikolon/Leerzeichen außerhalb der Links)?
- Sind Literaturangaben in Quellenzeilen unter Tabellen/Grafiken ebenfalls auf den Literaturanker verlinkt?
- Ist das Literaturverzeichnis APA-7-nah konsistent formatiert?
- Sind Zusatzlinks je Quelle konsistent als Badge (`lit-ub`, `lit-doi`, `lit-worldcat`) oder als normaler Weblink dargestellt?
- Zusätzlich alle einschlägigen Core Rules aus `ai_agents/master_agent.md` für
    Blogartefakte prüfen (insbesondere 17, 18, 19, 20, 25, 26, 27, 30, 31, 32, 33, 38, 39, 43).

---

## 8 Frontmatter- und Metadaten-Vollstaendigkeit (Pflicht)

Prüfe bei Blogartefakten das Frontmatter strikt gegen
`ai_agents/templates/blog_template.md`.

Verpflichtend zu prüfen:

- `title`, `authors`, `date`, `lastmod`, `draft`
- `description`, `summary`
- `tags`, `categories`
- `oer.is_oer`, `oer.kind`
- `oer.creators` mit `name`, `given_name`, `family_name`, `affiliation`, `url`, `orcid`
- `oer.publisher.name`, `oer.publisher.url`
- `oer.license.label`, `oer.license.url`
- `oer.source.label`, `oer.source.url`
- `oer.version`, `oer.status`
- `oer.in_language`, `oer.learning_resource_type`
- `oer.educational_level`, `oer.audience`, `oer.time_required`
- `oer.about` (mindestens ein `term`)
- `oer.todos` (optional, darf leer sein)
- `slug` ist optional; falls gesetzt, nur `snake_case` mit Unterstrichen (z. B. `did_allg_fach`)

Bewertungsregel:

- Fehlende Pflichtfelder, leere Pflichtfelder oder falsch strukturierte Pflichtfelder sind **Blocker**.
- Platzhalterwerte in Pflichtfeldern (z. B. `TODO`, `tbd`, `-`, `...`) sind ebenfalls **Blocker**.
- Ein Blogartefakt darf bei Blockern nicht als "final" bewertet werden.
- Wenn `lastmod` trotz inhaltlicher Aenderung nicht aktualisiert wurde, ist das ein **Blocker**.

---

## 9 Reveal-Pruefmatrix (verbindlich)

Prüfe Revealartefakte in der folgenden Reihenfolge.

### 9.1 Transformationsqualitaet

- Ist die Präsentation erkennbar aus dem Blogartikel abgeleitet?
- Deckt die Präsentation alle Blogkernpunkte inhaltlich ab (direkt oder gruppiert)?
- Sind Kernbehauptungen zwischen Blog und Reveal konsistent?
- Wurden keine neuen unbelegten Kernaussagen ergänzt?
- Ist die Präsentation verdichtet und interaktionsorientiert statt blogartig ausformuliert?

### 9.2 Folienqualitaet und Dramaturgie

- Ist die Foliengestaltung visuell klar (kurze Folientexte, fragmentierte Progression, eindeutige Kernbotschaften)?
- Entspricht die Tonalität eher einer präsentationsfähigen Dramaturgie als einer Folien-Textsammlung?
- Trägt jede Inhaltsfolie genau eine priorisierte Kernbotschaft?
- Liegt die Textdichte je Inhaltsfolie im foliengerechten Bereich (Richtwert 35-45 Wörter)?
- Ist je fachlichem Hauptkapitel mindestens eine visuelle Stützfolie vorhanden (Grafik/Diagramm/Tabelle/Schema)?
- Enthalten Visualisierungen kurze, saubere Quellenzeilen?
- Ist der Emoji-Einsatz semantisch konsistent gemäß `project_governance/content_emoji_policy.md`?
- Entsprechen sichtbare deutsche Folientexte den Typografie-/Sprachregeln gemäß `ai_agents/master_agent.md` (insbesondere Core Rules 14 und 20)?

### 9.3 Frontmatter- und Metadaten-Vollstaendigkeit

Prüfe bei Revealartefakten das Frontmatter strikt gegen
`ai_agents/templates/reveal_template.md`.

Verpflichtend zu prüfen:

- `title`, `date`, `title_reveal`, `emojis`, `veranstaltungstyp`, `veranstaltung`, `author`, `blog`, `lastmod`, `draft`
- `outputs`, `reveal_hugo.theme`, `reveal_hugo.slideNumber`, `reveal_hugo.hash`
- `description`, `summary`
- `tags`, `categories`
- `todos` (optional, darf leer sein)

### 9.4 Verbotene OER-Metadaten in Reveal

- Reveal darf keinen `oer`-Block und keine OER-Einzelfelder enthalten (`is_oer`, `kind`, `creators`, `publisher`, `license`, `source`, `in_language`, `learning_resource_type`, `educational_level`, `audience`, `time_required`, `about`, `rights_exceptions`).

### 9.5 Bewertungsregel

- Fehlende Pflichtfelder, leere Pflichtfelder oder falsch strukturierte Pflichtfelder sind **Blocker**.
- Platzhalterwerte in Pflichtfeldern (z. B. `TODO`, `tbd`, `-`, `...`) sind ebenfalls **Blocker**.
- Vorhandene OER-Metadaten in Reveal sind **Blocker**.
- Zusätzlich alle einschlägigen Core Rules aus `ai_agents/master_agent.md` für
    Revealartefakte prüfen (insbesondere 16, 20, 22, 24, 29, 32, 33, 34, 38, 40, 41).
- Zusätzlich gelten die Blocker-/Hinweislogiken aus `ai_agents/master_agent.md`
    (insbesondere 16, 23, 24, 29, 33, 34, 38, 40) unverändert.
- Ein Revealartefakt darf bei Blockern nicht als "final" bewertet werden.

---

## Ergebnisformat

Gib deine Analyse in vier Abschnitten aus:

## 🔴 Formale Blocker

Liste nur formale Blocker auf (z. B. fehlende Frontmatter-Pflichtfelder).
Wenn keine Blocker vorliegen, schreibe: `Keine formalen Blocker.`

---

## 🟢 Stärken der Planung

Was funktioniert didaktisch gut?

---

## 🟡 mögliche Inkonsistenzen

Wo gibt es Spannungen zwischen:

- Zielen
- Inhalten
- Methoden
- Medien

---

## Constructive Alignment

Prüfe, ob Lernziele, Lernaktivitäten und Leistungsüberprüfung konsistent aufeinander abgestimmt sind.

Fragen:

- Unterstützen die geplanten Methoden tatsächlich die formulierten Lernziele?
- Erfordert die Leistungsüberprüfung genau die Kompetenzen, die gelernt werden sollen?
- Gibt es Lernziele, die weder durch Aktivitäten noch durch Prüfung adressiert werden?
- Gibt es Aktivitäten, die nicht zu den Lernzielen beitragen?
- Passt die Art des Lernprozesses (z. B. Wissen aufbauen, analysieren, reflektieren) zu den geplanten Aktivitäten?
- Ist erkennbar, woran die Zielerreichung konkret festgestellt werden soll?

Wenn Inkonsistenzen auftreten:

schlage konkrete Anpassungen vor.

---

## 🔧 konkrete Verbesserungsvorschläge

Nenne maximal **3–5 gezielte Verbesserungen**.

Bei Reveal-Artefakten müssen die Vorschläge priorisiert sein als:

1. formale Blocker,
2. dramaturgische/stilistische Qualitätslücken,
3. optionale Feinschliffe.

---

## 🎨 mögliche Visualisierungen

Schlage Stellen vor, an denen eine Visualisierung helfen könnte.

Zum Beispiel:

- Ablaufdiagramm
- Vergleichstabelle
- Kompetenzschema
- Prozessgrafik
- Concept Map

---

## Ziel

Der Check soll helfen,

- **didaktische Kohärenz zu verbessern**
- **Deep Learning zu fördern**
- **Interaktion zu stärken**
- **die Planung realistischer zu machen**

Die Analyse soll **klar, konstruktiv und prägnant** sein.
