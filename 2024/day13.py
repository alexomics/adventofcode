import sys
import re
from dataclasses import dataclass


@dataclass
class XY:
    x: int
    y: int


data = [
    [XY(*map(int, re.findall("\d+", l))) for l in g.splitlines()]
    for g in sys.stdin.read().split("\n\n")
]


def solve_by_substitution(a, b, p):
    """Solve simultaneous equation by substitution
    px = ax * a + bx * b
    py = ay * a + by * b

    a = (px - bx * b) / ax
    py = ay * ((px - bx * b) / ax) + by * b
    py = ay / ax * (px - bx * b) + by * b
    py = ay / ax * px - ay / ax * bx * b + by * b
    py = ay / ax * px - (ay / ax * bx - by) * b
    b = (ay / ax * px - py) / (ay / ax * bx - by)
    """
    b_ = round((a.y / a.x * p.x - p.y) / (a.y / a.x * b.x - b.y))
    a_ = (p.x - b.x * b_) // a.x
    if a.x * a_ + b.x * b_ == p.x and a.y * a_ + b.y * b_ == p.y:
        return 3 * a_ + b_
    else:
        return 0


p1, p2 = 0, 0
for a, b, p in data:
    p1 += solve_by_substitution(a, b, p)
    p.x += 10_000_000_000_000
    p.y += 10_000_000_000_000
    p2 += solve_by_substitution(a, b, p)

print(p1, p2, sep="\n")
