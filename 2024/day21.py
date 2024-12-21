import sys
from collections import Counter

# fmt: off
numeric = {
    (0, 0): "7", (1, 0): "8", (2, 0): "9",
    (0, 1): "4", (1, 1): "5", (2, 1): "6",
    (0, 2): "1", (1, 2): "2", (2, 2): "3",
                 (1, 3): "0", (2, 3): "A",
}
numeric.update({v: k for k, v in numeric.items()})
directional = {
                 (1, 0): "^", (2, 0): "A",
    (0, 1): "<", (1, 1): "v", (2, 1): ">",
}
directional.update({v: k for k, v in directional.items()})
# fmt: on
codes = sys.stdin.read().strip().splitlines()


def pairwise(iterable):
    # pairwise('ABCDEFG') → AB BC CD DE EF FG
    iterator = iter(iterable)
    a = next(iterator, None)
    for b in iterator:
        yield a, b
        a = b


def jump(grid, curr, target):
    cx, cy = curr
    tx, ty = target
    dx, dy = tx - cx, ty - cy
    h = "<" * -dx if dx < 0 else ">" * dx
    v = "^" * -dy if dy < 0 else "v" * dy
    # Check corners so we don't fall of the grid
    if dx > 0 and (cx, ty) in grid:
        return f"{v}{h}A"
    if (tx, cy) in grid:
        return f"{h}{v}A"
    if (cx, ty) in grid:
        return f"{v}{h}A"
    raise TabError(f"{curr=} {target=} {(dx,dy)=} {grid=}")


p1, p2 = 0, 0
for code in codes:
    n = int(code[:-1])
    pairs = pairwise(map(numeric.get, "A" + code))
    code_ = Counter(["".join(jump(numeric, a, b) for a, b in pairs)])
    for i in range(25):
        new_code = Counter()
        for steps, count in code_.items():
            pairs = pairwise(map(directional.get, "A" + steps))
            next_ = Counter(jump(directional, a, b) for a, b in pairs)
            for k in next_:
                next_[k] *= count
            new_code.update(next_)

        code_ = new_code
        if i == 1:
            p1 += sum(len(k) * v for k, v in code_.items()) * n
    p2 += sum(len(k) * v for k, v in code_.items()) * n

print(p1, p2, sep="\n")
