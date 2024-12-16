import sys
from collections import defaultdict
import heapq


NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)
DIRS = [NORTH, EAST, SOUTH, WEST]

data = sys.stdin.read().strip().splitlines()
grid = {(x, y): c for y, l in enumerate(data) for x, c in enumerate(l)}
start = next(k for k, v in grid.items() if v == "S")
end = next(k for k, v in grid.items() if v == "E")

# Dijkstra's, I think... see 2022:12 and 2021:15
# (score, x pos, y pos, direction)
heap = [(0, *start, EAST)]
seen = set()
paths = defaultdict(list)
lowest_score = float("inf")

while heap:
    score, x, y, d = heapq.heappop(heap)

    if score > lowest_score:
        continue

    if (x, y) == end:
        lowest_score = score
        continue

    if (x, y, d) in seen:
        continue
    seen.add((x, y, d))

    for nd in DIRS:
        heapq.heappush(heap, (score + 1000, x, y, nd))
        paths[(score + 1000, x, y, nd)].append((score, x, y, d))

    dx, dy = d
    nx, ny = x + dx, y + dy
    if grid.get((nx, ny), "#") != "#":
        heapq.heappush(heap, (score + 1, nx, ny, d))
        paths[(score + 1, nx, ny, d)].append((score, x, y, d))

seen = set()
todo = [(lowest_score, *end, d) for d in DIRS]
while todo:
    s, x, y, d = todo.pop()
    seen.add((x, y))
    for state in paths[(s, x, y, d)]:
        todo.append(state)

print(lowest_score, len(seen), sep="\n")
