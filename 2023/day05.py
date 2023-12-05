import sys
from collections import namedtuple

R = namedtuple("R", ["dest", "src"])


def parse(lines):
    ret = {}
    name, _, seeds = next(lines).strip().partition(":")
    ret[name] = [int(x) for x in seeds.split()]

    for line in lines:
        if ":" in line:
            name = line.strip().split()[0]
            break
    _lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if ":" in line:
            ret[name] = _lines
            _lines = []
            name = line.strip().split()[0]
            continue
        d, s, l = (int(x) for x in line.split())
        _lines.append(R(range(d, d + l), range(s, s + l)))
    ret[name] = _lines
    return ret


path = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]
maps = parse(sys.stdin)
x = []
for seed in maps["seeds"]:
    locs = [seed]
    for step in path:
        found = False
        for r in maps[step]:
            if locs[-1] in r.src:
                locs.append(r.dest[r.src.index(locs[-1])])
                found = True
                break
        if not found:
            locs.append(locs[-1])
    x.append(locs[-1])
print(min(x))
