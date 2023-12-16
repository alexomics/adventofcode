import sys
from collections import Counter, defaultdict


data = sys.stdin.read().splitlines()
grid = {(row, col): v for row, line in enumerate(data) for col, v in enumerate(line)}
rows = len(data)
cols = len(data[0])
dirs = {"u": (-1, 0), "r": (0, 1), "d": (1, 0), "l": (0, -1)}
start = (0, 0)


def move(r, c, d):
    dr, dc = dirs[d]
    return (r + dr, c + dc, d)


def walk(g, rows, cols, row, col, dir_):
    steps = [(row, col, dir_)]
    seen = defaultdict(Counter)  # dict[(r, c), Counter[d, int]]
    while True:
        next_steps = []
        if not steps:
            break
        for r, c, d in steps:
            if 0 <= r < rows and 0 <= c < cols:
                if d in seen[(r, c)]:
                    continue
                seen[(r, c)][d] += 1
                char = grid[(r, c)]
                if char == ".":
                    next_steps.append(move(r, c, d))
                elif char == "/":
                    d = {"u": "r", "r": "u", "d": "l", "l": "d"}[d]
                    next_steps.append(move(r, c, d))
                elif char == "\\":
                    d = {"u": "l", "l": "u", "d": "r", "r": "d"}[d]
                    next_steps.append(move(r, c, d))
                elif char == "|":
                    if d in "ud":
                        next_steps.append(move(r, c, d))
                    else:
                        next_steps.append(move(r, c, "u"))
                        next_steps.append(move(r, c, "d"))
                elif char == "-":
                    if d in "rl":
                        next_steps.append(move(r, c, d))
                    else:
                        next_steps.append(move(r, c, "r"))
                        next_steps.append(move(r, c, "l"))
        steps = next_steps
    return len(seen)


print(walk(grid, rows, cols, 0, 0, "r"))
b = cols - 1
l = rows - 1
p2 = max(
    *(walk(grid, rows, cols, r, 0, "r") for r in range(rows)),
    *(walk(grid, rows, cols, r, b, "l") for r in range(rows)),
    *(walk(grid, rows, cols, 0, c, "d") for c in range(cols)),
    *(walk(grid, rows, cols, c, l, "u") for c in range(cols)),
)
print(p2)
