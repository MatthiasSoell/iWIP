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

Die Arbeit des Agenten basiert auf einem didaktischen Qualitätsmodell (DQM), das als didaktisches Referenzmodell fuer Planung und Ausarbeitung dient.

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

Die wichtigsten Dateien und Ordner fuer den Agenten sind:

| Datei oder Bereich | Rolle |
|---|---|
| `project_governance/agent_contract.md` | einzige verbindliche Regelquelle fuer State Machine, Gates, Guards, Hooks, Exit-Actions, Finalisierung und Sichtbarkeit |
| `ai_agents/master_agent.md` | didaktische Fuehrung, Dialoghaltung und Textarbeit innerhalb des Contracts |
| `prompts/plan.md` | Einstieg und Routing fuer den Planungsdialog |
| `prompts/check.md` | Pruefablauf und Ausgabeformat fuer Finalpruefungen |
| `ai_agents/templates/` | Vorlagen fuer Blog- und Reveal-Artefakte |

## Nutzung

Der Einstieg erfolgt in der Regel ueber die Prompts im Ordner `prompts/`, insbesondere ueber `prompts/plan.md` fuer den Planungsdialog und `prompts/check.md` fuer Finalpruefungen.

Die konkrete Befehlskette, alle Statusmeldungen und die Gate-Logik bleiben im Contract dokumentiert. Diese README fasst nur den Arbeitszusammenhang zusammen: Aus einem Planungsanliegen entsteht schrittweise ein Blogbeitrag; wenn gewuenscht, wird daraus anschliessend eine Praesentation abgeleitet.

## Version

Version: 1.0

## Lizenzhinweis

Der didaktische Agent steht unter der Lizenz **CC BY-SA 4.0**. Details sind in `ai_agents/LICENSE.md` dokumentiert.