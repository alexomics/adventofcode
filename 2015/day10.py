import re

p = re.compile(f"({'+|'.join('123456789')})")


def f(ns, s="1"):
    n = max(ns)
    for i in range(1, n + 1):
        t = ""
        for g in p.findall(s):
            t += f"{len(g)}{g[0]}"
        s = t
        if i in ns:
            yield s


for i, x in enumerate(f([40, 50], "1321131112"), 1):
    print(f"Part {i}: {len(x)}")
