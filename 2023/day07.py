import sys
from collections import Counter, deque


strength = {k: v for v, k in enumerate(reversed("AKQJT98765432"), start=2)}


def parse(stdin):
    for line in stdin:
        ca, b = line.split()
        yield tuple(strength.get(c) for c in ca), int(b)


# Five of a kind, where all five cards have the same label: AAAAA
def five_of_a_kind(cards):
    return len(set(cards)) == 1


# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
def four_of_a_kind(cards):
    c = Counter(cards)
    return 4 in c.values() and 1 in c.values()


# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
def full_house(cards):
    c = Counter(cards)
    return 3 in c.values() and 2 in c.values()


# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
def three_of_a_kind(cards):
    c = Counter(cards)
    return 3 in c.values()


# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
def two_pair(cards):
    c = Counter(cards)
    return list(c.values()).count(2) == 2


# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
def one_pair(cards):
    c = Counter(cards)
    return list(c.values()).count(2) == 1


# High card, where all cards' labels are distinct: 23456
def high_card(cards):
    return len(set(cards)) == 5


fs = [
    five_of_a_kind,
    four_of_a_kind,
    full_house,
    three_of_a_kind,
    two_pair,
    one_pair,
    high_card,
]

res = []
p2 = []
for cards, bid in parse(sys.stdin):
    # print(cards, " >> ", bid)
    rank = deque([rank for rank, f in enumerate(fs[::-1], 1) if f(cards)], maxlen=1)[0]
    res.append((rank, cards, bid))

    c = tuple(c if c != 11 else 1 for c in cards)
    c2 = Counter(c if c != 11 else 1 for c in cards)
    for k, v in [(k, v) for k, v in c2.most_common(5) if k != 1]:
        c2[k] += c2.get(1, 0)
        del c2[1]
        break
    c2_ = []
    for k, v in c2.items():
        c2_.extend([k] * v)
    c2_ = tuple(c2_)
    rank = deque([rank for rank, f in enumerate(fs[::-1], 1) if f(c2_)], maxlen=1)[0]
    p2.append((rank, c, bid))

res.sort()
x = 0
for i, (_, _, b) in enumerate(res, 1):
    x += (i) * b
print(x)
p2.sort()
x = 0
for i, (_, _, b) in enumerate(p2, 1):
    x += (i) * b
print(x)
