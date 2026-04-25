# Blog Template — SciBlog iWIP

Kontext: Frontmatter, Einstiegsblock und Zielstruktur für Blogartefakte

Dieses Template definiert die Standardstruktur für Blogartikel im SciBlog iWIP.

Der Blogartikel ist das **Primärartefakt**.
Die Reveal-Präsentation wird anschließend daraus abgeleitet.

Emojis werden gemäß **content_emoji_policy.md** verwendet.
Begriffe wie `veroeffentlichter Pfad` und `Finalisierung` folgen dem Glossar in `project_governance/agent_contract.md`.

Die folgenden mediendidaktischen Gestaltungsregeln gelten in diesem Template
als weiche Heuristiken fuer die Darstellung. Sie geben Orientierung fuer die
Ausarbeitung, erzeugen aber weder Hard-Fails noch Zwangsverhalten.

---

## Frontmatter (Pflichtstruktur)

```yaml
title: ""
# optional: nur setzen, wenn eine feste URL gewuenscht ist
# Format wenn gesetzt: nur lowercase + unterstriche (z. B. did_allg_fach)
slug: ""
author: ""
# mehrere Autor:innen als String mit Semikolon, z. B. "Matthias Söll; Max Mustermann"
date: YYYY-MM-DD
lastmod: YYYY-MM-DD
draft: true

description: ""
summary: ""

tags: []
categories: []

oer:
  is_oer: true
  kind: "lesson"

  # TULLU-Pflichtdaten (Frontend) + Basis für JSON-LD
  creators:
    - type: "Person"
      name: "Prof. Dr. Matthias Söll"
      given_name: "Matthias"
      family_name: "Söll"
      affiliation:
        name: "Universität Rostock"
        id: "https://ror.org/03zdwsf69"
        url: "https://www.uni-rostock.de/"
        type: "Organization"
      url: "https://www.iwip.uni-rostock.de/institut/iwip/team/prof-dr-matthias-soell/"
      orcid: "https://orcid.org/0000-0002-9717-3017"

  publisher:
    name: "SciBlog iWIP"
    url: "https://matthiassoell.github.io/iWIP/"

  license:
    label: "CC BY-SA 4.0"
    url: "https://creativecommons.org/licenses/by-sa/4.0/"

  image: "https://matthiassoell.github.io/iWIP/images/og/og_sciblog_default.jpg"

  version: "1.0"
  status: "pilot"

  # OERSI / schema.org-nahe Felder
  in_language:
    - "de"
  learning_resource_type:
    - id: "https://w3id.org/kim/hcrt/text"
      name: "Text"
  educational_level:
    - id: "https://w3id.org/kim/educationalLevel/level_6"
      name: "Bachelor oder aequivalent"
  audience:
    - "Studierende der Wirtschaftspaedagogik"
  keywords:
    - "<inhaltliches Schlagwort 1>"
    - "<inhaltliches Schlagwort 2>"
    - "<inhaltliches Schlagwort 3>"
    - "<inhaltliches Schlagwort 4>"
  time_required: "PT90M"

  about:
    - id: "https://w3id.org/kim/hochschulfaechersystematik/n270"
      name: "Berufs- und Wirtschaftspaedagogik"
    - id: "https://w3id.org/kim/hochschulfaechersystematik/n181"
      name: "Wirtschaftspaedagogik"
    - id: "https://w3id.org/kim/hochschulfaechersystematik/n33"
      name: "Erziehungswissenschaften"

  # Optional
  todos: []
```

Alle Felder sind verpflichtend, außer `slug` und `oer.todos`.
Wenn `slug` gesetzt wird, muss er `snake_case` mit Unterstrichen nutzen.
Fuer Autor:innen ist ausschliesslich `author` zulaessig; `authors` ist nicht erlaubt.

Fuer Blogbeitraege mit `draft: false` und `oer.is_oer: true` ist der `oer`-Block
immer vollstaendig und explizit auszufuellen; der Workflow ergaenzt oder errät
keine Fach- oder OERSI-Metadaten mehr.

Dabei gilt verbindlich:

- `oer.about` enthaelt immer exakt die drei Standard-Fachgebiete aus diesem Template; keine Ableitung aus Tags und keine zusaetzlichen Fachgebiete ohne ausdruecklichen Auftrag.
- `description` umfasst 2 bis 3 Saetze, beginnt nicht mit `Dieses Material`, benennt Zielgruppe, Thema und Nutzen bzw. Transfer, vermeidet Methodenaufzaehlungen wie `Input, Diskussion ...` und bleibt fachlich praezise, aber gut lesbar.
- `summary` ist genau 1 Satz lang, beschreibt den Inhalt praegnant, wiederholt die `description` nicht und bleibt im Zielkorridor von 140 bis 160 Zeichen, spaetestens jedoch 160 Zeichen.
- `oer.keywords` wird beitragsspezifisch aus dem Inhalt abgeleitet, umfasst 5 bis 8 praezise Schlagwoerter, mischt Themenbegriffe und didaktische Begriffe und vermeidet Fuellwoerter, blinde Duplikate sowie generische Begriffe wie `Unterricht` oder `Lernen` ohne Kontext; `tags` koennen Ausgangspunkt sein, ersetzen die Keywords aber nicht.
- `oer.learning_resource_type` und `oer.educational_level` sind Arrays aus Objekten mit `id` und `name`; freie String-Werte sind unzulaessig.
- `oer.image` ist immer absolut auf das Standard-OG-Bild gesetzt.
- `oer.creators[].affiliation.name` lautet immer `Universität Rostock`; Institutszusaetze sind dort unzulaessig.
- `description` formuliert den Gegenstand adressatenorientiert und konkret; typische Einstiege sind z. B. "In dieser Veranstaltung...", "Der Beitrag zeigt...", "Lehrkräfte arbeiten hier an..."

## Hinweis zur Steuerung

Alle Uebergaenge, Pruefungen und Finalisierungen erfolgen
ausschliesslich gemaess:

-> `project_governance/agent_contract.md`

Dieses Template definiert nur die Struktur des Blog-Artikels.

---

## Verbindlicher Einstiegsblock im Blog-Body (Pflicht)

Direkt nach dem Frontmatter muss immer folgender Block stehen:

```html
<div class="top-toggle">
  <button id="md-copy-btn" title="Markdown kopieren (ohne Bilder)">📑</button>
  <button onclick="triggerPrint()" title="Blog speichern">📥</button>
  <button onclick="location.href='<veroeffentlichter-praesentationspfad>'" title="Zur Präsentationsansicht">🖥️</button>
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

- Im Button steht immer der veroeffentlichte Praesentationspfad.
- Standard: `content/blog/<bereich>/<ordner>/index.md` -> `/iWIP/praesentation/<bereich>/<ordner>/`.
- Sonderfall `content/blog/lehre/widi/<ordner>/index.md`: Ziel ist `/iWIP/praesentation/widi/<ordner>/`.
- Technische Bundle-Orte gehoeren weder in den Button noch in sichtbare Hinweise oder Links.
- `<ordner>` ist immer genau der Ordnername des Blogbeitrags.

---

## Standardstruktur des Artikels

Dieses Template definiert nur Frontmatter, Einstiegsblock und Zielstruktur des Blogartefakts.

## Mediendidaktische Soft-Heuristiken fuer Blogabschnitte

- Laengere Textpassagen werden nach Moeglichkeit sichtbar segmentiert, z. B. durch Zwischenueberschriften, Bilder, Tabellen, Callouts oder andere klare Strukturmarker.
- Visuelle oder strukturelle Marker werden funktional eingesetzt; sie dienen der Darstellung, nicht als zusaetzliche Inhaltsebene.
- Emojis werden konsistent als Funktionsmarker genutzt, z. B. fuer Struktur, Frage, Ziel oder Reflexion, ohne Haeufung ohne erkennbaren Zweck.

### Zielgliederung (Standard)

1. `## 🧭 Hintergrund`
2. `## 💭 Ausgangsfrage`
3. `## 🎯 Lernziele`
4. `## Ablauf`
5. ein oder mehrere fachliche H2/H3-Hauptkapitel
6. optionale Ergänzungsabschnitte bei Bedarf
7. `## Literatur und Quellen`

Sammelüberschriften wie `Kernpunkte`, `Kernpunkte mit Evidenz` oder `Kernthemen`
werden im Artikelkörper nicht verwendet.

## 🧭 Hintergrund

- kurzer Lead-Absatz (2-4 Sätze)
- Thema, Kontext und Relevanz knapp einführen
- bei Bedarf eine kurze Einordnung zu Methoden oder Medien integrieren

---

## 💭 Ausgangsfrage

- zentrale Leitfrage oder Problemstellung knapp formulieren
- Übergang zu den Lernzielen vorbereiten

---

## 🎯 Lernziele

- Lernziele klar und knapp aufführen
- Formulierungen möglichst handlungs- oder verständnisorientiert halten

---

## Einordnung (optional)

- nur ergänzen, wenn eine eigene Einordnungssektion für Theorie-, Forschungs-
  oder Praxisbezug wirklich zusätzlichen Mehrwert bringt

---

## Ablauf

Für sitzungs- oder fortbildungsbezogene Beiträge den Ablauf als kompakte
Agenda-Tabelle anlegen.

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

## 🧠 Fachliche Hauptkapitel (Pflicht)

- nach dem Ablauf ein oder mehrere fachlich benannte H2/H3-Hauptkapitel anlegen
- keine Sammelüberschrift fuer alle Kernpunkte verwenden
- zentrale Aussagen im Fließtext ausführen und Quellen im Text sichtbar integrieren

Strukturmuster fuer Visualisierungen:

```html
<p>Einleitender Satz (optional)</p>
<p class="grafic-title">Kurztitel der Grafik</p>
<figure class="figure-frame">
  <img src="..." alt="...">
</figure>
<p class="bildquelle">Bildquelle: ... · Lizenz: <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener noreferrer">CC BY-SA 4.0</a></p>
```

- Jede visuelle Darstellung erhaelt direkt darueber genau einen kurzen Titel als `p class="grafic-title"`.
- Ein kurzer einleitender Kontextsatz vor Titel und Visualisierung ist optional und wird nur verwendet, wenn die Darstellung erklaerungsbeduerftig ist, z. B. bei komplexen Tabellen, Modellen, Matrizen oder Schaubildern.
- Nach jedem Bild, jeder Grafik, jedem Diagramm, jeder Tabelle, jedem Screenshot und jedem Foto steht direkt darunter genau eine Quellenzeile als `p class="bildquelle"`.
- Einzige Ausnahme: eindeutig als Ablaufplan erkennbare Tabellen innerhalb eines Abschnitts, also direkt unter einer Abschnittsueberschrift eingebettete Tabellen zur zeitlichen oder didaktischen Phasenstruktur mit organisatorischem Zweck. Nur in diesem Fall entfallen `grafic-title` und `bildquelle`; stattdessen steht direkt ueber der Tabelle genau die knappe Zeile `**Gesamtdauer:** ca. XX Minuten ⏱️`, wobei die Minuten aus den Phasen summiert oder konsistent geschaetzt werden.
- Die Quellenzeile folgt immer dem Muster `Bildquelle: [Herkunft] · Lizenz: [Lizenzangabe]`.
- Der Begriff bleibt auch bei Tabellen und vergleichbaren Visualisierungen immer `Bildquelle`.
- Im Blog werden freie Lizenzen immer als HTML-Link ausgegeben, z. B. `Lizenz: <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener noreferrer">CC BY-SA 4.0</a>`.
- Wenn KI beteiligt war, wird dies nur als Zusatz in der Herkunft genannt, z. B. `Eigene Darstellung (erstellt mit ChatGPT)`.
- Fuer nicht frei verwendbare Inhalte bleibt die Formulierung `Lizenz: nicht frei verwendbar` verbindlich.

---

## 📚 Literatur und Quellen (Pflichtformat)

Der Literaturteil beginnt mit einem stabilen Anker:

```markdown
<span id="literatur"></span>

## Literatur und Quellen
```

- bibliografische Haupteinträge gesammelt und konsistent ausgeben
- zusätzliche Zugriffe bei Bedarf als Badge oder Weblink ergänzen
