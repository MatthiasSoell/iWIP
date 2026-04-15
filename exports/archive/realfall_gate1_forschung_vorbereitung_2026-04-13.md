# Gate 1 - Vorbereitung weiterer Forschung mit Forschungsprotokoll

Datum: 2026-04-13
Status: vorbereitet, noch nicht durchgefuehrt
Ziel: den gehaerteten Agenten unter blinden Bedingungen auf Dialogzurueckhaltung, breiteren semantischen Emoji-Einsatz, Statusrobustheit und separates Forschungsprotokoll testen

## Testfokus

Geprueft werden insbesondere:

- sichtbare Zwischenstaende waehrend Recherche, Dateiarbeit und Routinepruefungen bleiben weitgehend aus
- Emojis erscheinen semantisch nicht nur in Ueberschriften, sondern bei Bedarf auch im sichtbaren Hauptkoerper
- natuerliche Statusformulierungen werden robust wie `BLOG FINAL`, `REVEAL GO` und `REVEAL FINAL` verstanden
- das Forschungsprotokoll laeuft mit `PLAN START` still im Hintergrund an und wird mit `REVEAL FINAL` automatisch abgeschlossen
- Blog-first, Snapshot-Logik und Finalisierungsdisziplin bleiben intakt

## Empfohlener Realfall

### Falltyp

Kompakte didaktische Sitzung mit klarer Zielgruppe, ohne Uploads, mit einem Thema, das natuerlich Leitfrage, Vergleich, Sortieraufgabe, Merksatz und Transfer erlaubt.

### Thema

Constructive Alignment in der Unterrichtsplanung fuer Masterstudierende im Lehramt

### Warum genau dieser Fall

- klarer didaktischer Kern ohne Spezialwissen oder Uploads
- natuerlicher Anlass fuer semantische Marker im sichtbaren Inhalt sowie fuer Vergleichstabelle und Merksatz
- gut geeignet fuer Blog- und Reveal-Ableitung
- ueberschaubar genug fuer eine echte Forschung

## Eingabetext fuer die echte Forschung

Mit diesem Text in einen neuen Dialog starten:

```text
PLAN START: Ich plane eine 45-minuetige Sitzung fuer Masterstudierende im Lehramt zum Thema Constructive Alignment in der Unterrichtsplanung. Die Sitzung ist Teil eines didaktischen Einfuehrungsseminars. Ziel ist, dass die Studierenden die Passung von Lernziel, Lernaktivitaet und Pruefung erklaeren, einen einfachen Fehlfit in einem Mini-Beispiel erkennen und eine kleine Anpassungsidee fuer die eigene Planung festhalten koennen. Geplant sind ein kurzer Einstieg mit Gegenbeispiel, eine begriffliche Klaerung, eine kleine Sortier- bzw. Zuordnungsaufgabe an einem Mini-Fall und ein Abschluss mit 1-Minuten-Commitment. Es gibt keine Uploads und kein umfangreiches Begleitmaterial.
```

## Vorbereitete Folgeprompts

### Prompt 1

Falls der Agent nach Profil oder Rahmendaten fragt:

```text
Profil A passt. Es sind etwa 20 Teilnehmende in einem Seminarraum mit Beamer. Die Sitzung soll kompakt, klar und aktivierend sein.
```

### Prompt 2

Falls noch eine fachliche Anschlussklaerung noetig ist:

```text
Am Ende reicht ein kurzes schriftliches 1-Minuten-Commitment. Darin sollen ein typischer Fehlfit und eine kleine Anpassungsidee fuer eine eigene Unterrichtssituation stehen. Es gibt keine benotete Pruefung.
```

### Prompt 3

Falls der Agent in die Blog-Ausarbeitung uebergeht und die Arbeitsdatei erstellt hat:

```text
Bitte knapp, leser:innenorientiert und im SciBlog-Stil ausformulieren.
```

### Prompt 4

Nach kurzer Sichtpruefung der `index.md` den Blog mit einer natuerlichen Statusformulierung finalisieren:

```text
Der Blog ist jetzt fertig. Bitte final pruefen und abschliessen.
```

### Prompt 5

Nach Blog-Finalisierung den Reveal-Uebergang ebenfalls natuerlich ausloesen:

```text
Bitte uebernimm den Wissensbasis-Eintrag und leite jetzt die Praesentation daraus ab.
```

### Prompt 6

Nach kurzer Sichtpruefung der `_index.md` die Praesentation finalisieren:

```text
Die Praesentation ist jetzt fertig. Bitte finalisieren.
```

### Forschungsprotokoll im Standardlauf

Kein zusaetzlicher Start- oder Abschluss-Prompt noetig:

- `PLAN START` soll das separate Forschungsprotokoll still im Hintergrund starten.
- `REVEAL FINAL` soll es im regulaeren Ablauf automatisch abschliessen.
- Die Zeitmarker sollen als `MARKER | <ISO-8601> | <EVENT> | <DETAIL>` in der separaten Exportdatei mitlaufen.

Nur wenn der Lauf **ohne** `REVEAL FINAL` endet oder du einen Zwischenstand brauchst, nutze zusaetzlich:

```text
FORSCHUNGSPROTOKOLL FINAL
```

## Alternative mit strikten Standardsignalen

Wenn der Lauf nicht gleichzeitig die Alias-Robustheit testen soll, koennen Prompt 4 bis 6 durch die Standardsignale ersetzt werden:

```text
BLOG FINAL
```

```text
Wissensbasis-Eintrag uebernehmen & REVEAL GO
```

```text
REVEAL FINAL
```

## Standardisierter Nachlauf (Meta-Ebene)

Die Meta-Arbeit nach der Forschung sollte standardisiert sein, aber **nicht** in den Kernablauf der Artefakterstellung eingreifen.

Empfohlener Ablauf:

1. Forschung regulär bis `REVEAL FINAL` beenden.
2. Danach in **derselben** Sitzung nur noch den Chat exportieren.
3. Die eigentliche Analyse anschließend in einem **neuen** Chat als Meta-Arbeit durchführen.

### Meta-Prompt 1 - Chat exportieren

Direkt nach `REVEAL FINAL` senden:

```text
Meta-Arbeit: Exportiere den gesamten sichtbaren Verlauf dieses Forschungs bis einschließlich der abgeschlossenen REVEAL-FINAL-Antwort nach `exports/forschung_chat_constructive_alignment_2026-04-13.md`. Dieser Exportauftrag selbst und jede nachfolgende Meta-Arbeit dürfen nicht Teil der Exportdatei sein. Exportiere nur sichtbare Nutzer- und Assistentenbeiträge, keine Toollogs, keine Systemtexte und keine Thinking-Inhalte.
```

### Meta-Prompt 2 - Forschung analysieren

Danach in einem **neuen Chat** senden:

```text
Meta-Arbeit: Analysiere die Forschung gründlich auf Basis von `exports/forschung_chat_constructive_alignment_2026-04-13.md` sowie der zugehörigen Artefakte in `content/blog/lehre/widi/constructive_alignment_einstieg/` und `content/praesentation/lehre/widi/constructive_alignment_einstieg/`. Arbeite im Review-Modus: zuerst Befunde nach Schweregrad mit Datei- und Zeilenverweisen, danach offene Fragen oder Annahmen, danach ein kurzes Gesamturteil. Prüfe insbesondere Routing, Prozesssprache, Blog-first, semantischen Emoji-Einsatz im sichtbaren Hauptkörper, Reveal-Finaltabellen, Forschungsprotokoll/Marker und Pfadhygiene.
```

## Sollbeobachtungen in der Forschung

- keine unnoetige Modusfrage am Start
- genau eine Frage gleichzeitig
- keine Artefakterzeugung bei offenen Kernluecken
- `blog_snapshot.txt` vor `index.md`
- `_index.md` und `reveal_snapshot.txt` erst nach Reveal-Uebergang
- deutlich weniger sichtbare Zwischenstaende als im letzten dokumentierten Lauf
- semantische Emojis nicht nur in H2/H3, sondern bei Bedarf auch in Listen, Leitfragen, Arbeitsauftrag, Merksatz oder Transferstellen des sichtbaren Inhalts
- Forschungsprotokoll startet mit `PLAN START`, bleibt im Dialog unsichtbar und wird mit `REVEAL FINAL` automatisch abgeschlossen

## Empfehlung fuer die Durchfuehrung

- neuen Dialog verwenden
- keine Uploads hinzufuegen
- waehrend des Tests keine Zusatzwuensche einstreuen
- wenn die Routinghaertung mitgeprueft werden soll, darf bewusst eine fachfremde oder stoerende Datei im Editor offen bleiben
- nur bei Blog-only-Faellen, Abbruch oder Zwischenstand zusaetzlich `FORSCHUNGSPROTOKOLL FINAL` senden
- Chat-Export nach `REVEAL FINAL` standardisiert als Meta-Schritt ausloesen, Analyse danach in neuem Chat starten