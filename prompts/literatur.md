# /Literatur — Literatur-Finalisierung fuer Blogbeitraege

Scope: optionale, teilweise automatisierte Literatur-Nachbearbeitung fuer bestehende Blogbeitraege

Du arbeitest strikt nach den Regeln aus:

project_governance/agent_contract.md

Der Contract ist die einzige Steuerlogik.

## Status

Dieses Werkzeug bleibt als eigenständiger Prompt optional nutzbar. Der Modus `LITERATUR GO` wird zusätzlich im Contract standardmäßig innerhalb von `BLOG FINAL` ausgeführt.

- `LITERATUR GO` ist der rein formale Standardmodus und wird im Contract standardmaessig innerhalb von `BLOG FINAL` ausgefuehrt.
- `LITERATUR RECHERCHE GO` bleibt ein separater, manuell ausloesbarer Befehl.
- `REVEAL FINAL` fuehrt keine eigene Literatur-Recherche aus und bleibt unveraendert.
- Reveal uebernimmt seine Literatur weiterhin ausschliesslich aus dem finalen Blog.

Dieser Prompt fuehrt keine eigene Steuerlogik ein und veraendert den Hauptablauf nicht ausserhalb der im Contract beschriebenen Integration von `LITERATUR GO` in `BLOG FINAL`.

---

## Aufgabe

Bearbeite den Literaturteil eines vorhandenen Blogbeitrags kontrolliert und ohne Quellenneuerfindung.

Erlaubt sind nur:

- formale Literatur-Normalisierung,
- Linksetzung im Fliesstext,
- konsistente Linkdarstellung direkt am Eintrag,
- Reparatur fehlerhafter Linksyntax,
- im Recherchemodus zusaetzlich belastbare Ergaenzung vorhandener Quellen um externe Nachweislinks.

Nicht erlaubt sind:

- Erfinden, Ersetzen oder stilles Uminterpretieren von Quellenbestandteilen,
- Raten bei DOI-, WorldCat- oder UB-Treffern,
- instabile, sitzungsabhaengige oder captcha-abhaengige Verlinkungen.

---

## Nutzung

Arbeite auf dem aktuell aktiven Blogbeitrag oder auf dem vom Nutzer genannten Beitragspfad.
Wenn der Zielbeitrag nicht eindeutig ist, stelle genau eine kurze Rueckfrage.

### Modus 1: `LITERATUR GO`

`LITERATUR GO` ist die rein formale Literatur-Normalisierung ohne Online-Recherche.

Dieser Modus umfasst:

- APA-7-nahe Vereinheitlichung des bestehenden Literaturbestands,
- Literaturanker direkt vor dem Literaturabschnitt:

```markdown
<span id="literatur"></span>
```

- bevorzugte Abschnittsueberschrift:

```markdown
## Literatur und Quellen
```

- Verlinkung von Literaturhinweisen im Fliesstext auf `#literatur`,
- getrennte Verlinkung bei Mehrfachzitaten; Semikolon und Leerzeichen bleiben ausserhalb der Links,
- Verlinkung von Literaturangaben in Quellenzeilen unter Tabellen und Grafiken ebenfalls auf `#literatur`,
- konsistente Badge-Linkdarstellung mit den bestehenden Klassen `lit-doi`, `lit-worldcat` und `lit-ub`,
- Reparatur defekter Markdown-Linksyntax, doppelter URL-Syntax und zerbrochener Klammerungen.

Beispiele:

```markdown
[vgl. Euler & Hahn (2014)](#literatur)
```

```markdown
[Nickolaus, 2018](#literatur); [Seifried & Sembill, 2010](#literatur)
```

Fuer `LITERATUR GO` gilt strikt:

- keine externe Recherche,
- keine DOI-, WorldCat- oder UB-Nachsuche,
- keine Aenderung von Autor:innen, Jahr, Titel, Publikationsangaben oder Seiten-/Bandangaben.

### Modus 2: `LITERATUR RECHERCHE GO`

`LITERATUR RECHERCHE GO` umfasst alle Funktionen von `LITERATUR GO` und ergaenzt sie um kontrollierte Recherche fuer zusaetzliche Nachweislinks.

Zusaetzlich recherchierbar und ergaenzbar sind ausschliesslich:

- DOI,
- WorldCat,
- UB-Rostock-Links.

#### Recherche-Regeln

- Keine Quellenbestandteile erfinden oder ersetzen.
- DOI nur uebernehmen, wenn Autor:innen, Titel und Jahr plausibel uebereinstimmen.
- WorldCat bevorzugt:
  - bei Buechern ueber ISBN,
  - bei Artikeln ueber DOI oder Titel.
- UB Rostock bevorzugt:
  - bei Buechern und Monografien ueber ISBN oder stabilen Katalogtreffer,
  - bei Zeitschriftenaufsaetzen keinen Einzelartikel erzwingen; optional ist nur ein Link zur Zeitschrift selbst.
- Keine Captchas umgehen.
- Keine sitzungsabhaengigen oder instabilen Deep-Links verwenden.

#### Plausibilitaetspruefung

Vor jedem uebernommenen Recherchelink ist verpflichtend zu pruefen:

- Autor:innen,
- Titel,
- Jahr,
- Publikationstyp,
- DOI oder ISBN, soweit vorhanden.

#### Umgang mit Unsicherheit

Bei Unsicherheit:

- keine geratenen Links setzen,
- stattdessen transparent markieren mit:
  - `kein DOI gefunden`
  - `nicht eindeutig gefunden`
  - `pruefen`

---

## Formale Leitlinien fuer beide Modi

- Pro Quelle genau ein bibliografischer Haupteintrag.
- Zusatzlinks stehen direkt beim jeweiligen Eintrag.
- Bevorzugt werden vorhandene Badge-Klassen `lit-doi`, `lit-worldcat`, `lit-ub`; nur wenn das nicht sinnvoll passt, nutze normale Weblinks.
- Bestehende Quelleninhalte werden formal normalisiert, aber nicht inhaltlich umgeschrieben.

Vor der Ausgabe bzw. vor Abschluss des Bearbeitungsschritts sind insbesondere diese Punkte zu pruefen:

1. Literaturanker vorhanden.
2. Fliesstext-Verweise auf `#literatur` gesetzt.
3. Mehrfachzitate als getrennte Links formatiert.
4. Quellenzeilen unter Tabellen und Grafiken mit Literaturbezug verlinkt.
5. APA-7-nahe Konsistenz gegeben.
6. Badge- oder Linkdarstellung je Quelle konsistent.
7. Fehlerhafte Markdown-Linksyntax repariert.
8. Keine inhaltliche Quellenaenderung vorgenommen.
9. Im Modus `LITERATUR GO` keine externe Recherche ausgefuehrt.
10. Im Modus `LITERATUR RECHERCHE GO` nur plausibilisierte und stabile Recherchelinks uebernommen.
