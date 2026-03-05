# Development Workflow – SciBlog iWIP

Version: 1.0.0  
Scope: technische Änderungen im Repository (Hugo, CSS, Layout, Docs)  
Status: verbindliche Projektregel

---

## 0. Kurzregeln

- Modify-first: vorhandene Dateien anpassen, nicht duplizieren.
- Framework-first: Hugo / PaperMod / reveal-hugo Lösungen bevorzugen.
- CSS Owner-Prinzip: jeder Selektor gehört genau einer Datei.
- Farben im Blog nur über Tokens (00_design_tokens.css).
- Reveal verwendet eigene Variablen in custom_reveal.css.
- Blog-CSS und Reveal-CSS strikt getrennt.
- Vor Änderungen: Diff prüfen und Smoke-Test durchführen.

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
- [ ] Doku konsistent (wenn betroffen)
- [ ] keine neuen unkommentierten `!important`
- [ ] keine neuen Hardcoded-Farben außerhalb von Tokens

---

## 8. Zusammenarbeit mit Copilot / AI

- AI soll **diese Dateien** als Leitplanken berücksichtigen:
  - `project_governance/ai_copilot_instructions.md`
  - `project_governance/ai_project_context.md`
  - `project_governance/css_architecture.md`
  - `project_governance/repo_architecture.md`
  - `project_governance/development_workflow.md`
- AI-Vorschläge werden **wie Code Reviews** behandelt: übernehmen nur, was du verstehst und getestet hast.
