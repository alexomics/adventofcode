import sys
from string import ascii_lowercase


lines = [l.replace("\n", "") for l in open(sys.argv[1]).read().split("\n\n")]
print(f"Part 1: {sum([len(set(l)) for l in lines])}")

lines = [l for l in open(sys.argv[1]).read().split("\n\n")]
res = []
for l in lines:
    group = set(ascii_lowercase)
    _g = [set(_l) for _l in l.split("\n")]
    res.append(len(group.intersection(*_g)))

print(f"Part 2: {sum(res)}")
