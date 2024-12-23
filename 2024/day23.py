import sys
from collections import defaultdict, Counter

data = [l.split("-") for l in sys.stdin.read().strip().splitlines()]
d = defaultdict(set)
for a, b in data:
    d[a].add(b)
    # d[a].add((b, a))
    d[b].add(a)
    # d[b].add((a, b))

p = set()
for a in d:
    for b in d[a] - {a}:
        for c in d[b] - {a, b}:
            if a in d[c]:
                p.add(tuple(sorted([a, b, c])))
p1 = sum(any(c[0] == "t" for c in t) for t in p)
print(p1)
