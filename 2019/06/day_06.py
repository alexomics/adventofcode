import fileinput


def get_orbits(_orbits, planet):
    """Return number of orbits a given planet has"""
    return sum(1 for _ in path_to_root(_orbits, planet))


def path_to_root(_orbits, planet):
    """Yield planets from planet to root"""
    while planet in _orbits:
        planet = _orbits[planet]
        yield planet


def part_1(s):
    """Solve aoc day 6 part 1

    Parameters
    ----------
    s : iterable
        List of input lines

    Returns
    -------
    planets : set
        Set of all planets seen in the input file
    orbits : dict
        Dictionary of planet (key) and orbit (value)

    Examples
    --------
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
    >>> sum(get_orbits(o, _p) for _p in p)
    42
    """
    # Make a dict of orbits: COM)B -> {B: COM}
    orbits = dict(tuple(reversed(l.split(")"))) for l in s)
    planets = set(p for l in s for p in l.split(")"))
    return planets, orbits


def part_2(orbits, *args):
    """Solve aoc day 6 part 2

    Parameters
    ----------
    orbits : dict
    num_orbits : dict
    args : str

    Returns
    -------
    int
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
    >>> part_2(o, 'SAN', 'YOU')
    4
    """
    return len(set.symmetric_difference(*[set(path_to_root(orbits, a)) for a in args]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    planets, orbits = part_1([l.strip() for l in fileinput.input()])
    print(f"Part 1: {sum(get_orbits(orbits, p) for p in planets)}")
    print(f"Part 2: {part_2(orbits, 'SAN', 'YOU')}")
