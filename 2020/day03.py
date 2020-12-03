import sys

lines = [l.strip() for l in open(sys.argv[1])]

rows = len(lines)
cols = len(lines[0])


def f(right, down):
    row = 0
    col = 0
    trees = 0
    while row < rows:
        row += down
        col += right
        if row >= rows:
            break
        if lines[row][col % cols] == "#":
            trees += 1
    return trees


print(f"Part 1: {f(3, 1)}")
print(f"Part 2: {f(1, 1) * f(3, 1) * f(5, 1) * f(7, 1) * f(1, 2)}")
