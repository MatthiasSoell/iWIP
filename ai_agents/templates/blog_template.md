# Blog Template — SciBlog iWIP

Version: 1.0.0
Status: Template-Spezifikation
Kontext: Frontmatter, Einstiegsblock und Zielstruktur für Blogartefakte

Dieses Template definiert die Standardstruktur für Blogartikel im SciBlog iWIP.

Der Blogartikel ist das **Primärartefakt**.
Die Reveal-Präsentation wird anschließend daraus abgeleitet.

Emojis werden gemäß **content_emoji_policy.md** verwendet.
Begriffe wie `veroeffentlichter Pfad` und `Finalisierung` folgen dem Glossar in `project_governance/agent_contract.md`.

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

Optionales Strukturmuster für Visualisierungen oder Abbildungen:

```html
<p class="grafic-title">Kurztitel der Grafik</p>
<figure class="figure-frame">
  <img src="..." alt="...">
</figure>
<p class="bildquelle">Bildquelle: ...</p>
```

- `grafic-title` nur verwenden, wenn die Visualisierung eine eigene sichtbare Ueberschrift braucht.
- Unter Bildern, Grafiken, Diagrammen, Screenshots und Fotos immer den Praefix `Bildquelle:` verwenden; Hinweise wie `Illustration:` oder `Fotograf:` folgen danach in derselben Zeile.
- Die Quellenzeile enthaelt immer auch den Lizenzstatus, z. B. `Lizenz: <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener noreferrer">CC BY-SA 4.0</a>` oder `Keine freie Lizenz (Rechte bei den dargestellten Personen)`.

---

## 📚 Literatur und Quellen (Pflichtformat)

Der Literaturteil beginnt mit einem stabilen Anker:

```markdown
<span id="literatur"></span>

## Literatur und Quellen
```

- bibliografische Haupteinträge gesammelt und konsistent ausgeben
- zusätzliche Zugriffe bei Bedarf als Badge oder Weblink ergänzen
