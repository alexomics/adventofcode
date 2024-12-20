import sys
from collections import deque

NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)
DIRS = [NORTH, EAST, SOUTH, WEST]
data = sys.stdin.read().strip().splitlines()
grid = {(x, y): c for y, l in enumerate(data) for x, c in enumerate(l)}
start = next(k for k, v in grid.items() if v == "S")
end = next(k for k, v in grid.items() if v == "E")


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def solve(grid, pos, end):
    todo = deque([pos])
    seen = set()
    path = []
    while todo:
        x, y = todo.popleft()
        if (x, y) in seen:
            continue
        path.append((x, y))
        seen.add((x, y))
        for dx, dy in DIRS:
            x_ = x + dx
            y_ = y + dy
            if grid.get((x_, y_), "") in ".SE":
                todo.append((x_, y_))
        if (x, y) == end:
            return path


def cheat(path, steps, saving=100):
    shortcuts = set()
    for i, p1 in enumerate(path, 0):
        for j, p2 in enumerate(path[i + 1 :], i + 1):
            if (m := manhattan_distance(p1, p2)) <= steps:
                if j - i - m >= saving:
                    shortcuts.add((p1, p2, m))
    return shortcuts


path = solve(grid, start, end)
pp1 = cheat(path, 2, 100)
pp2 = cheat(path, 20, 100)
print(len(pp1), len(pp2), sep="\n")
