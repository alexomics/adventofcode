import sys
import re
import operator
import collections
import math

ops = {"+": operator.add, "*": operator.mul}
digits = re.compile(r"\d+")
operation = re.compile(r"new = (.+)$")
s = sys.stdin.read().split("\n\n")


def parse_input(inp):
    d = {}
    for data in inp:
        monkey, items, op, test, test_true, test_false = data.split("\n")
        a, op, b = operation.findall(op)[0].split()
        d[digits.findall(monkey)[0]] = [
            collections.deque(map(int, digits.findall(items))),
            (a, ops.get(op), b),
            int(digits.findall(test)[0]),
            int(digits.findall(test_true)[0]),
            int(digits.findall(test_false)[0]),
        ]
    return d


def do_a_little_worrying(data, rounds=20, part=1):
    c = collections.Counter()
    lcm = math.lcm(*[t[2] for k, t in d.items()])
    count = 0
    while True:
        for k, (items, (a, op, b), test, test_true, test_false) in d.items():
            # print(f"Monkey {k}")
            while items:
                c[k] += 1
                item = items.popleft()
                # print(f"  inspect {item}")
                item = op(item, int(b) if b != "old" else item)
                if part == 1:
                    item = item // 3
                else:
                    item = item % lcm
                # print(f"  worry is now {item}")
                if item % test == 0:
                    # print(f"  divisible by {test}")
                    dest = test_true
                else:
                    # print(f"  not divisible by {test}")
                    dest = test_false
                d[str(dest)][0].append(item)
        count += 1
        if count == rounds:
            (_, a), (_, b) = c.most_common(2)
            return a * b


d = parse_input(s)
print("Part 1:", do_a_little_worrying(d, 20, 1))
d = parse_input(s)
print("Part 2:", do_a_little_worrying(d, 10000, 2))
