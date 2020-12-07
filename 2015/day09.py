import sys
import re
from itertools import permutations


class D(dict):
    def __getitem__(self, key):
        if not key in self:
            key = key[::-1]
        return super().__getitem__(key)


pat = re.compile(r"(\w+) to (\w+) = (\d+)")
d = D({(s, d): int(i) for s, d, i in (pat.findall(l)[0] for l in open(sys.argv[1]))})
locs = list(permutations(set((x for y in d.keys() for x in y))))
mi, ma = float("inf"), 0
for l in locs:
    x = 0
    for a, b in zip(l, l[1:]):
        x += d[a, b]
    mi, ma = min(mi, x), max(ma, x)
print(f"Part 1: {mi}\nPart 2: {ma}")
