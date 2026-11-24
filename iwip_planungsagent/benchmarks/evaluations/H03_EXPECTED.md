# H03 – Durchführung und Auswertung

Sichere nach jedem Nutzerzug die Beobachtungen zu Dialog und Dateien. Verwende
einen eigenen ignorierten oder temporären Laufordner. Lege darin außerhalb des
Fallordners neun Snapshot-Verzeichnisse `A1` bis `A6` und `B1` bis `B3` an.
Kopiere nach jedem Zug vorhandene Journal- und Übergabedateien in dessen
Verzeichnis. Bei Abwesenheit bleibt das Verzeichnis leer. Die Sitzung erhält
keinen Zugriff auf die Snapshots. Kontrolliere zusätzlich, dass der Agent nur
im benannten Fallordner schreibt und keinen Build oder Produktionsschritt auslöst.

Prüfe die [Journalsollstände](../fixtures/H03_JOURNAL_CHECKPOINTS.md). Der
[Strukturprüfer](../../../scripts/check_h03_journal.rb) prüft gespeicherte
Snapshots mit Ruby und YAML/Psych. Er führt keinen Agentenlauf aus.

```sh
ruby scripts/check_h03_journal.rb /pfad/zum/lauf/snapshots
```

Der Prüfer akzeptiert YAML-Listen für die Historie und Überschriften mit
YAML-Blöcken pro Eintrag. Falls ein Journal ein anderes lesbares Layout
verwendet, prüfe die Struktur und Referenzen anhand des Sollstands manuell
und dokumentiere das Format. Inhaltliche Gleichwertigkeit wird immer anhand
des Journals und des Dialogs beurteilt.

| Bereich | Beobachtbarer Beleg |
|---|---|
| Prozess | In A1 kein Journal, erste Anlage bei A2. Änderungen, Ruhephasen und Referenzen entsprechen dem Sollstand. In B1 wird die Revision ohne Rückgriff auf den alten Dialog rekonstruiert. Keine zusätzliche Freigabeschleife bei bestätigtem Pfad. |
| Didaktik | A1 verbindet Feedbackwirkung mit der Aufgabenanforderung. B2 verbindet die zwei Perspektiven mit der möglichen Wirkung. B3 erhält die gemeinsame Analyse und macht die Abwägung der zwei Strategien für die Lernenden begründbar. Fachlich tragfähige Formulierungen sind gleichwertig. |
| Dialog | Relevante Rückfragen und Prozessmeldungen mit Turn und Anlass erfassen. Eine kurze benutzerrelevante Statusinformation kann angemessen sein. |

Je Prüfpunkt `erfüllt`, `abweichend` oder `nicht beobachtbar` vergeben und
Belege angeben. Kernfehler sind vorzeitiges Schreiben, fehlende Persistenz
einer tragenden Entscheidung, Reaktivieren alter Entscheidungen und Verlust
der Entscheidungshistorie. Bei fehlendem Schreibzugriff oder fehlender
Möglichkeit, Sitzung B ohne alten Dialog zu öffnen, gilt der betroffene
Abschnitt als technisch nicht durchführbar. Einen solchen Abbruch separat
ausweisen.

## Optionale Prüfung des freigegebenen Übergabestands

Bei Änderungen an `planning_state.md` nach B3 den sichtbaren Stand ausdrücklich
freigeben und seine Speicherung im bestätigten Fallordner beauftragen. Prüfe die
Übereinstimmung mit dem freigegebenen Text, die getrennte Journalhistorie
und das Ausbleiben von Publikation oder Build. Revidiere anschließend die
Sicherung ohne neuen Speicherauftrag. Der gespeicherte Stand bleibt bytegleich,
der Dialog weist auf den veralteten Übergabestand hin. Erst erneute Freigabe
mit Speicherauftrag aktualisiert ihn. Für einen Plattformwechsel diese Datei
in einer frischen Sitzung ausdrücklich als Planungsgrundlage benennen und
eine aktuelle Vorgabe hinzufügen. Die aktuelle Vorgabe hat Vorrang. Diese
optionale Prüfung geht nicht in H03 ein.
