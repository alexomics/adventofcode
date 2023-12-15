import sys
import re
from functools import reduce, partial


def H(curr, char):
    curr += ord(char)
    curr *= 17
    curr %= 256
    return curr


HASH = partial(lambda it: reduce(H, it, 0))
cmds = sys.stdin.read().strip().split(",")
print(sum(HASH(c) for c in cmds))

box = {i: [] for i in range(256)}
for cmd in cmds:
    name, op, v = re.split("(-|=)", cmd)
    h = HASH(name)
    if op == "-":
        box[h] = [(lens, val) for lens, val in box[h] if lens != name]
    elif op == "=":
        v = int(v)
        if any(name == lens for lens, _ in box[h]):
            box[h] = [(lens, v if lens == name else val) for lens, val in box[h]]
        else:
            box[h].append((name, v))

p2 = sum((i + 1) * (j + 1) * v for i, b in box.items() for j, (n, v) in enumerate(b))
print(p2)
