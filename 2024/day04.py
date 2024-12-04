import sys


P1_DIRS = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
P2_DIRS = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
data = sys.stdin.read()
grid = {
    (x, y): c for y, line in enumerate(data.splitlines()) for x, c in enumerate(line)
}

p1, p2 = 0, 0
for (x, y), c in grid.items():
    for dx, dy in P1_DIRS:
        p1 += (
            c == "X"
            and grid.get((x + dx * 1, y + dy * 1), "") == "M"
            and grid.get((x + dx * 2, y + dy * 2), "") == "A"
            and grid.get((x + dx * 3, y + dy * 3), "") == "S"
        )
    p2 += c == "A" and [grid.get((x + dx, y + dy), "") for (dx, dy) in P2_DIRS] in [
        ["S", "S", "M", "M"],
        ["M", "S", "S", "M"],
        ["S", "M", "M", "S"],
        ["M", "M", "S", "S"],
    ]

print(p1, p2, sep="\n")
