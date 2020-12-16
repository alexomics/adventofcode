import sys

lines = [l for l in open(sys.argv[1])]

rules = []
ticket = []
nearby = []
nb = False

for i in range(len(lines)):
    l = lines[i].strip()
    if not l:
        continue
    p = l.split(": ")
    if len(p) > 1:
        r = p[0]
        n = [list(map(int, x.split("-"))) for x in p[1].split(" or ")]
        rules.append((r, n))
    if l.startswith("your"):
        ticket = list(map(int, lines[i + 1].split(",")))
    if l.startswith("nearby"):
        nb = True
        continue
    if nb:
        nearby.append(list(map(int, l.split(","))))

rules = dict(rules)

c = 0
for t in nearby:
    for i in t:
        p = any(a <= i <= b for v in rules.values() for a, b in v)
        if not p:
            c += i
print(c)

valid_nearby = []
for t in nearby:
    if all(any(a <= n <= b for v in rules.values() for a, b in v) for n in t):
        valid_nearby.append(t)

fields = [set(rules.keys()) for _ in ticket]

for t in valid_nearby:
    for i in range(len(t)):
        value = t[i]
        for k, v in rules.items():
            ok1 = any(a <= value <= b for a, b in v)
            if not ok1:
                fields[i].remove(k)

for k in range(len(fields)):
    for i in range(len(fields)):
        if len(fields[i]) == 1:
            for j in range(len(fields)):
                if j != i:
                    fields[j] -= fields[i]

c = 1

for i in range(len(ticket)):
    for field in fields[i]:
        if field.startswith("departure"):
            c *= ticket[i]

print(c)
