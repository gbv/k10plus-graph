default: downloads kxp-subjects.pg some-subjects.pg import/subjects.nodes.csv

docs:
	quarto render manual


csv: some-subjects.pg import/subjects.nodes.csv

downloads: rvko_xml.zip bk__default.jskos.ndjson sdnb-concepts.ndjson kxp-subjects

rvko_xml.zip:
	wget https://rvk.uni-regensburg.de/downloads/rvko_xml.zip

bk__default.jskos.ndjson:
	wget https://api.dante.gbv.de/export/download/bk/default/bk__default.jskos.ndjson

sdnb-concepts.ndjson:
	wget https://raw.githubusercontent.com/gbv/jskos-data/master/sdnb/sdnb-concepts.ndjson

kxp-subjects.tsv.gz:
	curl -L "https://zenodo.org/api/records/7016625" | jq -r '.files[] | select(.key | endswith(".tsv.gz")) | .links.self' | xargs -I {} wget -O kxp-subjects.tsv.gz {}

kxp-subjects.pg: kxp-subjects.tsv.gz
	zcat kxp-subjects.tsv.gz | cargo run tsv2pg-rs --release > kxp-subjects.pg

bk_broader.pg: bk__default.jskos.ndjson
	python3 jskos-scheme-to-pg.py bk bk__default.jskos.ndjson > bk_broader.pg

rvk_broader.pg: rvko_xml.zip
	unzip -p rvko_xml.zip rvko_2024_1.xml | python3 rvk_broader_xml.py > rvk_broader.pg

some-subjects.pg: kxp-subjects.pg bk__default.jskos.ndjson sdnb-concepts.ndjson rvko_xml.zip
	head -n 4000000 kxp-subjects.pg > some_subjects.pg && \
	python3 jskos-scheme-to-pg.py bk bk__default.jskos.ndjson >> some_subjects.pg && \
	python3 jskos-scheme-to-pg.py sdnb sdnb-concepts.ndjson >> some_subjects.pg && \
	python3 mappings_to_pg.py -s 20049,533,18785 >> some_subjects.pg && \
	unzip -p rvko_xml.zip | python3 rvk_broader_xml.py >> some_subjects.pg

import/subjects.nodes.csv: some_subjects.pg
	mkdir -p import
	pgraph $< -t csv import/subjects
	./import.sh subjects