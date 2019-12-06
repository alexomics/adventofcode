import fileinput


def get_orbits(_orbits, planet):
    """Return number of orbits a given planet has"""
    x = 0
    while planet in _orbits:
        planet = _orbits[planet]
        x += 1
    return x


def path_to_root(_orbits, planet):
    """Yield planets from planet to root"""
    while planet in _orbits:
        planet = _orbits[planet]
        yield planet


def part_1(s):
    """
    >>> s = '''COM)B
    ... B)C
    ... C)D
    ... D)E
    ... E)F
    ... B)G
    ... G)H
    ... D)I
    ... E)J
    ... J)K
    ... K)L'''
    >>> p, o = part_1([l for l in s.split('\\n')])
    >>> sum({_p: get_orbits(o, _p) for _p in p}.values())
    42
    """
    # Make a dict of orbits: COM)B -> {B: COM}
    orbits = dict(tuple(reversed(l.split(")"))) for l in s)
    planets = set(p for l in s for p in l.split(")"))
    return planets, orbits


def part_2(orbits, num_orbits, *args):
    """
    >>> s = '''COM)B
    ... B)C
    ... C)D
    ... D)E
    ... E)F
    ... B)G
    ... G)H
    ... D)I
    ... E)J
    ... J)K
    ... K)L
    ... K)YOU
    ... I)SAN'''
    >>> p, o = part_1([l for l in s.split('\\n')])
    >>> part_2(o, {_p: get_orbits(o, _p) for _p in p}, 'SAN', 'YOU')
    4
    """
    i = [set(path_to_root(orbits, a)) for a in args]
    m = max(num_orbits.get(planet) for planet in set.intersection(*i))
    return sum(num_orbits.get(a, 0) for a in args) - 2 * m - 2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    planets, orbits = part_1([l.strip() for l in fileinput.input()])
    num_orbits = {p: get_orbits(orbits, p) for p in planets}
    print(f"Part 1: {sum(num_orbits.values())}")
    print(f"Part 2: {part_2(orbits, num_orbits, 'SAN', 'YOU')}")
