# k10plus-graph

## Dependencies
- [Python3](https://www.python.org/)

## Obtaining the data
Dumps of subject indexing in K10plus catalog are published yearly to quarterly. Each dump is around 15 Gigabytes (that's around 10% of full K10plus data) and split into multiple files. Copies of the full dump may be found at https://analytics.gbv.de/dumps/kxp/. Data is provided in PICA Normalized format with one record per line.

The data is reduced to data fields used for subject indexing in K10plus catalog and limited to records with at least one library holding. Records without any subject indexing are omitted. See K10plus format documentation and file README.md of the data publication for details.

## tsv2pg/tsv2pg-rs
### Summary
A simple converter tool to convert a [tsv](https://en.wikipedia.org/wiki/Tab-separated_values) input to the [pg](https://pg-format.github.io/specification) graph format.

For creating the tsv file, see https://github.com/gbv/k10plus-subjects

The tsv file can be downloaded from https://doi.org/10.5281/zenodo.7016625

### Structure
The tsv file must not have a header and must have the following columns in the rigth order:
1. Bibliographic record identifier (PPN)
2. Vocabulary symbol
3. Notation or identifier in the vocabulary

The usage of single Quotes in the columns breaks the program.

#### Example Structure
```tsv
010000011  bk  58.55
010000011  gnd 4036582-7
```

### Usage
```sh
zcat kxp-subjects.tsv.gz | ./tsv2pg.py > kxp-subjects.pg
```
> [!NOTE]
> Using zcat to decompress the file to stdin

### tsv2pg-rs
For faster conversion it is recommend to use tsv2pg-rs

#### Usage
```sh
zcat kxp-subjects.tsv.gz | cargo run tsv2pg-rs --release > kxp-subjects.pg
```
## jskos2pg
### Summary
A simple converter tool to convert a [jskos ndjson](https://gbv.github.io/jskos/jskos.html) input to the [pg](https://pg-format.github.io/specification) graph format.

For downloading the data, see http://api.dante.gbv.de/voc/bk

### Structure
The input must be in the ndjson format. The following keys are necessary:
```json
{
  "uri": "http://uri.gbv.de/terminology/bk/44.76",
  "inScheme": [
    {
      "uri": "http://uri.gbv.de/terminology/bk/",
      "prefLabel": {
        "de": "Basisklassifikation",
        "en": "Basisclassification"
      },
      "notation": [
        "bk"
      ]
    }
  ],
  "notation": [
    "44.76"
  ],
  "prefLabel": {
    "de": "Ernährungsstörungen, Mangelkrankheiten"
  },
  "narrower": [
    {
      "uri": "http://uri.gbv.de/terminology/bk/86.79",
    },
  ]
}
```

### Usage
```sh
cat bk__default.jskos.ndjson | ./jskos2pg.py > bk.jskos.pg
```
