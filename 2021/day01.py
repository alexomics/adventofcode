import sys

lines = list(map(int, sys.stdin.readlines()))


def count_inc(it):
    return sum(i < j for i, j in zip(it, it[1:]))


print(f"Part 1: {count_inc(lines)}")
lines = [sum(lines[i : i + 3]) for i in range(len(lines) + 1)]
print(f"Part 2: {count_inc(lines)}")
