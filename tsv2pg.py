#!/usr/bin/env python3

import sys


def createTitleNode(ppn):
    return f"{ppn} :title"


def createSubjectEdge(ppn, sym, id):
    return f"{ppn} -> 'http://uri.gbv.de/terminology/{sym}/{id}' :subject"


uniquePpn = []

for line in sys.stdin.readlines():
    (ppn, sym, id) = tuple(line.strip().split("\t"))
    if ppn not in uniquePpn:
        print(createTitleNode(ppn))
        uniquePpn.append(ppn)
    print(createSubjectEdge(ppn, sym, id))
