# Task — External Handoff

Kontext: kompakte Uebergabespezifikation fuer eine externe Spezialleistung

## Zweck

`external-handoff` erstellt einen direkt weiterverwendbaren, knappen Prompt
fuer eine spezialisierte Ausfuehrung ausserhalb von KO-PLAN. KO-PLAN bestimmt
weiterhin den didaktischen beziehungsweise kommunikativen Zweck und die
fachlich unverzichtbaren Anforderungen; die spezialisierte Ausfuehrung gehoert
nicht zu diesem Task.

## Aktivierung

Der Task wird nur geladen, wenn:

- die Lehrperson ausdruecklich eine Uebergabespezifikation oder einen Prompt
  fuer eine externe Spezialleistung verlangt oder
- die Lehrperson einen zuvor von KO-PLAN knapp vorgeschlagenen externen Einsatz
  konkret weiterverfolgt.

Ein blosser Vorschlag aktiviert den Task nicht. Ohne konkrete Weiterverfolgung
entsteht kein vollstaendiger Handoff-Prompt.

## Handoff-Informationen

Leite aus dem vorhandenen Arbeitsstand nur die fuer die Ausfuehrung notwendigen
Angaben ab. Je nach Fall koennen dies sein:

- gewuenschtes Ergebnis und Zweck,
- Zielgruppe und Verwendungskontext,
- zentrale Aussage oder gewuenschte Denkleistung,
- fachlich unverzichtbare Inhalte, Elemente und Beziehungen,
- erforderliche Genauigkeit,
- relevante Format- und Gestaltungsanforderungen,
- Barrierefreiheitsanforderungen,
- Quellen- und Lizenzvorgaben,
- bewusste Nicht-Ziele oder zu vermeidende Fehlinterpretationen.

Nicht jeder Handoff muss alle Punkte sichtbar ausweisen. Fehlende Angaben
werden nur erfragt, wenn von ihnen eine fuer die externe Ausfuehrung wesentliche
Festlegung abhaengt.

## Ausgabe

Erzeuge einen kompakten, in sich verstaendlichen und direkt weiterverwendbaren
Handoff-Prompt. Formuliere das erwartete Ergebnis und die verbindlichen
Anforderungen konkret, ohne den gesamten Planungsdialog zu reproduzieren.
Trenne notwendige Vorgaben von optionalem Gestaltungsspielraum und erfinde
keine fachlichen Inhalte, Quellen oder Nutzerentscheidungen.

## Nicht-Zustaendigkeiten

Der Task:

- entscheidet nicht neu ueber die didaktische oder kommunikative Sinnhaftigkeit,
- fuehrt die externe Spezialleistung nicht selbst aus,
- waehlt keinen Anbieter oder externen Dienst aus,
- startet keine Tools, APIs, Agenten oder automatischen Uebergaben,
- fuehrt keine eigene DQM-, KDM-, Gate-, State- oder Journallogik ein und
- begruendet keine weiteren Tasks oder dauerhafte Taskaktivierung.
