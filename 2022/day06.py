import sys

s = sys.stdin.read().strip()


def find(data, window_size):
    for i in range(len(data) - window_size):
        sub = set(data[i : i + window_size])
        if len(sub) == window_size:
            return i + window_size


print("Part 1:", find(s, 4))
print("Part 2:", find(s, 14))
