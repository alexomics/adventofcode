import sys

lines = [l.strip() for l in open(sys.argv[1])]
earliest = int(lines[0].strip())
buses = [(i, int(x)) for i, x in enumerate(lines[1].split(",")) if x != "x"]

m = 999999999
d = {}
for _, b in buses:
    b = range(0, earliest * 2, int(b))
    for i, t in enumerate(b):
        if t >= earliest and i * b.step < m:
            m = min(m, i * b.step)
            d[m] = b.step
            break
print(f"Part 1: {d[m] * (m - earliest)}")

# https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Search_by_sieving
min_val = 0
product = 1
for i, v in buses:
    while (min_val + i) % v != 0:
        min_val += product
    product *= v
print(f"Part 2: {min_val}")

# from urllib.parse import quote_plus
# url = quote_plus(f"{', '.join(f'(t+{i}) mod {m} = 0' for i, m in buses)}")
# print(f"https://wolframalpha.com/input/?i={url}")
