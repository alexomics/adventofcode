import sys
from dataclasses import dataclass


DIRS = {
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
    "^": (0, -1),
}


@dataclass
class Grid:
    input: str
    grid: list[list[str]]
    dirs: str
    curr: tuple[int, int]

    @classmethod
    def from_str(cls, s):
        grid, dirs = s.split("\n\n")
        grid = [list(l) for l in grid.splitlines()]
        x, y = next(
            (x, y) for y, l in enumerate(grid) for x, c in enumerate(l) if c == "@"
        )
        return cls(s, grid, dirs.replace("\n", ""), (x, y))

    @property
    def x(self):
        return len(self.grid[0])

    @property
    def y(self):
        return len(self.grid)

    def _gen_grid_rows(self, colour=False):
        yield from ("".join(r) for r in self.grid)

    def print(self, pre=None, post=None):
        if pre is not None:
            print(pre)
        for row in self._gen_grid_rows():
            print(row)
        if post is not None:
            print(post)

    def gps_sum(self, boxes):
        return sum(
            100 * y + x
            for y, l in enumerate(self.grid)
            for x, c in enumerate(l)
            if c in boxes
        )

    def part1(self):
        x, y = self.curr
        for dx, dy in map(DIRS.get, self.dirs):
            nx, ny = x + dx, y + dy
            if self.grid[ny][nx] == ".":
                self.grid[ny][nx], self.grid[y][x] = self.grid[y][x], self.grid[ny][nx]
                x, y = nx, ny
                continue
            while self.grid[ny][nx] not in "#.":
                nx += dx
                ny += dy
            if self.grid[ny][nx] == "#":
                continue
            self.grid[ny][nx] = "O"
            self.grid[y][x] = "."
            x += dx
            y += dy
            self.grid[y][x] = "@"

        return self.gps_sum("O")

    def expand_map_inplace(self):
        grid, _ = self.input.split("\n\n")
        changes = {"#": "##", "O": "[]", ".": "..", "@": "@."}
        grid = [list("".join(map(changes.get, l))) for l in grid.splitlines()]
        x, y = next(
            (x, y) for y, l in enumerate(grid) for x, c in enumerate(l) if c == "@"
        )
        self.grid, self.curr = grid, (x, y)

    def part2(self):
        x, y = self.curr
        # self.print("Initial state:", "")
        for dx, dy in map(DIRS.get, self.dirs):
            nx, ny = x + dx, y + dy
            if self.grid[ny][nx] == ".":
                self.grid[ny][nx], self.grid[y][x] = self.grid[y][x], self.grid[ny][nx]
                x, y = nx, ny
                continue
            if dy == 0:
                # Easy, shift boxes in a single horizontal line
                while self.grid[y][nx] not in "#.":
                    nx += dx
                if self.grid[y][nx] == "#":
                    continue
                for nx in range(nx, x + dx, -dx):
                    self.grid[y][nx] = self.grid[y][nx - dx]
                self.grid[y][x] = "."
                x += dx
                self.grid[y][x] = "@"
            else:
                # 🤮 vertical movement
                ny = y
                xs = [x]
                boxes = []
                # While no walls and not all clear space above any boxes we've found
                while not any(self.grid[ny + dy][nx] == "#" for nx in xs) and not all(
                    self.grid[ny + dy][nx] == "." for nx in xs
                ):
                    ny += dy
                    new_xs = set()
                    for nx in xs:
                        if self.grid[ny][nx] == "[":
                            new_xs.add(nx)
                            new_xs.add(nx + 1)
                            boxes.extend([(nx, ny, "["), (nx + 1, ny, "]")])
                        elif self.grid[ny][nx] == "]":
                            new_xs.add(nx - 1)
                            new_xs.add(nx)
                            boxes.extend([(nx - 1, ny, "["), (nx, ny, "]")])
                    xs = new_xs

                if any(self.grid[ny + dy][nx] == "#" for nx in xs):
                    continue

                # clear old boxes; add new boxes
                for bx, by, _ in boxes:
                    self.grid[by][bx] = "."
                for bx, by, c in boxes:
                    self.grid[by + dy][bx] = c

                self.grid[y][x] = "."
                y += dy
                self.grid[y][x] = "@"

        return self.gps_sum("O[")


p1 = p2 = 0
data = sys.stdin.read()
grid = Grid.from_str(data)
# grid.print()
p1 = grid.part1()
grid.expand_map_inplace()
p2 = grid.part2()
# grid.print()
print(p1, p2, sep="\n")
