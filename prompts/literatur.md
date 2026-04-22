# /Literatur — Literatur-Finalisierung fuer Blogbeiträge

Scope: formale Literatur-Nachbearbeitung bestehender Blogbeitraege ohne Quellenneuerfindung

Du arbeitest strikt nach den Regeln aus:

project_governance/agent_contract.md

Der Contract ist die einzige Steuerlogik.

## Status

Dieses Werkzeug ist optional.
Es erzeugt keine eigene Steuerlogik und veraendert den Hauptablauf nicht.

---

Dieser Prompt fuehrt eine standardisierte Literatur-Nachbearbeitung
fuer einen bestehenden Blogbeitrag im SciBlog iWIP aus.

---

## Aufgabe

Bereite den Literaturteil eines vorhandenen Blogbeitrags formal auf,
ohne inhaltliche Quellenangaben zu veraendern.

Der Prompt darf nur folgende Aspekte veraendern:

- Linksetzung im Fliesstext,
- Formatkonsistenz im Literaturabschnitt,
- Linkdarstellung (Badge vs. normaler Link),
- Reparatur fehlerhafter Linksyntax.

Formale Literatur-Normalisierung bestehender Quellen ist ausdruecklich erlaubt.
Inhaltliche Quellenaussagen bleiben unveraendert.

---

## Orientierungspunkte

Zur Orientierung koennen folgende Aspekte beruecksichtigt werden:

- Arbeite auf dem aktuell aktiven Blogbeitrag oder auf dem vom Nutzer genannten Beitragspfad.
- Wenn nicht eindeutig, stelle genau eine kurze Rueckfrage.

- Falls nicht vorhanden, setze direkt vor dem Literaturabschnitt:

```markdown
<span id="literatur"></span>
```

- Verwende als Abschnittstitel bevorzugt:

```markdown
## Literatur und Quellen
```

- Wenn eine Quelle im Fliesstext genannt wird, verlinke auf `#literatur`.
- Beispiel:

```markdown
[vgl. Euler & Hahn (2014)](#literatur)
```

- Verlinke konsistent in allen relevanten Abschnitten.
- Bei mehreren Quellen setze pro Quelle einen eigenen Link; Semikolon und Leerzeichen bleiben ausserhalb der Links.
- Beispiel: `[Nickolaus, 2018](#literatur); [Seifried & Sembill, 2010](#literatur)`.
- Verlinke Literaturangaben in Quellenzeilen unter Tabellen/Grafiken (z. B. `bildquelle`, "in Anlehnung an ...") ebenfalls auf `#literatur`.

- Formatiere Eintraege APA-7-nah und einheitlich.
- Pro Quelle genau ein bibliografischer Haupteintrag.
- Setze Zusatzlinks direkt beim Eintrag:
  - bevorzugt als Badges mit vorhandenen Klassen `lit-ub`, `lit-doi`, `lit-worldcat`,
  - sonst als normaler Weblink.
- Korrigiere defekte Klammern, doppelte URL-Syntax und zerbrochene Markdown-Links.

- Aendere keine inhaltlichen Quellenbestandteile:
  - Autor:innen
  - Jahr
  - Titel
  - Publikationsangaben
  - Seiten-/Bandangaben
- Erlaubt sind nur formale Korrekturen, APA-7-nahe Normalisierung und Linkstruktur.

Zur Orientierung koennen vor der Ausgabe insbesondere diese Punkte geprueft werden:

1. Literaturanker vorhanden,
2. Fliesstext-Verweise gesetzt,
3. Mehrfachzitate als getrennte Links formatiert,
4. Quellenzeilen unter Tabellen/Grafiken mit Literaturbezug verlinkt,
5. APA-7-nahe Konsistenz gegeben,
6. Linkdarstellung je Quelle konsistent,
7. keine inhaltliche Quellenaenderung vorgenommen.
