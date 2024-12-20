import sys
import heapq
from collections import defaultdict, deque, Counter

NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)
DIRS = [NORTH, EAST, SOUTH, WEST]
data = sys.stdin.read().strip().splitlines()
grid = {(x, y): c for y, l in enumerate(data) for x, c in enumerate(l)}
start = next(k for k, v in grid.items() if v == "S")
end = next(k for k, v in grid.items() if v == "E")
mx = max(x for x, _ in grid)
my = max(y for _, y in grid)


def solve(grid, pos, end, mx, my):
    todo = deque([(*pos, 0)])
    seen = set()
    while todo:
        x, y, s = todo.popleft()
        if (x, y) == end:
            return s
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for dx, dy in DIRS:
            x_ = x + dx
            y_ = y + dy
            if 0 <= x_ < mx and 0 <= y_ < mx and grid.get((x_, y_), ".") != "#":
                todo.append((x_, y_, s + 1))


path = solve(grid, start, end, mx, my)
c = Counter(
    solve(grid | {pos: "."}, start, end, mx, my)
    for pos, char in grid.items()
    if char == "#"
)
print(sum(v for k, v in c.items() if path - k >= 100))
