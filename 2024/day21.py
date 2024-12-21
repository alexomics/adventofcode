import sys
from collections import deque, Counter
from functools import cache

# fmt: off
moves = {">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1)}
numeric = {
    (0, 0): "7", (1, 0): "8", (2, 0): "9",
    (0, 1): "4", (1, 1): "5", (2, 1): "6",
    (0, 2): "1", (1, 2): "2", (2, 2): "3",
                 (1, 3): "0", (2, 3): "A",
}
numeric.update({v: k for k, v in numeric.items()})
directional = {
                 (1, 0): "^", (2, 0): "A",
    (0, 1): "<", (1, 1): "v", (2, 1): ">",
}
directional.update({v: k for k, v in directional.items()})
# fmt: on
codes = sys.stdin.read().strip().splitlines()


@cache
def jump(grid_, curr, target):
    grid = {0: numeric, 1: directional}[grid_]
    cx, cy = curr
    tx, ty = target
    dx, dy = tx - cx, ty - cy
    h = "<" * -dx if dx < 0 else ">" * dx
    v = "^" * -dy if dy < 0 else "v" * dy
    # Check corners so we don't fall of the grid
    if dx > 0 and (cx, ty) in grid:
        return f"{v}{h}A"
    if (tx, cy) in grid:
        return f"{h}{v}A"
    if (cx, ty) in grid:
        return f"{v}{h}A"
    raise TabError(f"{curr=} {target=} {(dx,dy)=} {grid=}")


p1, p2 = 0, 0
for code in codes:
    n = int(code[:-1])
    pads = deque(
        [(0, numeric, (2, 3)), (1, directional, (2, 0)), (1, directional, (2, 0))]
    )
    while pads:
        g_, g, pos = pads.popleft()
        res = []
        for char in code:
            res.append(jump(g_, pos, g[char]))
            pos = g[char]
        code = "".join(res)
    p1 += len(code) * n

print(p1, p2, sep="\n")
