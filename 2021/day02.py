import sys
import re

pat = re.compile(r"^(forward|up|down)\s+(\d+)$", flags=re.MULTILINE)
lines = pat.findall(sys.stdin.read())

h_pos, depth = 0, 0
for direction, val in lines:
    val = int(val)
    if direction == "forward":
        h_pos += val
    elif direction == "up":
        depth -= val
    elif direction == "down":
        depth += val
print(f"Part 1: {h_pos*depth}")

h_pos, depth, aim = 0, 0, 0
for direction, val in lines:
    val = int(val)
    if direction == "forward":
        h_pos += val
        depth += aim * val
    elif direction == "up":
        aim -= val
    elif direction == "down":
        aim += val
print(f"Part 2: {h_pos*depth}")
