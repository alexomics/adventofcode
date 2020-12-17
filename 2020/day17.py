import sys
from itertools import product


lines = [l.strip() for l in open(sys.argv[1])]
DELTAS = [1, 0, -1]
grid = {(j, i, 0): c == "#" for i, l in enumerate(lines) for j, c in enumerate(l)}


def get_bounds(g):
    min_ = list(map(min, zip(*g.keys())))
    max_ = list(map(max, zip(*g.keys())))
    return list(zip(min_, max_))


def cycle(g):
    new = {}
    (x1, x2), (y1, y2), (z1, z2) = get_bounds(g)
    for x, y, z in product(
        range(x1 - 1, x2 + 2), range(y1 - 1, y2 + 2), range(z1 - 1, z2 + 2)
    ):
        active = g.get((x, y, z), False)
        count = 0
        for dx, dy, dz in product(DELTAS, DELTAS, DELTAS):
            if dx == dy == dz == 0:
                continue
            count += g.get((x + dx, y + dy, z + dz), False)
        if (active and count in (2, 3)) or (not active and count == 3):
            new[(x, y, z)] = True
    return new


for _ in range(6):
    grid = cycle(grid)
print(f"Part 1: {sum(grid.values())}")
