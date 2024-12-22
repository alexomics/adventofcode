import sys
from collections import deque, defaultdict
from itertools import islice


# fmt: off
# TY itertools recipes
def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) → ABCD BCDE CDEF DEFG
    iterator = iter(iterable)
    window = deque(islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)

def pairwise(iterable):
    # pairwise('ABCDEFG') → AB BC CD DE EF FG
    iterator = iter(iterable)
    a = next(iterator, None)
    for b in iterator:
        yield a, b
        a = b
# fmt: on


def calc(s: int, n=2000):
    yield s
    for _ in range(n):
        s = (s * 64) ^ s
        s %= 16777216
        s = (s // 32) ^ s
        s %= 16777216
        s = (s * 2048) ^ s
        s %= 16777216
        yield s


data = map(int, sys.stdin.read().strip().splitlines())
p1, p2 = 0, defaultdict(int)
for secret in data:
    secrets = list(calc(secret))
    p1 += secrets[-1]
    prices = [v % 10 for v in secrets]
    diffs = [b - a for a, b in pairwise(prices)]
    scores = {}
    # record first occurence of each set of 4 diffs
    for i, b in enumerate(sliding_window(diffs, 4)):
        if b not in scores:
            scores[b] = prices[i + 4]
    # accumulate part 2
    for k, v in scores.items():
        p2[k] += v

print(p1, max(p2.values()), sep="\n")
