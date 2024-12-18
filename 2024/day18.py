import sys
from collections import deque

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def solve(grid, mx, my):
    todo = deque([(0, 0, 0)])
    seen = set()
    while todo:
        x, y, s = todo.popleft()
        if (x, y) == (mx - 1, my - 1):
            return s
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for dx, dy in DIRS:
            x_ = x + dx
            y_ = y + dy
            if 0 <= x_ < mx and 0 <= y_ < mx and grid.get((x_, y_), ".") != "#":
                todo.append((x_, y_, s + 1))


grid = {}
data = sys.stdin.read().strip()
pts = [tuple(map(int, l.split(","))) for l in data.splitlines()]
steps = 12 if len(pts) < 100 else 1024
mx = my = 7 if len(pts) < 100 else 71
for i, (x, y) in enumerate(pts):
    grid[(x, y)] = "#"

    if i == steps:
        print(solve(grid, mx, my))
    elif i > steps and solve(grid, mx, my) is None:
        print(f"{x},{y}")
        break
