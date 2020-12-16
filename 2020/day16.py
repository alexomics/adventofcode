import sys

rules, ticket, nearby = [l.splitlines() for l in open(sys.argv[1]).read().split("\n\n")]
rules = {
    l.split(": ")[0]: [
        list(map(int, x.split("-"))) for x in l.split(": ")[1].split(" or ")
    ]
    for l in rules
}
ticket = list(map(int, ticket[1].split(",")))
nearby = [list(map(int, l.split(","))) for l in nearby[1:]]

c = 0
for t in nearby:
    for i in t:
        p = any(a <= i <= b for v in rules.values() for a, b in v)
        if not p:
            c += i
print(f"Part 1: {c}")

valid_nearby = [
    t
    for t in nearby
    if all(any(a <= n <= b for v in rules.values() for a, b in v) for n in t)
]

fields = [set(rules.keys()) for _ in ticket]

for t in valid_nearby:
    for i, value in enumerate(t):
        for k, v in rules.items():
            if not any(a <= value <= b for a, b in v):
                fields[i].remove(k)

while not all(len(f) == 1 for f in fields):
    for i in range(len(fields)):
        f = fields[i]
        if len(f) == 1:
            for j in range(len(fields)):
                if j != i:
                    fields[j] -= f

c = 1
for i, t in enumerate(ticket):
    for field in fields[i]:
        if field.startswith("departure"):
            c *= t
print(f"Part 2: {c}")
