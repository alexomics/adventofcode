import sys
import re
from array import array

pat = re.compile(r"^(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)$")
lines = [pat.findall(l)[0] for l in open(sys.argv[1])]
arr1 = [array("B", [0] * 1000) for _ in range(1000)]
arr2 = [array("B", [0] * 1000) for _ in range(1000)]
for inst, *nums in lines:
    x1, y1, x2, y2 = map(int, nums)
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if inst == "toggle":
                arr1[x][y] ^= 1
                arr2[x][y] += 2
            elif inst == "turn on":
                arr1[x][y] = 1
                arr2[x][y] += 1
            elif inst == "turn off":
                arr1[x][y] = 0
                arr2[x][y] -= 1 if arr2[x][y] > 0 else 0

print(f"Part 1: {sum(sum(a) for a in arr1)}")
print(f"Part 2: {sum(sum(a) for a in arr2)}")
