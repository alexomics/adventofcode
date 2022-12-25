import sys

digits = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
digits_inv = {v: k for k, v in digits.items()}
places = {i: 5 ** i for i in range(25)}


def decode(s):
    x = 0
    for n, c in enumerate(s[::-1]):
        x += places[n] * digits[c]
    return x


def encode(x):
    s = ""
    while x:
        d = (x + 2) % 5 - 2
        s += digits_inv[d]
        x -= d
        x //= 5
    return s[::-1]


s = sys.stdin.read()
total = sum(decode(l) for l in s.splitlines())
print("Part 1:", encode(total))
print("Part 2: \N{glowing star}")
