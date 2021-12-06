import sys
from collections import Counter


line = list(map(int, sys.stdin.read().strip().split(",")))


def grow_days(init, days):
    age_counts = Counter(init)

    for day in range(days):
        d = Counter()
        for age, n in age_counts.items():
            if age > 0:
                d[age - 1] += n
            else:
                d[6] += n
                d[8] += n
        age_counts = d
    return sum(age_counts.values())


print(f"Part 1: {grow_days(line, 80)}")
print(f"Part 2: {grow_days(line, 256)}")
