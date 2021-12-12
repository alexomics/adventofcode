import sys
from collections import defaultdict, deque

edges = defaultdict(set)
for line in sys.stdin:
    start, end = line.strip().split("-")
    edges[start].add(end)
    edges[end].add(start)


def search(G, start, seen, part_2=False):
    if start == "end":
        return 1

    total = 0
    for end in G[start]:
        if end not in seen:
            tmp = {end} if end.islower() else set()
            total += search(G, end, seen.union(tmp), part_2)
        elif part_2 and end != "start":
            total += search(G, end, seen, False)
    return total


print(f"Part 1: {search(edges, 'start', {'start'})}")
print(f"Part 2: {search(edges, 'start', {'start'}, True)}")
