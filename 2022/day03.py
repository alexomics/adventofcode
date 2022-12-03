import sys
import string

PRIORITY = {k: v for v, k in enumerate(string.ascii_letters, start=1)}
s = sys.stdin.read()
lines = s.splitlines()
split_lines = [(l[: len(l) // 2], l[len(l) // 2 :]) for l in lines]

t = sum(PRIORITY.get(s) for a, b in split_lines for s in set(a) & set(b))
print(f"Part 1: {t}")

t = [set.intersection(*map(set, lines[i : i + 3])) for i in range(0, len(lines), 3)]
t = sum(a for s in t for a in map(PRIORITY.get, s))
print(f"Part 2: {t}")
