import sys
import re
from dataclasses import dataclass, field


@dataclass
class XY:
    x: int
    y: int

    @property
    def t(self):
        return (self.x, self.y)


@dataclass
class Robot:
    start: XY
    velocity: XY
    curr: XY = field(init=False)

    def __post_init__(self):
        self.curr = XY(*self.start.t)

    @classmethod
    def from_tuple(cls, t):
        px, py, vx, vy = t
        return cls(XY(px, py), XY(vx, vy))

    def simulate(self, steps, xbound, ybound):
        for _ in range(steps):
            self.curr.x += self.velocity.x
            self.curr.y += self.velocity.y
            while self.curr.x < 0:
                self.curr.x += xbound
            while self.curr.x >= xbound:
                self.curr.x -= xbound
            while self.curr.y < 0:
                self.curr.y += ybound
            while self.curr.y >= ybound:
                self.curr.y -= ybound


@dataclass
class Grid:
    x: int
    y: int
    robots: list[Robot]

    @classmethod
    def from_str(cls, s):
        s = s.splitlines()
        x = 11 if len(s) < 100 else 101
        y = 7 if len(s) < 100 else 103
        robots = [Robot.from_tuple(map(int, re.findall(r"-?[0-9]+", l))) for l in s]
        return cls(x, y, robots)

    def _gen_grid_rows(self, colour=False):
        char = f"\033[32;1m#\033[0m" if colour else "#"
        grid = {r.curr.t: char for r in self.robots}
        for y in range(0, self.y):
            row = ""
            for x in range(0, self.x):
                row += grid.get((x, y), ".")
            yield row

    def print(self):
        for row in self._gen_grid_rows(colour=True):
            print(row)

    def simulate(self, steps):
        for r in self.robots:
            r.simulate(steps, self.x, self.y)

    def safety_factor(self):
        a = b = c = d = 0
        midx = self.x // 2
        midy = self.y // 2
        for r in self.robots:
            if r.curr.x < midx and r.curr.y < midy:
                a += 1
            if r.curr.x > midx and r.curr.y < midy:
                b += 1
            if r.curr.x < midx and r.curr.y > midy:
                c += 1
            if r.curr.x > midx and r.curr.y > midy:
                d += 1
        return a * b * c * d

    def find(self, s):
        for row in self._gen_grid_rows():
            if s in row:
                return True
        return False


data = sys.stdin.read().strip()
steps = 100
grid = Grid.from_str(data)
grid.simulate(steps)
p1 = grid.safety_factor()
target = "###############################"
while not grid.find(target):
    grid.simulate(1)
    steps += 1
# grid.print()
p2 = steps
print(p1, p2, sep="\n")
