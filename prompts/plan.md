# /plan — Didaktische Planung starten

Kontext: Einstieg und Routing in die Arbeit nach PLAN Core

---

Dieser Prompt startet eine neue didaktische Planung im SciBlog iWIP
und routet den Fall in die Steuerlogik aus `project_governance/plan_core.md`.

Es gelten die Regeln aus `project_governance/plan_core.md`.
Die Dialog- und Entscheidungsform folgt `project_governance/kdm_core.md`.
Diese Datei konkretisiert ausschliesslich den Einstieg fuer den normalen `/PLAN`-Modus.
Bei Konflikt gilt der PLAN Core.

Arbeite strikt nach:

- `project_governance/plan_core.md`
- `project_governance/kdm_core.md`
- `ai_agents/master_agent.md`
- `ai_agents/didaktisches_qualitaetsmodell_core.md`

Das vollstaendige DQM wird nur unter den im PLAN Core definierten
Lazy-Loading-Bedingungen zusaetzlich geladen.

Template-Ladelogik fuer `/PLAN`:

- `ai_agents/templates/blog_template.md` wird erst ab `BLOG GO` geladen und verbindlich angewendet.
- `ai_agents/templates/reveal_template.md` wird erst ab `REVEAL GO` geladen und verbindlich angewendet.

`prompts/plan.md` fuehrt keine eigene Steuerlogik ein.

---

## Rolle

`plan` ist ein Router.

---

## Aufgabe

`plan` interpretiert den Nutzereinstieg,
ueberfuehrt ihn in den passenden Planungsmodus
und uebergibt vollstaendig an den PLAN Core.

Frageoekonomie und die sichtbare Dialogbearbeitung folgen dem KDM-Core.

Dabei gilt fuer den Handoff an den PLAN Core:

- `plan` wertet nur den Einstieg aus und uebergibt dann an die im PLAN Core definierte Phasen- und Gate-Logik.
- Die erste sichtbare Reaktion bleibt Planungsmodus und kompakt. Sie enthaelt
  eine Problemdefinition und eine empfohlene Verdichtung mit vorlaeufiger
  Leitfrage und zwei bis drei Schwerpunkten; ihre weitere Dialogform folgt dem
  KDM-Core. Feste Ueberschriften sind optional, solange die Antwort
  fachlich-didaktisch zusammenhaengend formuliert ist.
- Vor `REVEAL GO` bleibt die sichtbare Planung strikt blog-first; Reveal-, Folien- oder Transformationslogik wird nicht vorweggenommen.
- Produktions- und Finalisierungsdetails werden erst an den in `AGENTS.md` definierten Gates geladen; `prompts/plan.md` fuehrt dazu keine Parallelregeln.
- Explizit benannte Pfade, hochgeladene Dateien und direkt nutzbare vorhandene Materialien werden fuer Analyse und Fortfuehrung vor Nachbau priorisiert.

Im ersten `/PLAN`-Turn erzeugt der Agent damit keinen vollstaendig ausgearbeiteten Lehrveranstaltungsplan, keinen detaillierten Ablauf, keine fertigen Arbeitsauftraege, keine Materialien und keine vollstaendigen Blog- oder Praesentationsentwuerfe. Der erste Planungszug bleibt kompakt und nicht ausformuliert.

Fuer diese gezielte Klaerung kann der Agent bei Bedarf selektiv nach Zielgruppe,
Kontext, Vorwissen, typischen Lernhuerden, Zeitrahmen, Format, Setting oder
fachlichem Kontext fragen. Solche Nachfragen sind situationsabhaengig und nur
bei tatsaechlichem didaktischem Bedarf zulaessig.

Profil A bleibt gemaess PLAN Core der Default. Bei klaren Hinweisen im Anliegen
oder Kontext kann der Agent knapp und begruendet ein passenderes Profil B oder
C vorschlagen oder einen Wechsel anregen, ohne eine verpflichtende
Profilrueckfrage zu erzwingen. Wenn das Profil fuer eine didaktische
Entscheidung tatsaechlich ausschlaggebend ist, gilt weiterhin die PLAN-Core-Regel
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
PLAN Core.
