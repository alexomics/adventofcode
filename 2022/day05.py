import sys
import re
from collections import deque

pat = re.compile(r"\d+")
s = sys.stdin.read()
start, moves = s.split("\n\n")


def transpose(sequences):
    m = max([len(v) for v in sequences])
    matrix = [list(v) for v in sequences]
    for seq in matrix:
        seq.extend(list("#" * (m - len(seq))))
    t_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(m)]
    return t_matrix


def build_start(start):
    start = transpose(start.splitlines())
    start = [l for l in start if not set(l).issubset(set(" []"))]
    return {n: deque(list("".join(chars).lstrip())) for *chars, n in start}


def rearrange(start, moves, part2=False):
    _start = build_start(start)
    moves = list(map(pat.findall, moves.split("\n")))

    for n, from_, to in moves:
        n = int(n)
        stack = [_start[from_].popleft() for _ in range(n)]
        _start[to].extendleft(reversed(stack) if part2 else stack)

    return "".join(v.popleft() for k, v in _start.items())


print("Part 1:", rearrange(start, moves))
print("Part 2:", rearrange(start, moves, True))
