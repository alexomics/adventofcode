import sys

DIRS = {">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1)}


def cycle_blizzards(blizzards, t, max_x, max_y):
    res = set()
    for x, y, c, dx, dy in blizzards:
        res.add(((x + t * dx) % max_x, (y + t * dy) % max_y))
    return res


WALLS = set()
BLIZZARDS = set()
s = sys.stdin.read()
# Start at -1 because it's easier on my brain when the grid starts at 0
for y, row in enumerate(s.splitlines(), start=-1):
    for x, c in enumerate(row, start=-1):
        if c == "#":
            WALLS.add((x, y))
        if c in DIRS:
            BLIZZARDS.add((x, y, c, *DIRS[c]))
max_x = max(x for x, _ in WALLS)
max_y = max(y for _, y in WALLS)
# cap the start and end to limit the search
WALLS.add((0, -2))
WALLS.add((max_x - 1, max_y + 1))
start = (0, -1)
end = (max_x - 1, max_y)

t, i = 0, 1
q = {start}
targets = [(end, True), (start, False), (end, True)]
while targets:
    t += 1
    b = cycle_blizzards(BLIZZARDS, t, max_x, max_y)
    new = set()
    for x, y in q:
        # (0, 0)! we can stand still
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in b and (nx, ny) not in WALLS:
                new.add((nx, ny))
    q = new
    if targets[0][0] in q:
        target, p = targets.pop(0)
        if p:
            print(f"Part {i}: {t}")
            i += 1
        q = {target}
