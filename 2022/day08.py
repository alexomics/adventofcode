import sys


s = sys.stdin.read().splitlines()
grid = {(x, y): val for y, row in enumerate(s) for x, val in enumerate(row)}


def visible(x, y):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        obscured = False
        while (nx, ny) in grid:
            if grid[nx, ny] >= grid[x, y]:
                obscured = True
                break
            nx += dx
            ny += dy
        if not obscured:
            return True
    return False


def score(x, y):
    score = 1
    self = grid[x, y]
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        count = 0
        nx, ny = x + dx, y + dy
        while (nx, ny) in grid:
            curr = grid[nx, ny]
            if curr < self:
                count += 1
                nx += dx
                ny += dy
            else:
                count += 1
                break
        score *= count
    return score


print("Part 1:", sum(visible(*coords) for coords in grid.keys()))
print("Part 2:", max(score(*coords) for coords in grid.keys()))
