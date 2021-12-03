import sys
from collections import Counter

lines = [l.strip() for l in sys.stdin.readlines()]
int_length = len(lines[0])

c = sum((Counter(x for x in enumerate(l)) for l in lines), start=Counter())
gamma = []
epsilon = []
for pos in range(int_length):
    if c[(pos, "0")] > c[(pos, "1")]:
        gamma.append("0")
        epsilon.append("1")
    else:
        gamma.append("1")
        epsilon.append("0")

g = int("".join(gamma), 2)
e = int("".join(epsilon), 2)
print(f"Part 1: {g * e}")

lines_o2 = lines[:]
lines_co2 = lines[:]
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
