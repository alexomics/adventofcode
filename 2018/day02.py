import sys
from collections import Counter

lines = [list(l.strip()) for l in sys.stdin]

i = [Counter(l) for l in lines]
x = sum(2 in v.values() for v in i) * sum(3 in v.values() for v in i)
print(f"Part 1: {x}")

for i in range(len(lines[0])):
    c = Counter(["".join(l[0:i] + l[i + 1 :]) for l in lines])
    if 2 in c.values():
        break
print(f"Part 2: {c.most_common()[0][0]}")
