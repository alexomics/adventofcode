import sys
import re
from functools import partial


pat = re.compile(r"\(([\d+* ]*?)\)")


def lr_eval(s):
    p = s.split()[::-1]
    res = int(p.pop())
    while p:
        curr = p.pop()
        if curr == "+":
            res += int(p.pop())
        elif curr == "*":
            res *= int(p.pop())
    return res


def rev_eval(s):
    p = s.split()[::-1]
    res = []
    x = int(p.pop())
    while p:
        curr = p.pop()
        if curr == "+":
            x += int(p.pop())
        else:
            res.extend([x, "*"])
            x = int(p.pop())
    res.append(x)
    return lr_eval(" ".join(map(str, res)))


def parse(s, eval_):
    if "(" in s:
        for m in reversed(list(pat.finditer(s))):
            s = s[: m.start()] + str(eval_(m.group(1))) + s[m.end() :]
        return parse(s, eval_)
    return eval_(s)


lines = open(sys.argv[1]).readlines()
print(f"Part 1: {sum(map(partial(parse, eval_=lr_eval), lines))}")
print(f"Part 2: {sum(map(partial(parse, eval_=rev_eval), lines))}")
