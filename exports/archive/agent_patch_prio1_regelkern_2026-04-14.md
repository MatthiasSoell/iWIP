# Patch Prio 1 - Regelkern konsolidieren

Datum: 2026-04-14
Status: bereit zur Ausfuehrung in separatem Fenster
Reihenfolge: 1 von 3
Voraussetzung: keine

## Ziel

Bereinige die widerspruechlichen Kernregeln der Agentenarchitektur, damit Workflow, Sichtbarkeit, Routing und Literaturlogik wieder deterministisch sind. Dieser Patch ist die Grundlage fuer alle spaeteren Bereinigungen.

## Bearbeitungsrahmen

Arbeite nur in diesen Dateien:

- project_governance/agent_contract.md
- ai_agents/master_agent.md
- prompts/create.md
- prompts/check.md
- prompts/literatur.md
- ai_agents/templates/blog_template.md
- ai_agents/templates/reveal_template.md

Lies zusaetzlich config.toml nur zur Klaerung der kanonischen Site-Basis, falls die Pfadkonvention davon abhaengt.

## Konkreter Arbeitsauftrag

### 1. Single Source of Truth festziehen

- project_governance/agent_contract.md ist die einzige normative Quelle fuer:
  - Arbeitsmodus
  - Statusmeldungen
  - Sichtbarkeitslogik
  - Routing
  - Snapshot-Grundregeln
  - Forschungsmodus-Grundregeln
- ai_agents/master_agent.md darf diese Regeln nur noch operativ verkuerzt referenzieren und konkretisieren, aber nicht noch einmal vollstaendig parallel definieren.
- prompts/create.md steuert nur Start, Uebergaenge und Nutzerinteraktion.
- prompts/check.md steuert nur Pruefungen und sichtbare Finalausgaben.
- Templates enthalten nur Struktur, Pflichtbloecke und artefaktnahe Beispiele.

### 2. Master-Agent hart konsolidieren

- Bereinige ai_agents/master_agent.md so, dass kein spaeterer Altblock mit zweitem Workflow, zweiter DoD-Logik oder eigener Chat-Reflexionslogik stehen bleibt.
- Pruefe insbesondere den spaeteren Block ab Standardverhalten bis Abgrenzung auf Doppelregeln und entferne oder integriere alles, was bereits im oberen Regelkern oder im Contract geregelt ist.
- Entferne insbesondere konkurrierende oder problematische Spaetregeln zu:
  - sichtbaren Selbstcheck-Fragen im Chat
  - optionaler Meta-Reflexion als Standardbestandteil
  - empfohlener OER-Standardpfade
  - Literatur-Agent-Abgrenzung, soweit sie der BLOG-FINAL-Literaturpflege widerspricht

### 3. Routing konsistent machen

- Vereinheitliche Contract, Master-Agent, Check und Templates auf genau eine sichtbare Pfadkonvention.
- Es darf keine Mischung mehr geben aus:
  - technischem Bundle-Ort
  - veroeffentlichtem Pfad ohne Site-Basis
  - veroeffentlichtem Pfad mit harter /iWIP-Vorsilbe
- Wenn config.toml eine eindeutige Site-Basis vorgibt, synchronisiere alle Beispiele, Buttonpfade, Alias-Beispiele und Pruefregeln darauf.
- Der Sonderfall widi muss mit derselben Konvention gefuehrt werden.

### 4. Sichtbarkeitslogik bereinigen

- Low-noise aus dem Contract darf nicht mehr durch sichtbare Selbstchecks, Meta-Reflexion oder Snapshot-Reflexionsprompts unterlaufen werden.
- Snapshot-Vergleiche nach BLOG FINAL oder REVEAL FINAL duerfen nicht mehr als Standardausgabe formuliert sein.
- Materialuebersicht bei REVEAL FINAL bleibt optional und darf nur dann sichtbar verlangt werden, wenn mehrere Dateien, Quellen oder Zielpfade tatsaechlich abgestimmt werden muessen.

### 5. Literaturlogik synchronisieren

- Stelle klar: keine Quellenneuerfindung, aber formale Literatur-Nachbearbeitung ist erlaubt.
- ai_agents/master_agent.md darf der in prompts/create.md und prompts/literatur.md vorgesehenen Literaturpflege nicht mehr widersprechen.
- Erhalte die Trennung: inhaltliche Quellenaussagen nicht erfinden, formale Normalisierung und Linksetzung aber zulassen.

## Nicht aendern

- keine Umgewichtung des DQM
- keine inhaltliche Aenderung der Profile A/B/C
- keine neue Forschungslogik
- keine neuen Prompts oder neuen Governance-Dateien anlegen, wenn die Bereinigung in Bestandsdateien moeglich ist

## Abnahmekriterien

- Es existiert nur noch ein konsistenter Regelpfad fuer Workflow, Sichtbarkeit, Routing und Literaturlogik.
- ai_agents/master_agent.md enthaelt keinen zweiten konkurrierenden Operativblock mehr.
- BLOG FINAL, REVEAL GO und REVEAL FINAL sind in Contract, Master, Create und Check widerspruchsfrei.
- Templates enthalten keine versteckte Prozess- oder Routinglogik mehr, die dem Contract widerspricht.
- Literaturnormalisierung ist erlaubt, Quellenneuerfindung bleibt verboten.

## Pruefung nach dem Patch

- Selektiver RC-Durchlauf mindestens mit RC-07, RC-08, RC-18, RC-24, RC-30, RC-31 und RC-34.
- Diff gezielt auf entfernte Doppelregeln und vereinheitlichte Pfadbeispiele pruefen.

## Erwartetes Ergebnis

Ein stabiler Regelkern ohne doppelte Workflow- und Sichtbarkeitssteuerung.

## Abschlussausgabe des ausfuehrenden Fensters

Am Ende knapp berichten:

- welche Dateien geaendert wurden
- welche Regelentscheidung fuer die Pfadkonvention getroffen wurde
- welche Konflikte entfernt wurden
- welche RCs geprueft wurden und mit welchem Ergebnis