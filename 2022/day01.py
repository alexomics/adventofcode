import sys

calories = sorted(
    (sum(map(int, l.split("\n"))) for l in sys.stdin.read().split("\n\n")), reverse=True
)

print(f"Part 1: {calories[0]}")
print(f"Part 2: {sum(calories[:3])}")
