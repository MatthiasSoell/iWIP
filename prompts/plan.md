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
- `project_governance/low_noise_response_patterns.md`
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

- `plan` wertet nur den Einstieg aus und uebergibt dann an die im Contract definierte State Machine mit ihren Gates, Guards, Hooks und Exit-Actions.
- `/PLAN FORSCHUNG` aktiviert den Forschungsmodus sofort und ohne weitere Routing-Rueckfrage; die Contract-Initialisierung laeuft vor weiterer Detailplanung an.
- Bei `/PLAN FORSCHUNG` ist diese Contract-Initialisierung zwingende Vorbedingung des ersten fachlichen Planungszuges: Vor `Problemdefinition`, `Empfohlene Verdichtung` oder jeder anderen fachlichen Verdichtung muessen `case_id` sowie `metadata.yaml`, `chat_log.md`, `planning_trace.md` und `decision_log.md` angelegt sein.
- Ein explizites `/PLAN FORSCHUNG` behaelt diesen Vorrang auch dann, wenn derselbe Nutzersatz bereits Thema, Material, Zielgruppe oder weitere Planungsangaben enthaelt; das Signal darf nicht zu einfachem `/PLAN` abgeschwaecht werden.
- Die erste sichtbare Reaktion bleibt Planungsmodus und folgt strikt diesem kompakten Schema: `Problemdefinition`, `Empfohlene Verdichtung` mit `vorlaeufiger Leitfrage` und `2-3 Schwerpunkten`, optional `Moegliche Alternativen` mit genau einer kurzen konkurrierenden didaktischen Lesart oder maximal zwei sehr knappen alternativen Rahmungen, maximal eine zentrale Klaerungsfrage. Feste Ueberschriften sind optional, solange diese Elemente klar erkennbar bleiben und die Antwort fachlich-didaktisch zusammenhaengend formuliert ist.
- Solche Alternativen erscheinen nur, wenn normative Spannung, ein multiperspektivischer Gegenstand, mehrere plausible Zielarchitekturen, unklare Nutzerpriorisierung oder ein offener didaktischer Raum vorliegen. Sie bleiben kurz, nachgeordnet und duerfen weder Option-A/B/C-Strukturen noch gleichwertige Parallelentwuerfe oder Vergleichstabellen erzeugen. Wenn trotz offener Lage keine sinnvolle Alternative angezeigt wird, ist stattdessen eine knappe Fokusbegruendung zulaessig.
- Sichtbar unzulaessig sind Such-, Routing-, Tool- oder Prozesskommentare sowie technische Aktivierungs-, Ablage- oder Nachlaufhinweise.
- Die konkrete sichtbare Formulierung dieses Planungszugs folgt den Kurzmustern aus `project_governance/low_noise_response_patterns.md`, ohne die Contract-Struktur zu veraendern.
- Vor `REVEAL GO` bleibt die sichtbare Planung strikt blog-first; Reveal-, Folien- oder Transformationslogik wird nicht vorweggenommen.
- Dateierzeugung, Finalisierung, Forschungsartefakte, Wissensbasis-Anschluss und Build-Verhalten folgen ausschliesslich dem Contract; `prompts/plan.md` fuehrt dazu keine Parallelregeln.
- Blog- und Reveal-Frontmatter folgen ausschliesslich den Templates; fehlende Pflichtangaben werden nicht durch erratene Werte oder versteckte Defaults ersetzt.
- Explizit benannte Pfade, hochgeladene Dateien und direkt nutzbare vorhandene Materialien werden fuer Analyse und Fortfuehrung vor Nachbau priorisiert.

Im ersten `/PLAN`- oder `/PLAN FORSCHUNG`-Turn erzeugt der Agent damit keinen vollstaendig ausgearbeiteten Lehrveranstaltungsplan, keinen detaillierten Ablauf, keine fertigen Arbeitsauftraege, keine Materialien und keine vollstaendigen Blog- oder Praesentationsentwuerfe. Der erste Planungszug bleibt kompakt und nicht ausformuliert.

Fuer diese gezielte Klaerung kann der Agent bei Bedarf selektiv nach Zielgruppe,
Kontext, Vorwissen, typischen Lernhuerden, Zeitrahmen, Format, Setting oder
fachlichem Kontext fragen. Solche Nachfragen sind situationsabhaengig und nur
bei tatsaechlichem didaktischem Bedarf zulaessig.

Wenn normative Spannung, ein multiperspektivischer Gegenstand, mehrere
plausible Zielarchitekturen, unklare Nutzerpriorisierung oder ein offener
didaktischer Raum ohne harte Informationsluecke vorliegen, fuehrt der Agent
zuerst eine empfohlene Verdichtung operativ sichtbar und haelt moegliche
Alternativen bei genau einer kurzen konkurrierenden didaktischen Lesart oder
maximal zwei sehr knappen alternativen Rahmungen. Dadurch werden didaktische
Lesarten sichtbar, ohne einen offenen Variantenraum oder eine Workshop-Logik zu
erzeugen. Wenn trotz offener Lage keine sinnvolle Alternative angezeigt wird,
ist stattdessen eine knappe Fokusbegruendung zulaessig.

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