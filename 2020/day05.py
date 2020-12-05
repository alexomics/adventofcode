import sys


def split_(min_, max_, s):
    for chr_ in s:
        mid = min_ + (max_ - min_) // 2
        if chr_ in "FL":
            max_ = mid
        else:
            min_ = mid + 1
    return min_


lines = [l.strip() for l in open(sys.argv[1])]

r = [8 * split_(0, 127, l[:7]) + split_(0, 7, l[-3:]) for l in lines]

print(f"Part 1: {max(r)}")

r = set(r)
for i in range(min(r), max(r)):
    if i not in r:
        print(f"Part 2: {i}")
