import sys
import re
from string import ascii_lowercase


DOUBLES = [c * 2 for c in ascii_lowercase]
DISALLOW = ["ab", "cd", "pq", "xy"]

vowels = lambda l: sum(l.count(c) for c in "aeiou") >= 3
double = lambda l: sum(d in l for d in DOUBLES) >= 1
remove = lambda l: sum(c in l for c in DISALLOW) == 0


def part_1_test(line):
    return all([vowels(line), double(line), remove(line)])


lines = [l.strip() for l in open(sys.argv[1])]

print(f"Part 1: {sum(part_1_test(l) for l in lines)}")

count = 0
for line in lines:
    m1 = re.findall(r"(\S{2}).*\1", line)
    m2 = re.findall(r"(\S{1}).{1}\1", line)
    count += bool(m1 and m2)
print(f"Part 2: {count}")
