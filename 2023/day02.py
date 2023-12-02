import sys


def parse(lines):
    def f(s):
        n, c = s.split()
        return c, int(n)

    for line in lines:
        game, _, data = line.strip().partition(": ")
        runs = (d.split(", ") for d in data.split("; "))
        yield int(game.split()[-1]), [dict(map(f, run)) for run in runs]


limits = {"red": 12, "green": 13, "blue": 14}
p1, p2 = 0, 0
for game, runs in parse(sys.stdin.read().splitlines()):
    impossbile = any(
        run.get(colour, 0) > limit for colour, limit in limits.items() for run in runs
    )
    max_values = {colour: max(run.get(colour, 0) for run in runs) for colour in limits}

    score = 1
    for v in max_values.values():
        score *= v
    p2 += score
    if not impossbile:
        p1 += game
print(p1, p2, sep="\n")
