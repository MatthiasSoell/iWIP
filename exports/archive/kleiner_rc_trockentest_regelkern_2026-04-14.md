# Kleiner RC-Trockentest – Regelkern nach Prio 1

Datum: 2026-04-14
Bearbeiter: GitHub Copilot
Typ: regelbasierter Kleintrockentest gegen den aktuellen Steuerstand
Tiefe: Desk-Check der Steuerdateien, kein ersetzender Live-Fall

## Grundlage

Geprueft wurden:

- `project_governance/agent_contract.md`
- `ai_agents/master_agent.md`
- `prompts/create.md`
- `prompts/check.md`
- `prompts/literatur.md`
- `ai_agents/templates/blog_template.md`
- `ai_agents/templates/reveal_template.md`
- `project_governance/development_workflow.md`

Fokus-RCs:

- `RC-07`
- `RC-08`
- `RC-18`
- `RC-24`
- `RC-30`
- `RC-31`
- `RC-34`

Mitgepruefte Stuetzkriterien:

- `RC-20`
- `RC-21`
- `RC-27`
- `RC-29`
- `RC-33`

## Vorbedingungen

- Frischer Dialog fuer Meta-Arbeit verwendet: nein, Desk-Check
- Frischer Dialog fuer Artefaktlauf verwendet: nein, Desk-Check
- Keine Uploads verwendet: ja
- Bundle-Hygiene vor dem Start geprueft: ja, regelbasiert
- Optionales Export-Aufraeumen vor dem Start vorgenommen: nein

## Stationsauswertung

| Station | Prüfschritt | Erwartetes Verhalten | Tatsächliches Verhalten | Status (OK/Teilweise/Nein) | Abweichung | Folgeort |
|---|---|---|---|---|---|---|
| Meta-Arbeit am Agenten | Keine Artefakterstellung | Meta-Arbeit bleibt artefaktfrei | Contract und Create trennen `Meta-Arbeit am Agenten` klar von `Artefakt-Arbeit`; fuer Meta-Arbeit sind keine Artefakte vorgesehen. | OK | keine | Contract, Prompt |
| Meta-Arbeit am Agenten | Sprache bleibt meta- und reviewgerecht | Meta-Modus bleibt reviewnah statt artefaktgetrieben | Der Regelstand priorisiert im Meta-Modus Analyse, Review und Regelarbeit; kein konkurrierender Artefaktblock im Master mehr vorhanden. | OK | keine | Contract, Master-Agent |
| BLOG FINAL | Kontextlücken führen zu genau einer Rückfrage | Eine klaerende Rueckfrage, dann Stopp vor Artefakterstellung | Contract, Master und Create nennen konsistent genau eine Klaerungsfrage bei Kernluecken oder Mehrdeutigkeit. | OK | keine | Contract, Master-Agent, Prompt |
| BLOG FINAL | Profilsteuerung A/B/C ist sichtbar korrekt | Profil A als Default, nur bei klaren Signalen aktive Klaerung | Create und Master fuehren Profil A als Default und beschraenken aktive Profilnachfrage auf klare Kontextsignale. | OK | keine | Master-Agent, Prompt |
| BLOG FINAL | Blog-first und Uebergangsdisziplin bleiben intakt | Erst Blog, dann Reveal | Contract, Master und Create halten `blog_snapshot.txt` -> `index.md` -> `REVEAL GO` -> `_index.md` konsistent. | OK | keine | Contract, Master-Agent, Prompt |
| BLOG FINAL | Dialogstil bleibt didaktisch und adressatenorientiert | Keine prozessnahe Standardsprache | Contract und Create verbieten sichtbare Prozesssaetze; Master fuehrt fachliche Einordnung oder naechste sinnvolle Arbeitsfrage als Leitform. | OK | keine | Contract, Master-Agent, Prompt |
| BLOG FINAL | Uploads werden nur als Quellmaterial behandelt | Uploads loesen ohne Freigabe keine Reveal-Erzeugung aus | Contract, Master und Create behandeln Uploads konsistent als Quellmaterial bis `REVEAL GO` oder gleichwertiger Freigabe. | OK | keine | Contract, Master-Agent, Prompt |
| BLOG FINAL | Mindestpruefungen und sichtbare Zusammenfassung greifen korrekt | DQM-Pruefbericht, formale Freigabe/Blocker, Zusammenfassung | Check und Contract definieren die sichtbare Reihenfolge klar; das Summary-Schema ist im Master konsolidiert. | OK | keine | Contract, Master-Agent, Prompt |
| REVEAL GO -> REVEAL FINAL | Reveal startet erst nach Übergang/Freigabe | `_index.md` erst nach `REVEAL GO`, Finalisierung erst nach `REVEAL FINAL` | Der Regelstand trennt Arbeitsphase und Finalisierung durchgaengig und ohne Restkonflikte. | OK | keine | Contract, Master-Agent, Prompt |
| REVEAL GO -> REVEAL FINAL | Gleichwertige Statusmeldungen werden korrekt interpretiert | Natuerliche Freigaben mappen robust auf Standardstatus | Contract und Create nennen gleichwertige Formulierungen explizit; bei Mehrdeutigkeit ist genau eine Rueckfrage vorgesehen. | OK | keine | Contract, Prompt |
| REVEAL GO -> REVEAL FINAL | Snapshot- und Bundle-Hygiene bleiben sauber | nur `.txt`-Snapshots, keine rendernden Altdateien | Contract und Create definieren `blog_snapshot.txt` und `reveal_snapshot.txt` als nicht-operativ; Bundle-Hygiene wird nicht mehr durch Altlogik unterlaufen. | OK | keine | Contract, Prompt |
| REVEAL GO -> REVEAL FINAL | Abgleich, optionale Materialübersicht und Finalisierung stimmen | Abgleich verpflichtend, Materialuebersicht nur bei Bedarf | Check, Master und Contract ziehen dieselbe Logik: Abgleich verpflichtend, Materialuebersicht optional aber tabellarisch, wenn sichtbar ausgegeben. | OK | keine | Contract, Master-Agent, Prompt |

## Sichtpruefung der Exportartefakte

| Artefakt | Erwartung | Ergebnis | Anmerkung |
|---|---|---|---|
| separates Forschungsprotokoll in `exports/` | nur in `FORSCHUNG START` aktiv, mit schlanken Markern und verifizierbaren Metadaten | OK | Contract definiert Aktivierung, Markerformat und Abschluss sauber und ohne konkurrierende Zweitlogik. |
| sichtbares Forschungs-Transkript in `exports/` | nur sichtbare finale Turns, keine Tool- oder Metaspuren | OK | Contract definiert append-only Sichttranskript mit expliziter Negativliste; kein Restkonflikt in Master oder Prompts gefunden. |

## RC-Kurzbewertung

| RC | Ergebnis | Kurzbefund |
|---|---|---|
| RC-07 | OK | Contract bleibt klar Fuehrungsdokument; Master und Prompts uebersteuern ihn nicht mehr. |
| RC-08 | OK | Summary-Schema ist vereinheitlicht; sichtbare Zusammenfassungen sind sauber begrenzt. |
| RC-18 | OK | `REVEAL GO` und `REVEAL FINAL` sind getrennt und widerspruchsfrei beschrieben. |
| RC-24 | OK | Blog bleibt ueberall Primaerartefakt. |
| RC-30 | OK | Gleichwertige Statusmeldungen sind konsistent geregelt. |
| RC-31 | OK | Low-noise ist nicht mehr durch sichtbare Selbstchecks oder Meta-Reflexion unterlaufen. |
| RC-34 | OK | Sichtbare Pfade folgen durchgaengig `/iWIP/...`; der `widi`-Sonderfall ist konsistent. |

## Kurzfazit

- Staerken: Der Regelkern ist jetzt deutlich eindeutiger geschichtet; Finalausgaben, Routing und Uebergaenge sind konsistent beschrieben; alte Parallelregeln im Master sind entfernt.
- Hauptabweichungen: Keine in den geprueften Fokus-RCs. Rest-Risiko bleibt nur, dass dies noch kein echter Lauf mit Artefakterzeugung ist.
- Empfohlene Nacharbeit: Vor dem naechsten Live-Fall einen schmalen echten Repo-Fall durchspielen, damit die regelbasische Konsistenz auch im Dialogverhalten und in den Artefaktpfaden praktisch bestaetigt wird.

## Go/No-Go

- Vor naechstem Live-Fall freigabefaehig: ja, mit dem ueblichen Hinweis auf einen anschliessenden schmalen Realfall
- Begruendung: Der kleine Trockentest zeigt keine verbleibenden Regelkonflikte in den geaenderten Steuerdateien; die Fokus-RCs sind im aktuellen Stand konsistent abgedeckt.