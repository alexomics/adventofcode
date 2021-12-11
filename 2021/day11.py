import sys
from collections import deque
from itertools import product

DIRS = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]


class Dumbo(int):
    def __new__(cls, value, *args, **kwargs):
        return super(cls, cls).__new__(cls, value)

    def __str__(self):
        if self == 0:
            return f"\033[97;1m{self:1d}\033[0m"
        return f"\033[37m{self:1d}\033[0m"

    def __iadd__(self, other):
        return Dumbo(0 if (x := self + other) > 9 else x)


class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.flashes = 0

    def __contains__(self, t):
        x, y = t
        return 0 <= x < self.rows and 0 <= y < self.cols

    def __getitem__(self, k):
        return self.grid[k]

    def __repr__(self):
        return "\n".join("".join(f"{n}" for n in row) for row in self.grid)

    def neighbours(self, row, col, deltas):
        for dr, dc in deltas:
            r, c = row + dr, col + dc
            if (r, c) in self:
                yield r, c

    def step(self):
        q = deque()
        for row, col in product(range(self.rows), range(self.cols)):
            self[row][col] += 1
            if self[row][col] == 0:
                q.append((row, col))
        while q:
            row, col = q.popleft()
            self.flashes += 1
            for r, c in self.neighbours(row, col, DIRS):
                if self[r][c] != 0:
                    self[r][c] += 1
                    if self[r][c] == 0:
                        q.append((r, c))

    def synced(self, at):
        return all(n == at for row in self for n in row)


lines = [list(map(Dumbo, l.strip())) for l in sys.stdin]
grid = Grid(lines)

steps = 100
for _ in range(steps):
    grid.step()
print(f"Part 1: {grid.flashes}")

while not grid.synced(at=0):
    steps += 1
    grid.step()
print(f"Part 2: {steps}")
