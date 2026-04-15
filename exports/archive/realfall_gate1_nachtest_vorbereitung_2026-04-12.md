# Gate 1 – Vorbereitung schmaler Realfall-Nachtest

Datum: 2026-04-12
Status: vorbereiteter echter Nachtest, noch nicht durchgefuehrt
Ziel: gehaerteten Agenten einmal unter realen Bedingungen mit begrenztem Material pruefen, ohne neue Regelarbeit waehrend des Falls

## Testziel

Der Nachtest soll nicht noch einmal die Regeltexte pruefen, sondern zeigen, ob der aktuelle Stand im echten Arbeitsfluss stabil bleibt.

Geprueft werden insbesondere:

- Arbeitsmodus wird aus dem Anliegen abgeleitet und nicht unnötig abgefragt.
- Rueckfragen bleiben knapp, didaktisch und einzeln.
- Blog bleibt Primaerartefakt.
- Reveal entsteht erst nach ausdruecklichem Uebergang.
- Sichtbare Struktur erscheint nur an echten Uebergaengen oder bei Finalisierung.
- Profilsteuerung A/B/C funktioniert sichtbar und konsistent.

## Empfohlener Realfall

### Falltyp

Kurze Einfuehrungsveranstaltung mit klarer Zielgruppe, ohne Uploads, mit begrenztem Umfang und anschlussfaehigem Projektthema.

### Thema

OER-Kurzeinstieg fuer Masterstudierende der Wirtschaftspaedagogik

### Warum genau dieser Fall

- schmaler Umfang: 30 Minuten
- klare Zielgruppe und klarer Anlass
- keine komplexe Materiallage
- vorhandene Projektanschluesse ueber OER-Beitraege in der Wissensbasis
- eignet sich fuer Blog- und Reveal-Ableitung, ohne Speziallogik zu brauchen

## Eingabetext fuer den echten Nachtest

Mit diesem Text in den Fall starten:

```text
PLAN START: Ich plane eine 30-minuetige Einfuehrung fuer Masterstudierende der Wirtschaftspaedagogik zum Thema OER. Die Veranstaltung ist Teil eines Einfuehrungsseminars. Ziel ist, dass die Studierenden verstehen, was OER sind, warum offene Lizenzen relevant sind und wie sie mindestens zwei Suchwege fuer OER benennen koennen. Geplant sind ein kurzer Impuls, ein kleines Suchbeispiel und eine Abschlussfrage. Es gibt keine Uploads und kein umfangreiches Begleitmaterial.
```

Wichtig an diesem Starttext:

- Artefakt-Arbeit ist klar erkennbar.
- Das didaktische Profil fehlt absichtlich und soll vom Agenten sauber geklaert werden.
- Der Kontext ist hinreichend konkret, sodass keine Modusfrage noetig sein sollte.

## Vorbereitete Folgeantworten

### Antwort 1

Falls der Agent nach Profil oder offenem Kontext fragt:

```text
Default A passt. Es sind etwa 18 Teilnehmende in einem Seminarraum mit Beamer. Die Veranstaltung soll aktivierend, aber kompakt sein.
```

### Antwort 2

Falls noch eine Anschlussklaerung noetig ist:

```text
Am Ende sollen die Studierenden zwei Suchwege fuer OER benennen und einfache Lizenzhinweise grob einordnen koennen. Eine formale Pruefung ist nicht geplant.
```

### Antwort 3

Wenn der Agent in die Entwurfsphase uebergeht und die Blog-Arbeitsdatei vorbereitet hat:

```text
Bitte knapp und leser:innenorientiert ausformulieren.
```

### Antwort 4

Nach kurzer Sichtpruefung der `index.md`:

```text
BLOG FINAL
```

### Antwort 5

Nach Blog-Finalisierung:

```text
REVEAL GO
```

### Antwort 6

Nach kurzer Sichtpruefung der `_index.md`:

```text
REVEAL FINAL
```

## Sollverhalten im Nachtest

| Station | Sollverhalten |
|---|---|
| Start | Keine Modusfrage trotz klarem Planungsanliegen; stattdessen kurze Zusammenfassung und genau eine gezielte Rueckfrage |
| Klaerung | Profil A/B/C wird explizit geklaert oder Default A transparent gesetzt |
| Planung | Keine Artefakterzeugung, solange zentrale Kontextluecken offen sind |
| Blog-Entwurf | Zuerst `blog_snapshot.txt`, dann `index.md`; Blog bleibt Primaerartefakt |
| BLOG FINAL | Sichtbar: DQM-Pruefbericht, formale Blocker oder Freigabehinweis, danach knappe Zusammenfassung |
| REVEAL GO | `_index.md` und `reveal_snapshot.txt` werden erzeugt; noch keine Endfreigabe |
| REVEAL FINAL | Sichtbar: Abgleich, Materialuebersicht, formale Blocker oder Freigabehinweis, danach knappe Zusammenfassung |

## Relevante RCs fuer die Auswertung

- RC-07 Konfliktaufloesung nach Prioritaet
- RC-20 Profilsteuerung explizit
- RC-21 Kontextluecken stoppen Artefaktproduktion
- RC-24 Blog-first bleibt Default
- RC-28 Dialogsprache bleibt didaktisch
- RC-29 Uploads bleiben Quellmaterial bis Freigabe
- RC-30 Gleichwertige Statusmeldungen werden robust interpretiert

## Go/No-Go-Kriterien

### Go

- keine unnoetige Modusfrage am Start
- Profilsteuerung sichtbar sauber
- keine Reveal-Erzeugung vor `REVEAL GO`
- Rueckfragen knapp und einzeln
- Finalisierungen zeigen die erwarteten sichtbaren Ausgaben

### No-Go

- Agent fragt trotz klarer Lage zuerst nach `Meta-Arbeit` oder `Artefakt-Arbeit`
- Agent erstellt Artefakte trotz offener Kernluecken
- Agent wechselt in prozessprotokollartige Sprache statt didaktischer Fuehrung
- Reveal entsteht vor Blog-Finalisierung
- `BLOG FINAL` oder `REVEAL FINAL` liefern die sichtbaren Pflichtausgaben nicht

## Dokumentation waehrend der Durchfuehrung

Nach dem echten Nachtest kurz festhalten:

- Datum
- verwendeter Starttext
- tatsaechlich gestellte Rueckfragen
- ob der Agent den Arbeitsmodus still korrekt abgeleitet hat
- ob Profil A/B/C sauber gefuehrt wurde
- ob Blog-first und Uebergangsdisziplin gehalten wurden
- ob die sichtbaren Finalisierungsausgaben vollstaendig waren
- kurzes Urteil: bestanden, teilweise, nicht bestanden

Direkt ausfuellbare Vorlage:

- `exports/realfall_gate1_nachtest_auswertung_2026-04-12.md`

## Empfehlung fuer die Durchfuehrung

- Den Fall ohne Uploads fahren.
- Keine Zusatzwuensche waehrend des Tests einstreuen.
- Nur dann eingreifen, wenn der Agent erkennbar von der Sollspur abweicht.
- Nach dem Fall die Ergebnisse gegen den RC-Katalog spiegeln und erst dann ueber Gate 2 gehen.