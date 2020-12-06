import sys

line = [l.strip() for l in open(sys.argv[1])][0]


class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = set()

    def move(self, direction):
        if direction == "^":
            self.y += 1
        elif direction == ">":
            self.x += 1
        elif direction == "v":
            self.y -= 1
        elif direction == "<":
            self.x -= 1
        else:
            raise RuntimeError("direction {direction!r} not recognised")
        self.visited.add((self.x, self.y))


grid = Grid(0, 0)
for c in line:
    grid.move(c)
print(f"Part 1: {len(grid.visited)}")

santa = Grid(0, 0)
robot = Grid(0, 0)
for i, c in enumerate(line):
    if i % 2 == 0:
        santa.move(c)
    else:
        robot.move(c)
print(f"Part 2: {len(santa.visited | robot.visited)}")
