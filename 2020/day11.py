import sys
from itertools import product

lines = [list(l.strip()) for l in open(sys.argv[1])]
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]


class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    def __contains__(self, t):
        x, y = t
        return 0 <= x < self.rows and 0 <= y < self.cols

    def __getitem__(self, k):
        return self.grid[k]

    def __eq__(self, other):
        return self.grid == other.grid

    def neighbours(self, row, col, deltas):
        for i, j in deltas:
            r, c = row + i, col + j
            if (r, c) in self:
                yield self[r][c]

    def walk(self, row, col, delta):
        i, j = delta
        r, c = row + i, col + j
        while (r, c) in self:
            yield self[r][c]
            r, c = r + i, c + j

    def part1(self):
        new = [[] for _ in range(self.rows)]
        for row, col in product(range(self.rows), range(self.cols)):
            char = self[row][col]
            nbs = list(self.neighbours(row, col, DIRS))
            if char == "L" and "#" not in nbs:
                new[row].append("#")
            elif char == "#" and nbs.count("#") >= 4:
                new[row].append("L")
            else:
                new[row].append(char)
        return Grid(new)

    def part2(self):
        new = [[] for _ in range(self.rows)]
        for row, col in product(range(self.rows), range(self.cols)):
            char = self[row][col]
            nbs = []
            for d in DIRS:
                for c in self.walk(row, col, d):
                    if c in "L#":
                        nbs.append(c)
                        break
            if char == "L" and "#" not in nbs:
                new[row].append("#")
            elif char == "#" and nbs.count("#") >= 5:
                new[row].append("L")
            else:
                new[row].append(char)
        return Grid(new)


x = Grid(lines)
while True:
    g = x.part1()
    if g == x:
        print(f"Part 1: {sum(y.count('#') for y in g.grid)}")
        break
    x = g

x = Grid(lines)
while True:
    g = x.part2()
    if g == x:
        print(f"Part 2: {sum(y.count('#') for y in g.grid)}")
        break
    x = g
