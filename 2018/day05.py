import sys
from collections import deque

line = sys.stdin.read().strip()


def collapse_polymer(s):
    s = deque(s)
    rebuild = []
    while s:
        u = s.pop()
        if rebuild and (u.lower() == rebuild[-1].lower() and u != rebuild[-1]):
            rebuild.pop()
        else:
            rebuild.append(u)
    return len(rebuild)


print(f"Part 1: {collapse_polymer(line)}")

res = []
for letter in set(line.lower()):
    s = "".join(char for char in line if char.lower() != letter)
    res.append(collapse_polymer(s))

print(f"Part 2: {min(res)}")
