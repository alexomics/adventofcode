import sys


def read_input(fh):
    for line in fh:
        if line.startswith("$"):
            name = line[1:].strip()
            break

    output = []

    for line in fh:
        if line.startswith("$"):
            yield name, output

            output = []
            name = line[1:].strip()
            continue
        output.append(line.strip())
    yield name, output


def nest(d):
    result = {}
    for key, value in d.items():
        target = result
        for k in key[:-1]:
            target = target.setdefault(k, {})
        target[key[-1]] = value
    return result


tree = {}
loc = []
for cmd, output in read_input(sys.stdin):
    cmd, *args = cmd.split()
    if cmd == "cd":
        arg = args[0]
        if arg != "..":
            loc.append(arg)
            tree[tuple(loc)] = {}
        else:
            loc.pop()
    elif cmd == "ls":
        tree[tuple(loc)] = {
            name: int(t) for t, name in (s.split() for s in output) if t != "dir"
        }


def traverse(tree, res={}, *path):
    s = 0
    for key, val in tree.items():
        if isinstance(val, int):
            s += val
        else:
            res, s_ = traverse(val, res, *path, key)
            s += s_

    if path:
        res[path] = s
    return res, s


res, t = traverse(nest(tree))
print("Part 1:", sum(i for k, i in res.items() if i < 100_000))

total = 70_000_000
target = 30_000_000
current = res[("/",)]
unused = total - current
min_delete_size = target - unused


deletable = []
for k, v in res.items():
    if v > min_delete_size:
        deletable.append((v, k))

increase, path = sorted(deletable)[0]
print("Part 2:", increase)
