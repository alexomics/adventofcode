import sys
from collections import deque

DIRS = [(1, 0), (0, 1), (0, -1), (-1, 0)]
data = sys.stdin.read()
grid = {
    (x, y): int(c)
    for y, line in enumerate(data.splitlines())
    for x, c in enumerate(line)
}

paths = deque([(p, p) for p, v in grid.items() if v == 0])
seen = set()
count = 0
while paths:
    start, curr = paths.popleft()
    if grid[curr] == 9:
        seen.add((start, curr))
        count += 1
        continue
    x, y = curr
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if grid.get((nx, ny), -1) == grid[curr] + 1:
            paths.append((start, (nx, ny)))

print(len(seen), count, sep="\n")
