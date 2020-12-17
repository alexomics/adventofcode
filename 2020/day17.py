import sys
from itertools import product


class Grid(dict):
    def bounds(self):
        return zip(map(min, zip(*self.keys())), map(max, zip(*self.keys())))

    def neighbour_deltas(self):
        dims = len(list(self.keys())[0])
        yield from (k for k in product([1, 0, -1], repeat=dims) if any(k))

    def iter_neighbours(self, loc):
        for k in self.neighbour_deltas():
            k = tuple(sum(p) for p in zip(loc, k))
            yield self.get(k, False)

    def cycle(self, n):
        for _ in range(n):
            new = Grid()
            bounds = product(*[range(a - 1, b + 2) for a, b in self.bounds()])
            for i in bounds:
                active = self.get(i, False)
                count = 0
                for n in self.iter_neighbours(i):
                    count += n
                if (active and count in (2, 3)) or (not active and count == 3):
                    new[i] = True
            self.clear()
            self.update(new)


lines = [l.strip() for l in open(sys.argv[1])]
grid = Grid({(j, i, 0): c == "#" for i, l in enumerate(lines) for j, c in enumerate(l)})
grid.cycle(6)
print(f"Part 1: {sum(grid.values())}")
grid = {(j, i, 0, 0): c == "#" for i, l in enumerate(lines) for j, c in enumerate(l)}
grid = Grid(grid)
grid.cycle(6)
print(f"Part 2: {sum(grid.values())}")
