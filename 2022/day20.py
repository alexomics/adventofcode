import sys


def mix(data, locs=(1000, 2000, 3000), its=1):
    N = len(data)
    reindex = list(range(N))
    for _ in range(its):
        for i, n in enumerate(data):
            old_idx = reindex.index(i)
            reindex.pop(old_idx)
            new_idx = (old_idx + n) % (N - 1)
            if new_idx == 0:
                reindex.append(i)
            else:
                reindex.insert(new_idx, i)

    z = reindex.index(data.index(0))
    return sum(data[reindex[(z + x) % N]] for x in locs)


s = list(map(int, sys.stdin.read().splitlines()))
print("Part 1:", mix(s))
s = [x * 811589153 for x in s]
print("Part 2:", mix(s, its=10))
