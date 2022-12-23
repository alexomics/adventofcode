import sys
import collections


def print_grid(grid, pos=None):
    if isinstance(pos, tuple) or pos is None:
        pos = set([pos])
    minx, maxx = min(x for x, _ in grid), max(x for x, _ in grid) + 1
    miny, maxy = min(y for _, y in grid), max(y for _, y in grid) + 1
    for y in range(miny - 1, maxy + 1):
        row = ""
        for x in range(minx - 1, maxx + 1):
            fstr = "\033[32;1m{}\033[0m" if (x, y) in pos else "{}"
            row += fstr.format("#" if (x, y) in grid else ".")
        print(row)


data = sys.stdin.read()

grid = set(
    (x, y)
    for y, line in enumerate(data.splitlines())
    for x, c in enumerate(line)
    if c == "#"
)


def check_direction(x, y, c):
    if c == "N":
        yield x, y - 1
        yield x + 1, y - 1
        yield x - 1, y - 1
    elif c == "S":
        yield x, y + 1
        yield x + 1, y + 1
        yield x - 1, y + 1
    elif c == "W":
        yield x - 1, y
        yield x - 1, y - 1
        yield x - 1, y + 1
    elif c == "E":
        yield x + 1, y
        yield x + 1, y - 1
        yield x + 1, y + 1
    else:
        assert False


def adjacent(x, y):
    for y_d in (-1, 0, 1):
        for x_d in (-1, 0, 1):
            if y_d == x_d == 0:
                continue
            yield x + x_d, y + y_d


directions = [
    ("N", (0, -1)),
    ("S", (0, 1)),
    ("W", (-1, 0)),
    ("E", (1, 0)),
]
rounds = 0
while True:
    rounds += 1
    to_move = {}
    for x, y in grid:
        if all(a not in grid for a in adjacent(x, y)):
            # All clear
            continue
        for d, (dx, dy) in directions:
            # Check N, S, W, E
            if all(a not in grid for a in check_direction(x, y, d)):
                to_move[(x, y)] = (x + dx, y + dy)
                break
    if not to_move:
        break
    counts = collections.Counter(to_move.values())
    for current, new in to_move.items():
        if counts[new] > 1:
            continue
        grid.remove(current)
        grid.add(new)
    if rounds == 10:
        print(
            "Part 1:",
            (max(x for x, _ in grid) - min(x for x, _ in grid) + 1)
            * (max(y for _, y in grid) - min(y for _, y in grid) + 1)
            - len(grid),
        )
    directions.append(directions.pop(0))
    # print_grid(grid)

print("Part 2:", rounds)
