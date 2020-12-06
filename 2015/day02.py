import sys
import math

lines = [list(map(int, l.strip().split("x"))) for l in open(sys.argv[1])]
area = 0
ribbon = 0
for l, w, h in lines:
    sides = (h * l, h * w, l * w)
    area += 2 * sum(sides) + min(sides)
    arr = sorted([l, w, h])
    a, b, _ = arr
    ribbon += 2 * (a + b) + math.prod(arr)
print(f"Part 1: {area}")
print(f"Part 2: {ribbon}")
