# Benchmark

Dieser Bereich enthaelt die aktuellen manuellen Regressionstests fuer den
didaktischen Planungsagenten. Die Testdefinitionen sind oeffentlich versioniert;
konkrete Testlaeufe und Rohoutputs bleiben lokal.

## Bestand

- `inputs/`: Fallkontexte und Dialogskripte fuer H01, H02 und H03
- `evaluations/`: vorhandene Erwartungshorizonte; derzeit H01
- `fixtures/`: versionierte Sollzustaende; derzeit das erwartete H03-Planning-Journal

Die Dialogtests werden derzeit manuell durchgefuehrt. Ein automatischer Runner
oder ein Benchmark-Harness ist nicht vorhanden. Erwartungen duerfen waehrend
eines Testlaufs nicht als Agentenkontext verwendet werden.

Laufartefakte, Transkripte und Rohdaten gehoeren nach
`agent_entwicklung/benchmark_runs/`. Dieser lokale, ignorierte Bereich ist keine
normative Quelle fuer den aktuellen Agenten. Das gilt ebenso fuer historische
Runs; massgeblich sind die aktuellen Agentenregeln und die hier versionierten
Testdefinitionen.
