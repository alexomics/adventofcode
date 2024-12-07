import sys
from operator import add, mul


def calc(vals, ops):
    if len(vals) == 1:
        yield vals[0]
    elif len(vals) >= 2:
        for op in ops:
            yield from calc([op(*vals[:2])] + vals[2:], ops)


def cat(a, b):
    return int(f"{a}{b}")


data = sys.stdin.read()
data = {
    int(l.split(": ")[0]): list(map(int, l.split(": ")[-1].split()))
    for l in data.splitlines()
}
p1 = sum(
    target
    for target, vals in data.items()
    if any(target == res for res in calc(vals, (add, mul)))
)
p2 = sum(
    target
    for target, vals in data.items()
    if any(target == res for res in calc(vals, (add, mul, cat)))
)


print(p1, p2, sep="\n")
