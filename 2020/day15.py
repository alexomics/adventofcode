from collections import defaultdict, deque
from functools import partial
from operator import sub

nums = [0, 14, 1, 3, 7, 9]
d = defaultdict(partial(deque, maxlen=2))
for i, n in enumerate(nums):
    d[n].append(i)


def run(prev, start, stop, d_=d):
    for i in range(start, stop):
        if len(d_[prev]) == 1:
            num_spoken = 0
        else:
            num_spoken = sub(*d_[prev])
        d_[num_spoken].appendleft(i)
        prev = num_spoken
    return num_spoken, i


p1, start = run(nums[-1], len(nums), 2020)
print(f"Part 1: {p1}")
p2, _ = run(p1, start + 1, 30_000_000)
print(f"Part 2: {p2}")
