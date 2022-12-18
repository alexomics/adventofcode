import sys
import re

PAT = re.compile(r"(\d+)")
s = sys.stdin.read().splitlines()
d = {tuple(map(int, PAT.findall(line))) for line in s}


def adjacents(x, y, z):
    yield x + 1, y, z
    yield x - 1, y, z
    yield x, y + 1, z
    yield x, y - 1, z
    yield x, y, z + 1
    yield x, y, z - 1


print("Part 1:", sum(c not in d for k in d for c in adjacents(*k)))

# Get the bounding box with some padding
min_x = min(x for x, _, _ in d) - 1
max_x = max(x for x, _, _ in d) + 1
min_y = min(y for _, y, _ in d) - 1
max_y = max(y for _, y, _ in d) + 1
min_z = min(z for _, _, z in d) - 1
max_z = max(z for _, _, z in d) + 1

# [BF] Search the outside counting faces we can reach
stack = [(min_x, min_y, min_z)]
seen = set()
count = 0
while stack:
    c = stack.pop()
    if c in seen:
        continue
    seen.add(c)
    for x, y, z in adjacents(*c):
        if (x, y, z) in d:
            # On the outside
            count += 1
        elif (x, y, z) not in seen and all(
            (
                min_x <= x <= max_x,
                min_y <= y <= max_y,
                min_z <= z <= max_z,
            )
        ):
            stack.append((x, y, z))
print("Part 2:", count)
