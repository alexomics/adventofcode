import sys
import itertools
import re

PAT = re.compile(r"(.+?)\1+")


def get_spawn(maxy):
    return (2, maxy + 4)


def go_up(coords):
    return set([(x, y + 1) for x, y in coords])


def go_down(coords):
    return set([(x, y - 1) for x, y in coords])


def go_left(coords, bound=0):
    if any(x == bound for x, _ in coords):
        return coords
    return set([(x - 1, y) for x, y in coords])


def go_right(coords, bound=6):
    if any(x == bound for x, _ in coords):
        return coords
    return set([(x + 1, y) for x, y in coords])


def print_tunnel(occupied, maxy):
    for y in range(maxy, 0, -1):
        row = "".join("#" if (x, y) in occupied else " " for x in range(7))
        print(f"|{row}|")
    print(f"+{'-'*7}+")


moves = itertools.cycle(sys.stdin.read().strip())
rocks = [
    set([(0, 0), (1, 0), (2, 0), (3, 0)]),
    set([(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]),
    set([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]),
    set([(0, 0), (0, 1), (0, 2), (0, 3)]),
    set([(0, 0), (1, 0), (0, 1), (1, 1)]),
]
rocks = enumerate(itertools.cycle(rocks), start=1)
highest = (0, 0)
minx, maxx = 0, 6
miny, maxy = 0, 0
occupied = set([(x, 0) for x in range(maxx + 1)])
i, its = 0, 1000000000000
diffs = []
sim_len = 1000


def guess_repeat(seq):
    seq = "".join(map(str, seq))
    matches = sorted(PAT.finditer(seq), key=lambda m: len(m.group(1)))[::-1]
    if matches:
        match = matches[0]
        m = match.group(1)
        offset = seq.index(m)
        return offset, m
    return None, None


cycle = None
for _ in range(its):
    i, coords = next(rocks)
    x, y = get_spawn(maxy)
    coords = [(x + dx, y + dy) for dx, dy in coords]
    while True:
        m = next(moves)
        if m == ">":
            coords = go_right(coords)
            if coords & occupied:
                coords = go_left(coords)
        elif m == "<":
            coords = go_left(coords)
            if coords & occupied:
                coords = go_right(coords)
        else:
            assert False, f"Funky coord: {m}"
        coords = go_down(coords)
        if coords & occupied:
            coords = go_up(coords)
            occupied |= coords
            new_maxy = max(maxy, max(y for _, y in coords))
            diffs.append(new_maxy - maxy)
            maxy = new_maxy
            # print_tunnel(occupied, maxy)
            break

    if i == 2022:
        print("Part 1:", maxy)

    if i % sim_len == 0:
        offset, new_cycle = guess_repeat(diffs)
        if new_cycle == cycle:
            pre = sum(diffs[:offset])
            pat = list(map(int, cycle))
            rem = (its - offset) % len(cycle)
            rep = (its - offset) // len(cycle)
            print("Part 2:", pre + rep * sum(pat) + sum(pat[:rem]))
            break
        else:
            cycle = new_cycle
