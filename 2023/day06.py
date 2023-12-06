import sys
from math import prod
from itertools import starmap


def parse(line):
    return [int(x) for x in line.split(":")[1].split()]


def f(time, dist):
    return sum(i * (time - i) > dist for i in range(time + 1))


time, dist = map(parse, sys.stdin)
print(prod(starmap(f, zip(time, dist))))
time = int("".join(map(str, time)))
dist = int("".join(map(str, dist)))
print(f(time, dist))
