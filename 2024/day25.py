import sys
from collections import Counter

data = sys.stdin.read().strip().split("\n\n")
keys = [
    Counter(t for l in g.splitlines() for t in enumerate(l))
    for g in data
    if "#" in g[:5]
]
locks = [
    Counter(t for l in g.splitlines() for t in enumerate(l))
    for g in data
    if "#" not in g[:5]
]

ans = 0
for k in keys:
    for l in locks:
        if all(k[(i, "#")] + l[(i, "#")] <= 7 for i in range(5)):
            ans += 1
print(ans)
