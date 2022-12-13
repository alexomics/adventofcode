import sys
from ast import literal_eval
import itertools
import functools


def cmp(a, b):
    """https://docs.python.org/3.0/whatsnew/3.0.html#ordering-comparisons"""
    return (a > b) - (a < b)


def compare(x, y):
    """Comparison function
    https://docs.python.org/3/howto/sorting.html#comparison-functions
    if x < y: return -1
    if x > y: return  1
    if x = y: return  0
    """
    if isinstance(x, int) and isinstance(y, int):
        return cmp(x, y)

    if isinstance(x, int):
        return compare([x], y)

    if isinstance(y, int):
        return compare(x, [y])

    for left, right in zip(x, y):
        if c := compare(left, right):
            return c
    return compare(len(x), len(y))


s = sys.stdin.read().split("\n\n")
lines = [list(map(literal_eval, ls.splitlines())) for ls in s]
print("Part 1:", sum(i for i, (l, r) in enumerate(lines, 1) if compare(l, r) < 0))
lines = sorted(
    list(itertools.chain(*lines)) + [[[2]], [[6]]], key=functools.cmp_to_key(compare)
)
a = lines.index([[2]]) + 1
b = lines.index([[6]]) + 1
print("Part 2:", a * b)
