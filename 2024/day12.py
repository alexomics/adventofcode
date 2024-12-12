import sys
from collections import defaultdict, deque

DIRS = [(1, 0), (0, -1), (-1, 0), (0, 1)]


# fmt: off
def draw(region):
    lx, ux = min(x for x, _ in region), max(x for x, _ in region)
    ly, uy = min(y for _, y in region), max(y for _, y in region)
    arr = [
        [char if (x, y) in region else " " for x in range(lx, ux + 1)]
        for y in range(ly, uy + 1)
    ]
    print("\n".join("".join(a) for a in arr))
def neighbours(x, y, deltas=DIRS):
    yield from ((x + dx, y + dy) for dx, dy in deltas)
def valid_neighbours(x, y, S, deltas=DIRS):
    yield from ((nx, ny) for nx, ny in neighbours(x, y, deltas) if (nx, ny) in S)
# fmt: on


grid = defaultdict(list)
grid2 = {}
data = sys.stdin.read().strip()
# print(data)
mx, my = 0, 0
for y, line in enumerate(data.splitlines()):
    for x, c in enumerate(line):
        grid[c].append((x, y))
        grid2[(x, y)] = c
        mx = max(mx, x)
    my = max(my, y)

p1 = 0
p2 = 0
for char, coords in grid.items():
    # print(char)
    cs = set(coords)
    while cs:
        x, y = next(iter(list(cs)))
        cs.discard((x, y))
        region = [(x, y)]
        path = deque([(x, y)])
        key = (x, y, char)
        no_self_neighbours = 0
        while path:
            x, y = path.popleft()
            for n in valid_neighbours(x, y, cs):
                region.append(n)
                path.append(n)
                cs.remove(n)

        no_self_neighbours += sum(
            grid2.get((nx, ny), "") != char
            for (x, y) in region
            for nx, ny in neighbours(x, y)
        )

        def _corners(region):
            res = []
            for x, y in region:
                # OUTER CORNERS
                if (x - 1, y) not in region and (x, y - 1) not in region:
                    # XX
                    # X
                    res.append((x, y))
                if (x + 1, y) not in region and (x, y + 1) not in region:
                    # XX
                    #  X
                    res.append((x, y))
                if (x + 1, y) not in region and (x, y - 1) not in region:
                    #  X
                    # XX
                    res.append((x, y))
                if (x - 1, y) not in region and (x, y + 1) not in region:
                    # X
                    # XX
                    res.append((x, y))
                # INNER CORNERS
                if ((x + 1, y) in region and (x, y + 1) in region) and (
                    (x + 1, y + 1) not in region
                ):
                    # OX
                    # X
                    res.append((x, y))
                if (
                    (x - 1, y) in region
                    and (x, y + 1) in region
                    and (x - 1, y + 1) not in region
                ):
                    # XX
                    #  X
                    res.append((x, y))
                if (
                    (x - 1, y) in region
                    and (x, y - 1) in region
                    and (x - 1, y - 1) not in region
                ):
                    #  X
                    # XO
                    res.append((x, y))
                if (
                    (x + 1, y) in region
                    and (x, y - 1) in region
                    and (x + 1, y - 1) not in region
                ):
                    # X
                    # OX
                    res.append((x, y))
            return res

        p1 += len(region) * no_self_neighbours
        # print(key, region, no_self_neighbours)
        p2 += len(region) * len(_corners(region))
        # print(_corners(region))
        # draw(region)
        # draw(outer)
        # break
    # break


print(p1, p2, sep="\n")
