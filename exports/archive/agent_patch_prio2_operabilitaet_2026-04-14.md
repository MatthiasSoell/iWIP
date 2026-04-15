# Patch Prio 2 - Operabilitaet und Pruefschicht schaerfen

Datum: 2026-04-14
Status: bereit zur Ausfuehrung in separatem Fenster
Reihenfolge: 2 von 3
Voraussetzung: Patch Prio 1 ist bereits eingearbeitet

## Ziel

Reduziere operative Reibung im Einsatz: Profilsteuerung, Finalpruefung und Forschungsmodus sollen klar, priorisiert und ohne unnnoetige Rueckfragen funktionieren.

## Bearbeitungsrahmen

Arbeite primaer in diesen Dateien:

- project_governance/agent_contract.md
- ai_agents/master_agent.md
- prompts/create.md
- prompts/check.md

Andere Dateien nur anfassen, wenn eine direkte Synchronisierung zwingend noetig ist.

Scope-Guard fuer dieses Patchpaket:

- Ziel ist ein **Minimalpatch ohne Scope Drift**.
- `README.md`, `ai_agents/blog_wissensbasis.md`, `ai_agents/didaktisches_qualitaetsmodell.md`, `project_governance/content_emoji_policy.md`, Content-Dateien, Exportdateien und sonstige Repo-Dateien sind fuer dieses Paket **nicht** zu aendern.
- Wenn waehrend der Arbeit sichtbar wird, dass eine gewuenschte Aenderung nur durch zusaetzliche Dateien loesbar waere, ist **nicht** still zu erweitern. Dann die Aenderung im Abschluss als bewusst offener Restpunkt benennen.

## Konkreter Arbeitsauftrag

### 1. Profilsteuerung operationalisieren

- Lege eine eindeutige Default-Regel fest: Wenn kein Profil genannt ist, gilt Profil A.
- Diese Default-Setzung soll im Standardfall genau einmal sichtbar werden, naemlich in der ersten strukturierten Planungszusammenfassung oder gleichwertigen Klarstellung.
- prompts/check.md darf am Ende keine neue Profilrunde erzwingen, wenn Profil A bereits sichtbar oder sauber dokumentiert gesetzt wurde.
- Ein Profilwechsel mitten im Fall bleibt rueckfragepflichtig, aber ohne zweite Parallelregel.

### 2. Pruefschicht priorisieren

- Strukturiere die Finalpruefung in prompts/check.md klar nach Prioritaetsklassen.
- Verwende mindestens diese drei Ebenen:
  - formale Publikationsblocker
  - didaktische Freigabeblocker
  - Hinweise oder Optimierungen
- Definiere die sichtbare Ausgabereihenfolge fuer BLOG FINAL und REVEAL FINAL eindeutig.
- Die sichtbare Blockerliste soll kompakt und priorisiert sein, nicht als ungewichtete Sammlung aller Einzelkriterien.

### 3. create.md auf echte Ablaufsteuerung zurueckbauen

- Entferne in prompts/create.md Detailwiederholungen, die bereits in Contract, Master oder Check normativ geregelt sind.
- Erhalte nur das, was create wirklich steuert:
  - Modusableitung zu Beginn
  - Kontextklaerung
  - Uebergaenge in BLOG FINAL, REVEAL GO, REVEAL FINAL
  - Nutzerinteraktion und Wartepunkte
- Keine erneute Vollbeschreibung der kompletten Prueflogik im Startprompt.

### 4. Forschungsmodus aus dem Standardpfad herausnehmen

- Behalte die vollstaendige Forschungslogik nur dort, wo sie normativ hingehoert.
- In Master und Create nur noch kurze Verweise oder knappe Aktivierungsregeln belassen.
- Vermeide wiederholte Markerlisten, Exportformate und Abschlusslogiken in mehreren Dateien.

### 5. Eine Frage wirklich als eine Frage behandeln

- Harmonisiere die Regeln zu genau einer Klaerungsfrage und nur einer Frage gleichzeitig.
- Vermeide Konstellationen, in denen fehlender Kontext, Profilunklarheit und Finalisierungsunschärfe parallel mehrere Rueckfragen triggern koennen.
- Das System soll sichtbar immer nur die naechste entscheidende Rueckfrage ausgeben.

## Nicht aendern

- keine inhaltliche Aenderung des DQM
- keine neue Statusmeldung einfuehren
- keine neue Artefaktphase bauen
- keine neue Exportstruktur fuer Forschung anlegen
- keine Aenderung an `README.md`
- keine Aenderung an `ai_agents/blog_wissensbasis.md`
- keine Aenderung an `project_governance/content_emoji_policy.md`
- keine Aenderung an bestehenden Content-Artefakten oder sonstigen Blog-/Reveal-Dateien
- keine neuen Hilfs-, Mapping-, Delta- oder Archivdateien anlegen

## Abnahmekriterien

- Profil A fuehrt nicht mehr spaet in der Finalpruefung zu einer zusaetzlichen Rueckfrage, wenn es vorher sauber gesetzt wurde.
- BLOG FINAL und REVEAL FINAL liefern priorisierte, kompakte Pruefausgaben statt ungeordneter Vollstaendigkeitslisten.
- prompts/create.md ist sichtbar schlanker und steuert nur noch den Ablauf.
- Forschungsmodus ist im Standardpfad nicht mehr ueberpraesent.
- Die Ein-Frage-Regel fuehrt operativ nicht mehr zu konkurrierenden Rueckfrageausloesern.

## Pruefung nach dem Patch

- Selektiver RC-Durchlauf mindestens mit RC-20, RC-21, RC-26, RC-30 und RC-33.
- Diff gezielt auf gekuerzte Doppelbeschreibungen in create.md und priorisierte Pruefstruktur in check.md pruefen.
- Zusaetzlich explizit pruefen: Der Diff enthaelt nur die vier Ziel-Dateien oder klar begruendete, vorher benannte Synchronisationsdateien. Jede weitere Datei gilt als Scope Drift.

## Erwartetes Ergebnis

Ein Agent, der in realen Faellen weniger Regelballast sichtbar macht und Finalisierungen besser priorisiert.

## Abschlussausgabe des ausfuehrenden Fensters

Am Ende knapp berichten:

- wie Profil A jetzt sichtbar gesetzt wird
- wie die Prioritaetslogik der Pruefschicht aussieht
- welche Forschungsmodus-Dopplungen entfernt wurden
- welche RCs geprueft wurden und mit welchem Ergebnis
- ob der Diff scope-sauber geblieben ist; wenn nein, jede Off-scope-Datei einzeln benennen