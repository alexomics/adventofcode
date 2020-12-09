import sys
from itertools import combinations


nums = [int(l) for l in open(sys.argv[1])]
pre = 25

for i in range(pre, len(nums)):
    n = nums[i]
    if n not in [a + b for a, b in combinations(nums[i - pre : i], 2)]:
        ans = n
        break
print(f"Part 1: {ans}")

for i in range(len(nums)):
    j, x = 0, 0
    while x < ans:
        j += 1
        x = sum(nums[i:j])
    if x == ans:
        break

ans = nums[i:j]
print(f"Part 2: {min(ans) + max(ans)}")
