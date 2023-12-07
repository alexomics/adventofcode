import sys
from collections import Counter


def parse(stdin):
    strength = {k: v for v, k in enumerate("23456789TJQKA", start=2)}
    for line in stdin:
        ca, b = line.split()
        yield tuple(strength.get(c) for c in ca), int(b)


fs = dict(
    high_card=lambda c: c == [1, 1, 1, 1],
    one_pair=lambda c: c == [1, 1, 1, 2],
    two_pair=lambda c: c == [1, 2, 2],
    three_of_a_kind=lambda c: c == [1, 1, 3],
    full_house=lambda c: c == [2, 3],
    four_of_a_kind=lambda c: c == [1, 4],
    five_of_a_kind=lambda c: c == [5],
)


def score(cards: Counter[int, int]):
    g = (i for i, f in enumerate(fs.values(), 1) if f(sorted(cards.values())))
    return max(g, default=0)


p1, p2 = [], []
for cards, bid in parse(sys.stdin):
    p1.append((score(Counter(cards)), cards, bid))

    cards = tuple(c if c != 11 else 1 for c in cards)
    counts = Counter(cards)
    for k, v in counts.most_common(5):
        if k == 1:
            continue
        counts[k] += counts.get(1, 0)
        del counts[1]
        break
    cards_ = tuple(k for k, v in counts.items() for _ in range(v))
    p2.append((score(Counter(cards_)), cards, bid))

p1.sort()
p2.sort()
print(sum(i * b for i, (_, _, b) in enumerate(p1, 1)))
print(sum(i * b for i, (_, _, b) in enumerate(p2, 1)))
