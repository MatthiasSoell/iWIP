# Patch Prio 3 - Vereinfachung und Strukturhygiene

Datum: 2026-04-14
Status: bereit zur Ausfuehrung in separatem Fenster
Reihenfolge: 3 von 3
Voraussetzung: Patch Prio 1 und Patch Prio 2 sind bereits eingearbeitet

## Ziel

Baue verbleibende Redundanz ab und fuehre die Agentenarchitektur auf wenige klare Regelorte zurueck, ohne das Zielsystem erneut umzubauen.

## Bearbeitungsrahmen

Arbeite primaer in diesen Dateien:

- project_governance/agent_contract.md
- project_governance/content_emoji_policy.md
- ai_agents/master_agent.md
- prompts/create.md
- prompts/check.md
- ai_agents/templates/blog_template.md
- ai_agents/templates/reveal_template.md

Scope-Guard fuer dieses Patchpaket:

- Ziel ist ein **Minimalpatch ohne Scope Drift**.
- `README.md`, `ai_agents/blog_wissensbasis.md`, `ai_agents/didaktisches_qualitaetsmodell.md`, Content-Dateien, Exportdateien und sonstige Repo-Dateien bleiben unangetastet.
- Wenn eine Vereinfachung nur durch Aenderungen ausserhalb der oben genannten Dateien erreichbar waere, diese Erweiterung **nicht** still mitziehen, sondern im Abschluss als offenen Restpunkt melden.

## Konkreter Arbeitsauftrag

### 1. Emoji-Regeln zentralisieren

- project_governance/content_emoji_policy.md bleibt die einzige normative Detailquelle fuer Emoji-Regeln.
- agent_contract.md, master_agent.md, create.md, check.md und die Templates sollen nur noch knapp auf die Policy verweisen.
- Artefaktspezifische Mindestpruefungen duerfen erhalten bleiben, aber keine mehrfach ausformulierten Detailkataloge mit denselben Schwellenwerten.

### 2. Templates auf Struktur zurueckbauen

- ai_agents/templates/blog_template.md und ai_agents/templates/reveal_template.md sollen nur noch enthalten:
  - Frontmatter-Schema
  - Pflichtbloecke
  - Zielstruktur der Inhalte
  - wenige artefaktnahe Formatbeispiele
- Entferne oder kuerze alles, was eigentlich Workflow-, Prüf- oder Governance-Logik ist.

### 3. Terminologie normalisieren

- Ergaenze in project_governance/agent_contract.md eine kurze, knappe Glossar-Sektion fuer die Kernbegriffe der Steuerarchitektur, zum Beispiel:
  - Arbeitsmodus
  - Prozessphase
  - veroeffentlichter Pfad
  - technischer Bundle-Ort
  - sichtbare Ausgabe
  - Finalisierung
- Gleiche master_agent.md, create.md, check.md und Templates auf diese Begriffe an.

### 4. Wissensbasis entkoppeln

- Die blog_wissensbasis bleibt nuetzlich, soll aber nicht mehr wie ein verdecktes Gate im Standardprozess wirken.
- Halte sie als optionale Anschlusspruefung in der Planung oder als Vorschlag nach BLOG FINAL.
- Entferne jede Formulierung, die Wissensbasis-Bezuege wie einen verbindlichen DoD-Bestandteil aussehen laesst.

### 5. Letzte Restdoppelungen entfernen

- Suche gezielt nach wiederholten Regeltexten zu:
  - Emoji-Abdeckung
  - Sichtbare Zusammenfassung
  - Frontmatter-Vollstaendigkeit
  - Material- oder Quellenuebersichten
- Behalte pro Thema moeglichst nur einen normativen Regelort plus schlanke Verweise.

## Nicht aendern

- keine neue Agentenphase
- keine neue Promptfamilie
- keine inhaltliche Aenderung der Templatestruktur, soweit sie fuer Blog und Reveal gebraucht wird
- keine Aenderung des DQM-Referenzmodells
- keine Aenderung an `README.md`
- keine Aenderung an `ai_agents/blog_wissensbasis.md`
- keine Aenderung an bestehenden Content-Artefakten oder sonstigen Blog-/Reveal-Dateien
- keine neuen Hilfs-, Mapping-, Delta- oder Archivdateien anlegen

## Abnahmekriterien

- Emoji-Detailregeln stehen normativ nur noch in der Emoji-Policy.
- Templates sind sichtbar schlanker und enthalten keine versteckte Prozesslogik.
- Kernbegriffe werden in allen Steuerdateien konsistent verwendet.
- Die Wissensbasis ist nuetzlich, aber kein implizites Pflicht-Gate mehr.
- Die Zahl der wiederholten Regelbloeke ist deutlich reduziert.

## Pruefung nach dem Patch

- Selektiver RC-Durchlauf mindestens mit RC-08, RC-11, RC-12, RC-32, RC-35.
- Diff gezielt auf verschlankte Templates, gekuerzte Emoji-Dopplungen und vereinheitlichte Terminologie pruefen.
- Zusaetzlich explizit pruefen: Der Diff enthaelt nur die sieben Ziel-Dateien. Jede weitere Datei gilt als Scope Drift und ist im Abschluss zu melden.

## Erwartetes Ergebnis

Eine deutlich leichtere, besser wartbare Agentenarchitektur mit klaren Regelorten und weniger kognitischem Overhead.

## Abschlussausgabe des ausfuehrenden Fensters

Am Ende knapp berichten:

- welche Regelorte verschlankt wurden
- welche Begriffe vereinheitlicht wurden
- wie die Wissensbasis jetzt eingebunden ist
- welche RCs geprueft wurden und mit welchem Ergebnis
- ob der Diff scope-sauber geblieben ist; wenn nein, jede Off-scope-Datei einzeln benennen