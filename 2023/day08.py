import sys
import re
from math import lcm


def forever(steps):
    m = {"L": 0, "R": 1}
    while True:
        yield from map(m.get, steps)


def parse(lines):
    steps, lookup = lines.split("\n\n")
    data = {}
    for line in lookup.split("\n"):
        if not line:
            continue
        n, *d = re.findall("([A-Z]{3})", line)
        data[n] = d
    return steps, data


steps, data = parse(sys.stdin.read())

c = 0
n = data["AAA"]
for d in forever(steps):
    c += 1
    if n[d] == "ZZZ":
        break
    n = data[n[d]]
print(c)

A = [k for k in data if k.endswith("A")]

res = []
for start in A:
    c = 0
    n = data[start]
    for d in forever(steps):
        c += 1
        if n[d][-1] == "Z":
            res.append(c)
            break
        n = data[n[d]]
print(lcm(*res))
