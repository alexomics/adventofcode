import sys
from collections import deque

inputs, data = sys.stdin.read().strip().split("\n\n")
inputs = dict(l.split(": ") for l in inputs.splitlines())
inputs = {k: int(v) for k, v in inputs.items()}
print(inputs)

data = deque(data.splitlines())
while data:
    line = data.popleft()
    a, op, b, _, res = line.split()
    if not (a in inputs and b in inputs):
        data.append(line)
        continue
    match op:
        case "AND": inputs[res] =inputs[a]&inputs[b]
        case "OR": inputs[res] =inputs[a]|inputs[b]
        case "XOR": inputs[res] =inputs[a]^inputs[b]
        case _: raise TabError
print(inputs)
r = ""
k = 0
while (x := f"z{k:0>2}") in inputs:
    r += str(inputs.pop(x))
    k += 1
r = r[::-1]
print(r, int(r, 2))
