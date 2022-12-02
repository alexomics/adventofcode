import sys

s = sys.stdin.read()
lines = [
    list(map(int, l.split()))
    for l in s.strip()
    .replace("A", "1")  # ROCK
    .replace("B", "2")  # PAPER
    .replace("C", "3")  # SCISSORS
    .replace("X", "1")  # ROCK
    .replace("Y", "2")  # PAPER
    .replace("Z", "3")  # SCISSORS
    .splitlines()
]

total = 0
for op, you in lines:
    if op == 1 and you == 1:
        total += you + 3
    elif op == 1 and you == 2:
        total += you + 6
    elif op == 1 and you == 3:
        total += you + 0
    elif op == 2 and you == 1:
        total += you + 0
    elif op == 2 and you == 2:
        total += you + 3
    elif op == 2 and you == 3:
        total += you + 6
    elif op == 3 and you == 1:
        total += you + 6
    elif op == 3 and you == 2:
        total += you + 0
    elif op == 3 and you == 3:
        total += you + 3

print(f"Part 1: {total}")

total = 0
for op, you in lines:
    if op == 1 and you == 1:
        total += 3 + 0
    elif op == 1 and you == 2:
        total += 1 + 3
    elif op == 1 and you == 3:
        total += 2 + 6
    elif op == 2 and you == 1:
        total += 1 + 0
    elif op == 2 and you == 2:
        total += 2 + 3
    elif op == 2 and you == 3:
        total += 3 + 6
    elif op == 3 and you == 1:
        total += 2 + 0
    elif op == 3 and you == 2:
        total += 3 + 3
    elif op == 3 and you == 3:
        total += 1 + 6

print(f"Part 2: {total}")
