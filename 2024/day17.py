import sys
import re

data = sys.stdin.read().strip()
ops = {
    0: (lambda a, b, c, op, combo, ip: a // 2**combo, "A"),
    1: (lambda a, b, c, op, combo, ip: b ^ op, "B"),
    2: (lambda a, b, c, op, combo, ip: combo % 8, "B"),
    3: (lambda a, b, c, op, combo, ip: (op - 2 if a != 0 else ip), "ip"),
    4: (lambda a, b, c, op, combo, ip: b ^ c, "B"),
    5: (lambda a, b, c, op, combo, ip: combo % 8, "output"),
    6: (lambda a, b, c, op, combo, ip: a // 2**combo, "B"),
    7: (lambda a, b, c, op, combo, ip: a // 2**combo, "C"),
}


def parse(inp):
    regs, prog = inp.split("\n\n")
    regs = {l.split(" ")[1][0]: int(l.split(": ")[-1]) for l in regs.splitlines()}
    prog = list(map(int, re.findall("\d+", prog)))
    regs["ip"] = 0
    regs["output"] = []
    return regs, prog


def run(r, p):
    while r["ip"] < len(p):
        cmd = p[r["ip"]]
        op = p[r["ip"] + 1]
        combo = [0, 1, 2, 3, r["A"], r["B"], r["C"]][op]
        func, target = ops.get(cmd)
        res = func(r["A"], r["B"], r["C"], op, combo, r["ip"])
        if target == "output":
            r["output"].append(res)
        else:
            r[target] = res
        r["ip"] += 2


regs, prog = parse(data)
run(regs, prog)
print(",".join(map(str, regs["output"])))
regs, prog = parse(data)
todo = [(len(prog) - 1, 0)]
printed = False
for pos, val in todo:
    for a in range(val * 8, val * 8 + 8):
        regs, prog = parse(data)
        regs["A"] = a
        run(regs, prog)
        if regs["output"] == prog[pos:]:
            todo += [(pos - 1, a)]
            if pos == 0:
                print(a)
                printed = True
                break
        if printed:
            break
    if printed:
        break
