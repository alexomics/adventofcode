import sys
from dataclasses import dataclass


def area(x, y, border):
    "https://rosettacode.org/wiki/Shoelace_formula_for_polygonal_area"
    s1 = sum(i * j for i, j in zip(x, y[1:] + y[:1]))
    s2 = sum(i * j for i, j in zip(x[1:] + x[:1], y))
    s = abs(s1 - s2) / 2
    return int(s + border / 2 + 1)


@dataclass
class Step:
    dir: str
    len: int
    col: str

    @classmethod
    def from_str(cls, s):
        d, l, c = s.strip().split()
        return cls(d, int(l), c[1:-1])

    def corrected(self):
        conv = {"0": "R", "1": "D", "2": "L", "3": "U"}
        d = conv[self.col[-1]]
        l = int("0x" + self.col[1:6], 16)
        return Step(d, l, self.col)


@dataclass
class Poly:
    steps: list[Step]

    def area(self):
        dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        loc, x, y, border = (0, 0), [], [], 0
        for i in self.steps:
            r, c = loc
            dr, dc = dirs[i.dir]
            x.append(r + i.len * dr)
            y.append(c + i.len * dc)
            border += i.len
            loc = (x[-1], y[-1])
        return area(x, y, border)


s1 = [Step.from_str(s) for s in sys.stdin]
s2 = [s.corrected() for s in s1]
p1, p2 = Poly(s1), Poly(s2)
print(p1.area())
print(p2.area())
