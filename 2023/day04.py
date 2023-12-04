import sys
import collections


def parse(data):
    for line in data:
        card, numbers = line.split(":")
        ws, ns = numbers.split("|")
        yield (
            int(card.split()[-1]),
            [int(x) for x in ws.split()],
            [int(x) for x in ns.split()],
        )


p1 = 0
played = collections.defaultdict(int)
for card, winners, numbers in parse(sys.stdin):
    played[card] += 1
    wins = len(set(winners) & set(numbers))
    p1 += 2 ** (wins - 1) if wins else 0
    for c in range(1, wins + 1):
        played[card + c] += played[card]
print(p1, sum(played.values()), sep="\n")
