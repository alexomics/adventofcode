import sys
from collections import deque
from functools import cache


def pairwise(iterable):
    # pairwise('ABCDEFG') → AB BC CD DE EF FG

    iterator = iter(iterable)
    a = next(iterator, None)

    for b in iterator:
        yield a, b
        a = b


"""
code='029A' (4)
      029A
code='<A^A^^>AvvvA' (12)
      <A^A>^^AvvvA
code='v<<A>>^A<A>AvA^<AA>Av<AAA>^A' (28)
      v<<A>>^A<A>AvA<^AA>A<vAAA>^A

      <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A

"""
DIRS_MAP = {
    "<": (-1, 0),
    "v": (0, 1),
    ">": (1, 0),
    "^": (0, -1),
}
DIRS = {v: k for k, v in DIRS_MAP.items()}
# fmt: off
numeric = {
    (0, 0): "7", (1, 0): "8", (2, 0): "9",
    (0, 1): "4", (1, 1): "5", (2, 1): "6",
    (0, 2): "1", (1, 2): "2", (2, 2): "3",
                 (1, 3): "0", (2, 3): "A",
}
directional = {
                 (1, 0): "^", (2, 0): "A",
    (0, 1): "<", (1, 1): "v", (2, 1): ">",
}
# fmt: on
codes = sys.stdin.read().strip().splitlines()

numeric_jumps = {}
for curr, target, move in [
    ("7", "8", ">"),
    ("7", "4", "v"),
    ("8", "9", ">"),
    ("8", "5", "v"),
    ("9", "6", "v"),
    ("4", "5", ">"),
    ("4", "1", "v"),
    ("5", "6", ">"),
    ("5", "2", "v"),
    ("6", "3", "v"),
    ("1", "2", ">"),
    ("2", "3", ">"),
    ("2", "0", "v"),
    ("3", "A", "v"),
    ("0", "A", ">"),
]:
    numeric_jumps[(curr, target)] = move
    numeric_jumps[(target, curr)] = {"v": "^", ">": "<"}[move]


# @cache
# def jump_n(curr, target):
#     return [(curr, target)]


def walk(grid, pos, target):
    todo = deque([pos])
    came_from = {pos: None}
    x, y = pos
    while todo:
        x, y = todo.popleft()
        if grid[(x, y)] == target:
            break
        for dx, dy in DIRS:
            x_, y_ = x + dx, y + dy
            if (x_, y_) not in came_from and (x_, y_) in grid:
                todo.append((x_, y_))
                came_from[(x_, y_)] = (x, y)
    curr = (x, y)
    path = []
    while curr != pos:
        path.append(curr)
        curr = came_from[curr]
    path.append(pos)
    return path[::-1]


s = 0
for code in codes:
    n = int(code[:-1])
    typed = []
    positions = deque(
        [
            (numeric, 2, 3),
            (directional, 2, 0),
            (directional, 2, 0),
            # (directional, 2, 0),
        ]
    )
    while positions:
        k, x, y = positions.popleft()
        print(f"{code=} ({len(code)})")
        res = []
        for char in code:
            path = walk(k, (x, y), char)
            diff = [(p2[0] - p1[0], p2[1] - p1[1]) for p1, p2 in pairwise(path)]
            c = "".join([DIRS[d] for d in diff]) + "A"
            (x, y) = path[-1]
            print(f"{char=} {c} {k[(x, y)]}")
            res.append(c)
        typed.append(res)
        code = "".join(res)
    print(f"{code=} ({len(code)})")

    # print(typed)
    print(len("".join(typed[-1])), "*", n)
    s += len("".join(typed[-1])) * n
print(s)
