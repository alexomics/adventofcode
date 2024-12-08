import sys
from collections import defaultdict
from itertools import combinations

data = sys.stdin.read()
grid = defaultdict(list)
p1, p2 = set(), set()
mx, my = 0, 0
for y, line in enumerate(data.splitlines()):
    for x, c in enumerate(line):
        mx = max(x, mx)
        if c == ".":
            continue
        grid[c].append((x, y))
        p2.add((x, y))
    my = max(y, my)

for char, locs in grid.items():
    for (ax, ay), (bx, by) in combinations(locs, 2):
        dx, dy = abs(ax - bx), abs(ay - by)
        ax_, bx_ = (ax + dx, bx - dx) if ax >= bx else (ax - dx, bx + dx)
        ay_, by_ = (ay + dy, by - dy) if ay >= by else (ay - dy, by + dy)
        p1a, p1b = (ax_, ay_), (bx_, by_)
        while 0 <= ax_ <= mx and 0 <= ay_ <= my:
            if p1a not in p1:
                p1.add(p1a)
            p2.add((ax_, ay_))
            ax_ = ax_ + dx if ax >= bx else ax_ - dx
            ay_ = ay_ + dy if ay >= by else ay_ - dy
        while 0 <= bx_ <= mx and 0 <= by_ <= my:
            if p1b not in p1:
                p1.add(p1b)
            p2.add((bx_, by_))
            bx_ = bx_ - dx if ax >= bx else bx_ + dx
            by_ = by_ - dy if ay >= by else by_ + dy

print(len(p1), len(p2), sep="\n")
