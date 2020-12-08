import sys
import re
from itertools import permutations


class D(dict):
    def __getitem__(self, item):
        a, b = item
        return super().__getitem__((a, b)) + super().__getitem__((b, a))

    def add_diner(self, diner, cost):
        people = set(x for y in self.keys() for x in y)
        for p in people:
            self.__setitem__((p, diner), cost)
            self.__setitem__((diner, p), cost)


pat = re.compile(r"^(\w+).*(gain|lose) (\d+).* (\w+).$")
c = {"gain": "+", "lose": "-"}
lines = [pat.findall(l)[0] for l in open(sys.argv[1])]
lines = D({(a, b): int(f"{c[gl]}{i}") for a, gl, i, b in lines})

people = set(p for p, *_ in lines)
m = 0
for perm in permutations(people):
    perm = perm + (perm[0],)
    m = max(m, sum(lines[a, b] for a, b in zip(perm, perm[1:])))
print(f"Part 1: {m}")

lines.add_diner("Alex", 0)

people = set(p for p, *_ in lines)
m = 0
for perm in permutations(people):
    perm = perm + (perm[0],)
    m = max(m, sum(lines[a, b] for a, b in zip(perm, perm[1:])))
print(f"Part 2: {m}")
