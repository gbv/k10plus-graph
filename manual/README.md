## Handbuch [![Status](https://github.com/gbv/k10plus-graph/actions/workflows/quarto-publish.yml/badge.svg)](https://github.com/gbv/k10plus-graph/actions/workflows/quarto-publish.yml)

Das Handbuch zum K10plus Knowledge Graphen wird mit [quarto](https://quarto.org/)
erstellt. Die Konfiguration liegt in [`_quarto.yml`](_quarto.yml) und die
einzelnen Kapitel in Quarto-Markdown-Syntax in Dateien mit der Endung `.qmd`.

Die HTML-Version des Handbuch kann lokal mit Aufruf von `quarto render` in
diesem Ordern oder mit `make docs` im Wurzelverzeichnis aktualisiert werden und
liegt anschließend im Verzeichnis `docs`. Die publizierte Version unter
<https://gbv.github.io/k10plus-graph/> wird bei GitHub automatisch aus dem
`main` Branch erzeugt.
