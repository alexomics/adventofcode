import sys
import re


def lr_eval(s):
    p = s[1:-1].split()[::-1]
    res = int(p.pop())
    while p:
        curr = p.pop()
        if curr == "+":
            res += int(p.pop())
        elif curr == "*":
            res *= int(p.pop())
    return res


def rev_eval(s):
    p = s[1:-1].split()[::-1]
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
    return lr_eval(f"({' '.join(map(str, res))})")


def parse(s, part1=True):
    pat = re.compile(r"\(([\d+* ]*?)\)")
    s = f"({s})"
    while "(" in s:
        m = pat.finditer(s)
        for g in m:
            a, b = g.span()
            if part1:
                s = s[:a] + str(lr_eval(g.group())) + s[b:]
            else:
                s = s[:a] + str(rev_eval(g.group())) + s[b:]
            break
    return int(s)


print(f"Part 1: {sum(parse(l.strip()) for l in open(sys.argv[1]))}")
print(f"Part 2: {sum(parse(l.strip(), part1=False) for l in open(sys.argv[1]))}")
