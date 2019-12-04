import sys
from pathlib import Path


def fuel_req(i):
    return i // 3 - 2

if Path(sys.argv[1]).is_file():
    with open(sys.argv[1], "r") as fh:
        modules = [float(l.strip()) for l in fh]
else:
    modules = [float(l) for l in sys.argv[1:]]

print(f"Part 01: {sum(fuel_req(i) for i in modules)}")
res = []

for i in modules:
    i = fuel_req(i)
    while i > 0:
        res.append(i)
        i = fuel_req(i)

print(f"Part 02: {sum(res)}")

