import fileinput

def get_orbits(_orbits, planet):
    return sum(1 for _ in path_to_root(_orbits, planet))

def path_to_root(_orbits, planet):
    while planet in _orbits:
        planet = _orbits[planet]
        yield planet

def part_1(s):
    return dict(reversed(l.split(")")) for l in s)

def part_2(orbits, *args):
    return len(set.symmetric_difference(*[set(path_to_root(orbits, a)) for a in args]))

orbits = part_1([l.strip() for l in fileinput.input()])
print(f"Part 1: {sum(get_orbits(orbits, p) for p in orbits)}")
print(f"Part 2: {part_2(orbits, 'SAN', 'YOU')}")
