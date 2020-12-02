import sys
import re

p1 = 0
p2 = 0
with open(sys.argv[1], "r") as fh:
    for l in fh:
        m0, m1, ch, pas = re.findall("(\d+)-(\d+) (\w+): (\w+)", l.strip())[0]
        m0, m1 = int(m0), int(m1)
        if pas.count(ch) in range(m0, m1 + 1):
            p1 += 1
        if sum([pas[m0 - 1] == ch, pas[m1 - 1] == ch]) == 1:
            p2 += 1

print(f"Part 1: {p1}\nPart 2: {p2}")

"""Minimised:
import sys, re

parts = [re.findall("(\d+)-(\d+) (\w+): (\w+)", l.strip())[0] for l in open(sys.argv[1])]
print(f"Part 1: {sum(int(x) <= p.count(c) <= int(y) for x, y, c, p in parts)}")
print(f"Part 2: {sum((p[int(x) - 1] == c) + (p[int(y) - 1] == c) == 1 for x, y, c, p in parts)}")
"""
