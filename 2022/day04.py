import sys
import re

pat = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")

s = sys.stdin.read()

lines = [list(map(int, pat.findall(l)[0])) for l in s.splitlines()]
lines = [(set(range(a, b + 1)), set(range(c, d + 1))) for a, b, c, d in lines]

s = [a.issubset(b) or b.issubset(a) for a, b in lines]
print(f"Part 1: {sum(s)}")

s = [len(a & b) > 0 for a, b in lines]
print(f"Part 2: {sum(s)}")
