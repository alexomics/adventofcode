import sys
from collections import defaultdict
from functools import lru_cache

lines = [int(l) for l in open(sys.argv[1])]
lines.extend([0, max(lines) + 3])
lines.sort()

nums = lines[:]
j = nums.pop(0)
d = defaultdict(int)
while nums:
    n = nums.pop(0)
    _d = n - j
    j += _d
    d[_d] += 1

print(f"Part 1: {d[3] * d[1]}")

d = {n: [x for x in lines[i:] if 1 <= x - n <= 3] for i, n in enumerate(lines)}


@lru_cache
def calc(start):
    if not d.get(start, []):
        # Reached the end, count this path
        return 1
    x = 0
    for n in d[start]:
        x += calc(n)
    return x


print(f"Part 2: {calc(min(lines))}")

"""
import networkx as nx
import matplotlib.pyplot as plt

G = nx.convert.from_dict_of_lists(d)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=50)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, arrows=True)
plt.show()
"""
