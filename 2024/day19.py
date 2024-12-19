import sys
from functools import cache


# fmt:off
def make_patterns(d: str, curr):
    for p in pats:
        if d.startswith(p):
            if d == p:
                yield (*curr, p)
            else:
                yield from count_pattern(d[len(p) :], curr)

@cache
def count_patterns(d):
    return 1 if not d else sum(count_patterns(d[len(p) :]) for p in pats if d.startswith(p))
# fmt:on

pats, desgins = sys.stdin.read().strip().split("\n\n")
pats = pats.split(", ")
desgins = desgins.splitlines()
p1, p2 = 0, 0
for d in desgins:
    count = count_patterns(d)
    p1 += count > 0
    p2 += count
print(p1, p2, sep="\n")
