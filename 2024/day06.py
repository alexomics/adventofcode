import sys

data = sys.stdin.read()
grid = {
    (x, y): c for y, line in enumerate(data.splitlines()) for x, c in enumerate(line)
}
start = next(p for p, char in grid.items() if char == "^")
TURNS = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}


def walk(g, p, d):
    path, seen = [], set()
    while p in g:
        if (p, d) in seen:
            # loop, bail
            return []
        path.append((p, d))
        seen.add((p, d))
        while g.get(next_pos := (p[0] + d[0], p[1] + d[1])) == "#":
            d = TURNS[d]
        p = next_pos
    return path


path = walk(grid, start, (0, -1))
p1 = len({pos for (pos, _) in path})
# Go backwards through the path and the step before, for each position record
# the previous position and direction. Then add an obstacle at every position
# and walk the grid again counting the loops we find.
first_entries = {
    pos: (prev_pos, prev_dir)
    for (prev_pos, prev_dir), (pos, _) in zip(path[-2::-1], path[-1::-1])
    if pos != start
}
p2 = sum(
    not walk(grid | {pos: "#"}, prev_pos, prev_dir)
    for pos, (prev_pos, prev_dir) in first_entries.items()
)
print(p1, p2, sep="\n")
