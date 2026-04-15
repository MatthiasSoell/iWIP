# Gate 1 – Vorbereitung nächster Trockentest

Datum: 2026-04-13
Status: vorbereitet, noch nicht durchgefuehrt
Ziel: den nachgeschaerften Agenten vor dem naechsten Live-Fall auf Low-noise-Dialog, Body-Emoji-Pflicht, `FORSCHUNG START`, sauberes Sichttranskript, schlanke Protokollierung und sauberes `lehre/widi`-Routing pruefen

## Empfehlung vor dem Start

### Alte Faelle in `content/`

- Alte Testfaelle vor diesem Trockentest nicht pauschal loeschen.
- Sie stoeren den naechsten Lauf technisch nicht, solange in den betroffenen Bundles keine zusaetzlichen rendernden Markdown-Dateien liegen.
- Kritisch waeren nur Alt- oder Ursprungsfassungen als `.md` innerhalb eines Blog- oder Reveal-Bundles. Solche Dateien muessen ausserhalb von `content/` liegen oder als `.txt` archiviert sein.

### Alte Dateien in `exports/`

- Fuer den naechsten Trockentest ist Aufraeumen in `exports/` sinnvoll, aber nicht zwingend.
- Organisatorisch stoeren vor allem alte Chat-Dumps und Hilfsexporte im Wurzelverzeichnis, weil der neue Lauf dann schlechter lesbar ist.
- Dafuer ist bereits ein Archivpfad vorbereitet: `exports/archive/2026-04_gate1/`.

### Empfohlene Minimal-Hygiene vor dem Start

1. Keine bestehenden Blog- oder Reveal-Bundles loeschen.
2. Nur pruefen, dass in relevanten Bundles keine zusaetzlichen `.md`-Archivdateien liegen.
3. Optional alte reine Chat- oder Hilfsexporte aus `exports/` in `exports/archive/2026-04_gate1/` verschieben.
4. Fuer den neuen Lauf einen frischen Dialog verwenden.

## Testaufbau

Der Trockentest soll in zwei getrennten Dialogen plus Nachlauf stattfinden.

1. Kurztest `Meta-Arbeit am Agenten`
2. Artefaktlauf mit `FORSCHUNG START`
3. Auswertung mit vorbereitetem Bogen

## Station 1 – Meta-Arbeit am Agenten

### Ziel

- pruefen, dass Meta-Arbeit artefaktfrei bleibt
- pruefen, dass der Dialog im Meta-Modus reviewgerecht und nicht artefaktorientiert reagiert

### Prompt

```text
Meta-Arbeit am Agenten: Pruefe nur, ob die neuen Regeln fuer Low-noise-Dialog, Body-Emoji-Pflicht und `FORSCHUNG START` in Contract, Master-Agent und Prompts konsistent beschrieben sind. Keine Artefakte anlegen, keine Bundles anfassen, nur kurz einschaetzen, ob der Regelstand fuer einen Trockentest konsistent wirkt.
```

### Soll

- keine Artefakterstellung
- keine Aenderung an `index.md`, `_index.md` oder Bundles
- Sprache bleibt meta- und reviewgerecht

## Station 2 – Artefaktlauf mit `FORSCHUNG START`

### Falltyp

Kompakte didaktische Sitzung mit frischem `lehre/widi`-Slug, ohne Uploads, mit klarer Leitfrage, Mini-Fall, Transfer und natuerlichem Anlass fuer semantische Emojis im sichtbaren Hauptkoerper.

### Thema

Lernziele formulieren in der Unterrichtsplanung fuer Bachelorstudierende im Lehramt

### Warum genau dieser Fall

- frischer Zielpfad ohne Kollision mit bereits angelegten `lehre/widi`-Testfaellen
- natuerlicher Anlass fuer `Hintergrund`, `Lernziele`, erklaerendes Hauptkapitel, Listen, Merksatz und Transfer
- gut geeignet fuer Blog- und Reveal-Ableitung
- Routing-Sonderfall `lehre/widi` wird automatisch mitgeprueft

### Erwartete Zielpfade

- `content/blog/lehre/widi/lernziele_formulieren_einstieg/`
- `content/praesentation/lehre/widi/lernziele_formulieren_einstieg/`
- sichtbares Forschungs-Transkript: `exports/forschung_chat_lernziele_formulieren_einstieg_2026-04-13.md`

### Startprompt

```text
FORSCHUNG START: Ich plane eine 45-minuetige Sitzung fuer Bachelorstudierende im Lehramt zum Thema Lernziele formulieren in der Unterrichtsplanung. Die Sitzung ist Teil eines didaktischen Einfuehrungsseminars. Ziel ist, dass die Studierenden zwischen vagen und beobachtbaren Lernzielen unterscheiden, ein Lernziel an einem kleinen Unterrichtsbeispiel ueberarbeiten und eine kurze Transferidee fuer die eigene Planung festhalten koennen. Geplant sind ein kurzer Einstieg mit Gegenbeispiel, eine begriffliche Klaerung, eine kleine Ueberarbeitungsaufgabe an einem Mini-Fall und ein Abschluss mit 1-Minuten-Commitment. Es gibt keine Uploads und kein umfangreiches Begleitmaterial.
```

### Vorbereitete Folgeantworten

#### Antwort 1

Falls der Agent nach Profil oder Rahmendaten fragt:

```text
Profil A passt. Es sind etwa 18 Teilnehmende in einem Seminarraum mit Beamer. Die Sitzung soll kompakt, klar und aktivierend sein.
```

#### Antwort 2

Falls der Agent nach fachlichem Anschluss oder Umgang mit bestehenden Beitraegen fragt:

```text
Wenn es thematisch passende Beitraege gibt, bitte nur punktuell verweisen. Der neue Beitrag soll fuer sich allein verstaendlich bleiben.
```

#### Antwort 3

Falls der Agent in die Blog-Ausarbeitung uebergeht und die Arbeitsdatei erstellt hat:

```text
Bitte knapp, leser:innenorientiert und im SciBlog-Stil ausformulieren.
```

#### Antwort 4

Nach kurzer Sichtpruefung der `index.md`:

```text
Der Blog ist jetzt fertig. Bitte final pruefen und abschliessen.
```

#### Antwort 5

Nach Blog-Finalisierung:

```text
Bitte uebernimm den Wissensbasis-Eintrag und leite jetzt die Praesentation daraus ab.
```

#### Antwort 6

Nach kurzer Sichtpruefung der `_index.md`:

```text
Die Praesentation ist jetzt fertig. Bitte finalisieren.
```

### Sollbeobachtungen im Artefaktlauf

- keine unnoetige Modusfrage am Start
- genau eine Rueckfrage gleichzeitig
- keine seriellen sichtbaren Prozesssaetze waehrend Recherche, Dateioperationen oder Routinechecks
- `blog_snapshot.txt` entsteht vor `index.md`
- `_index.md` und `reveal_snapshot.txt` entstehen erst nach dem Reveal-Uebergang
- `FORSCHUNG START` fuehrt parallel ein sauberes sichtbares Transkript in `exports/`
- im Blog tragen `Hintergrund`, `Lernziele` und das erste erklaerende Hauptkapitel mindestens je eine semantische Emoji-Markierung im sichtbaren Body
- das `top-toggle` im Blog zeigt fuer `lehre/widi` auf `/iWIP/praesentation/widi/lernziele_formulieren_einstieg/`
- im Forschungsprotokoll erscheinen nur schlanke, verifizierbare Metadaten; unsichere Zaehldaten werden nicht geschaetzt
- das sichtbare Forschungs-Transkript enthaelt keine Toollogs, keine Meta-Arbeit, keine Debugtexte, keine Streaming-Fragmente und keine leeren Codebloecke

## Station 3 – Nachlauf und Auswertung

### Direkt nach `REVEAL FINAL`

- kein zusaetzlicher Exportprompt noetig, wenn das Forschungs-Transkript sauber parallel geschrieben wurde
- nur kurz pruefen, ob das sichtbare Transkript unter `exports/forschung_chat_lernziele_formulieren_einstieg_2026-04-13.md` vorliegt

### Auswertungsbogen

- vorbereitete Datei: `exports/realfall_gate1_trockentest_auswertung_2026-04-13.md`

### Optionaler spaeterer Meta-Prompt fuer die Analyse

```text
Meta-Arbeit: Analysiere den Trockentest auf Basis von `exports/forschung_chat_lernziele_formulieren_einstieg_2026-04-13.md` sowie der zugehoerigen Artefakte unter `content/blog/lehre/widi/lernziele_formulieren_einstieg/` und `content/praesentation/lehre/widi/lernziele_formulieren_einstieg/`. Arbeite im Review-Modus: zuerst Befunde nach Schweregrad mit Datei- und Zeilenverweisen, danach offene Fragen oder Annahmen, danach ein kurzes Gesamturteil. Pruefe insbesondere Low-noise-Dialog, Body-Emoji-Abdeckung, Routing `lehre/widi`, sauberes Forschungs-Transkript, schlankes Forschungsprotokoll und Reveal-Finalausgaben.
```

## Empfehlung fuer die Durchfuehrung

- Station 1 und Station 2 in getrennten neuen Dialogen fahren
- keine Uploads verwenden
- waehrend des Artefaktlaufs keine Zusatzwuensche einstreuen
- alte Vergleichsfaelle nicht loeschen, sondern hoechstens `exports/` organisatorisch entlasten
- den Trockentest erst nach kurzer Bundle-Hygiene und mit frischem Dialog starten