import sys
import re
from collections import defaultdict

pat = re.compile(r"(\d+|no) ([\w ]+?) bags*[,.]")
is_in = defaultdict(defaultdict)
for l in open(sys.argv[1]):
    colour, rest = l.strip().split(" bags contain ")
    for num, col in pat.findall(rest):
        if num == "no":
            num = 0
        is_in[colour][col] = int(num)

can_hold = ["shiny gold"]
count = set()
while can_hold:
    lookup = can_hold.pop()
    for k, v in is_in.items():
        if lookup in v:
            can_hold.append(k)
            count.add(k)

print(f"Part 1: {len(count)}")


def calculate_cost(bag, d=is_in):
    x = 0
    for k, v in d[bag].items():
        x += v + v * calculate_cost(k)
    return x


y = calculate_cost("shiny gold")
print(f"Part 2: {y}")
