import sys
from collections import Counter

poly, lines = sys.stdin.read().split("\n\n")
d = dict(l.split(" -> ") for l in lines.split("\n"))

# Count all pairs in initial string
c = Counter(f"{a}{b}" for a, b in zip(poly, poly[1:]))
steps = 40
for step in range(steps + 1):
    if step == 10 or step == 40:
        res = Counter()
        for (a, b), n in c.items():
            res[a] += n
        res[poly[-1]] += 1
        i = 1 if step == 10 else 2
        print(f"Part {i}: {max(res.values()) - min(res.values())}")
    c_ = Counter()
    for k in c.keys():
        sub = d.get(k)
        a, b = k
        c_[a + sub] += c[k]
        c_[sub + b] += c[k]
    c = c_
