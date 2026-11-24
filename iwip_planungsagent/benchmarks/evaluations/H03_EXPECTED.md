# H03 – Durchführung und Auswertung

## Beobachtungen sichern

Lege in einem ignorierten oder temporären Laufordner außerhalb des Fallordners
ein Verzeichnis `snapshots` an. Nach jeder Agentenantwort erstelle darin den
Unterordner für den abgeschlossenen Zug (`A1` bis `A6`, `B1` bis `B3`).
Kopiere vorhandene `planning_journal.md` und `planning_state.md` unverändert
dorthin. Ein leerer Snapshot belegt, dass am Ende des ausgeführten Zugs keine
der beiden Dateien vorlag. Für ausgefallene Züge keine Snapshots anlegen.
Die Sitzungen erhalten keinen Zugriff auf die Snapshots. Protokolliere die
beobachtbaren Datei- und Toolaktionen, auch Schreibzugriffe außerhalb des
Fallordners und etwaige Builds oder Produktionsschritte.

## Struktur prüfen

Rufe den [Strukturprüfer](../../../scripts/check_h03_journal.rb) mit Ruby und
YAML/Psych aus dem Wurzelverzeichnis des Repositorys auf:

```sh
ruby scripts/check_h03_journal.rb "PFAD_ZUM_LAUFORDNER/snapshots"
```

Der Prüfer kontrolliert Dateiexistenz, Bytegleichheit in Ruhephasen,
Feldnamen, Ereignisstruktur, Erhalt der Historie und formale Referenzen.
Exitcode `0` bestätigt diese technischen Teilprüfungen. Bei `1` die
Fehlermeldung dem betroffenen Prüfpunkt zuordnen und zwischen fehlender
Laufdokumentation und belegter Abweichung unterscheiden. Bei `2` ist das
Layout für den Prüfer nicht auswertbar. In diesem Fall **alle** Strukturpunkte
manuell anhand der Sollstände prüfen und Layout und Belege dokumentieren.
Bei Teilläufen die vorliegenden Checkpoints manuell prüfen.

## Inhalt und Dialog prüfen

Die [Journalsollstände](../fixtures/H03_JOURNAL_CHECKPOINTS.md) sind für
jeden ausgeführten Zug verpflichtend. Prüfe den gesamten geltenden Stand,
die erhaltene Historie und die inhaltliche Zuordnung der Revisionsverweise
immer manuell, auch bei Exitcode `0`. Werte zusätzlich die folgenden
Belege aus:

| Bereich | Beobachtbarer Beleg |
|---|---|
| Prozess | Schreibzugriffe nur im bestätigten Fallordner, kein Build oder Produktionsschritt, keine erneute Ordnerfreigabe. B ist eine frische Sitzung ohne A-Dialog. Die Antwort auf B1 rekonstruiert den geltenden Stand und den Wechsel vom Mehrfallvergleich zum gemeinsamen Fall anhand des Journals. |
| Didaktik | A1 verbindet Feedbackwirkung mit der Aufgabenanforderung. B2 verbindet die zwei Perspektiven mit der möglichen Wirkung. B3 erhält die gemeinsame Analyse und macht die Abwägung der zwei Strategien für die Lernenden begründbar. Fachlich tragfähige Formulierungen sind gleichwertig. |
| Dialogbeobachtungen | Rückfragen und Prozessmeldungen mit Zug und Anlass erfassen. Eine kurze benutzerrelevante Statusinformation kann angemessen sein. |

## Prüfurteil

Je Pflichtpunkt der Sollstände, des Prozesses und der Didaktik
`erfüllt`, `abweichend` oder `nicht beobachtbar` mit Beleg vergeben.
Weise Struktur, Journalinhalt, Prozess und Didaktik getrennt aus.
Ein vollständiger H03-Lauf ist **bestanden**, wenn alle Pflichtpunkte
erfüllt sind. Bei mindestens einer belegten Abweichung ist er
**nicht bestanden**. Sind alle beobachtbaren Pflichtpunkte erfüllt, aber
Pflichtbelege fehlen, lautet das Urteil **unvollständig**. Fehlender
Schreibzugriff oder ein technisch unmöglicher Sitzungswechsel werden
als Abbruchgrund ausgewiesen. Geplante Teilläufe erhalten ein Urteil
ausschließlich für ihren Prüfumfang.

Kennzeichne vorzeitiges Schreiben, fehlende Persistenz einer tragenden
Entscheidung, Reaktivierung alter Entscheidungen und Verlust der Historie
zusätzlich als Kernfehler.
