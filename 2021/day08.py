import sys


def get_nine(four, maybe_nine):
    return len(four & maybe_nine) == 4


def get_three(seven, maybe_three):
    return len(maybe_three - seven) == 2


def get_two(nine, maybe_two):
    return maybe_two - nine


def get_five(two, three, maybe_five):
    return maybe_five != two and maybe_five != three


def get_six(one, eight, maybe_six):
    return len(maybe_six & eight & one) == 1


def get_zero(six, nine, maybe_zero):
    return maybe_zero != six and maybe_zero != nine


seg_nums = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}


def decode(entry):
    # Possible values
    p = {i: [] for i in range(10)}
    pats, code = entry.strip().split("|")
    for signal in pats.split() + code.split():
        for s in seg_nums[len(signal)]:
            p[s].append(set(signal))
    p = {
        k: [set(vv) for vv in set(tuple(sorted(v_)) for v_ in v)] for k, v in p.items()
    }
    p = {k: v[0] if len(v) == 1 else v for k, v in p.items()}
    p[9] = [s for s in p[9] if get_nine(p[4], s)][0]
    p[3] = [s for s in p[3] if get_three(p[7], s)][0]
    p[2] = [s for s in p[2] if get_two(p[9], s)][0]
    p[5] = [s for s in p[5] if get_five(p[2], p[3], s)][0]
    p[6] = [s for s in p[6] if get_six(p[1], p[8], s)][0]
    p[0] = [s for s in p[0] if get_zero(p[6], p[9], s)][0]
    rev = {"".join(sorted(v)): str(k) for k, v in p.items()}
    return int("".join(rev["".join(sorted(s))] for s in code.split()))


p1, p2 = 0, 0
for line in sys.stdin:
    x = decode(line)
    s = str(x)
    p1 += sum(s.count(n) for n in "1478")
    p2 += x
print(f"Part 1: {p1}\nPart 2: {p2}")
