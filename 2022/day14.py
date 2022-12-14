import sys
import re
from itertools import tee


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    yield from zip(a, b)


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
    x, y = source
    while True:
        if (x, y + 1) not in walls and (x, y + 1) not in sand:
            # Going down
            y += 1
        elif (x - 1, y + 1) not in walls and (x - 1, y + 1) not in sand:
            # Going left
            x -= 1
            y += 1
        elif (x + 1, y + 1) not in walls and (x + 1, y + 1) not in sand:
            # Going right
            x += 1
            y += 1
        else:
            # Stop
            sand.add((x, y))
            break

        if y >= max_y:
            break
    if y >= max_y:
        break
print("Part 1:", len(sand))

max_y += 2
walls |= set(yield_points((min_x // 2, max_y), (max_x * 2, max_y)))
sand = set()
while source not in sand:
    x, y = source
    while source not in sand:
        if (x, y + 1) not in walls and (x, y + 1) not in sand:
            # Going down
            y += 1
        elif (x - 1, y + 1) not in walls and (x - 1, y + 1) not in sand:
            # Going left
            x -= 1
            y += 1
        elif (x + 1, y + 1) not in walls and (x + 1, y + 1) not in sand:
            # Going right
            x += 1
            y += 1
        else:
            # Stop
            sand.add((x, y))
            break

        if y >= max_y:
            break
print("Part 2:", len(sand))
