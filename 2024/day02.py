import sys


def dampen(ns):
    yield ns
    for i in range(len(ns)):
        yield ns[:i] + ns[i + 1 :]


p1, p2 = 0, 0
for l in sys.stdin.read().split("\n"):
    if not l:
        continue
    ns = list(map(int, l.split()))
    for p, ns in enumerate(dampen(ns), 1):
        s = [(b - a) for a, b in zip(ns[:-1], ns[1:])]
        decreasing = all(y in (-1, -2, -3) for y in s)
        increasing = all(y in (1, 2, 3) for y in s)
        if increasing or decreasing:
            if p == 1:
                p1 += 1
            p2 += 1
            break

print(p1, p2, sep="\n")
