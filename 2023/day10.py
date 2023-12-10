import sys

adj_lookup = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    "S": [(-1, 0), (0, -1), (1, 0), (0, 1)],
    ".": [],
}
data = sys.stdin.read().split("\n")
grid = {(row, col): v for row, line in enumerate(data) for col, v in enumerate(line)}
start = [t for t, v in grid.items() if v == "S"][0]


def steps(G, curr):
    r, c = curr
    for dr, dc in adj_lookup[G.get(curr, ".")]:
        nr, nc = r + dr, c + dc
        if (nr, nc) in G:
            yield nr, nc


r, c = start
next_steps = [t for t in steps(grid, start)]
seen = set([start])
if grid[start] == "S":
    # Check reverse
    next_steps = [s for s in next_steps if "S" in [grid[t] for t in steps(grid, s)]]
while next_steps:
    next_ = next_steps.pop(0)
    seen.add(next_)
    for n in steps(grid, next_):
        if n not in seen:
            next_steps.append(n)
print(len(seen) // 2)
inners = {}
# Scan each row for verticals on one side
for (r, c), v in grid.items():
    g = inners.setdefault(r, [])
    if v in "|LJ" and (r, c) in seen:
        g.append(c)
count = 0
for r, idxs in inners.items():
    while idxs:
        a, b = idxs.pop(0), idxs.pop(0)
        count += sum((r, c) not in seen for c in range(a, b))

print(count)
