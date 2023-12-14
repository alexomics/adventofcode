import sys

data = sys.stdin.read().split("\n")
grid = {(row, col): v for row, line in enumerate(data) for col, v in enumerate(line)}
rows = max(r for r, c in grid) + 1
cols = max(c for r, c in grid) + 1


def state(g, rows, cols):
    return "\n".join("".join(g[(r, c)] for c in range(cols)) for r in range(rows))


def tilt(g, d, rows, cols):
    dr, dc = d
    ir = range(rows - 1, -1, -1) if d == (1, 0) else range(rows)
    ic = range(cols - 1, -1, -1) if d == (0, 1) else range(cols)
    it = ((row, col) for col in ic for row in ir)
    for row, col in it:
        nr, nc = row + dr, col + dc
        while (
            g[(row, col)] == "O"
            and 0 <= nr < rows
            and 0 <= nc < cols
            and g.get((nr, nc), None) == "."
        ):
            g[(row, col)] = "."
            g[(nr, nc)] = "O"
            row, col = nr, nc
            nr, nc = row + dr, col + dc
    return g


def score(grid, rows, cols):
    return sum(
        (rows - r) * sum(grid[(r, c)] == "O" for c in range(cols)) for r in range(rows)
    )


seen = {}
target = 1_000_000_000
t = 0
p1 = None
while t < target:
    t += 1
    for c in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        grid = tilt(grid, c, rows, cols)
        if p1 is None:
            p1 = score(grid, rows, cols)
    g = state(grid, rows, cols)
    if g in seen:
        cycle_length = t - seen[g]
        count = (target - t) // cycle_length
        t += count * cycle_length
    seen[g] = t
print(p1)
print(score(grid, rows, cols))
