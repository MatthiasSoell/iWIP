# Reveal Template — SciBlog iWIP

Version: 1.0.0
Status: Template-Spezifikation
Kontext: Frontmatter und Zielstruktur für Reveal-Artefakte

Dieses Template definiert die Standardstruktur
für Reveal-Präsentationen im SciBlog iWIP.

Die Präsentation wird aus dem Blogartikel abgeleitet.

Emojis werden gemäß **content_emoji_policy.md** verwendet.
Begriffe wie `veroeffentlichter Pfad` und `Finalisierung` folgen dem Glossar in `project_governance/agent_contract.md`.

---

## Frontmatter (Pflichtstruktur Reveal)

```yaml
---
title: ""
date: YYYY-MM-DD

title_reveal: ""
emojis: ""
veranstaltungstyp: ""
veranstaltung: ""
author: ""
blog: ""
aliases:
  - "/praesentation/<bereich>/<ordner>/"

lastmod: YYYY-MM-DD
draft: true

outputs:
  - Reveal

reveal_hugo:
  theme: "simple"
  slideNumber: true
  hash: true

description: >
  

summary: >
  

tags:
  - ...

categories:
  - ...

todos: []
---
```

Regeln:

- Reveal-Frontmatter enthält ausschließlich präsentationsbezogene Metadaten.
- In Reveal-Dateien sind OER-Metadaten strikt verboten.
- Verboten sind insbesondere: `oer`, `is_oer`, `kind`, `creators`, `publisher`, `license`, `source`, `in_language`, `learning_resource_type`, `educational_level`, `audience`, `time_required`, `about`, `rights_exceptions`.
- `blog` soll auf die veroeffentlichte Blogansicht mit Site-Base zeigen, nicht auf einen technischen Content-Pfad.
- Der sichtbare veroeffentlichte Praesentationspfad lautet `/iWIP/praesentation/<bereich>/<ordner>/`; fuer `widi` ist dies `/iWIP/praesentation/widi/<ordner>/`.
- `aliases` fuehrt den Hugo-Alias relativ zur Site-Base; im Frontmatter steht daher `/praesentation/<bereich>/<ordner>/`, fuer `widi` `/praesentation/widi/<ordner>/`.
- Sichtbare Links, Buttons und Hinweise verwenden nur den veroeffentlichten Pfad; technische Bundle-Orte und Alias-Semantik bleiben intern.
- Metadaten müssen kontextspezifisch zur jeweiligen Präsentation ausgefüllt sein (keine Copy-Paste-Werte).
- Pflichtfelder muessen semantisch gefuellt sein (keine Platzhalterwerte wie `TODO`, `tbd`, `-`, `...`).

## Hinweis zur Steuerung

Die Ableitung, Pruefung und Finalisierung der Praesentation
erfolgt ausschliesslich gemaess:

-> `project_governance/agent_contract.md`

Dieses Template definiert nur die Struktur der Praesentation.

## Folienstruktur

Dieses Template definiert nur Frontmatter und Zielstruktur des Reveal-Artefakts.

### Mindestreihenfolge

1. Titel
2. Leitfrage oder Problem
3. Ablauf
4. Lernziele
5. optionale Einordnung
6. ein oder mehrere inhaltliche Themenfolien
7. optionale Arbeits-, Diskussions- oder Transferfolien
8. Literatur
9. Abschluss

---

## Folie 1 — Titel

```markdown
{{< titleSlide >}}
```

Nutze nach Möglichkeit `title_reveal` und `emojis` im Frontmatter.

---

## Folie 2 — Leitfrage / Problem

- zentrale Leitfrage oder Problemstellung knapp zuspitzen
- visuell und sprachlich als Einstieg markieren

---

## Folie 3 — Ablauf

- Sitzungs- oder Präsentationslogik knapp sichtbar machen
- bei Bedarf nummerierte Schrittfolge oder kurze Agenda nutzen

---

## Folie 4 — Lernziele

- wichtigste Lernziele oder Zielperspektiven knapp darstellen
- Emojis im Folieninhalt folgen `project_governance/content_emoji_policy.md`

Beispiel:

```markdown
## 🎯 Lernziele

- 🎯 zwei Kriterien fuer lernfoerderliches Feedback benennen
- 🧠 ein Fallbeispiel didaktisch einordnen
- 🪞 einen Transfer in die eigene Praxis formulieren
```

---

## Folie 5 — Einordnung (optional)

- nur ergänzen, wenn eine eigene Einordnungsfolie wirklich Mehrwert bringt

---

## Themenfolien (wiederholbar)

- ein oder mehrere fachlich benannte Inhaltsfolien anlegen
- pro Folie eine klare Kernbotschaft fokussieren
- Arbeitsauftrag, Diskussion oder Transfer nur ergänzen, wenn es zur Dramaturgie passt
- Ziel: visuelle Strukturierung, schnelle kognitive Orientierung und Hervorhebung zentraler Aussagen.

Robustes Fragmentmuster fuer Listen:

```html
<ul>
  <li>🧭 erster Punkt</li>
  <li class="fragment">🧠 zweiter Punkt</li>
  <li class="fragment">🪞 dritter Punkt</li>
</ul>
```

Hinweis:
Emojis werden über mehrere Fragmente hinweg konsistent fortgeführt und nicht nur im ersten Punkt verwendet.

## Arbeits-, Diskussions- und Transferfolien (optional)

- Arbeits-, Diskussions- und Transferfolien setzen Emojis im sichtbaren Folieninhalt gemaess `project_governance/content_emoji_policy.md` ein.

Beispiel Arbeitsauftrag:

```markdown
## 💬 Arbeitsauftrag

💬 Vergleicht zu zweit ein Beispiel aus eurer Praxis und haltet fest:

- 🧩 Welche Methode wird sichtbar?
- 🪞 Wo braucht es eine Anpassung?
```

Beispiel Transfer / Reflexion:

```markdown
## 🪞 Transfer

🪞 Welche Veraenderung uebernimmst du in deine naechste Sitzung?
```

Optionales Muster fuer Bild- oder Medienfolien:

```html
<figure class="figure-frame figure-frame-sm">
  <img src="..." alt="...">
</figure>
<p class="zitat-quelle">Bildquelle: ... · Lizenz: CC BY-SA 4.0</p>
```

- In Reveal steht die Bildquelle schlank unter der Visualisierung; ein eigener Bildtitel ist meist entbehrlich, wenn der Folientitel die Funktion bereits uebernimmt.
- Unter Bildern, Grafiken, Diagrammen, Screenshots und Fotos immer `zitat-quelle` mit dem Praefix `Bildquelle:` verwenden.
- Die Quellenzeile enthaelt immer Herkunft und Lizenzstatus; `Illustration:` ist optional. Lizenzlinks sind in Reveal nicht erforderlich.

---

## Vorletzte Folie — Literatur

```markdown
{{< literatureSlide >}}
```

---

## Letzte Folie — Abschluss

```markdown
{{< endSlide >}}
```
