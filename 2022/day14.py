import sys
import re
from itertools import pairwise


def yield_points(a, b):
    x1, y1 = a
    x2, y2 = b
    if x1 == x2:
        ys = list(range(min(y1, y2), max(y1, y2) + 1))
        xs = [x1] * len(ys)
    elif y1 == y2:
        xs = list(range(min(x1, x2), max(x1, x2) + 1))
        ys = [y1] * len(xs)
    else:
        assert False, "doh"
    yield from zip(xs, ys)


pat = re.compile(r"\d+")
s = sys.stdin.read().splitlines()
directions = [
    [tuple(map(int, pat.findall(l))) for l in line.split(" -> ")] for line in s
]
walls = {
    tuple(step)
    for dirs in directions
    for a, b in pairwise(dirs)
    for step in yield_points(a, b)
}

source = (500, 0)
min_x = min(x for x, _ in walls)
max_x = max(x for x, _ in walls)
min_y = min(y for _, y in walls)
max_y = max(y for _, y in walls)
sand = set()
while True:
    occupied = walls | sand
    sand_x, sand_y = source
    while True:
        if (sand_x, sand_y + 1) not in occupied:
            # Going down
            sand_y += 1
        elif (sand_x - 1, sand_y + 1) not in occupied:
            # Going left
            sand_x -= 1
            sand_y += 1
        elif (sand_x + 1, sand_y + 1) not in occupied:
            # Going right
            sand_x += 1
            sand_y += 1
        else:
            # Stop
            sand.add((sand_x, sand_y))
            break

        if sand_y >= max_y:
            break
    if sand_y >= max_y:
        break
print("Part 1:", len(sand))

max_y += 2
walls |= set(yield_points((min_x // 2, max_y), (max_x * 2, max_y)))
sand = set()
while source not in sand:
    occupied = walls | sand
    sand_x, sand_y = source
    while source not in sand:
        if (sand_x, sand_y + 1) not in occupied:
            # Going down
            sand_y += 1
        elif (sand_x - 1, sand_y + 1) not in occupied:
            # Going left
            sand_x -= 1
            sand_y += 1
        elif (sand_x + 1, sand_y + 1) not in occupied:
            # Going right
            sand_x += 1
            sand_y += 1
        else:
            # Stop
            sand.add((sand_x, sand_y))
            break

        if sand_y >= max_y:
            break
print("Part 2:", len(sand))
