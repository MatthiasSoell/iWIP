# Agenten-Haertung – Prozessoptimierung

Datum: 2026-04-15
Status: dokumentiert
Fokus: prozessuale Haertung der Agentenlogik

## 1. Ziel der Aenderungen

Der Agent wurde nicht inhaltlich, sondern prozessual nachgeschaerft. Ziel war, bereits vorhandene Regeln so zu verankern, dass sie nicht nur beschrieben, sondern operativ wirksam werden. Im Fokus standen vier Risikobereiche: Stilkonsistenz, Trennung von Planungs- und Artefaktsprache, deterministische Blog-zu-Reveal-Ableitung und belastbare Snapshot-Gates. Geloest werden sollte vor allem das Problem, dass Regelverletzungen zuvor moeglich waren, ohne den Prozess zwingend zu stoppen.

## 2. Kernaenderungen

### 2.1 Stil-Engine

Problem:
Stilvorgaben waren verteilt vorhanden, aber nicht scharf genug als Pflichtbedingung fuer finale Artefakte operationalisiert.

Geaendert:
Stilkonsistenz wurde als strukturelle Pflicht verankert. Planungs-, Scaffold- und Meta-Formulierungen wurden fuer sichtbare finale Artefakte explizit untersagt; konsistente Ansprache, Ton und semantischer Emoji-Einsatz wurden als nicht-optionale Artefaktregeln festgezogen.

Wo:
- Contract
- Check
- Master-Agent

### 2.2 Modustrennung (Planung vs. Output)

Problem:
Planungs- und Artefaktsprache konnten ineinanderlaufen; die Grenze zwischen Vorbereitung und publizierbarem Output war zu implizit.

Geaendert:
`Planungsmodus` und `Outputmodus` wurden explizit definiert. Fuer `P1` und `P2` gilt sichtbare Planungssprache, fuer `P3` bis `P5` nur publizierbare Artefaktsprache. Planungsraster, Scaffold-Formeln und Agentenarbeitsanweisungen sind im Outputmodus verboten.

Wo:
- Contract
- Master-Agent
- Create
- Check

### 2.3 Blog -> Reveal Transformation

Problem:
Die Reveal-Ableitung war zu frei interpretierbar und damit anfaellig fuer Bedeutungsdrift, Auslassungen und Rueckgriff auf falsche Quellenstaende.

Geaendert:
Die Transformation wurde deterministisch gefasst. Zulaessig sind nur Verdichtung, Gruppierung, foliengerechte Umstellung im Nahbereich, Visualisierung und aus dem Blog ableitbare Interaktionsimpulse. Unzulaessig sind neue unbelegte Kernbehauptungen, Rueckgriff auf Planungsnotizen oder Snapshots als Inhaltsquelle sowie stille semantische Verschiebungen.

Wo:
- Contract
- Master-Agent
- Create
- Check

### 2.4 Snapshot-Logik

Problem:
Snapshots waren vorgesehen, aber nicht als harter Gate-Mechanismus abgesichert; dadurch konnte Finalisierung trotz fehlender Snapshot-Datei denkbar bleiben.

Geaendert:
`blog_snapshot.txt` und `reveal_snapshot.txt` wurden als verpflichtende Gates verankert. Ohne Blog-Snapshot sind weder `P4` noch `BLOG FINAL` zulaessig; ohne Reveal-Snapshot ist weder die Reveal-Arbeitsphase abgeschlossen noch `REVEAL FINAL` zulaessig. Snapshot-Pruefung wurde zusaetzlich in die Mindestpruefungen vor Finalisierung aufgenommen.

Wo:
- Contract
- Check
- Master-Agent
- Create

## 3. Technische Umsetzung

Betroffene Dateien:

- `project_governance/agent_contract.md`
- `ai_agents/master_agent.md`
- `prompts/create.md`
- `prompts/check.md`

Relevante RCs:

- `RC-02`
- `RC-05`
- `RC-13`
- `RC-17`
- `RC-18`

## 4. Wirkungslogik

Vorher:
Regeln waren in weiten Teilen bereits vorhanden, aber an kritischen Stellen zu implizit oder zu schwach als Blocker operationalisiert.

Nachher:
Regelverstoesse werden nicht nur beschrieben, sondern als formale Blocker behandelt. Fehlende Snapshots, sichtbare Planungssprache im Artefakt oder nicht-deterministische Reveal-Ableitung koennen die Finalisierung jetzt regelbasiert stoppen.

## 5. Validierung

Ansatz:
Gezielter Stresstest mit absichtlich eingebauten Regelverstoessen in den vier Risikobereichen.

Ergebnis:

- Stil: `FAIL` erkannt
- Modustrennung: `FAIL` erkannt
- Reveal: `FAIL` erkannt
- Snapshot: `FAIL` erkannt

Systemreaktion:

`STOP`

Begruendung:
Der simulierte Lauf waere nach Contract zu blockieren, weil sichtbare Planungs-/Scaffold-Sprache im Artefakt vorliegt und verpflichtende Snapshot-Dateien fehlen. Ohne `blog_snapshot.txt` sind `P4` und `BLOG FINAL` unzulaessig; ohne `reveal_snapshot.txt` ist `REVEAL FINAL` unzulaessig.

## 6. Fazit

Die Prozesslogik ist nach der Haertung deutlich robuster als zuvor, weil die vier kritischen Risikobereiche jetzt als operative Sperren statt als weiche Leitlinien gefasst sind. Restrisiko bleibt vor allem ausserhalb des Desk-Checks: Die Regelkonsistenz ist abgesichert, muss sich aber weiterhin in echten Laeufen gegen Dialogdrift und Grenzfaelle bewaehren.