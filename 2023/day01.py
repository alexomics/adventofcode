import sys

vals = [
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("0", "0"),
]
extended = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9"),
]


def findall(pat, s):
    """Yields all the positions of the pattern in the string s."""
    i = s.find(pat)
    while i != -1:
        yield i
        i = s.find(pat, i + 1)


def get(l, values):
    r = []
    for lookup, val in values:
        if lookup in l:
            for idx in findall(lookup, l):
                r.append((idx, val))
    r.sort(key=lambda t: t[0])
    return [v for _, v in r]


p1, p2 = [], []
for l in sys.stdin.read().split("\n"):
    if not l:
        continue
    _1 = get(l, vals)
    _2 = get(l, vals + extended)
    p1.append(int(f"{_1[0]}{_1[-1]}"))
    p2.append(int(f"{_2[0]}{_2[-1]}"))
print(sum(p1), sum(p2), sep="\n")
