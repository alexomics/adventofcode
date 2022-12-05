import sys
import re
from collections import deque
from itertools import zip_longest

pat = re.compile(r"\d+")
s = sys.stdin.read()
start, moves = s.split("\n\n")


def transpose(sequences):
    return list(map(list, zip_longest(*list(sequences), fillvalue=None)))


def build_start(start):
    start = transpose(start.splitlines())
    return {n: deque("".join(chars).lstrip()) for *chars, n in start if n != " "}


def rearrange(start, moves, part2=False):
    _start = build_start(start)
    moves = map(pat.findall, moves.split("\n"))

    for n, from_, to in moves:
        n = int(n)
        stack = [_start[from_].popleft() for _ in range(n)]
        _start[to].extendleft(reversed(stack) if part2 else stack)

    return "".join(v.popleft() for k, v in _start.items())


print("Part 1:", rearrange(start, moves))
print("Part 2:", rearrange(start, moves, True))
