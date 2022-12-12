import sys
from heapq import heappop, heappush


DIRS = [(1, 0), (0, -1), (-1, 0), (0, 1)]


class Grid(dict):
    _rows = None
    _cols = None

    def __repr__(self):
        return "\n".join(
            "".join(f"{self[row, col]}" for col in range(self.cols))
            for row in range(self.rows)
        )

    def _neighbours(self, row, col, deltas=DIRS):
        for dr, dc in deltas:
            r, c = row + dr, col + dc
            if (r, c) in self:
                yield r, c

    def valid_neighbours(self, row, col, deltas=DIRS):
        cur = self[row, col]
        for r, c in self._neighbours(row, col, deltas):
            val = grid[r, c]
            if cur == "S":
                if val in "ab":
                    yield r, c
            elif val == "E":
                if cur in "yz":
                    yield r, c
            elif ord(val) - ord(cur) <= 1:
                yield r, c

    def traverse(self, start, target):
        """This is, I think, Dijkstra's algorithm."""
        # (distance, current coord)
        heap = [(0, start)]
        seen = set()
        while heap:
            dist, node = heappop(heap)
            if node == target:
                return dist

            if node in seen:
                continue
            seen.add(node)

            for neighbor in self.valid_neighbours(*node):
                if neighbor in seen:
                    continue
                heappush(heap, (dist + 1, neighbor))

    @property
    def cols(self):
        if self._cols is None:
            self._cols = max(c for _, c in self.keys()) + 1
        return self._cols

    @property
    def rows(self):
        if self._rows is None:
            self._rows = max(c for c, _ in self.keys()) + 1
        return self._rows

    @staticmethod
    def from_str(s, func=lambda x: x):
        return Grid(
            {
                (r, c): func(n)
                for r, line in enumerate(s.splitlines())
                for c, n in enumerate(line.strip())
            }
        )


s = sys.stdin.read()
grid = Grid.from_str(s)
start, target = False, False
for k, v in grid.items():
    if v == "S":
        start = k
    if v == "E":
        target = k
    if start and target:
        break

p1 = grid.traverse(start, target)
print("Part 1:", p1)

p2 = [
    a
    for s in (k for k, v in grid.items() if v in "Sa")
    if (a := grid.traverse(s, target)) is not None
]
print("Part 2:", min(p2))
