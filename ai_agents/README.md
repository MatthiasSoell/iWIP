# Didaktischer Planungsagent im SciBlog iWIP

Der didaktische Planungsagent ist ein unterstützendes System für die Planung, Strukturierung und publizistische Ausarbeitung von Lehr-Lern-Inhalten im SciBlog iWIP. Er ist Teil des Projekts, aber kein eigenständiges Automatisierungssystem.

## Ziel des Agenten

Der Agent unterstützt die didaktische Arbeit vom ersten Planungsstand bis zur veröffentlichungsfähigen Ausarbeitung. Der zentrale Arbeitszusammenhang lautet:

**Planung → Blog → Präsentation**

Damit hilft der Agent insbesondere dabei,

- didaktische Vorhaben zu klären und zu strukturieren
- Blogbeiträge als fachlich und didaktisch tragfähige Arbeitsdokumente zu entwickeln
- aus finalen Blogbeiträgen Präsentationen abzuleiten

## Grundprinzip

Der Blog ist das zentrale Arbeitsdokument. Hier werden Inhalte ausgearbeitet, didaktisch geordnet und in eine Form gebracht, die sowohl für Lehre als auch für Veröffentlichung geeignet ist.

Die Präsentation entsteht nicht unabhängig davon, sondern wird aus dem finalen Blogbeitrag abgeleitet. Dadurch bleibt der Prozess klar: zuerst inhaltliche und didaktische Arbeit, dann eine mögliche Verdichtung für den Präsentationskontext.

## Funktionsweise

Der Agent arbeitet dialogisch, strukturierend und unterstützend.

- dialogisch, weil die Ausarbeitung im Austausch mit den Nutzenden erfolgt
- strukturierend, weil der Agent Ziele, Inhalte und Arbeitsstände ordnet
- unterstützend, weil er Vorschläge macht, aber keine didaktischen Entscheidungen ersetzt

Der Agent ist damit bewusst als Human-in-the-Loop-System angelegt.

## (Fach-)Didaktische Grundlage

Die Arbeit des Agenten basiert auf einem didaktischen Qualitätsmodell (DQM), das als normative Orientierung für Planung und Ausarbeitung dient. 

Ziel ist es, Lehr-Lern-Prozesse nicht nur formal zu strukturieren, sondern inhaltlich begründet und lernförderlich zu gestalten. Der Agent orientiert sich dabei insbesondere an zentralen didaktischen Dimensionen wie Zielorientierung, Strukturierung, Lernverständnis, Lernqualität, Reflexion und Adaptivität. 

Gleichzeitig ist der Agent fachlich im Sinne der Wirtschaftsdidaktik gerahmt. Er berücksichtigt ökonomische Inhalte nicht nur als Gegenstand, sondern als spezifische Perspektive auf gesellschaftliche, institutionelle und individuelle Handlungszusammenhänge. Damit zielt er auf die Förderung professioneller und beruflicher Handlungskompetenz sowie auf die reflexive Auseinandersetzung mit wirtschaftlichen Entscheidungen und deren Bedingungen.

Diese Perspektive verpflichtet den Agenten dazu, Vorschläge nicht nur technisch oder formal zu generieren, sondern (fach-)didaktisch zu begründen und auf ihre Qualität hin zu reflektieren. Planung wird damit als nachvollziehbarer, argumentativer Prozess verstanden – nicht als rein schematische Ableitung.

## Wofür der Agent gedacht ist

Der Agent ist insbesondere gedacht für:

- die Planung von Lehrveranstaltungen, Lerneinheiten und Fortbildungen
- die Entwicklung und Überarbeitung von Blogbeiträgen
- die Ableitung von Präsentationen aus einem finalen Blogbeitrag

## Was der Agent nicht ist

Der Agent ist

- kein Automatisierungs-Tool für vollständig selbstständige Materialproduktion; Planung entsteht bewusst als schrittweiser, iterativer, reflektierter Prozess und nicht als auf Knopfdruck erzeugte Lösung
- kein Ersatz für didaktische Entscheidungen, fachliche Verantwortung oder redaktionelle Prüfung

Er unterstützt die Arbeit, steuert sie aber nicht anstelle der Lehrenden oder Autor:innen.

## Zentrale Dateien

Die wichtigsten Dateien und Ordner für den Agenten sind:

- `ai_agents/master_agent.md` – beschreibt Rolle, Arbeitsfokus und didaktische Grundausrichtung
- `project_governance/agent_contract.md` – enthält die verbindliche Steuer- und Prozesslogik
- `prompts/` – Einstiegspunkte für typische Arbeits- und Prüfprozesse
- `ai_agents/templates/` – Vorlagen für Blog- und Reveal-Artefakte

## Nutzung

Der Einstieg erfolgt in der Regel über die Prompts im Ordner `prompts/`, insbesondere über `prompts/plan.md` für den Planungsdialog und `prompts/check.md` für Finalpruefungen.

Die dokumentierte Befehlskette lautet:

- `/PLAN` startet den Planungsdialog, sichtet vorhandenen Kontext und erzeugt keine Dateien.
- `/PLAN FORSCHUNG` startet denselben Planungsdialog mit zusaetzlichem Forschungs-/Rohdatenmodus.
- `BLOG GO` erzeugt `index.md` aus einem freigegebenen oder explizit benannten Planungsstand.
- `BLOG FINAL` prueft und finalisiert den Blog.
- `REVEAL GO` erzeugt `_index.md` ausschliesslich aus dem finalen Blog.
- `REVEAL FINAL` prueft und finalisiert die Praesentation; nach Start mit `/PLAN FORSCHUNG` schliesst es zusaetzlich aktive Forschungsartefakte ab.

Die Nutzung ist als dialogischer Prozess angelegt: Aus einem Planungsanliegen entsteht schrittweise ein Blogbeitrag; wenn gewuenscht, wird daraus anschliessend eine Praesentation abgeleitet.

## Version

Version: 1.0

## Lizenzhinweis

Der didaktische Agent steht unter der Lizenz **CC BY-SA 4.0**. Details sind in `ai_agents/LICENSE.md` dokumentiert.