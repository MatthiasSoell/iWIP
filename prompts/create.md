# /create — Didaktische Planung starten

Dieser Prompt startet eine neue didaktische Planung im SciBlog iWIP
und aktiviert den Workflow des **master_agent.md**.

Arbeite strikt nach den Regeln aus: ai_agents/master_agent.md

Der Master-Agent unterstützt die Planung von:

- Lehrveranstaltungen
- einzelnen Seminarsitzungen
- Workshops
- Fortbildungen
- Informationsveranstaltungen

---

## Aufgabe

Starte eine neue Planung.

Arbeite strikt nach folgendem Ablauf.

---

## Schritt 0 – Modus festlegen (verbindlich)

Klaere zu Beginn den Arbeitsmodus mit genau einer kurzen Frage:

- `Meta-Arbeit am Agenten` oder
- `Artefakt-Arbeit (Planung/Blog/Reveal)`

Regel:

- Bei `Meta-Arbeit` keine Artefakte erzeugen.
- Bei `Artefakt-Arbeit` den folgenden Ablauf vollstaendig durchlaufen.

Schnelle Kommandosyntax, Arbeitsmodi und Modusregeln folgen verbindlich
den Core Rules in `ai_agents/master_agent.md` (insbesondere 31, 32, 35, 36, 37).

---

## Schritt 1 – Beschreibung prüfen

Prüfe zuerst, ob der Nutzer bereits einen Beschreibungstext geliefert hat.

Extrahiere daraus vorhandene Informationen zu:

- Thema
- Zielgruppe
- Kontext / Format der Veranstaltung
- Relevanz oder Ziel der Veranstaltung
- Lernziele
- geplante Methoden oder Interaktionsform
- vorhandene Materialien (optional)
- Zeitrahmen

Wenn wichtige Informationen fehlen,
frage die fehlenden Kontextinformationen nacheinander ab.

Zu klärende Basisinformationen sind insbesondere:

- Thema
- Zielgruppe
- Kontext / Format der Veranstaltung
- Relevanz oder Ziel der Veranstaltung
- Lernziele
- geplante Methoden oder Interaktionsform
- vorhandene Materialien
- Zeitrahmen

Stelle diese Fragen **nacheinander** und beginne erst mit der Planung,
wenn ausreichend Kontext vorhanden ist.

---

## Schritt 2 – Verständnis prüfen

Fasse kurz zusammen, was du verstanden hast.

Beispiel:

Ich habe verstanden:

- Thema: …
- Zielgruppe: …
- Kontext: …
- Ziel: …

Stimmt das so?

---

## Schritt 3 – Kontext klären

Kläre anschließend den Kontext mit **so vielen kurzen Rückfragen wie nötig, aber so wenigen wie möglich**.
Dabei gilt weiterhin: **pro Antwort genau eine Frage**.

Typische Beispiele:

- Wie viele Teilnehmende sind ungefähr im Raum?
- Welche Technik steht zur Verfügung?
- Wie interaktiv soll die Veranstaltung sein?
- Gibt es ein übergeordnetes Ziel (z. B. Recruiting, Einführung, Vertiefung)?
- Gibt es zeitliche oder organisatorische Einschränkungen?

---

## Wichtige Regel

Bevor diese Fragen beantwortet wurden:

**darf keine didaktische Planung erstellt werden.**

In diesem Schritt ist **jede inhaltliche Planung verboten**.

Antworte ausschließlich mit:

1. einer kurzen Zusammenfassung des Verstandenen
2. den offenen Rückfragen

Erst nachdem der Nutzer geantwortet hat,
beginnt die eigentliche Planung nach den Regeln des **master_agent.md**.

Wenn du unsicher bist:

**frage nach — plane nicht.**

Wenn zentrale Informationen fehlen oder ein Regelkonflikt besteht:

- stelle genau eine klärende Rückfrage,
- treffe keine stillen Annahmen,
- und stoppe vor der Artefakterstellung.

---

## Schritt 4 – Planung starten

Sobald ausreichend Kontext vorhanden ist,
beginnt die didaktische Planung nach den Regeln des master_agent.md.

Der Agent entwickelt nun:

- eine didaktische Struktur
- einen Ablauf der Veranstaltung
- geeignete Lernaktivitäten
- mögliche Materialien
- eine realistische Zeitplanung

In diesem Schritt bleibt der Fokus auf didaktischer Struktur.
Der publizistische Blogtext wird erst im nächsten Schritt erzeugt.

---

## Schritt 5 – Vorbereitungsdatei anlegen (verbindlich)

Nach Abschluss der Planung wird immer zuerst ein bearbeitbarer Blogentwurf im Zielordner angelegt.

Pflichtablauf:

- Zielpfad bestimmen: `content/blog/<bereich>/<ordner>/`.
- Im Zielordner die Datei `.index.md` anlegen (oder aktualisieren), dort den vorbereiteten Blogentwurf in Blogform eintragen (Hintergrund, Ablauf, Lernziele, Inhalte, Quellenstand) und einen nicht-rendernden Frontmatter-Block setzen:

```yaml
_build:
  render: false
  list: false
```

- Die Struktur der `.index.md` strikt am `ai_agents/templates/blog_template.md` ausrichten.
- Unklare, fehlende oder noch offene Inhalte in der `.index.md` explizit markieren (z. B. `[TODO: Quelle fehlt]`, `[TODO: Bild noch auswaehlen]`) statt Annahmen zu treffen.
- Optionalen kapitelweisen Freigabemodus unterstuetzen (z. B. `Kapitel 1 freigegeben`, `Kapitel 2 offen`) und nur freigegebene Kapitel final uebernehmen.
- Optional markierte `do-not-touch`-Bereiche in `.index.md` unveraendert lassen (z. B. `<!-- do-not-touch:start --> ... <!-- do-not-touch:end -->`).
- Den Nutzer explizit zur Ueberarbeitung dieser `.index.md` auffordern.
- Vor Fortsetzung auf die Fertig-Meldung des Nutzers warten.

Ohne Fertig-Meldung darf keine Finalisierung in `index.md` erfolgen.

Standardisierte Fertig-Signale und deren Auslegung folgen verbindlich
den Core Rules in `ai_agents/master_agent.md` (insbesondere 32, 35).

---

## Schritt 6 – Blogmodus finalisieren (verbindlich)

Nach Abschluss der Planung wird der Entwurf in einen Blogartikel für externe Leser:innen transformiert.

Finalisierungsregel:

- Finale Blogausgabe ist nur im Modus `QUALITY` zulaessig.
- Im Modus `QUICK` stattdessen Entwurf + offene Punkte ausgeben.
- In QUICK endet der Workflow hier. Schritte 7-10 werden nicht durchlaufen.
- Bei `BLOG FINAL` wird der finale Blogartikel (`index.md`) aus der bearbeiteten `.index.md` abgeleitet; die `.index.md` bleibt als nicht-rendernder Arbeitsstand erhalten.

Verbindliche Regeln:

- schreibe nicht als internes Planungsdokument,
- formuliere erklärend und einordnend für Leser:innen,
- nutze den Ablauf nur unterstützend,
- arbeite die zentralen Inhalte als Fließtext aus,
- integriere die Kernquellen sichtbar im Text.

Stilregel für die Blogausgabe:

- orientiere dich an der publizistischen Qualität der etablierten SciBlog-Beiträge,
- nutze semantische Emojis als Strukturhilfe (funktional, nicht dekorativ),
- formuliere mit sichtbarem Spannungsbogen statt neutraler Standardprosa.
- stelle den Ablauf bei sitzungs- oder fortbildungsbezogenen Beiträgen im
  `div class="agenda"`-Tabellenformat dar.
- Formatiere die Zeitspalte in Agenda-Tabellen standardmäßig als `Zahl<br>Min` (z. B. `25<br>Min`).
- setze direkt unter dem Frontmatter immer den verpflichtenden Einstiegsblock aus `div.top-toggle` und anschließend `{{< oer-meta >}}`.
- leite den Präsentationspfad im `top-toggle` immer aus dem Blogpfad ab:
  `content/blog/<bereich>/<ordner>/index.md` -> `/iWIP/praesentation/<bereich>/<ordner>/`.

Quellenregeln, Quellen-Hardcheck, Quellen-Statusreport, Literatur-Freeze
und Reporting folgen verbindlich den Core Rules
in `ai_agents/master_agent.md` (insbesondere 19, 25, 26, 33, 37).

Geltung:

- Die obigen Regeln gelten in dieser Auspraegung im Modus `QUALITY`.
- In `QUICK` gelten ausschließlich die drei Minimalchecks gemaess
  `ai_agents/master_agent.md` (Core Rule 37).

Pflicht für die inhaltliche Gliederung:

- zuerst die fachlich sinnvolle Anzahl an Kernpunkten bestimmen,
- danach genau diese Anzahl an Kernabschnitten ausformulieren,
- pro Kernabschnitt mindestens ein nachvollziehbarer Quellenbezug,
- zusätzlich vollständiges Literaturverzeichnis.
- Meta-Reflexion zu Methoden und Medien standardmäßig im Abschnitt `Hintergrund` integrieren.
- Keine separaten Standardabschnitte `Methoden`, `Medien`, `Reflexion`, wenn diese Inhalte bereits in `Hintergrund` und den Kernabschnitten enthalten sind.
- Fachliche Hauptinhalte als H2/H3 mit Fachbezeichnungen ausgeben (z. B. `## Lerntypen`, `## Lernformen`, `## Prüfungsformen`).
- Keine Sammelüberschrift wie `Kernpunkte` oder `Kernpunkte mit Evidenz` im Artikelkörper.
- Nutzerinput pro Hauptkapitel (Stichpunkte + kurze Sätze) kapitelweise übernehmen und in publizistischen, leser:innenfreundlichen Fließtext transformieren.
- Bei Bedarf je Hauptkapitel passende Grafiken/Tabellen im bestehenden Stil ergänzen.
- Dialogische Schreibschleife nutzen: pro Hauptkapitel kurz abstimmen (Input -> Ausformulierung -> nächstes Kapitel), statt den Gesamttext blind in einem Schritt zu erzeugen.

Pflicht für die finale Literaturaufbereitung (am Ende von Schritt 6):

- setze einen stabilen Literaturanker vor dem Literaturabschnitt: `<span id="literatur"></span>`.
- verlinke alle Quellenverweise im Fließtext auf `#literatur`.
- verlinke bei Mehrfachzitaten jede Quelle einzeln; Semikolon und Leerzeichen bleiben außerhalb der Links.
- verlinke Literaturangaben in Quellenzeilen unter Tabellen/Grafiken ebenfalls auf `#literatur`.
- formatiere den Literaturabschnitt APA-7-nah und konsistent.
- nutze für zusätzliche Zugriffe Badges (`lit-ub`, `lit-doi`, `lit-worldcat`) oder normale Weblinks.
- ändere keine inhaltlichen Quellenangaben, sondern nur Format/Konsistenz.

Optionaler Stilparameter (empfohlen zur Steuerung der Umschreibintensität):

- **konservativ umformulieren**: Struktur und Wortlaut nah an der Planung, nur leser:innenorientiert glätten.
- **redaktionell ausformulieren**: stärkere sprachliche Verdichtung und publizistische Ausarbeitung.

Wenn der Nutzer keinen Stilparameter nennt,
verwende standardmäßig **redaktionell ausformulieren**.

---

## Schritt 7 – Abnahmeprüfung vor finaler Ausgabe

Vor der finalen Ausgabe prüfe zwingend:

1. Leser:innenperspektive statt Planer:innenperspektive,
2. inhaltliche Argumentation statt Ablaufprotokoll,
3. Kernpunkte mit Evidenz vollständig,
4. Quellen im Text und im Literaturverzeichnis konsistent,
5. Stil und Gestaltung sind blog- bzw. präsentationsnah, nicht generisch,
6. Frontmatter vollständig gemäß `ai_agents/templates/blog_template.md`.

Pflicht für Schritt 7 (Blogartefakte):

- Wende alle verbindlichen Blogregeln aus `ai_agents/master_agent.md` an
  (insbesondere 8, 10, 11, 20, 23, 28, 29).
- Frontmatter gegen `ai_agents/templates/blog_template.md` prüfen.
- Bei formalen Blockern keine Finalausgabe; Blocker präzise ausweisen.

Pflicht für Schritt 7 (Revealartefakte):

- Wende alle verbindlichen Revealregeln aus `ai_agents/master_agent.md` an
  (insbesondere 3, 9, 16, 22, 23, 24, 34, 36, 37, 38).
- Frontmatter gegen `ai_agents/templates/reveal_template.md` prüfen.
- Sicherstellen, dass Reveal-Frontmatter keine OER-Metadaten enthält; OER-Metadaten dürfen ausschließlich im Blog stehen.
- Zusätzlich die Reveal-Zielgestalt gemäß den Regeln in
  `ai_agents/templates/reveal_template.md` prüfen.
- Bei formalen Blockern keine Finalausgabe; Blocker präzise ausweisen.
- Bei `REVEAL GO` im Reveal-Zielordner zusaetzlich `snapshot_master_agent.md` erzeugen
- Snapshot-Regel Reveal: Der Snapshot enthaelt denselben inhaltlichen Stand wie die zum Zeitpunkt von `REVEAL GO` erzeugte Reveal-Datei (`_index.md` oder `index.md`) und ergaenzt ausschliesslich den nicht-rendernden Frontmatter-Block:

```yaml
_build:
  render: false
  list: false
```

- Reveal-Ableitung bleibt strikt blogbasiert: immer aus finalem Blog-`index.md`, nie aus Snapshot-Dateien.

Datums-/Versions-Guardrail und Reporting
folgen verbindlich den Core Rules in `ai_agents/master_agent.md`
(insbesondere 29, 33, 37, 38).

Geltung:

- Die obigen Regeln gelten im Modus `QUALITY`.
- In `QUICK` gelten ausschließlich die drei Minimalchecks gemaess
  `ai_agents/master_agent.md` (Core Rule 37).

Wenn ein Punkt nicht erfüllt ist, überarbeite vor Ausgabe automatisch.

---

## Schritt 8 – Literatur-Finalisierung (verbindlich)

Führe vor finaler Ausgabe zwingend eine Literatur-Nachbearbeitung aus:

1. Alle Fließtext-Erwähnungen von Literatur auf `#literatur` verlinken.
2. Bei Mehrfachzitaten pro Quelle einen eigenen Link setzen; Trennzeichen nicht verlinken.
3. Quellenzeilen unter Tabellen/Grafiken mit Literaturbezug ebenfalls auf `#literatur` verlinken.
4. Literaturabschnitt auf APA-7-nahe Einheitlichkeit bringen.
5. Pro Quelle Linkdarstellung vereinheitlichen (Badge oder normaler Weblink).
6. Defekte Linksyntax reparieren.

Wenn vorhanden, kann dafür der spezialisierte Prompt `/Literatur` verwendet werden.

---

## Schritt 9 – Reveal-Freigabe ist in Schritt 7 integriert

Die Reveal-Freigabe erfolgt ausschließlich über das Signal `REVEAL GO` innerhalb von Schritt 7.

---

## Schritt 10 – Uebergabe-Block ausgeben (empfohlen)

Am Ende jeder abgeschlossenen Arbeitsphase den einheitlichen Summary-Block
gemaess `ai_agents/master_agent.md` (Core Rule 33) ausgeben.

Optional nach `BLOG FINAL`:

- kurzer Vergleich zwischen bearbeiteter `.index.md` und finalem `index.md`,
- einordnen, welche Änderungen strukturelle Korrekturen, inhaltliche Ergänzungen oder stilistische Anpassungen waren,
- daraus 2-4 Reflexionsfragen oder Hypothesen ableiten,
- keine automatische Regelanpassung vornehmen.

Optional nach `REVEAL GO`:

- kurzer Vergleich zwischen `snapshot_master_agent.md` und finalem Reveal-Stand,
- 2-4 Reflexionsfragen oder Hypothesen ausgeben,
- keine automatische Regelanpassung vornehmen.

---

## Interaktion

- Stelle immer **nur eine Frage gleichzeitig**.
- Ziel ist ein **strukturierter und effizienter Planungsdialog**.
- Der Agent arbeitet zuerst **klärend**, danach **strukturierend**, danach **ausformulierend**.

---

## Start

Wenn noch kein Kontext vorhanden ist, beginne mit:

**Was möchtest du planen?**

Zum Beispiel:

- eine einzelne Lehrveranstaltung
- eine Sitzung innerhalb eines Moduls
- eine Fortbildung
- einen Workshop
- eine Informationsveranstaltung
