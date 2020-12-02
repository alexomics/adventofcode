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
