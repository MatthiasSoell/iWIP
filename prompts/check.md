# /check — Didaktischer Qualitätscheck

Dieser Prompt führt einen **didaktischen Qualitätscheck** für eine geplante Lehrveranstaltung oder Lehr-Lern-Einheit durch.

Arbeite strikt nach den Regeln aus:

ai_agents/master_agent.md

Der Fokus liegt auf der **didaktischen Kohärenz** der Planung.

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

QUICK-Modus:

- Wenn der Arbeitsmodus `QUICK` ist, prüfe ausschließlich die drei Minimalchecks gemaess `ai_agents/master_agent.md` (Core Rule 37).
- Alle weiteren Prüfkategorien, Reportings und Guardrails werden in `QUICK` nicht angewendet.

QUALITY-Modus:

- Alle folgenden detaillierten Prüfkategorien gelten vollständig im Modus `QUALITY`.

## Materialien ↔ Planung

- Werden vorhandene Materialien sinnvoll in die Planung eingebunden?
- Unterstützen sie die Lernziele und den Ablauf?
- Gibt es Material, das eher dekorativ als lernförderlich eingesetzt wird?

---

## Prüfkategorien

## 1 🎯 Zielklarheit

- Sind die Lernziele klar formuliert?
- Beschreiben sie Verständnis, Anwendung oder Reflexion?
- Sind sie realistisch im Zeitrahmen erreichbar?

---

## 2 Inhalte ↔ Ziele

- Unterstützen die Inhalte die Lernziele?
- Gibt es Inhalte ohne klaren Bezug zu den Zielen?

---

## 3 Methoden ↔ Ziele

- Unterstützen die gewählten Methoden die Lernziele?
- Fördern sie **Verständnis, Anwendung und Reflexion**?

---

## 4 Interaktionsgrad

- Gibt es ausreichend Aktivierungsphasen?
- Überwiegt Vortrag oder Interaktion?
- Werden Lernende aktiv eingebunden?

---

## 5 Mediennutzung 💻

- Unterstützen die Medien das Lernen?
- Oder sind sie nur Präsentationshilfe?

---

## 6 Wissenschaftliche Fundierung

- Wird das Thema fachlich korrekt dargestellt?
- Wird zwischen **Bachelor- und Master-Niveau** sinnvoll differenziert?

---

## 7 Zeitrealismus

- Ist der Ablauf realistisch umsetzbar?
- Gibt es zu viele Inhalte oder Aktivitäten?

---

## 8 Blogmodus-Qualität

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
    Blogartefakte prüfen (insbesondere 17, 18, 19, 20, 25, 26, 27, 30, 31, 32, 33, 36, 37).

---

## 9 Frontmatter- und Metadaten-Vollständigkeit (Pflicht)

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

## 10 Reveal-Transformationsqualität

- Ist die Präsentation erkennbar aus dem Blogartikel abgeleitet?
- Deckt die Präsentation alle Blogkernpunkte inhaltlich ab (direkt oder gruppiert)?
- Sind Kernbehauptungen zwischen Blog und Reveal konsistent?
- Wurden keine neuen unbelegten Kernaussagen ergänzt?
- Ist die Präsentation verdichtet und interaktionsorientiert statt blogartig ausformuliert?
- Ist die Foliengestaltung visuell klar (kurze Folientexte, fragmentierte Progression, eindeutige Kernbotschaften)?
- Entspricht die Tonalität eher einer präsentationsfähigen Dramaturgie als einer Folien-Textsammlung?
- Trägt jede Inhaltsfolie genau eine priorisierte Kernbotschaft?
- Liegt die Textdichte je Inhaltsfolie im foliengerechten Bereich (Richtwert 35-45 Wörter)?
- Ist je fachlichem Hauptkapitel mindestens eine visuelle Stützfolie vorhanden (Grafik/Diagramm/Tabelle/Schema)?
- Enthalten Visualisierungen kurze, saubere Quellenzeilen?
- Ist der Emoji-Einsatz semantisch konsistent gemäß `project_governance/content_emoji_policy.md`?
- Entsprechen sichtbare deutsche Folientexte den Typografie-/Sprachregeln gemäß `ai_agents/master_agent.md` (insbesondere Core Rules 14 und 20)?
- Zusätzlich alle einschlägigen Core Rules aus `ai_agents/master_agent.md` für
    Revealartefakte prüfen (insbesondere 16, 20, 22, 24, 29, 32, 33, 34, 36, 37, 38).

---

## 11 Reveal-Frontmatter- und Metadaten-Vollständigkeit (Pflicht)

Prüfe bei Revealartefakten das Frontmatter strikt gegen
`ai_agents/templates/reveal_template.md`.

Verpflichtend zu prüfen:

- `title`, `title_reveal`, `emojis`, `veranstaltungstyp`, `veranstaltung`, `author`, `blog`, `source_lastmod`, `date`, `lastmod`, `draft`
- `outputs`, `reveal_hugo.theme`, `reveal_hugo.slide_number`, `reveal_hugo.transition`, `reveal_hugo.custom_theme`
- `description`, `summary`
- `tags`, `categories`
- `oer.is_oer`, `oer.kind`, `oer.note`
- `oer.creators` mit `name`, `given_name`, `family_name`, `affiliation`, `url`, `orcid`
- `oer.publisher.name`, `oer.publisher.url`
- `oer.license.label`, `oer.license.url`
- `oer.source.label`, `oer.source.url`
- `oer.in_language`, `oer.learning_resource_type`
- `oer.educational_level`, `oer.audience`, `oer.time_required`
- `oer.about` (mindestens ein `term`)
- `oer.rights_exceptions` (optional)
- `oer.todos` (optional, darf leer sein)

Bewertungsregel:

- Fehlende Pflichtfelder, leere Pflichtfelder oder falsch strukturierte Pflichtfelder sind **Blocker**.
- Platzhalterwerte in Pflichtfeldern (z. B. `TODO`, `tbd`, `-`, `...`) sind ebenfalls **Blocker**.
- Zusätzlich gelten die Blocker-/Hinweislogiken aus `ai_agents/master_agent.md`
    (insbesondere 16, 23, 24, 29, 33, 34, 37, 38) unverändert.
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
