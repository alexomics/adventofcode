import sys
from collections import defaultdict


data = [l.split("-") for l in sys.stdin.read().strip().splitlines()]
d = defaultdict(set)
for a, b in data:
    d[a].add(b)
    d[b].add(a)

p = set()
for a in d:
    for b in d[a] - {a}:
        for c in d[b] - {a, b}:
            if a in d[c]:
                p.add(tuple(sorted([a, b, c])))
p1 = sum(any(c[0] == "t" for c in t) for t in p)

print(p1)
# TY solution megathread for p2
import networkx as nx

G = nx.Graph(data)
cliques = nx.find_cliques(G)
p2 = ",".join(sorted(max(cliques, key=len)))

print(p2)
