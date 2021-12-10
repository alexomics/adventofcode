import sys
import re
from collections import deque

open_chars = ("\(", "\[", "\{", "<")
close_chars = ("\)", "\]", "\}", ">")
goods = {f"{l}{r}" for l, r in zip(open_chars, close_chars)}
good_pats = [re.compile(rf"{p}") for p in goods]
bad_pats = [
    re.compile(s)
    for l in open_chars
    for r in close_chars
    if (s := rf"{l}{r}") not in goods
]
rev = dict(list(pair.replace("\\", "")) for pair in goods)

table1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
table2 = {")": 1, "]": 2, "}": 3, ">": 4}


def rec_re(s):
    for pat in good_pats:
        if p := pat.search(s):
            return rec_re(s[: p.start()] + s[p.end() :])
    return s


illegals, scores = [], []
for line in sys.stdin:
    res = rec_re(line.strip())
    if i := [table1.get(m.group()[-1], 0) for p in bad_pats if (m := p.search(res))]:
        illegals.extend(i)
    else:
        s, q = deque(res), deque()
        while s:
            q.appendleft(rev[s.popleft()])
        t = 0
        while q:
            t = (5 * t) + table2[q.popleft()]
        scores.append(t)

scores.sort()
print(f"Part 1: {sum(illegals)}")
print(f"Part 2: {scores[len(scores) // 2]}")
