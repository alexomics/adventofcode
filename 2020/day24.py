import sys
from collections import defaultdict, deque, namedtuple

# https://www.redblobgames.com/grids/hexagons/#neighbors-axial
_Hex = namedtuple("Hex", ["x", "y"])
#     nw
#  w /‾\ ne
# sw \_/ e
#    se
hex_directions = {
    "e": _Hex(1, 0),
    "se": _Hex(0, -1),
    "sw": _Hex(-1, -1),
    "w": _Hex(-1, 0),
    "nw": _Hex(0, 1),
    "ne": _Hex(1, 1),
}


class Hex(_Hex):
    def __add__(self, other):
        return Hex(self.x + other.x, self.y + other.y)


def iter_line(line):
    line = deque(line)
    ch = ""
    while line:
        ch += line.popleft()
        if ch in hex_directions:
            yield hex_directions[ch]
            ch = ""


lines = [l.strip() for l in open(sys.argv[1])]

grid = defaultdict(int)
for line in lines:
    tile = Hex(0, 0)
    for delta in iter_line(line):
        tile += delta
    grid[tile] ^= 1
print(f"Part 1: {sum(grid.values())}")


def run(grid):
    new_grid = {}
    adjacent_black = defaultdict(int)
    for tile, black in grid.items():
        if black:
            for delta in hex_directions.values():
                adjacent_black[tile + delta] += 1

    for tile, black in grid.items():
        if black:
            n = adjacent_black.get(tile, 0)
            if n == 0 or n > 2:
                new_grid[tile] = 0
            else:
                new_grid[tile] = 1
    for tile, count in adjacent_black.items():
        if count == 2 and grid.get(tile, 0) == 0:
            new_grid[tile] = 1
    return new_grid


for i in range(100):
    grid = run(grid)
print(f"Part 2: {sum(grid.values())}")
