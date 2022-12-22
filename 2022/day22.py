import sys
import re


def print_grid(grid, pos=None):
    minx, maxx = min(x for x, _ in grid.keys()), max(x for x, _ in grid.keys()) + 1
    miny, maxy = min(y for _, y in grid.keys()), max(y for _, y in grid.keys()) + 1
    for y in range(miny, maxy):
        row = ""
        for x in range(minx, maxx):
            row += f"\033[32;1m*\033[0m" if (x, y) == pos else grid.get((x, y), " ")
        print(row)


pat = re.compile(r"(\d+|[LR])")
facings = {0: (1, 0), 90: (0, 1), 180: (-1, 0), 270: (0, -1)}
s, path = sys.stdin.read().split("\n\n")
grid = {
    (x, y): c
    for y, l in enumerate(s.splitlines(), 1)
    for x, c in enumerate(l, 1)
    if c in ".#"
}
minx, maxx = min(x for x, _ in grid.keys()), max(x for x, _ in grid.keys()) + 1
miny, maxy = min(y for _, y in grid.keys()), max(y for _, y in grid.keys()) + 1
facing = 0
start = [(x, 1) for x in range(minx, maxx + 1) if grid.get((x, 1)) == "."][0]
x, y = start
dx, dy = 1, 0
for i, step in enumerate(pat.findall(path)):
    if step == "L":
        facing -= 90
    elif step == "R":
        facing += 90
    else:
        dx, dy = facings.get(facing % 360)
        for _ in range(int(step)):
            nx, ny = x + dx, y + dy
            cell = grid.get((nx, ny))
            if cell is None:
                nnx, nny = x, y
                while (nnx, nny) in grid:
                    nx, ny = nnx, nny
                    nnx -= dx
                    nny -= dy
                cell = grid[nx, ny]
            if cell == "#":
                break
            x, y = nx, ny
        # print_grid(grid, (x, y))
        # print("-" * maxx)

f = (facing % 360) // 90
print(sum((1000 * y, 4 * x, f)))
