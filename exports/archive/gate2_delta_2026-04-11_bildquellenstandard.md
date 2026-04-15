# Gate 2 – Delta Bildquellenstandard (2026-04-11)

## Geaendert

- Zukunftsstandard fuer Bild-/Grafikquellen in Governance, Master-Agent, Templates und Checks praezisiert.
- Blog-Standard festgezogen:
  - optional `p.grafic-title` direkt ueber der Visualisierung
  - `figure.figure-frame` fuer die Darstellung
  - `p.bildquelle` mit Praefix `Bildquelle:` unter der Visualisierung
- Reveal-Standard festgezogen:
  - `figure.figure-frame` als Default-Muster fuer Bildfolien
  - schlanke Quellenzeile als `p.zitat-quelle` mit Praefix `Bildquelle:` unter der Visualisierung
  - Lizenzinformation bzw. klarer Rechtehinweis ist verpflichtend, Lizenzlink aber nicht
- `prompts/check.md` prueft die Unterscheidung jetzt ausdruecklich.

## Nicht geaendert

- Keine Rueckmigration bestehender Blog- oder Reveal-Inhalte.
- Keine CSS-Refaktorierung an Altklassen oder Altbelegen.
- Keine Massenkorrektur alter Praefixe wie `Quelle:` oder `Foto:` in publizierten Inhalten.

## Konsequenz fuer kuenftige Laeufe

- Neue Blog-Artefakte sollen Bildquellen einheitlich mit `Bildquelle:` in `p.bildquelle` ausgeben.
- Neue Reveal-Artefakte sollen Bildquellen einheitlich als schlanke `p.zitat-quelle` mit `Bildquelle:` und sichtbarer Lizenzinformation ausgeben.
- Abweichungen werden kuenftig im Check frueher sichtbar.