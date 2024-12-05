import sys
from collections import defaultdict
from functools import cmp_to_key


rules, pages = sys.stdin.read().strip().split("\n\n")
rules = [tuple(map(int, l.split("|"))) for l in rules.split("\n")]
pages = [list(map(int, l.split(","))) for l in pages.split("\n")]
rule_before = defaultdict(set)
for first, later in rules:
    rule_before[later].add(first)


@cmp_to_key
def cmp(a, b):
    return 1 if b in rule_before[a] else -1


p1, p2 = 0, 0
for page in pages:
    mid = len(page) // 2
    if sorted(page, key=cmp) == page:
        p1 += page[mid]
    else:
        page.sort(key=cmp)
        p2 += page[mid]
print(p1, p2, sep="\n")
