import re

inp = "target area: x=253..280, y=-73..-46"

pat = re.compile(r"(-?\d+)")
x1, x2, y1, y2 = list(map(int, pat.findall(inp)))

ymax = (y1 * (y1 + 1 if y1 < 0 else -1)) // 2
print(f"Part 1: {ymax}")

count = 0
for dx_init in range(min(0, x1 - 1), max(0, x2 + 1)):
    for dy_init in range(y1, abs(y1)):
        solved = False
        dx, dy = dx_init, dy_init
        x = 0
        y = 0
        while y > y1 and x < x2:
            x += dx
            y += dy
            if dx < 0:
                dx += 1
            if dx > 0:
                dx -= 1
            dy -= 1
            if x1 <= x <= x2 and y1 <= y <= y2:
                count += 1
                break
print(f"Part 2: {count}")
