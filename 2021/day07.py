import sys


def arithmetic_sum(n):
    return n * (n + 1) // 2


def solve(locs, f=lambda x: x):
    res = float("inf")
    for target in range(min(locs), max(locs) + 1):
        cost = sum(f(abs(crab - target)) for crab in locs)
        if cost < res:
            res = cost
    return res


lines = [int(x) for x in sys.stdin.read().split(",")]
print(f"Part 1: {solve(lines)}")
print(f"Part 1: {solve(lines, arithmetic_sum)}")
