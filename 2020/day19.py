import sys
from functools import lru_cache
from itertools import product

rules, messages = open(sys.argv[1]).read().split("\n\n")
rules = {
    i: p if '"' in p else [x.split() for x in p.split(" | ")]
    for i, p in map(lambda s, c=": ": s.split(c), rules.splitlines())
}
messages = messages.splitlines()


@lru_cache
def make_strs(i):
    rule = rules[i]
    if isinstance(rule, str):
        return rule[1]
    out = []
    for option in rule:
        temp = [make_strs(next_i) for next_i in option]
        out.extend("".join(x) for x in product(*temp))
    return out


valid_strs = set(make_strs("0"))
a = sum(m in valid_strs for m in messages)
print(f"Part 1: {a}")
