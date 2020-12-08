import sys
import json
import re

pat = re.compile(r"(-?\d+)")
s = open(sys.argv[1]).read()
print(f"Part 1: {sum(map(int, pat.findall(s)))}")


def parse(obj, exclude="red"):
    x = 0
    for item in obj:
        if isinstance(item, int):
            x += item
        elif isinstance(item, list):
            x += parse(item, exclude=exclude)
        elif isinstance(item, dict):
            if not exclude in item.values():
                x += parse(item.values(), exclude=exclude)
    return x


# print(f"Part 1: {parse(json.loads(s), exclude=None)}")
print(f"Part 2: {parse(json.loads(s))}")
