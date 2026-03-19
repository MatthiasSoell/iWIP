# Blog Template — SciBlog iWIP

Dieses Template definiert die Standardstruktur für Blogartikel im SciBlog iWIP.

Der Blogartikel ist das **Primärartefakt**.
Die Reveal-Präsentation wird anschließend daraus abgeleitet.

Emojis werden gemäß **content_emoji_policy.md** verwendet.

Design und Darstellung orientieren sich an:

- 00_design_tokens.css
- 10_custom.css
- 20_custom_callouts.css

Referenzstil (qualitatives Zielbild):

- `content/blog/oer/uplan_ki_oer/index.md`
- `content/blog/widi/hosp_feed_refl/index.md`

---

## Frontmatter (Pflichtstruktur)

```yaml
title: ""
# optional: nur setzen, wenn eine feste URL gewuenscht ist
# Format wenn gesetzt: nur lowercase + unterstriche (z. B. did_allg_fach)
slug: ""
authors:
  - ""
date: YYYY-MM-DD
lastmod: YYYY-MM-DD
draft: true

description: ""
summary: ""

tags: []
categories: []

oer:
  is_oer: true
  kind: ""

  # TULLU-Pflichtdaten (Frontend) + Basis für JSON-LD
  creators:
    - name: ""
      given_name: ""
      family_name: ""
      affiliation: ""
      url: ""
      orcid: ""

  publisher:
    name: ""
    url: ""

  license:
    label: ""
    url: ""

  source:
    label: ""
    url: ""

  # Version / Reifegrad (kein Qualitätsurteil)
  version: "1.0"
  status: "pilot"   # draft | pilot | stable | aligned

  # OERSI / schema.org-nahe Felder
  in_language: "de"
  learning_resource_type: ""
  educational_level: []
  audience: []
  time_required: ""

  about:
    - term: ""

  # Optional
  todos: []
```

Alle Felder sind verpflichtend, außer `slug` und `oer.todos`.
Wenn `slug` gesetzt wird, muss er `snake_case` mit Unterstrichen nutzen.

Tags und Kategorien sind wichtig für Auffindbarkeit
und OERSI-Metadaten.

Zusatzregel zur Vollständigkeit:

- Der Agent darf keinen Blogartikel als final ausgeben,
  wenn eines der oben genannten Pflichtfelder fehlt oder leer geblieben ist.
- Falls `slug` gesetzt ist und nicht `snake_case` mit Unterstrichen folgt,
  ist dies ebenfalls ein formaler Blocker.

---

## Verbindlicher Einstiegsblock im Blog-Body (Pflicht)

Direkt nach dem Frontmatter muss immer folgender Block stehen:

```html
<div class="top-toggle">
  <button id="md-copy-btn" title="Markdown kopieren (ohne Bilder)">📑</button>
  <button onclick="triggerPrint()" title="Blog speichern">📥</button>
  <button onclick="location.href='/iWIP/praesentation/<bereich>/<ordner>/'" title="Zur Präsentationsansicht">🖥️</button>
  <button class="iwip_help_btn"
        type="button"
        aria-haspopup="dialog"
        aria-controls="iwip_help_overlay"
        aria-expanded="false"
        title="Hinweise zur Nutzung">
  ⓘ
  </button>
</div>

{{< oer-meta >}}
```

Pfadregel für den Präsentationsbutton (verbindlich):

- Der Pfad wird immer aus dem Blogpfad abgeleitet.
- Muster: `content/blog/<bereich>/<ordner>/index.md` -> `/iWIP/praesentation/<bereich>/<ordner>/`.
- `<ordner>` ist immer genau der Ordnername des Blogbeitrags.

---

## Standardstruktur des Artikels

## Stilprofil (verbindlich)

Der Blogtext soll nicht nur korrekt, sondern auch publikationsreif wirken.

Nutze dafür:

- klaren Spannungsbogen (Problem -> Einordnung -> Bearbeitung -> Transfer),
- didaktisch-essayistischen Fließtext statt neutraler KI-Standardprosa,
- funktionale Callouts (`TIPP`, `IMPORTANT`, `QUOTE`) an Scharnierstellen,
- prägnante Überschriften mit semantischem Emoji-Anker.

Vermeide:

- monotone Abschnittsblöcke mit immer gleicher Satzstruktur,
- reine Aufzählungslogik ohne erklärende Einordnung,
- stilistisch flache Formulierungen ohne Übergänge.

## Schreibperspektive

Der Blogartikel richtet sich an **Leser:innen des SciBlog iWIP**,
nicht an die planende Lehrperson.

Deshalb gilt:

- schreibe erklärend und einordnend,
- formuliere Inhalte für externe Leser:innen nachvollziehbar aus,
- verwandle Planungsstichpunkte in lesbare Abschnitte,
- nutze Ablauf, Methoden und Medien nur als Unterstützung der inhaltlichen Darstellung.

Wenn der Beitrag auf einer Lehrveranstaltung oder Fortbildung basiert,
soll diese als **Anwendungsbeispiel** erscheinen,
nicht als alleinige Struktur des Textes.

### Verbindliche Qualitätsregel

Der Blogtext muss so geschrieben sein,
dass externe Leser:innen ihn ohne Kenntnis der internen Planung verstehen.

Wenn der Text wie ein Planungsdokument klingt,
muss er in eine leser:innenorientierte Darstellung transformiert werden,
bevor der Beitrag als final gilt.

### Sprachqualität

Der Text soll sich lesen wie ein guter SciBlog-Beitrag:

- adressiert Leser:innen klar und direkt,
- verbindet Theorie, Praxis und Begründung sichtbar,
- variiert Satzlängen und Übergänge,
- markiert zentrale Aussagen gezielt (nicht inflationär).

### Zielstruktur (Standard)

Die Standardreihenfolge des Artikels ist:

1. Hintergrund
2. Ausgangsfrage
3. Lernziele
4. Aufbau & Ablauf
5. fachliche Hauptkapitel als H2/H3 (z. B. Lerntypen, Lernformen, Prüfungsformen)
6. Nachhaltige Unterrichts- und Schulentwicklung (optional, falls inhaltlich sinnvoll)
7. Literatur

Sammelüberschriften wie `Kernpunkte` oder `Kernpunkte mit Evidenz` werden im Artikelkörper nicht verwendet.

## 🧭 Hintergrund

Kurze Einführung in Thema, Kontext und Relevanz der Veranstaltung.

Beantworte kurz:

- Worum geht es?
- In welchem Kontext wird die Veranstaltung eingesetzt?
- Warum ist das Thema relevant?

Integriere hier außerdem eine knappe Meta-Reflexion zu Methoden- und Medienlogik
(z. B. warum wenige klare Formate gewählt wurden und wie Medien die Diskussion stützen).

Formhinweis:

- Ein kurzer Lead-Absatz (2-4 Sätze) ist verpflichtend.

---

## 💭 Ausgangsfrage

Formuliere die zentrale Leitfrage der Veranstaltung.

Die Leitfrage soll:

- Interesse wecken
- das Problem sichtbar machen
- in die Lernziele überleiten.

---

## 🎯 Lernziele

Formuliere klare Lernziele.

Die Lernziele sollen:

- verständnisorientiert sein
- möglichst handlungsbezogen formuliert sein
- zu den geplanten Lernaktivitäten passen.

---

## Einordnung (optional)

Eine eigene Einordnungssektion ist optional.
Wenn der Hintergrund bereits Theorie-, Forschungs- und Praxisbezug klar enthält,
kann auf eine separate Sektion verzichtet werden.

---

## Ablauf

Beschreibe den Ablauf nur so weit,
wie er für Leser:innen zum Verständnis des didaktischen Konzepts hilfreich ist.

Der Ablauf soll **nicht die inhaltliche Argumentation ersetzen**.
Zentrale fachliche oder didaktische Punkte müssen im Fließtext erklärt und eingeordnet werden.

Typischer Ablauf:

1 Einstieg
2 Aktivierung
3 Arbeitsphase
4 Diskussion
5 Reflexion
6 Transfer

Der Ablauf sollte realistisch zum Zeitrahmen passen.

Formhinweis:

- Verwende bei sitzungs- oder fortbildungsbezogenen Beiträgen verpflichtend
  eine Ablauf-Tabelle im folgenden Muster:

```markdown
<div class="agenda">

| Phase | Inhalt | Ziel | Zeit |
|:------|:--------|:------|:------:|
| **1️⃣ ...** | ... | ... | ⏱️ ...<br>Min |
| **2️⃣ ...** | ... | ... | ⏱️ ...<br>Min |
| **3️⃣ ...** | ... | ... | ⏱️ ...<br>Min |
| **4️⃣ ...** | ... | ... | ⏱️ ...<br>Min |
| **5️⃣ ...** | ... | ... | ⏱️ ...<br>Min |

</div>
```

---

## 🧠 Fachliche Hauptkapitel mit Evidenz (Pflicht)

Die Anzahl der fachlichen Hauptkapitel wird je Beitrag dynamisch bestimmt.

Der Agent prüft zuerst,
wie viele inhaltliche Gliederungspunkte für das Thema sinnvoll sind,
und arbeitet anschließend genau diese Anzahl als eigene inhaltliche Abschnitte aus.

Pflicht je Kernpunkt:

- klare Kernaussage,
- kurze Einordnung,
- mindestens ein Quellenbezug im Fließtext.

Wichtig:

- Die Kernpunkte dürfen nicht nur in der Ablaufsektion auftauchen.
- Die fachliche Argumentation steht im Vordergrund,
  der Ablauf bleibt unterstützend.
  - Abschnittsüberschriften müssen als fachlich benannte H2/H3 erscheinen
    (z. B. `## Lerntypen`, `## Lernformen`, `## Prüfungsformen`).
  - Keine Sammelüberschrift wie `Kernpunkte`, `Kernpunkte mit Evidenz` oder `Kernthemen` im Artikelkörper.
  - Die fachlichen Hauptkapitel folgen direkt nach dem Ablauf.

  Ko-kreativer Schreibprozess (verbindlich):

  - Nutzer liefert Inhalte pro Hauptkapitel in Stichpunkten und kurzen Sätzen.
  - Agent übernimmt diese Inhalte kapitelweise in den Blogtext.
  - Agent formuliert publizistisch und leser:innenfreundlich aus (Fließtext, Übergänge, Einordnung), ohne die inhaltliche Aussage zu verfälschen.
  - Agent ergänzt bei Bedarf passende Grafiken, Tabellen und Quellenzeilen im bestehenden Stil.

Stilhinweis je Kernpunkt:

- beginne mit einer klaren Leitthese,
- ordne sie in 2-4 Sätzen didaktisch ein,
- schließe mit einer kurzen Praxisimplikation ab.

---

## 📚 Literatur und Quellen (Pflichtformat)

Verwende am Ende des Blogartikels verpflichtend einen stabilen Anker fuer Literaturverweise im Fliesstext:

```markdown
<span id="literatur"></span>

## Literatur und Quellen
```

Regeln fuer Verweise im Fliesstext:

- Wenn eine Quelle im Fliesstext genannt wird, setze einen Link auf `#literatur`.
- Beispiel: `[Euler & Hahn (2014)](#literatur)`.
- Nutze diese Verweise konsistent in allen Kernabschnitten.
- Bei mehreren Quellen setze getrennte Links pro Quelle; das Trennzeichen bleibt ausserhalb der Links.
- Beispiel: `[Nickolaus, 2018](#literatur); [Seifried & Sembill, 2010](#literatur)`.

Regeln fuer Quellenzeilen unter Tabellen/Grafiken (`bildquelle`):

- Wenn dort Literatur genannt wird (z. B. "in Anlehnung an ..."), verlinke diese Angabe ebenfalls auf `#literatur`.
- Das gilt systematisch fuer Tabellen- und Grafikquellen.

Regeln fuer den Literaturabschnitt:

- Formatiere Eintraege APA-7-nah und konsistent.
- Fuehre pro Quelle genau einen bibliografischen Haupteintrag.
- Hinterlege zusaetzliche Zugriffe als Badges (`lit-ub`, `lit-doi`, `lit-worldcat`) oder als normalen Weblink, wenn kein Badge-Typ passt.
- Erhalte den inhaltlichen Quellenbestand unveraendert (keine inhaltlichen Aenderungen an Autor:innen, Jahr, Titel, Publikation).
- Korrigiere nur Form, Konsistenz und Linkdarstellung.

---

## 🧩 Methoden / 💻 Medien / 🪞 Reflexion (Standard: integriert)

Standardfall:

- Methoden-, Medien- und Reflexionsaspekte werden im Abschnitt **Hintergrund**
  und in den jeweiligen Kernabschnitten integriert statt als eigene Kapitel.

Nur wenn fachlich notwendig oder explizit gewünscht:

- eigene Unterabschnitte für Methoden, Medien, Reflexion oder Erweiterung ergänzen.

---

## Visualisierung

Der Agent prüft,
an welchen Stellen Visualisierungen sinnvoll sind.

Mögliche Formen:

- Diagramm
- Ablaufgrafik
- Schema
- Vergleichstabelle
- Concept Map

Wenn sinnvoll, ergänze explizite Medienblöcke:

- `<figure class="figure-frame">...</figure>` für eigene Visualisierungen,
- kurze Bildquellenzeile unterhalb der Visualisierung.

## Emoji-Einsatz (verbindlich, funktional)

Emojis sind semantische Strukturmarker, keine Dekoration.

Regeln:

- nutze in Hauptüberschriften und zentralen Listenpunkten passende Emojis,
- halte die Dichte moderat bis hoch, aber funktional konsistent,
- setze keine zufälligen oder themenfremden Emojis.

Zielbild: visuelle Orientierung wie in den Referenzblogs,
ohne den Lesefluss zu überladen.

---

## OER-Hinweis

Alle Materialien sollen,
wenn möglich, OER-kompatibel sein.

---

## Definition of Done (Blogartikel)

Vor finaler Ausgabe prüfen:

1. Frontmatter vollständig,
2. Leser:innenperspektive erkennbar,
3. Ablauf nicht dominierend,
4. Kernpunkte inhaltlich ausformuliert,
5. Quellen im Text und Literaturteil konsistent,
6. Stil wirkt blog- und leser:innennah (nicht generisch),
7. Emoji-Einsatz ist funktional konsistent.
