import sys
from itertools import combinations

data = [l for l in sys.stdin.read().split("\n") if l]
grid = {
    (row, col): v
    for row, line in enumerate(data)
    for col, v in enumerate(line)
    if v == "#"
}
rows = len(data)
cols = len(data[0])
empty_rows = [r for r in range(rows) if "#" not in data[r]]
empty_cols = [c for c in range(cols) if "#" not in "".join(r[c] for r in data)]

for exp in (1, 1_000_000):
    g = {}
    for r, c in grid:
        nr = sum(r > r_ for r_ in empty_rows)
        nc = sum(c > c_ for c_ in empty_cols)
        g[r + (exp * nr), c + (exp * nc)] = "#"
    total = 0
    for i, ((r, c), (r2, c2)) in enumerate(combinations(g.keys(), 2), 1):
        total += abs(r2 - r) + abs(c2 - c)
    print(total)
