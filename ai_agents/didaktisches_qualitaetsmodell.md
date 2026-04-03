# Didaktisches Qualitätsmodell (DQM) – SciBlog iWIP

Referenzdokument für den Master-Agent.
Das DQM steuert die didaktische Strukturierung, die profilabhängige Planung,
den Kohärenzcheck und die abschließende Qualitätsprüfung.

## Nutzungsprinzipien

1. **Vorrang des DQM**: Das DQM hat Vorrang vor der Blog-Wissensbasis.
   Die Wissensbasis dient der inhaltlichen Konsistenz und Anschlussfähigkeit;
   das DQM steuert die didaktische Qualität normativ.
   Bestehende Blogartikel dürfen nicht unkritisch reproduziert werden,
   wenn sie DQM-Kriterien nicht erfüllen.

2. **Diagnose als Heuristik**: Wenn der Agent Lernhürden, Vorwissensdefizite
   oder typische Schwierigkeiten benennt, formuliert er diese als plausible
   Annahmen („Lernende könnten Schwierigkeiten haben mit…"), nicht als
   deterministische Aussagen. Ziel: didaktische Sensibilität ohne Scheinsicherheit.

3. **Mindeststandard**: Auch bei niedrig gewichteten Dimensionen prüft der Agent
   einen Mindeststandard. Keine Dimension darf vollständig ignoriert werden;
   der Mindeststandard ist ⚠️ (teilweise), nicht ❌ (fehlt).

---

## Leitdimensionen

### 1. 🎯 Zielorientierung

Lernziele sind kompetenzorientiert formuliert und an den Kontext angepasst.

Prüffragen:
- Sind die Lernziele als beobachtbare Handlungen formuliert (nicht nur „kennen" oder „wissen")?
- Passen die Lernziele zum Niveau der Zielgruppe (Bachelor vs. Master, Lehrkräftefortbildung, Sek I vs. Sek II)?
- Ist das Anforderungsniveau transparent (Anderson & Krathwohl: Erinnern → Schaffen)?

Typische Schwächen: Zu vage Ziele, Niveauangabe fehlt, Ziele nicht zur Zielgruppe passend.

### 2. 🧭 Strukturierung

Der Lehr-Lern-Prozess ist schlüssig sequenziert und zeitlich realistisch.

Prüffragen:
- Folgt der Verlauf einer erkennbaren didaktischen Logik (z. B. Einstieg → Erarbeitung → Sicherung → Transfer)?
- Ist der Zeitrahmen realistisch (keine Überfrachtung)?
- Gibt es klare Übergänge zwischen den Phasen?

Typische Schwächen: Überfrachtung, fehlende Sicherungsphase, unrealistische Zeitplanung.

### 3. 🧠 Lernverständnis

Das zugrunde liegende Lernverständnis ist erkennbar und konsistent umgesetzt.

Prüffragen:
- Ist das Verhältnis von Lehrenden- und Lernendenaktivität bewusst gestaltet?
- Fördern die Aktivitäten Kompetenzerleben, Autonomieerleben und soziale Eingebundenheit der Lernenden (Deci & Ryan, SDT)?
- Durchlaufen die Lernenden eine vollständige Handlung (Planen → Durchführen → Kontrollieren → Bewerten)?
- Auf welcher Problemorientierungsstufe arbeiten die Lernenden (Schema anwenden → erweitern → neu konstruieren)?
- In welchen Phasen arbeiten die Lernenden eigenständig (ohne KI)? Wo kann KI unterstützen?

Typische Schwächen: Implizites Lernverständnis, Widerspruch zwischen formuliertem Anspruch und Methodenwahl.

### 4. 👥 Lernqualität

Die kognitive Tiefe und Vielfalt der Lernprozesse ist angemessen.

Prüffragen:
- Gehen die Aufgaben über Reproduktion hinaus (Erklären, Vergleichen, Begründen, Bewerten)?
- Wird Wissen in unterschiedlichen Kontexten angewendet (Transfer)?
- Gibt es Aufgaben, die kooperatives Arbeiten erfordern?
- Ist Constructive Alignment erkennbar (Lernziele ↔ Aktivitäten ↔ Assessment)?

Typische Schwächen: Nur Surface Learning, fehlender Transfer, Assessment passt nicht zu Zielen.

### 5. 🪞 Reflexion

Reflexionsphasen sind eingeplant und methodisch verankert.

Prüffragen:
- Gibt es explizite Reflexionsanlässe für Lernende (nicht nur Zusammenfassung)?
- Enthält die Planung formative Feedbackelemente für die Lernenden (Feed-up / Feed-back / Feed-forward nach Hattie & Timperley)?
- Wird das ALACT-Modell oder ein vergleichbarer Reflexionszyklus genutzt?

Typische Schwächen: Reflexion vergessen oder nur als Alibi, kein formatives Feedback.

### 6. 🌱 Adaptivität

Die Planung berücksichtigt Heterogenität und ermöglicht Anpassung.

Prüffragen:
- Gibt es Differenzierungsoptionen (Niveau, Tempo, Zugang)?
- Ist die Planung an unterschiedliche Kontexte anpassbar?
- Ist die KI-Rolle im Lernprozess bewusst gestaltet (wo KI-gestützt, wo eigenständig, wo der Mensch überlegen)?

Typische Schwächen: Einheitsgröße für alle, keine Differenzierung, KI-Rolle nicht reflektiert.

---

## Didaktische Profile

### Profil A – Integrativ-kompetenzorientiert (Default)

**Grundlogik**: Lehrende strukturieren den Lernprozess, Lernende arbeiten aktiv und kompetenzorientiert.

**Ziel**: Aufbau von Fach- und Handlungskompetenz durch angeleitete, aber aktive Auseinandersetzung.

**Gewichtung im DQM**:

| Dimension | Gewichtung |
|---|---|
| 🎯 Zielorientierung | hoch |
| 🧭 Strukturierung | hoch |
| 🧠 Lernverständnis | mittel |
| 👥 Lernqualität | hoch |
| 🪞 Reflexion | mittel |
| 🌱 Adaptivität | mittel |

**Charakteristika im Agenten**:
- klare Lernziele und Alignment
- strukturierter Ablauf mit Aktivierungsphasen
- Aufgaben verbinden Verständnis und Anwendung
- Scaffolding vorhanden
- Reflexion punktuell integriert

**Typische Formate**: strukturierte Fallarbeit, angeleitete Problemlösung, kombinierte Input- und Aktivphasen

### Profil B – Handlungsorientiert-konstruktivistisch

**Grundlogik**: Lernen erfolgt durch eigenständige Bearbeitung komplexer Probleme in sozialen und situativen Kontexten.

**Ziel**: Entwicklung von Handlungskompetenz, Urteilsfähigkeit und reflexiver Praxis.

**Gewichtung im DQM**:

| Dimension | Gewichtung |
|---|---|
| 🎯 Zielorientierung | mittel |
| 🧭 Strukturierung | mittel |
| 🧠 Lernverständnis | sehr hoch |
| 👥 Lernqualität | hoch |
| 🪞 Reflexion | sehr hoch |
| 🌱 Adaptivität | hoch |

**Charakteristika im Agenten**:
- Einstieg über Problem oder Situation
- offene Aufgaben mit Entscheidungsspielräumen
- kooperative Arbeitsformen
- mehrere Lösungswege möglich
- Reflexion integraler Bestandteil

**Typische Formate**: Fallarbeit/Szenarien, Projekte, Gruppenarbeit, diskursive Aufgaben

### Profil C – Instruktional-kognitivistisch

**Grundlogik**: Lernen erfolgt durch klare Strukturierung, gezielte Instruktion und schrittweisen Wissensaufbau.

**Ziel**: Aufbau von strukturiertem Wissen und kognitiven Schemata.

**Gewichtung im DQM**:

| Dimension | Gewichtung |
|---|---|
| 🎯 Zielorientierung | sehr hoch |
| 🧭 Strukturierung | sehr hoch |
| 🧠 Lernverständnis | niedrig |
| 👥 Lernqualität | mittel |
| 🪞 Reflexion | niedrig |
| 🌱 Adaptivität | mittel |

**Charakteristika im Agenten**:
- klare Abfolge von Input, Übung, Sicherung
- starke Führung durch Lehrperson
- reduzierte Komplexität
- schrittweise Aufgaben
- Fokus auf Verständnisaufbau

**Typische Formate**: strukturierter Input, Übungsphasen, gelenkte Aufgaben, Sicherungsphasen

### Profilregel

Das gewählte Profil bestimmt:
- Gewichtung der DQM-Dimensionen
- Struktur des Unterrichts
- Art der Aufgaben
- Rolle der Lernenden

Der Agent flaggt inkonsistente Mischformen und fragt nach,
lässt aber bewusstes Mischen nach Begründung zu.

Profilwechsel wird explizit gemacht und begründet.

---

## Querschnittsprinzipien

Diese Prinzipien gelten dimensionsübergreifend:

1. **Wissenschaftliche Fundierung**: Planungen basieren auf belastbaren Modellen und Befunden, nicht auf Mythen (z. B. Lerntypen).
2. **Lebenswelt- und Berufsbezug**: Inhalte und Aufgaben haben erkennbaren Bezug zur Lebens- und Arbeitswelt der Lernenden.
3. **Nachhaltigkeit und Offenheit**: Materialien werden unter offener Lizenz erstellt (OER), Formate sind nachhaltig.
4. **Konstruktive Fehlerkultur**: Fehler sind Lernanlässe, nicht Defizite.
5. **Medien- und Methodenbewusstheit**: Methoden- und Medienwahl ist begründet, nicht beliebig.

---

## Kompakte Prüfmatrix

| Dimension | Pflichtprüfung | ✅ erfüllt | ⚠️ teilweise | ❌ fehlt |
|---|---|---|---|---|
| 🎯 Zielorientierung | Kompetenz-Lernziele formuliert? | Beobachtbar + niveaupassend | Vorhanden, aber vage | Fehlt oder nur „kennen/wissen" |
| 🧭 Strukturierung | Phasenlogik + Zeitrahmen? | Schlüssig + realistisch | Logik erkennbar, Zeit unklar | Keine Phasenstruktur |
| 🧠 Lernverständnis | Lernenden-Aktivität geplant? | SDT-Kriterien adressiert | Aktivität ja, aber ohne Begründung | Rein rezeptiv |
| 👥 Lernqualität | Über Reproduktion hinaus? | Transfer + Alignment | Tiefe stellenweise | Nur Reproduktion |
| 🪞 Reflexion | Reflexionsanlass vorhanden? | Feed-up/back/forward | Zusammenfassung vorhanden | Keine Reflexion |
| 🌱 Adaptivität | Differenzierung möglich? | Mehrere Zugänge | Eine Alternative | Keine Differenzierung |

Mindeststandard: Keine Dimension darf ❌ sein, auch nicht bei niedriger Profilgewichtung.
Bei ❌ in einer Pflichtdimension ist Rückfrage verpflichtend; Finalisierung erst nach Klärung.

Die Prüfmatrix wird vor `BLOG FINAL` als DQM-Prüfbericht ausgegeben.
