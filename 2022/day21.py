import sys
import operator


OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "=": operator.eq,
}

s = sys.stdin.read().splitlines()
data = {l.split(":")[0]: l.split(": ")[-1].split() for l in s}

done = {k: int(v[0]) for k, v in data.items() if len(v) == 1}
todo = {k: v for k, v in data.items() if len(v) == 3}
while "root" not in done:
    for k, (a, op, b) in todo.items():
        if a in done and b in done:
            a, b = done[a], done[b]
            done[k] = OPS[op](a, b)
    todo = {x: y for x, y in todo.items() if x not in done}
print("Part 1:", int(done["root"]))

a, _, b = data["root"]
data["root"] = [a, "=", b]
done = {k: int(v[0]) for k, v in data.items() if len(v) == 1}
done["humn"] = "???"
todo = {k: v for k, v in data.items() if len(v) == 3}
while "root" not in done:
    for k, (a, op, b) in todo.items():
        if a in done and b in done:
            a, b = done[a], done[b]
            done[k] = f"({a} {op} {b})"
    todo = {x: y for x, y in todo.items() if x not in done}

a, b = done["root"][1:-1].split("=")
if "???" in a:
    a, b = b, a
a = eval(a)
guess, add = 0, 10 ** 32
cmp, tries = operator.gt, 0
switches = 0
while True:
    v = eval(b.replace("???", str(guess)))
    if v == a:
        print("Part 2:", guess)
        break
    if tries > 1000:
        if switches > 1:
            assert False
        guess, add = 0, 10 ** 32
        cmp = operator.lt
        tries = 0
        switches += 1

    if cmp(v, a):
        guess += add
    else:
        guess -= add
        add //= 2
    tries += 1
