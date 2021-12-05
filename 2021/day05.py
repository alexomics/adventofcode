import sys
import re
from collections import defaultdict


pat = re.compile(r"^(\d+),(\d+) -> (\d+),(\d+)", flags=re.MULTILINE)
lines = pat.findall(sys.stdin.read())

p1 = defaultdict(int)
p2 = defaultdict(int)
for x1, y1, x2, y2 in lines:
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    if x1 == x2:
        y1, y2 = sorted((y1, y2))
        for y in range(y1, y2 + 1):
            p1[(x1, y)] += 1
            p2[(x1, y)] += 1
    elif y1 == y2:
        x1, x2 = sorted((x1, x2))
        for x in range(x1, x2 + 1):
            p1[(x, y1)] += 1
            p2[(x, y1)] += 1
    else:
        dx = -1 if x1 > x2 else 1
        dy = -1 if y1 > y2 else 1
        x, y = x1, y1
        while x != x2 and y != y2:
            p2[(x, y)] += 1
            x += dx
            y += dy
        p2[(x, y)] += 1
print(f"Part 1: {sum(v > 1 for v in p1.values())}")
print(f"Part 2: {sum(v > 1 for v in p2.values())}")
