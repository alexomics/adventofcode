import sys
from itertools import pairwise
from functools import reduce


def parse(stream):
    yield from (map(int, l.strip().split()) for l in stream)


def expand(record):
    r = [list(record)]
    while not all(x == 0 for x in r[-1]):
        r.append([b - a for a, b in pairwise(r[-1])])
    return [a[0] for a in r], [a[-1] for a in r]


s1, s2 = 0, 0
for p2, p1 in map(expand, parse(sys.stdin)):
    s1 += sum(p1)
    s2 += reduce(lambda a, b: b - a, p2[::-1])
print(s1)
print(s2)
