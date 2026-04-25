# /create — Didaktische Planung starten

Kontext: Einstieg und Routing in die Arbeit nach Contract

---

Dieser Prompt startet eine neue didaktische Planung im SciBlog iWIP
und routet den Fall in die Steuerlogik aus `project_governance/agent_contract.md`.

Arbeite strikt nach:

- `project_governance/agent_contract.md`
- `ai_agents/master_agent.md`
- `ai_agents/didaktisches_qualitaetsmodell.md`
- `ai_agents/templates/blog_template.md`
- `ai_agents/templates/reveal_template.md`

`prompts/create.md` fuehrt keine eigene Steuerlogik ein.

---

## Rolle

`create` ist ein Router.

---

## Aufgabe

`create` interpretiert den Nutzereinstieg,
ueberfuehrt ihn in den passenden Arbeitsmodus
und uebergibt vollstaendig an den Contract.

Der Agent nutzt vorhandene Informationen aus Initialprompt, Folgeprompts und
Kontext vorrangig. Er fragt nur dann gezielt nach, wenn fuer didaktisch
relevante Entscheidungen wesentliche Informationen fehlen, Angaben
widerspruechlich sind oder sich nicht tragfaehig ableiten lassen. Es gibt
keine Standardabfrage und keine routinemaessige Vollabfrage aller Parameter.

Dabei gilt fuer den Handoff an den Contract:

- In `P1` und `P2` bleibt `create` strikt im Planungsmodus; es werden keine publizierbaren Blog- oder Reveal-Passagen vorweggenommen.
- Der Uebergang in `P3` erzeugt erst dann `blog_snapshot.txt` in `exports/snapshots/` und `index.md`, wenn Planungslogik in Artefaktsprache ueberfuehrt werden kann.
- Der Uebergang in die Reveal-Arbeit nutzt ausschliesslich das finale Blog-`index.md`; Planungsnotizen, Fruehfassungen und Snapshots werden nicht direkt transformiert.
- Wenn fuer einen Blogbeitrag `draft: false` und `oer.is_oer: true` gesetzt werden, wird der OER-Block bereits in `index.md` vollstaendig gemaess `ai_agents/templates/blog_template.md` ausgearbeitet; fehlende OERSI-Pflichtfelder werden nicht spaeter durch Workflow-Defaults, Fachableitungen oder erratene Werte ersetzt.
- Nach erfolgreichem `BLOG FINAL` wird standardmaessig ein kuratierter Wissensbasis-Entwurf als Review-Anschluss vorgeschlagen; erst nach einer kurzen Bestaetigung oder gezielten Korrektur wird `blog_wissensbasis.md` aktualisiert. Bei ausdruecklicher sofortiger Uebernahmeanweisung kann die Rueckfrage entfallen. `REVEAL GO` allein ist dafuer kein Trigger.

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

Keine eigene Steuerlogik.

Aktiver Editorpfad, geoeffnete oder markierte Prompt- oder Regeldateien, aktive Textauswahlen oder sonstiger Editor-Kontext steuern den Arbeitsmodus nicht.