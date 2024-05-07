#!/usr/bin/env python3

import sys


def createTitleNode(ppn):
    return f"{ppn} :Title"


def createSubjectNode(sym, id):
    return f"'{sym}:{id}' :Concept id:'{id}'"


def createSubjectEdge(ppn, sym, id):
    return f"{ppn} -> '{sym}:{id}' :Subject"


uniquePpn = []

for line in sys.stdin.readlines():
    (ppn, sym, id) = tuple(line.strip().split("\t"))
    if ppn not in uniquePpn:
        print(createTitleNode(ppn))
        uniquePpn.append(ppn)
    print(createSubjectNode(sym, id))
    print(createSubjectEdge(ppn, sym, id))
