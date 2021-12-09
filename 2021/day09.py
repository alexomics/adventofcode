import sys

INF = float("inf")
dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

d = {
    (row, col): int(n)
    for row, line in enumerate(sys.stdin)
    for col, n in enumerate(line.strip())
}
c = sum(
    n + 1
    for (y, x), n in d.items()
    if all(n < d.get((y + dy, x + dx), INF) for dy, dx in dirs)
)

print(f"Part 1: {c}")

basins, seen = [], set()
for loc, n in d.items():
    if loc not in seen and n < 9:
        # We're in a new basin
        size = 0
        pos = [loc]
        while pos:
            # Search around for all other points in the basin
            loc_ = pos.pop(0)
            if loc_ in seen:
                continue
            seen.add(loc_)
            size += 1
            y, x = loc_
            others = [
                (y + dy, x + dx) for dy, dx in dirs if d.get((y + dy, x + dx), INF) < 9
            ]
            pos.extend(others)
        # Done with this basin
        basins.append(size)
basins.sort(reverse=True)
print(f"Part 2: {basins[0] * basins[1] * basins[2]}")
