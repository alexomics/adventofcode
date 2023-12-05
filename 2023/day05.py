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


def f(ranges, maps):
    ans = []
    for r in maps:
        new_ranges = []
        while ranges:
            (start, end) = ranges.pop()
            before = (start, min(end, r.src.start))
            inter = (max(start, r.src.start), min(r.src.stop, end))
            after = (max(r.src.stop, start), end)
            if before[1] > before[0]:
                new_ranges.append(before)
            if inter[1] > inter[0]:
                ans.append(
                    (
                        inter[0] - r.src.start + r.dest.start,
                        inter[1] - r.src.start + r.dest.start,
                    )
                )
            if after[1] > after[0]:
                new_ranges.append(after)
        ranges = new_ranges
    return ans + ranges


res = []
pairs = list(zip(maps["seeds"][::2], maps["seeds"][1::2]))
for start, size in pairs:
    # Create a single range [start, start + size)
    ranges = [(start, start + size)]
    for step in path:
        ranges = f(ranges, maps[step])
    res.append(min(ranges)[0])
print(min(res))
