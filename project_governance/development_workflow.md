# Development Workflow – SciBlog iWIP

Kontext: technische Änderungen im Repository (Hugo, CSS, Layout, Docs)  

---

## 0. Kurzregeln

- Modify-first: vorhandene Dateien anpassen, nicht duplizieren.
- Framework-first: Hugo / PaperMod / reveal-hugo Lösungen bevorzugen.
- CSS Owner-Prinzip: jeder Selektor gehört genau einer Datei.
- Farben im Blog nur über Tokens (00_design_tokens.css).
- Reveal verwendet eigene Variablen in custom_reveal.css.
- Blog-CSS und Reveal-CSS strikt getrennt.
- Agentenlogik nach Änderungen direkt gegen die betroffenen Regeln in PLAN-, KDM- und DQM-Core prüfen.
- Testtiefe proportional zum Änderungsrisiko wählen.
- Vor Commits: Diff pruefen; Smoke-Tests nur, wenn die Aenderungsklasse sie erfordert.

## 1. Grundprinzip

- **Änderungen klein halten** (eine Sache pro Änderungspaket).
- **Modify-first**: vorhandene Regeln/Dateien anpassen, bevor neue ergänzt werden.
- **Framework-first**: offizielle Hugo / PaperMod / reveal-hugo Lösungen bevorzugen (keine Hacks).

---

## 2. Branching

Änderungen erfolgen in der Regel **direkt auf dem Branch `main`**.

Da das Repository aktuell von einer Person gepflegt wird, wird kein
Feature-Branch-Workflow verwendet.

Vor größeren Änderungen wird eine **lokale Sicherheitskopie** erstellt
oder ein separater temporärer Branch genutzt.

---

## 3. Änderungen prüfen (Diff)

Vor jedem Commit:

- **Git Diff prüfen** (nur beabsichtigte Änderungen).
- In VS Code: Source Control → Datei anklicken → **Diff** (Side-by-side aktivieren).

---

## 4. Lokal testen (Smoke-Test)

### 4.1 Blog (PaperMod)
- `hugo server`
- Smoke-Test:
  - Light/Dark Toggle
  - OER-Tooltip (Hover + Fokus, nicht geclippt)
  - Help-Overlay öffnen/schließen + Scroll-Lock
  - Footer-Icons (Hover + Focus)
  - Callouts (Tip/Quote/Important/Note)

### 4.2 Präsentation (reveal-hugo)
- Präsentationsseite öffnen (Reveal)
- Smoke-Test:
  - Titlecard / Buttons / Author
  - Callouts (Reveal)
  - K3-Diagramm-Slide
  - Endslide / Endcard
  - Portrait vs Landscape Typografie (wenn vorhanden)

### 4.3 Agenten-Validierung

Wenn Änderungen an folgenden Dateien erfolgen, ist zusätzlich eine direkte Validierung gegen die betroffenen Regeln aus PLAN-, KDM- und DQM-Core erforderlich:

- `project_governance/plan_core.md`
- `project_governance/kdm_core.md`
- `ai_agents/didaktisches_qualitaetsmodell_core.md`
- `ai_agents/master_agent.md`
- `prompts/plan.md`
- `prompts/check.md`
- `ai_agents/templates/blog_template.md`
- `ai_agents/templates/reveal_template.md`

Der PLAN-Core bleibt dabei die normative Quelle fuer Prozess, Routing, Gates und
Lazy Loading; KDM und DQM behalten ihre dort beschriebenen Zustaendigkeiten.
Dieser Workflow regelt nur Tiefe und Form der Validierung.

Ausführungslogik:

- Kleine Text- oder Regelkorrekturen: Diff-Pruefung plus die betroffenen Regeln der aktuellen kanonischen Komponenten.
- Aenderungen an Moduslogik, Uebergaengen, Snapshot-Regeln, Bundle-Hygiene oder DoD: ein geschlossener Dry Run im Standardmodus ueber `/PLAN`, `BLOG GO`, `BLOG FINAL` inklusive automatischem `LITERATUR GO`, `REVEAL GO` -> `REVEAL FINAL`.
- Bei Aenderungen an der Planungsheuristik zusaetzlich offene Planungsstarts und
  konkrete Analyse-, Feedback-, Reflexions-, Review- oder
  Entscheidungshilfeauftraege pruefen. Eine empfohlene Verdichtung bleibt bei
  offenen Planungsstarts fuehrend; vorhandene Planungsstaende werden dagegen
  zuerst im beauftragten Umfang bearbeitet und nicht ungefragt neu geplant.
- Bei Aenderungen an der Wissensbasis-Anschlusslogik zusaetzlich gezielt den Anschluss nach `BLOG FINAL` pruefen, insbesondere Entwurf, Bestaetigungsfrage und Uebernahme erst nach Freigabe.

### 4.4 Proportionale Testtiefe

- Reine Text- oder Formulierungsänderungen an Doku, Prompts oder Regeln: Diff-Prüfung plus betroffene Kernregeln; kein voller Smoke-Test nötig.
- Änderungen an Workflow, Pfaden, Bundles, Frontmatter-Logik oder Renderlogik: betroffene Kernregeln plus technischer Smoke-Test.
- Reveal-, Bundle- oder CSS-Änderungen: zusätzlicher Reveal-Sichttest und Bundle-Prüfung auf unerwünschte Markdown-Dateien.

### 4.5 Dry-Run-Auswertungsvorlage

Der praktische Dry Run prueft die im PLAN-Core definierte Gatefolge.

Fuer diesen Dry Run wird das Ergebnis nicht nur summarisch, sondern als kurzer Auswertungsbogen festgehalten.

Ziel:

- den Testfall stationenweise nachvollziehbar auswerten,
- Regel-, Prompt- und Template-Fehler trennen,
- Folgearbeiten gezielt ableiten.

Pflichtstationen im praktischen Dry Run:

- `/PLAN`
- `BLOG GO`
- `BLOG FINAL`
- `REVEAL GO` -> `REVEAL FINAL`

Die Pflichtstationen werden gegen die Gatefolge im PLAN-Core geprueft. Der
Auswertungsbogen dokumentiert das beobachtete Verhalten je Station mit Verweis
auf die einschlaegige aktuelle Kernregel, statt die Gate-Logik hier erneut
auszuschreiben.

Fuer die Auswertung gilt zusaetzlich: Besondere Aufmerksamkeit erhalten
unbeabsichtigte Artefakterzeugung und Umgehungen der regulaeren Gates.

Pro Station mindestens erfassen:

- welches Verhalten erwartet wurde,
- was tatsächlich passiert ist,
- ob der Schritt bestanden ist,
- welche Abweichung vorliegt,
- wo die Korrektur voraussichtlich hingehoert (PLAN, KDM, DQM, didaktischer Planungsagent, Prompt, Template, Doku).

Kopierbare Vorlage:

```md
## Dry Run – Auswertung

Fall:
Datum:
Bearbeiter:

| Station | Prüfschritt | Erwartetes Verhalten | Tatsächliches Verhalten | Status (OK/Teilweise/Nein) | Abweichung | Folgeort |
|---|---|---|---|---|---|---|
| /PLAN | Keine Artefakterstellung | | | | | |
| /PLAN | Sprache bleibt planungs- und dialoggerecht | | | | | |
| /PLAN | Offener Planungsstart wird verdichtet; konkrete Analyse- oder Feedbackauftraege werden ohne ungefragte Neuplanung bearbeitet | | | | | |
| /PLAN | Keine sichtbaren Such-, Routing-, Tool- oder Prozesskommentare | | | | | |
| BLOG GO | Erzeugt `index.md` auf Basis des freigegebenen Planungsstands | | | | | |
| BLOG FINAL | Kontextlücken führen zu genau einer Rückfrage | | | | | |
| BLOG FINAL | Profilsteuerung A/B/C ist sichtbar korrekt | | | | | |
| BLOG FINAL | Blog-first und Uebergangsdisziplin bleiben intakt | | | | | |
| BLOG FINAL | Dialogstil bleibt didaktisch und adressatenorientiert | | | | | |
| BLOG FINAL | Uploads werden nur als Quellmaterial behandelt | | | | | |
| BLOG FINAL | Buildfreie Inhalts-, DQM-, Frontmatter- und Formalpruefung laeuft vor jeder Transformation | | | | | |
| BLOG FINAL | Automatisches `LITERATUR GO` laeuft als rein formaler Schritt ohne Recherche und vor dem Content-Emoji-Postprocessing | | | | | |
| BLOG FINAL | Content-Emoji-Postprocessing arbeitet fail-closed nur bis zum eindeutigen kanonischen Literaturanker und startet keinen Build | | | | | |
| BLOG FINAL | Genau ein abschliessender Build laeuft nach allen Mutationen; Lychee prueft danach bevorzugt die gebaute HTML-Ausgabe des aktuellen Blogartefakts. Nur ein ausgefuehrter fehlerfreier Lauf gilt als PASS; Nichtverfuegbarkeit wird ohne automatischen FINAL-Blocker dokumentiert, festgestellte relevante interne Linkfehler sind Blocker. | | | | | |
| BLOG FINAL | Nach dem abschliessenden Build erfolgt keine Mutation und kein zweiter vollstaendiger FINAL-Check | | | | | |
| BLOG FINAL | Ein fehlendes Reveal ist weder Blocker noch Warnung; kein toter Praesentationslink wird erzeugt | | | | | |
| BLOG FINAL | Wissensbasis-Hook wird geprueft, blockiert `REVEAL GO` aber nicht | | | | | |
| REVEAL GO -> REVEAL FINAL | Reveal startet erst nach Uebergang/Freigabe | | | | | |
| REVEAL GO -> REVEAL FINAL | Gleichwertige Statusmeldungen werden korrekt interpretiert | | | | | |
| REVEAL GO -> REVEAL FINAL | Buildfreie Ableitungs- und Formalpruefung laeuft ohne vollstaendiges DQM vor dem Emoji-Postprocessing | | | | | |
| REVEAL GO -> REVEAL FINAL | Content-Emoji-Postprocessing startet keinen Build | | | | | |
| REVEAL GO -> REVEAL FINAL | Genau ein abschliessender Build laeuft nach allen Mutationen; Lychee prueft danach bevorzugt die gebaute HTML-Ausgabe des aktuellen Revealartefakts. Nur ein ausgefuehrter fehlerfreier Lauf gilt als PASS; Nichtverfuegbarkeit wird ohne automatischen FINAL-Blocker dokumentiert, festgestellte relevante interne Linkfehler sind Blocker. | | | | | |
| REVEAL GO -> REVEAL FINAL | Nach dem abschliessenden Build erfolgt keine Mutation und kein zweiter vollstaendiger FINAL-Check | | | | | |
| REVEAL GO -> REVEAL FINAL | Abgleich, optionale Materialuebersicht und Finalisierung stimmen | | | | | |

### Kurzfazit

- Staerken:
- Hauptabweichungen:
- Empfohlene Nacharbeit:
```

Faustregel fuer `Folgeort`:

- **PLAN**: Prozess, Routing, Uebergaenge, Gates und Konfliktlogik.
- **KDM**: Dialog-, Interventions- und Entscheidungsform.
- **DQM**: didaktische Qualitaet und Diagnose.
- **Didaktischer Planungsagent**: operative Arbeitslogik, Dialogstil, Statusauswertung.
- **Prompt**: Start-, Check- oder Interaktionssteuerung.
- **Template**: Frontmatter, Artefaktstruktur, Template-Pflichtlogik.
- **Doku**: README oder Workflow erklaert den Stand noch falsch oder unvollstaendig.

---

## 5. Commit-Regel

- Commit-Nachrichten: **kurz, beschreibend, im Imperativ** (englisch oder deutsch – aber konsistent).
- Beispiele:
  - `chore: tidy custom_reveal.css documentation`
  - `fix: prevent tooltip clipping in oer meta`
  - `docs: update css architecture diagram`

Arbeitsprinzip: lieber mehrere kleine Commits als ein großer „Wurf“.

---

## 6. Dokumentation mitpflegen

Wenn du **Architektur, Pfade, Owners oder Regeln** änderst, dann gilt:

- passende Doku aktualisieren (mindestens):
  - `project_governance/css_architecture.md`
  - `project_governance/repo_architecture.md`
  - `project_governance/content_emoji_policy.md`
  - `project_governance/ai_copilot_instructions.md`
  - `project_governance/ai_project_context.md`
  - `project_governance/development_workflow.md`
  - `README.md` (nur wenn es „Entry-Point“-Infos betrifft)

Regel: **Wenn Code sich ändert und die Doku dadurch falsch wäre → Doku mit ändern.**

---

## 7. Merge-Checkliste (kurz)

Vor Merge nach `main`:

- [ ] Diff geprüft (keine unbeabsichtigten Änderungen)
- [ ] Smoke-Test Blog OK
- [ ] Smoke-Test Reveal OK (falls betroffen)
- [ ] Betroffene Kernregeln geprueft; Dry Run durchgefuehrt (falls Agentenlogik betroffen)
- [ ] Doku konsistent (wenn betroffen)
- [ ] keine neuen unkommentierten `!important`
- [ ] keine neuen Hardcoded-Farben außerhalb von Tokens

---

## 8. Zusammenarbeit mit Copilot / AI

- AI soll **diese Dateien** als Leitplanken berücksichtigen:
  - `project_governance/ai_copilot_instructions.md`
  - `project_governance/ai_project_context.md`
  - `project_governance/css_architecture.md`
  - `project_governance/content_emoji_policy.md`
  - `project_governance/repo_architecture.md`
  - `project_governance/development_workflow.md`
- AI-Vorschläge werden **wie Code Reviews** behandelt: übernehmen nur, was du verstehst und getestet hast.
