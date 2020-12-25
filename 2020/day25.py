import sys

# https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange#Description
a, b = [int(l) for l in open(sys.argv[1])]
p = 20201227
g = 7


def f(x, i=1):
    while pow(g, i, p) != x:
        i += 1
    return i


print("Part 1:", pow(a, f(b), p))
