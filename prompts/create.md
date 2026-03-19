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

Kläre anschließend den Kontext mit **mindestens zwei kurzen Rückfragen über mehrere Turns**.
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

## Schritt 5 – Blogmodus aktivieren (verbindlich)

Nach Abschluss der Planung wird der Entwurf in einen Blogartikel für externe Leser:innen transformiert.

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

Quellenregel im Blogmodus:

- nutze spezifische Quellen nur, wenn sie vom Nutzer genannt oder im Projektkontext belastbar vorhanden sind,
- erfinde keine konkreten Studien, DOI-Angaben oder Publikationsdetails,
- wenn eine zusätzliche spezifische Quelle nötig wäre: stelle vorab eine klärende Rückfrage,
- wenn keine belastbare spezifische Quelle vorliegt: argumentiere ohne erfundene Literaturangabe.

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

Pflicht für die finale Literaturaufbereitung (am Ende von Schritt 5):

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

## Schritt 6 – Abnahmeprüfung vor finaler Ausgabe

Vor der finalen Ausgabe prüfe zwingend:

1. Leser:innenperspektive statt Planer:innenperspektive,
2. inhaltliche Argumentation statt Ablaufprotokoll,
3. Kernpunkte mit Evidenz vollständig,
4. Quellen im Text und im Literaturverzeichnis konsistent,
5. Stil und Gestaltung sind blog- bzw. präsentationsnah, nicht generisch,
6. Frontmatter vollständig gemäß `ai_agents/templates/blog_template.md`.

Pflicht für Schritt 6 (Blogartefakte):

- Prüfe alle Frontmatter-Pflichtfelder inklusive vollständigem OER-/TULLU-/OERSI-Block.
- `slug` ist optional; falls gesetzt, nur `snake_case` mit Unterstrichen.
- Prüfe, dass direkt nach dem Frontmatter der Pflichtblock `div.top-toggle` plus `{{< oer-meta >}}` enthalten ist.
- Prüfe, dass der Präsentationsbutton im `top-toggle` den Pfad `/iWIP/praesentation/<bereich>/<ordner>/` nutzt, wobei `<bereich>/<ordner>` exakt dem Blogpfad entsprechen.
- Fehlende, leere oder falsch strukturierte Pflichtfelder sind **formale Blocker**.
- Bei formalen Blockern darf der Agent den Blog nicht als final ausgeben.
- Stattdessen listet der Agent die Blocker präzise auf und fordert gezielt die fehlenden Angaben nach.

Pflicht für Schritt 6 (Revealartefakte):

- Prüfe alle Frontmatter-Pflichtfelder gemäß `ai_agents/templates/reveal_template.md` inklusive vollständigem OER-Metadatenblock.
- `blog` muss auf den zugehörigen Blogbeitrag verweisen.
- Fehlende, leere oder falsch strukturierte Pflichtfelder sind **formale Blocker**.
- Bei formalen Blockern darf der Agent die Präsentation nicht als final ausgeben.
- Stattdessen listet der Agent die Blocker präzise auf und fordert gezielt die fehlenden Angaben nach.
- Prüfe zusätzlich die Reveal-Zielgestalt:
  - pro Inhaltsfolie eine klare Kernbotschaft,
  - foliengerechte Textdichte (Richtwert 35-45 Wörter je Inhaltsfolie),
  - pro fachlichem Hauptkapitel mindestens eine visuelle Stützfolie mit kurzer Quellenzeile,
  - fragmentierter Argumentationsaufbau statt Textwand,
  - semantisch konsistenter Emoji-Einsatz gemäß Emoji-Policy.
- Prüfe Sprachnormalisierung in sichtbaren deutschen Folientexten:
  - `ae/oe/ue` zu `ä/ö/ü` normalisieren,
  - ausnehmen: URLs, Pfade, Dateinamen, Slugs, Alias-Pfade, `src`-Attribute,
    maschinenlesbare Keys und bewusst zitierte Originalschreibweisen.
- Wenn diese Stil-/Sprachkriterien verletzt sind, gilt die Reveal-Ausgabe
  als **nicht final** und muss vor Ausgabe überarbeitet werden.

Wenn ein Punkt nicht erfüllt ist, überarbeite vor Ausgabe automatisch.

---

## Schritt 7 – Literatur-Finalisierung (verbindlich)

Führe vor finaler Ausgabe zwingend eine Literatur-Nachbearbeitung aus:

1. Alle Fließtext-Erwähnungen von Literatur auf `#literatur` verlinken.
2. Bei Mehrfachzitaten pro Quelle einen eigenen Link setzen; Trennzeichen nicht verlinken.
3. Quellenzeilen unter Tabellen/Grafiken mit Literaturbezug ebenfalls auf `#literatur` verlinken.
4. Literaturabschnitt auf APA-7-nahe Einheitlichkeit bringen.
5. Pro Quelle Linkdarstellung vereinheitlichen (Badge oder normaler Weblink).
6. Defekte Linksyntax reparieren.

Wenn vorhanden, kann dafür der spezialisierte Prompt `/Literatur` verwendet werden.

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
