from itertools import islice
import argparse
from pathlib import Path


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"P({self.x}, {self.y})"

    def __repr__(self):
        return str(self)

    def __add__(self, P):
        return Point(self.x + P.x, self.y + P.y)

    def l_c(self, P):
        """Return coefficients of a line made by two points"""
        return self.y - P.y, P.x - self.x, self.x * P.y - P.x * self.y

    def m_dist(self, P=None):
        """Manhattan distance from origin or Point(P)"""
        if P is None:
            P = Point(0, 0)
        return abs(self.x - P.x) + abs(self.y - P.y)

def cramers_rule(L1, L2):
    """Cramer's rule
    
    | L1[0] L1[1] L1[2] |
    | L2[0] L2[1] L2[2] | --> L1[0] * | L2[1] L2[2] | ...
    |   1     1     1   |             |   1     1   | 
    """

    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return Point(x, y)
    else:
        return False


def ccw(a, b, c):
    """Counter-clockwise test

    http://jeffe.cs.illinois.edu/teaching/373/notes/x06-sweepline.pdf
    """
    return (c.y-a.y) * (b.x-a.x) > (b.y-a.y) * (c.x-a.x)


def intersect(A, B, C, D):
    """Return true if line segments AB and CD intersect

    http://jeffe.cs.illinois.edu/teaching/373/notes/x06-sweepline.pdf
    """
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


class Line:
    def __init__(self, L):
        self.L = L
        self.line = list(self.parse())

    def __str__(self):
        return f"{self.line}"

    def __repr__(self):
        return f"{self.line}"

    def __len__(self):
        return len(self.line)

    def __iter__(self):
        yield from self.line

    def window(self, n=2):
        """Yield tuples of size N from an iterable"""
        it = iter(self)
        result = tuple(islice(it, n))
        if len(result) == n:
            yield result
        for elem in it:
            result = result[1:] + (elem,)
            yield result

    def parse(self):
        prev_p = Point(0, 0)
        yield prev_p
        for d in self.L.split(","):
            direction, distance = d[0], int(d[1:])
            if direction == "R":
                p = Point(distance, 0)
            elif direction == "U":
                p = Point(0, distance)
            elif direction == "L":
                p = Point(-distance, 0)
            elif direction == "D":
                p = Point(0, -distance)
            yield prev_p + p
            prev_p += p

    def intersects(self, L):
        for p0, p1 in self.window():
            for p2, p3 in L.window():
                if intersect(p0, p1, p2, p3):
                    yield cramers_rule(p0.l_c(p1), p2.l_c(p3))


def brute_walk(line):
    x = 0
    y = 0
    for d in line.split(","):
        direction, distance = d[0], int(d[1:])
        for _ in range(distance):
            yield x, y
            if direction == "U":
                y += 1
            elif direction == "L":
                x -= 1
            elif direction == "D":
                y -= 1
            elif direction == "R":
                x += 1
    yield x, y


def main(parser, args):
    if Path(args.input).is_file():
        with open(args.input, "r") as fh:
            m = [l.strip() for l in fh]
    else:
        parser.error("input is not a file")

    if args.part == "1":
        print("Part 01")
        a, b = m
        a = Line(a)
        print(a)
        b = Line(b)
        r = [x.m_dist() for x in a.intersects(b)]
        print(int(min(r)))
    elif args.part == "2":
        print("Part 02")
        result = 0
        hold = {}
        distances = {}
        for i, line in enumerate(m):
            distance = 0
            for coord in brute_walk(line):
                if not coord[0] and not coord[1]:
                    pass
                elif coord not in hold:
                    hold[coord] = i
                    distances[coord] = distance
                elif hold[coord] != i:
                    other = distances[coord]
                    if not result or result > other + distance:
                        result = other + distance
                    if other > distance:
                        hold[coord] = i
                        distances[coord] = distance
                distance += 1
        print(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    s = parser.add_subparsers(dest="part")

    p1 = s.add_parser("1")
    p1.add_argument("input")

    p2 = s.add_parser("2")
    p2.add_argument("input")
    main(parser, parser.parse_args())

