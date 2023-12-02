import sys

data = {
    int(l.split(": ")[0].split()[-1]): [
        {d_.split()[-1]: int(d_.split()[0]) for d_ in d.split(", ")}
        for d in l.split(": ")[1].split("; ")
    ]
    for l in sys.stdin.read().splitlines()
}

limits = {"red": 12, "green": 13, "blue": 14}
p1, p2 = 0, 0
for game, runs in data.items():
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
