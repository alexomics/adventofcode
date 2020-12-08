import sys

lines = [l.strip().split() for l in open(sys.argv[1])]


def run(p, p1=False):
    n = 0
    idx = 0
    s = set()
    while True:
        if idx in s:
            return n if p1 else None
        if idx == len(p):
            return n
        s.add(idx)
        op, i = p[idx]
        i = int(i)
        if op == "acc":
            n += i
            idx += 1
        elif op == "jmp":
            idx += i
        elif op == "nop":
            idx += 1


print(f"Part 1: {run(lines, p1=True)}")

for i in range(len(lines)):
    p = lines[:]
    if p[i][0] == "jmp":
        p[i] = ("nop", p[i][1])
    elif p[i][0] == "nop":
        p[i] = ("jmp", p[i][1])
    p2 = run(p)
    if p2 is not None:
        break

print(f"Part 2: {p2}")
