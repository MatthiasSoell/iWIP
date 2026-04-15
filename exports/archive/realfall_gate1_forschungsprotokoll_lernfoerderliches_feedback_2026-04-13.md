# Forschungsprotokoll - Testlauf lernfoerderliches Feedback

Datengrundlage: sichtbarer Dialogverlauf inklusive eingeblendeter Gespraechszusammenfassung. Nicht einzeln sichtbare oder nur indirekt rekonstruierbare Turnfolgen werden nicht geschaetzt.

## Planungsstart

- Datum: 2026-04-13
- Uhrzeit: nicht verlaesslich verfuegbar
- Startsignal: `PLAN START`
- Gegenstand: 45-minuetige Sitzung fuer Masterstudierende im Lehramt zum Thema lernfoerderliches Feedback im Unterricht

## Zeitpunkte zentraler Uebergaenge und Finalisierungen

- 2026-04-13, Uhrzeit nicht verlaesslich verfuegbar: Planungsstart fuer die Sitzung.
- 2026-04-13, Uhrzeit nicht verlaesslich verfuegbar: eine sichtbare Assistenten-Rueckfrage zu didaktischem Profil und Raumsetup; darauf eine sichtbare Nutzerantwort mit Profil A, ca. 20 Teilnehmenden, Seminarraum mit Beamer.
- 2026-04-13, Uhrzeit nicht verlaesslich verfuegbar: BLOG-Finalisierung angefordert.
- 2026-04-13, Uhrzeit nicht verlaesslich verfuegbar: Blog finalisiert.
- 2026-04-13, Uhrzeit nicht verlaesslich verfuegbar: Uebergang zu Wissensbasis-Uebernahme und Reveal-Ableitung angefordert.
- 2026-04-13, Uhrzeit nicht verlaesslich verfuegbar: REVEAL-Finalisierung angefordert.
- 2026-04-13, Uhrzeit nicht verlaesslich verfuegbar: Reveal-Praesentation finalisiert.
- 2026-04-13, Uhrzeit nicht verlaesslich verfuegbar: separates Forschungsprotokoll angefordert.

## Sichtbare Zaehldaten

| Merkmal | Wert | Anmerkung |
| --- | --- | --- |
| Sichtbare Nutzerturns im Gesamtlauf | nicht verlaesslich verfuegbar | Die fruehe Phase liegt im aktuellen Verlauf nur aggregiert als Gespraechszusammenfassung vor. |
| Sichtbare Assistententurns im Gesamtlauf | nicht verlaesslich verfuegbar | Die fruehe Phase liegt im aktuellen Verlauf nur aggregiert als Gespraechszusammenfassung vor. |
| Sichtbare Assistenten-Rueckfragen | 1 | Explizit dokumentierte Klaerungsfrage vor der Artefakterzeugung. |
| Sichtbare Nutzerantworten auf Rueckfragen | 1 | Antwort mit Profil A und Raum-/Teilnehmendenkontext. |
| Sichtbare Nutzersteuerungen | 5 | PLAN START, BLOG FINAL aequivalent, Wissensbasis + Reveal-Ableitung, REVEAL FINAL aequivalent, Forschungsprotokoll. |
| Sichtbare Zwischenstaende oder Fortschrittsmeldungen des Assistenten | nicht verlaesslich verfuegbar | Gesamtzahl ist wegen der aggregierten Fruehphase nicht turngenau rekonstruierbar. |
| Zusaetzliche technische Hook-Nachricht im Nutzerkanal | 1 | Sichtbar, aber nicht als Nutzersteuerung gezaehlt. |

## Erzeugte Artefaktpfade

- `content/blog/lehre/widi/lernfoerderliches_feedback_einstieg/blog_snapshot.txt`
- `content/blog/lehre/widi/lernfoerderliches_feedback_einstieg/index.md`
- `content/praesentation/lehre/widi/lernfoerderliches_feedback_einstieg/_index.md`
- `content/praesentation/lehre/widi/lernfoerderliches_feedback_einstieg/reveal_snapshot.txt`
- `ai_agents/blog_wissensbasis.md` (kuratiert aktualisiert)

## Editor-Status und Build-Status

| Bezug | Editor-Status | Build-Status |
| --- | --- | --- |
| Blog-Arbeitsdatei `content/blog/lehre/widi/lernfoerderliches_feedback_einstieg/index.md` | fehlerfrei geprueft laut dokumentiertem Lauf | Hugo-Draft-Build in der Entwurfsphase erfolgreich; regulaerer Hugo-Build nach Blog-Finalisierung erfolgreich |
| Wissensbasis `ai_agents/blog_wissensbasis.md` | `No errors found` | zusammen mit dem Reveal-Draft in einen erfolgreichen site-weiten Draft-Build einbezogen |
| Reveal-Arbeitsdatei `content/praesentation/lehre/widi/lernfoerderliches_feedback_einstieg/_index.md` | `No errors found` im Draft- und Finalisierungsstand | `hugo -D --destination /tmp/iwip-hugo-check-feedback` erfolgreich; `hugo --destination /tmp/iwip-hugo-final-feedback` erfolgreich |
