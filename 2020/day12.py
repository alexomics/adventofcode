import sys

lines = [(l[:1], int(l[1:])) for l in sys.stdin]

x, y, d = 0, 0, 0

# We are initially facing east, so that is 0
#   All turns are multiples of 90º, so total
#   degrees % 360 gives a relative direction
dir_conv = {0: "E", 90: "N", 180: "W", 270: "S"}

for action, val in lines:
    if action == "F":
        action = dir_conv[d % 360]
    if action == "N":
        y += val
    elif action == "E":
        x += val
    elif action == "S":
        y -= val
    elif action == "W":
        x -= val
    elif action == "L":
        d += val
    elif action == "R":
        d -= val

print(f"Part 1: {abs(x) + abs(y)}")


def rotate(x, y, d):
    if d == 90:
        return -y, x
    elif d == 180:
        return -x, -y
    elif d == 270:
        return y, -x


i, j = 10, 1
x, y = 0, 0

for action, val in lines:
    if action == "F":
        x += i * val
        y += j * val
    elif action == "N":
        j += val
    elif action == "E":
        i += val
    elif action == "S":
        j -= val
    elif action == "W":
        i -= val
    elif action == "L":
        i, j = rotate(i, j, val)
    elif action == "R":
        i, j = rotate(i, j, 360 - val)

print(f"Part 2: {abs(x) + abs(y)}")
