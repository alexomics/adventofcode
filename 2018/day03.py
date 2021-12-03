import sys
import re
from collections import defaultdict

# Line format
# #<ID> @ <LEFT>,<TOP>: <WIDTH>X<HEIGHT>
pat = re.compile(r"^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$", flags=re.MULTILINE)
lines = [tuple(map(int, x)) for x in pat.findall(sys.stdin.read())]

# print(lines)
seen = defaultdict(int)
overlaps = 0
for id_, left, top, width, height in lines:
    for y in range(top, top + height):
        for x in range(left, left + width):
            seen[(x, y)] += 1

print(f"Part 1: {sum(v > 1 for v in seen.values())}")

res_id = None
for id_, left, top, width, height in lines:
    if any(
        seen[(x, y)] > 1
        for y in range(top, top + height)
        for x in range(left, left + width)
    ):
        continue
    else:
        res_id = id_
        break
print(f"Part 2: {res_id}")
