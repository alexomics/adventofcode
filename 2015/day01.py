import sys

line = [l.strip() for l in open(sys.argv[1])][0]

print(f"Part 1: {line.count('(') - line.count(')')}")

floor = 0
for i, c in enumerate(line, start=1):
    if c == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(f"Part 2: {i}")
        break
