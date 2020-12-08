import re
from string import ascii_lowercase as A

ban_list = {"i", "o", "l"}
l = {b: i for i, b in enumerate(A, 1)}
l["z"] = 0


def g(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] in ban_list:
            s[i] = A[l[s[i]]]
            for j in range(i + 1, len(s)):
                s[j] = "a"
    i = len(s) - 1
    while True:
        was_z = s[i] == "z"
        s[i] = A[l[s[i]]]
        if was_z and i != 0:
            i -= 1
        else:
            i = len(s) - 1
            if not set(s) & ban_list:
                yield "".join(s)


triples = f"({'|'.join([f'{a}{b}{c}' for a, b, c in zip(A, A[1:], A[2:])])})"
doubles = [f"{a}{a}" for a in A]
pattern = re.compile(f"{triples}")
c = 0
for p in g("hxbxwxba"):
    x = 0
    for m in pattern.findall(p):
        x = sum(d in p for d in doubles)
    if x >= 2:
        print(p)
        c += 1
        if c >= 2:
            break
