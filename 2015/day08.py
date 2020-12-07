import sys
from ast import literal_eval

x, y = 0, 0
for s in open(sys.argv[1], "rb"):
    s = s[:-1] if s.endswith(b"\n") else s
    x += len(s) - len(literal_eval(s.decode()))
    y += len(s.replace(b"\\", b"\\\\").replace(b'"', b'\\"')) - len(s) + 2
print(f"Part 1: {x}\nPart 2: {y}")
