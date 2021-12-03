import sys
from itertools import cycle

L = [int(l.strip()) for l in sys.stdin]

print(f"Part 1: {sum(L)}")

seen = set()
freq = 0
for i in cycle(L):
    freq += i
    if freq in seen:
        break
    seen.add(freq)

print(f"Part 2: {freq}")
