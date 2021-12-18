import sys
from ast import literal_eval
from math import ceil
from itertools import permutations
from collections import deque


def magnitude(seq):
    """
    >>> magnitude([[1,2],[[3,4],5]])
    143
    >>> magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]])
    1384
    >>> magnitude([[[[1,1],[2,2]],[3,3]],[4,4]])
    445
    >>> magnitude([[[[3,0],[5,3]],[4,4]],[5,5]])
    791
    >>> magnitude([[[[5,0],[7,4]],[5,5]],[6,6]])
    1137
    >>> magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])
    3488
    """
    a, b = seq
    if isinstance(a, list):
        a = magnitude(a)
    if isinstance(b, list):
        b = magnitude(b)
    return 3 * a + 2 * b


def add_left(seq, n):
    if isinstance(seq, list):
        return [add_left(seq[0], n), seq[1]]
    return seq + n


def add_right(seq, n):
    if isinstance(seq, list):
        return [seq[0], add_right(seq[1], n)]
    return seq + n


def explode(seq, depth=0):
    """
    The left value is added to the first number to the left.
    The right value is added to the first number to the right.

    >>> explode([[[[[9,8],1],2],3],4])
    (True, [[[[0, 9], 2], 3], 4])
    >>> explode([7,[6,[5,[4,[3,2]]]]])
    (True, [7, [6, [5, [7, 0]]]])
    >>> explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])
    (True, [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]])
    """

    def _explode(seq, depth):
        if isinstance(seq, int):
            return False, seq, 0, 0
        a, b = seq
        if depth < 4:
            exploded, next_a, left, right = _explode(a, depth + 1)
            if exploded:
                seq = [next_a, add_left(b, right)]
                return True, seq, left, 0
            exploded, next_b, left, right = _explode(b, depth + 1)
            if exploded:
                seq = [add_right(a, left), next_b]
                return True, seq, 0, right
            return False, seq, 0, 0
        else:
            return True, 0, a, b

    changed, seq, _, _ = _explode(seq, depth)
    return changed, seq


def split(seq, n=10):
    """
    >>> split(10)
    (True, [5, 5])
    >>> split(11)
    (True, [5, 6])
    >>> split(12)
    (True, [6, 6])
    """
    if isinstance(seq, int):
        if seq >= n:
            return True, [seq // 2, ceil(seq / 2)]
        return False, seq
    a, b = seq
    changed, a = split(a, n)
    if changed:
        return True, [a, b]
    changed, b = split(b, n)
    return changed, [a, b]


def add(l, r):
    s = [l, r]
    while True:
        changed, s = explode(s)
        if changed:
            continue
        changed, s = split(s)
        if not changed:
            break
    return s


lines = list(map(literal_eval, sys.stdin.read().splitlines()))
it = iter(lines)
x = next(it)
for y in it:
    x = add(x, y)

print(f"Part 1: {magnitude(x)}")
mags = [magnitude(add(l, r)) for l, r in permutations(lines, 2)]
print(f"Part 2: {max(mags)}")

if any(f in sys.argv for f in ("-v", "-vv")):
    import doctest

    doctest.testmod(verbose="-vv" in sys.argv)
