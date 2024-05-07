#!/usr/bin/env python3

import sys
import json


def createVoc(uri, sym, label):
    tags = ""
    for key, val in label.items():
        tags += f' PrefLabel@{key}:"{val}"'
    return f"'{uri}' :voc id:'{uri}' sym:'{sym}'{tags}"


def createNode(sym, notation, uri, label: dict):
    tags = ""
    for key, val in label.items():
        tags += f' prefLabel@{key}:"{val}"'
    return (
        f"'{uri}' :concept id:'{notation}' voc:'{sym}'{tags}\n'{sym}' -> '{uri}' :voc"
    )


def createHierarchyEdges(src, narrower):
    edges = []
    for i in narrower:
        dest = i["uri"]
        edges.append(f"'{src}' -> '{dest}' :narrower")

    return edges


input = sys.stdin.read()

result = []

for ndjson_line in input.splitlines():
    if not ndjson_line.strip():
        continue  # ignore empty lines
    json_line = json.loads(ndjson_line)
    result.append(json_line)

vocs = []

for i in result:
    uri = i["uri"]
    voc_uri = i["inScheme"][0]["uri"]
    notation = i["notation"][0]
    label = i["prefLabel"]
    narrower = i["narrower"]

    if voc_uri not in vocs:
        sym = i["inScheme"][0]["notation"][0]
        voc_label = i["inScheme"][0]["prefLabel"]
        vocs.append(voc_uri)
        print(createVoc(voc_uri, sym, voc_label))

    print(createNode(voc_uri, notation, uri, label))
    if i := "\n".join(createHierarchyEdges(uri, narrower)):
        print(i)
