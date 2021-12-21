import re
from functools import cache

inp = """\
Player 1 starting position: 7
Player 2 starting position: 1
"""


class RollingInt(int):
    _max = 10

    def __new__(cls, value, *args, **kwargs):
        return super().__new__(cls, value)

    def __add__(self, other):
        res = x if (x := super().__add__(other) % self._max) else self._max
        return self.__class__(res)


def cycle(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    while True:
        yield from range(start, stop, step)


p1, p2 = map(RollingInt, re.findall(r": (\d+)$", inp, flags=re.MULTILINE))
s1, s2 = 0, 0
c = cycle(1, 101, 1)

first = True
rolls = 0
rolls_per_turn = 3
while True:
    p1 += sum(next(c) for _ in range(rolls_per_turn))
    s1 += p1
    rolls += rolls_per_turn
    if s1 >= 1000:
        break
    p2 += sum(next(c) for _ in range(rolls_per_turn))
    s2 += p2
    rolls += rolls_per_turn
    if s2 >= 1000:
        break
print(f"Part 1: {rolls * min(s1, s2)}")

# Only three options, pre-compute all rolls
r = (1, 2, 3)
rolls = [a + b + c for a in r for b in r for c in r]


@cache
def play(p1, s1, p2, s2):
    if s1 >= 21:
        return 1, 0
    if s2 >= 21:
        return 0, 1
    p1_wins, p2_wins = 0, 0
    for r in rolls:
        _p1 = p1 + r
        s2_, s1_ = play(p2, s2, _p1, s1 + _p1)
        p1_wins += s1_
        p2_wins += s2_
    return p1_wins, p2_wins


p1, p2 = map(RollingInt, re.findall(r": (\d+)$", inp, flags=re.MULTILINE))
s1, s2 = 0, 0
print(f"Part 2: {max(play(p1, s1, p2, s2))}")
