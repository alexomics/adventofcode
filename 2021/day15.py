import sys
from heapq import heappop, heappush

DIRS = [(1, 0), (0, -1), (-1, 0), (0, 1)]


class RollingInt(int):
    _min = 1
    _max = 9

    def __new__(cls, value, *args, **kwargs):
        return super().__new__(cls, value)

    def __add__(self, other):
        return self.__class__(
            x if (x := super().__add__(other) % self._max) else self._max
        )


class Grid(dict):
    _rows = None
    _cols = None

    def __repr__(self):
        return "\n".join(
            "".join(f"{self[row, col]}" for col in range(self.cols))
            for row in range(self.rows)
        )

    def neighbours(self, row, col, deltas=DIRS):
        for dr, dc in deltas:
            r, c = row + dr, col + dc
            if (r, c) in self:
                yield r, c

    def traverse(self, start, target):
        """This is, I think, Dijkstra's algorithm."""
        # distance, row, col
        heap = [(0, 0, 0)]
        seen = {start}
        t_row, t_col = target
        while heap:
            distance, row, col = heappop(heap)
            if col == t_col and row == t_row:
                return distance

            for r, c in self.neighbours(row, col):
                n = self[r, c]
                if (r, c) not in seen:
                    seen.add((r, c))
                    heappush(heap, (distance + n, r, c))

    @property
    def cols(self):
        if self._cols is None:
            self._cols = max(c for _, c in self.keys()) + 1
        return self._cols

    @property
    def rows(self):
        if self._rows is None:
            self._rows = max(c for _, c in self.keys()) + 1
        return self._rows

    @staticmethod
    def from_str(s, inc=0, func=RollingInt):
        return Grid(
            {
                (r, c): func(n) + inc
                for r, line in enumerate(s.splitlines())
                for c, n in enumerate(line.strip())
            }
        )


grid = Grid.from_str(sys.stdin.read())
print("Part 1:", grid.traverse((0, 0), (grid.rows - 1, grid.cols - 1)))

expanded_grid = [[Grid.from_str(repr(grid), i + j) for i in range(5)] for j in range(5)]
new = {}
for i, row in enumerate(expanded_grid):
    for j, grid in enumerate(row):
        for (row, col), val in grid.items():
            new[(row + i * grid.rows, col + j * grid.cols)] = val

grid = Grid(new)
print("Part 2:", grid.traverse((0, 0), (grid.rows - 1, grid.cols - 1)))
