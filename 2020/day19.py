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
    """Make all strings starting from `i`"""
    rule = rules[i]
    if isinstance(rule, str):
        return rule[1]
    out = []
    for option in rule:
        temp = [make_strs(next_i) for next_i in option]
        out.extend("".join(x) for x in product(*temp))
    return out


valid_strs = set(make_strs("0"))
print(f"Part 1: {sum(m in valid_strs for m in messages)}")


def make_str_from_rule(s, seq):
    """Attempt to make string `s` from rule `seq`"""
    if not s or not seq:
        return s == "" and seq == []
    rule = rules[seq[0]]
    if isinstance(rule, str):
        # Strip first character, False if cannot
        return make_str_from_rule(s[1:], seq[1:]) if s[0] in rule else False
    else:
        # Expand first term in seq rules list
        return any(make_str_from_rule(s, t + seq[1:]) for t in rule)


# Add rules for part 2
rules["8"] = [["42"], ["42", "8"]]
rules["11"] = [["42", "31"], ["42", "11", "31"]]

print(f"Part 2: {sum(make_str_from_rule(m, ['0']) for m in messages)}")
