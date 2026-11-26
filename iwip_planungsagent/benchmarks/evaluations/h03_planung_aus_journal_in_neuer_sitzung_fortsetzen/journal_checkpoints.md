# H03 – Journalsollstände

Prüfe die Struktur und den Inhalt an jedem Checkpoint. Wortlaut, Layout,
Datumswerte und Anzahl sachlich begründeter Historieneinträge sind variabel.

## Struktur

- Die Datei enthält `Current State` mit genau `planning_focus`, `main_line`,
  `commitments`, `constraints` und `open_item` sowie `Decision History`.
- Die Historie verwendet fortlaufende stabile IDs ab `J-001`, ISO-Daten
  und die Typen `decision`, `revision`, `open` und `resolved`. Erlaubte
  Felder sind `id`, `date`, `type`, `content`, `rationale`, `refers_to`,
  `rejected_alternative` und `dialogue_ref`. Prüfe die Existenz der Dateien und die
  Bytegleichheit in den unten genannten Ruhephasen.
- Jeder Eintrag braucht Inhalt. `rationale` enthält nur Gründe, die die
  Lehrperson ausdrücklich genannt oder übernommen hat. Bei Entscheidungen
  und Revisionen wird eine belegte Begründung aufgenommen, bei anderen
  Einträgen nur bei Erklärungsbedarf. Ohne belegten Grund entfällt das Feld.
- `dialogue_ref` ist optional. Wenn es vorhanden ist, muss es die im Dialog
  ausdrücklich vorhandene eindeutige Zugkennung wortgetreu wiedergeben.
  Prüfe beide Felder anhand des Dialogs.
- Referenzen zeigen auf frühere Einträge. `resolved` verweist auf den
  erledigten offenen Punkt. Eine Revision verweist auf passende frühere
  Einträge, sofern diese existieren. In H03 sind die Vorgänger aus der Tabelle
  einschlägig.
- Frühere Historieneinträge bleiben in Inhalt und Reihenfolge erhalten.
  `planning_state.md` fehlt in sämtlichen Snapshots.

## Pflichtpunkte je Checkpoint

| Nach Zug | Datei und Historie | Geltender Stand |
|---|---|---|
| A1 | Fallordner bleibt ohne Journal | Analyse ohne Planungsentscheidung |
| A2 | Journal entsteht mit tragender Entscheidung | Drei betriebliche Feedbacksituationen mit gemeinsamen Kriterien systematisch vergleichen. Begründete Wirkungsanalyse ist der Kern. |
| A3 | Eigene Entscheidung zur Sicherung kommt hinzu | Vergleichsmatrix ergänzt den Mehrfallvergleich. Einzelpräsentationen entfallen. |
| A4 und A5 | Bytegleich zu A3 | Sprachliche Neufassung und abgelehnter Vorschlag ergeben keine materielle Änderung. |
| A6 | Die Revisionsreferenzen decken zusammen die abgelöste Mehrfallentscheidung aus A2 und die Matrixentscheidung aus A3 ab. Der Archivbestand dient als Vergleichsbasis für B. | Eine gemeinsame komplexere Ausbildungssituation. Perspektiven von lernender und ausbildender Person, mögliche Feedbackwirkung, begründeter und gemeinsam kommentierter Gesprächsentwurf. Die Drei-Fall-Logik und ihre Vergleichsmatrix sind im Current State entfallen. |
| B1 und B2 | Journal und Archiv jeweils bytegleich zu A6. | A6 bleibt gültig. |
| B3 | Die Revision verweist auf den A6-Eintrag, der den Gesprächsentwurf als Sicherung festhält. Genau ein neuer Sitzungs-Snapshot ist bytegleich zum Journal nach A6. Der bisherige Archivbestand bleibt erhalten. | Die gemeinsame Situation, Perspektiven und Wirkungsanalyse bleiben. Zwei Feedbackstrategien werden in einer Entscheidungstabelle verglichen und ihre bedingte Eignung begründet. Der kommentierte Gesprächsentwurf entfällt aus dem Current State. |

Prüfe ab A2 in jedem Snapshot den vollständigen `Current State`, auch
unveränderte Festlegungen. Die 90 Minuten und die Grenze ohne externe
Recherche gelten durchgehend. Historische Inhalte dürfen als verworfene oder
revidierte Setzungen in der Historie stehen. Im `Current State` gelten nur
die bestätigten Entscheidungen. Höchstens ein aus dem Dialog begründeter,
entscheidungsrelevanter offener Punkt ist zulässig. Prüfe neue
Historieneinträge auf den zugehörigen materiellen Planungsanlass.
Bloße Vorschläge, Ablehnungen und sprachliche Änderungen lösen keinen
eigenen Eintrag aus. Eine verworfene Alternative darf bei späterer
Erklärungsrelevanz als `rejected_alternative` vermerkt sein.
