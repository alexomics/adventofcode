import sys
import argparse
import re
from itertools import product

M_PAT = re.compile(r"mem\[(\d+)\] = (\d+)")
X_PAT = re.compile(r"X")


def parse(fh):
    for line in fh:
        if line.startswith("mask = "):
            name = line[7:].strip()
            break

    op_lines = []
    for line in fh:
        if line.startswith("mask = "):
            yield name, op_lines
            op_lines = []
            name = line[7:].strip()
            continue
        op_lines.append(map(int, M_PAT.findall(line)[0]))
    yield name, op_lines


def main(args):
    p1 = {}
    p2 = {}
    DEBUG = args.debug
    for mask, ops in parse(open(args.puzzle_input)):
        if DEBUG:
            print(f"mask = {mask} ({int(mask.replace('X', '0'), 2)})")
        floats = [p.start() for p in X_PAT.finditer(mask)]
        for pos, n in ops:
            p1[pos] = (n | int(mask.replace("X", "0"), 2)) & int(
                mask.replace("X", "1"), 2
            )
            r = int(mask.replace("X", "0"), 2) | pos
            if DEBUG:
                print(f" pos = {pos:0>36b} ({pos})")
                print(f"  or = {r:0>36b} ({r})")
            for p in product("01", repeat=len(floats)):
                m = list(f"{r:0>36b}")
                for i, x in zip(floats, p):
                    m[i] = x
                m = int("".join(m), 2)
                p2[m] = n
                if DEBUG:
                    print(f"       {m:0>36b} ({m})")

    print(f"Part 1: {sum(p1.values())}")
    print(f"Part 2: {sum(p2.values())}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("puzzle_input")
    p.add_argument("--debug", action="store_true")
    main(p.parse_args())
