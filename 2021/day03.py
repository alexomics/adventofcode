import sys
from collections import Counter

lines = [l.strip() for l in sys.stdin]

# Transpose
lines_t = [list(l) for l in zip(*lines)]
g, e = [], []
for pos in lines_t:
    (g_bit, _), (e_bit, _) = Counter(pos).most_common(2)
    g.append(g_bit)
    e.append(e_bit)

g = int("".join(g), 2)
e = int("".join(e), 2)
print(f"Part 1: {g * e}")

lines_o2 = lines[:]
lines_co2 = lines[:]
int_length = len(lines_t)
for pos in range(int_length):
    count_o2 = Counter([x[pos] for x in lines_o2])
    count_co2 = Counter([x[pos] for x in lines_co2])

    if count_o2["0"] > count_o2["1"]:
        lines_o2 = [x for x in lines_o2 if x[pos] == "1"]
    else:
        lines_o2 = [x for x in lines_o2 if x[pos] == "0"]

    if count_co2["0"] > count_co2["1"]:
        lines_co2 = [x for x in lines_co2 if x[pos] == "0"]
    else:
        lines_co2 = [x for x in lines_co2 if x[pos] == "1"]

    if lines_o2:
        o2 = lines_o2[0]
    if lines_co2:
        co2 = lines_co2[0]

o2 = int("".join(o2), 2)
co2 = int("".join(co2), 2)
print(f"Part 2: {o2 * co2}")
