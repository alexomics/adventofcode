import sys


data = open(sys.argv[1]).read()
p1, p2 = [list(map(int, l.split("\n")[1:])) for l in data.split("\n\n")]
while p1 and p2:
    a, b = p1.pop(0), p2.pop(0)
    if a > b:
        p1.extend([a, b])
    else:
        p2.extend([b, a])
if p1:
    ans = sum(i * x for i, x in enumerate(p1[::-1], 1))
else:
    ans = sum(i * x for i, x in enumerate(p2[::-1], 1))
print(f"Part 1: {ans}")


def play_game(p1, p2):
    seen = set()
    while p1 and p2:
        decks = (tuple(p1), tuple(p2))
        if decks in seen:
            return 1, p1
        seen.add(decks)
        a, b = p1.pop(0), p2.pop(0)
        if len(p1) >= a and len(p2) >= b:
            winner, _ = play_game(p1[:a], p2[:b])
            if winner == 1:
                p1.extend([a, b])
            else:
                p2.extend([b, a])
        else:
            if a > b:
                p1.extend([a, b])
            else:
                p2.extend([b, a])

    return 1 if p1 else 2, p1 if p1 else p2


p1, p2 = [list(map(int, l.split("\n")[1:])) for l in data.split("\n\n")]
_, winner = play_game(p1, p2)
print(f"Part 2: {sum(i * x for i, x in enumerate(winner[::-1], 1))}")
