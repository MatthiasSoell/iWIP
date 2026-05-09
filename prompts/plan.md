# /plan — Didaktische Planung starten

Kontext: Einstieg und Routing in die Arbeit nach Contract

---

Dieser Prompt startet eine neue didaktische Planung im SciBlog iWIP
und routet den Fall in die Steuerlogik aus `project_governance/agent_contract.md`.

Es gelten die Regeln aus `project_governance/agent_contract.md`.
Diese Datei konkretisiert ausschliesslich den Einstieg fuer `/PLAN` und `/PLAN FORSCHUNG`.
Bei Konflikt gilt der Contract.

Arbeite strikt nach:

- `project_governance/agent_contract.md`
- `ai_agents/master_agent.md`
- `ai_agents/didaktisches_qualitaetsmodell.md`
- `ai_agents/templates/blog_template.md`
- `ai_agents/templates/reveal_template.md`

`prompts/plan.md` fuehrt keine eigene Steuerlogik ein.

---

## Rolle

`plan` ist ein Router.

---

## Aufgabe

`plan` interpretiert den Nutzereinstieg,
ueberfuehrt ihn in den passenden Planungsmodus
und uebergibt vollstaendig an den Contract.

Der Agent nutzt vorhandene Informationen aus Initialprompt, Folgeprompts und
Kontext vorrangig. Er fragt nur dann gezielt nach, wenn fuer didaktisch
relevante Entscheidungen wesentliche Informationen fehlen, Angaben
widerspruechlich sind oder sich nicht tragfaehig ableiten lassen. Es gibt
keine Standardabfrage und keine routinemaessige Vollabfrage aller Parameter.

Dabei gilt fuer den Handoff an den Contract:

- `/PLAN` startet immer in `P1` oder `P2`; die erste Reaktion bleibt Planungs- und Strukturierungsmodus.
- `/PLAN FORSCHUNG` startet denselben Planungsdialog, aktiviert zusaetzlich aber einen optionalen Forschungs-/Rohdatenmodus in `exports/research/`.
- Die Forschungsbefehle `/PLAN FORSCHUNG`, `FORSCHUNGSPROTOKOLL START` und `FORSCHUNGSPROTOKOLL FINAL` gehoeren ausschliesslich zu diesem optionalen Forschungsmodus; der Kernworkflow mit `/PLAN`, `BLOG GO`, `BLOG FINAL`, `REVEAL GO` und `REVEAL FINAL` bleibt unveraendert.
- `plan` nutzt vorhandenen Kontext vorrangig und stellt nur die naechste entscheidende Rueckfrage.
- `plan` darf in der ersten Reaktion strukturieren, analysieren, genau eine priorisierte Rueckfrage stellen oder einen kompakten Planungsstand formulieren; ohne explizites `BLOG GO` werden keine Dateien angelegt.
- Der erste `/PLAN`-Turn bleibt immer Planung. Formulierungen wie `leg los`, `mach direkt`, `erstell das`, `Blog und Reveal` oder `fertig ausarbeiten` loesen im ersten Turn keine Dateierzeugung aus.
- Ohne explizites `BLOG GO` entstehen weder `index.md` noch `_index.md`; im Standardmodus entstehen ausserdem keine Snapshots, keine Chatlogs und keine Rohdatenexporte.
- Der Forschungsmodus ist ein Zusatzmodus und ersetzt keine Standardstatusmeldung; auch mit `/PLAN FORSCHUNG` bleiben `BLOG GO`, `BLOG FINAL`, `REVEAL GO` und `REVEAL FINAL` unveraendert.
- Forschungsartefakte sind optional. Empfohlene Dateien unter `exports/research/` sind `chat_log.md`, `planning_trace.md` und `decision_log.md`; Snapshots sind kein Pflichtbestandteil.
- `BLOG GO` ist das erste Erzeugungsgate fuer den Blog. Reveal bleibt sekundaer und entsteht erst spaeter durch `REVEAL GO` aus dem finalen Blog-`index.md`.
- `plan` loest keinen Hugo-Build aus.
- Blog- und Reveal-Frontmatter werden ausschliesslich nach den Templates ausgearbeitet; fehlende OER-Pflichtfelder werden nicht durch Defaults, Fachableitungen oder erratene Werte ersetzt.
- Der optionale Wissensbasis-Anschluss folgt dem Contract und wird nicht durch `/PLAN` oder `REVEAL GO` ausgeloest.

Fuer diese gezielte Klaerung kann der Agent bei Bedarf selektiv nach Zielgruppe,
Kontext, Vorwissen, typischen Lernhuerden, Zeitrahmen, Format, Setting oder
fachlichem Kontext fragen. Solche Nachfragen sind situationsabhaengig und nur
bei tatsaechlichem didaktischem Bedarf zulaessig.

Profil A bleibt gemaess Contract der Default. Bei klaren Hinweisen im Anliegen
oder Kontext kann der Agent knapp und begruendet ein passenderes Profil B oder
C vorschlagen oder einen Wechsel anregen, ohne eine verpflichtende
Profilrueckfrage zu erzwingen. Wenn das Profil fuer eine didaktische
Entscheidung tatsaechlich ausschlaggebend ist, gilt weiterhin die Contract-Regel
einer gezielten Klaerungsfrage.

Fuer die Planung beruecksichtigt der Agent intern insbesondere die Passung von
Zielen, Inhalten, Aktivitaeten und gegebenenfalls Pruefung, eine erkennbare
lernlogische Struktur statt additiver Aneinanderreihung, Lernaktivitaet ueber
reine Rezeption hinaus, funktional eingebundene Reflexion sowie grundlegende
Adaptivitaet im Blick auf typische Lernhuerden. Diese Punkte werden weder als
Checkliste ausgegeben noch routinemaessig abgefragt, sondern nur genutzt, um
gezielte Anschlussfragen oder knappe Hinweise zu generieren.

Bei geeigneten Themen kann der Agent zusaetzlich situativ Perspektivwechsel,
Zielkonflikte, gesellschaftliche Einbettung oder Lebenswelt- bzw. Berufsbezug
anregen. Auch dies erfolgt ohne formale Zusatzstruktur und nur, wenn es die
Planung sichtbar staerkt.

---

## WICHTIG

Aktiver Editorpfad, geoeffnete oder markierte Prompt- oder Regeldateien, aktive
Textauswahlen oder sonstiger Editor-Kontext steuern den Einstieg nicht.
Massgeblich sind Anliegen und eindeutig erkennbare Arbeitsbefehle gemaess
Contract.