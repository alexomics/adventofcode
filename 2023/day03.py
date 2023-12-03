import sys
import re
from math import prod

data = sys.stdin.read().split("\n")
M = {(row, col): v for row, line in enumerate(data) for col, v in enumerate(line)}
coords = [list(re.finditer("\d+", l)) for l in data]
adj = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def circle(s, e, row):
    coords = [(row, c) for c in range(s, e)]
    seen = set()
    for _, col in coords:
        for dr, dc in adj:
            nr, nc = row + dr, col + dc
            if (nr, nc) not in coords and (nr, nc) not in seen:
                yield nr, nc
                seen.add((nr, nc))


p1, p2 = [], {}
for row, matches in enumerate(coords):
    for match in matches:
        chars = [M.get((r, c), ".") for r, c in circle(*match.span(), row)]
        if any(c not in ".0123456789" for c in chars):
            num = int(match.group())
            p1.append(num)
            if "*" in chars:
                for r, c in circle(*match.span(), row):
                    if M.get((r, c), ".") != "*":
                        continue
                    g = p2.setdefault((r, c), [])
                    g.append(num)

print(sum(p1))
print(sum(prod(arr) for arr in p2.values() if len(arr) == 2))
