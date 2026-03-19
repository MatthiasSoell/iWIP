# /Literatur — Literatur-Finalisierung fuer Blogbeiträge

Dieser Prompt fuehrt eine standardisierte Literatur-Nachbearbeitung
fuer einen bestehenden Blogbeitrag im SciBlog iWIP aus.

Arbeite strikt nach den Regeln aus:

ai_agents/master_agent.md

---

## Aufgabe

Bereite den Literaturteil eines vorhandenen Blogbeitrags formal auf,
ohne inhaltliche Quellenangaben zu veraendern.

Der Prompt darf nur folgende Aspekte veraendern:

- Linksetzung im Fliesstext,
- Formatkonsistenz im Literaturabschnitt,
- Linkdarstellung (Badge vs. normaler Link),
- Reparatur fehlerhafter Linksyntax.

Inhaltliche Quellenaussagen bleiben unveraendert.

---

## Verbindlicher Ablauf

## Schritt 1 – Zielartefakt bestimmen

- Arbeite auf dem aktuell aktiven Blogbeitrag oder auf dem vom Nutzer genannten Beitragspfad.
- Wenn nicht eindeutig, stelle genau eine kurze Rueckfrage.

## Schritt 2 – Literaturanker sicherstellen

- Falls nicht vorhanden, setze direkt vor dem Literaturabschnitt:

```markdown
<span id="literatur"></span>
```

- Verwende als Abschnittstitel bevorzugt:

```markdown
## Literatur und Quellen
```

## Schritt 3 – Verweise im Fliesstext verlinken

- Wenn eine Quelle im Fliesstext genannt wird, verlinke auf `#literatur`.
- Beispiel:

```markdown
[vgl. Euler & Hahn (2014)](#literatur)
```

- Verlinke konsistent in allen relevanten Abschnitten.
- Bei mehreren Quellen setze pro Quelle einen eigenen Link; Semikolon und Leerzeichen bleiben ausserhalb der Links.
- Beispiel: `[Nickolaus, 2018](#literatur); [Seifried & Sembill, 2010](#literatur)`.
- Verlinke Literaturangaben in Quellenzeilen unter Tabellen/Grafiken (z. B. `bildquelle`, "in Anlehnung an ...") ebenfalls auf `#literatur`.

## Schritt 4 – Literaturverzeichnis normalisieren

- Formatiere Eintraege APA-7-nah und einheitlich.
- Pro Quelle genau ein bibliografischer Haupteintrag.
- Setze Zusatzlinks direkt beim Eintrag:
  - bevorzugt als Badges mit vorhandenen Klassen `lit-ub`, `lit-doi`, `lit-worldcat`,
  - sonst als normaler Weblink.
- Korrigiere defekte Klammern, doppelte URL-Syntax und zerbrochene Markdown-Links.

## Schritt 5 – Integritaetsregel

- Aendere keine inhaltlichen Quellenbestandteile:
  - Autor:innen
  - Jahr
  - Titel
  - Publikationsangaben
  - Seiten-/Bandangaben
- Erlaubt sind nur formale Korrekturen und Linkstruktur.

## Schritt 6 – Abschlusscheck

Pruefe vor finaler Ausgabe:

1. Literaturanker vorhanden,
2. Fliesstext-Verweise gesetzt,
3. Mehrfachzitate als getrennte Links formatiert,
4. Quellenzeilen unter Tabellen/Grafiken mit Literaturbezug verlinkt,
5. APA-7-nahe Konsistenz gegeben,
6. Linkdarstellung je Quelle konsistent,
7. keine inhaltliche Quellenaenderung vorgenommen.

Wenn Punkte fehlen, ueberarbeite automatisch vor finaler Ausgabe.
