import sys
from functools import cache


@cache
def compute(n):
    if n == 0:
        return (1,)
    elif len(s := str(n)) % 2 == 0:
        l = len(s) // 2
        return int(s[:l]), int(s[l:])
    else:
        return (n * 2024,)


@cache
def run(n, x):
    """run `n` for `x` steps"""
    if x == 0:
        return 1
    ret = 0
    for res in compute(n):
        ret += run(res, x - 1)
    return ret


data = list(map(int, sys.stdin.read().strip().split()))
p1 = sum(run(n, 25) for n in data)
p2 = sum(run(n, 75) for n in data)
print(p1, p2, sep="\n")
