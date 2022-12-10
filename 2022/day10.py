import sys

s = [l.split() for l in sys.stdin.read().splitlines()]
X = 1
arr = [X]
for op, *v in s:
    arr.append(X)
    if op == "noop":
        continue
    elif op == "addx":
        X += int(v[0])
        arr.append(X)

inspect = [20, 60, 100, 140, 180, 220]
print("Part 1:", sum(arr[i - 1] * i for i in inspect))
print("Part 2:")
for x, pos in enumerate(arr):
    if x % 40 in (pos - 1, pos, pos + 1):
        print("#", end="")
    else:
        print(" ", end="")
    if x % 40 == 39:
        print("")
print("")
