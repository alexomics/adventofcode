import sys
from collections import Counter


ll, rl = [], []
for l in sys.stdin.read().split("\n"):
    if not l:
        continue
    a, b = list(map(int, l.split()))
    ll.append(a)
    rl.append(b)

ll.sort()
rl.sort()

print(sum(abs(a - b) for a, b in zip(ll, rl)))
counts = Counter(rl)
print(sum(a * counts[a] for a in ll))
