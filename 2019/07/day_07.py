import fileinput
from itertools import permutations


OPS = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    99: 0,
}

_OP = {
    1: "add",
    2: "mul",
    3: "input",
    4: "output",
    5: "jump if true",
    6: "jump if false",
    7: "less than",
    8: "equals",
    99: "halt",
}


def run(D, name):
    def parse(_idx):
        # Get first OP code
        a, b, c, *de = f"{D[_idx]:05d}"
        modes, de = [int(c), int(b), int(a)], int("".join(de))
        _idx += 1  # Move pointer to first parameter
        # target pointer, parameter array
        update_idx, _params = 0, []

        for mode in modes[: OPS[de]]:
            _params.append(D[_idx] if mode else D[D[_idx]])
            update_idx = _idx if mode else D[_idx]
            _idx += 1

        return de, update_idx, _params, _idx

    idx = 0
    while D[idx] != 99:
        # print(f"{name}:{idx}:{','.join(map(str, D))}", end=": ")
        op, loc, params, idx = parse(idx)
        # print(f"{_OP.get(op, '??')} to {loc} ({params})")
        if op == 1:
            D[loc] = params[0] + params[1]
        elif op == 2:
            D[loc] = params[0] * params[1]
        elif op == 3:
            D[loc] = yield
            # print(f"{name} -> ", end="") # {D[loc]}")
        elif op == 4:
            yield params[0]
        elif op == 5:
            if params[0]:
                idx = params[1]
        elif op == 6:
            if not params[0]:
                idx = params[1]
        elif op == 7:
            D[loc] = int(params[0] < params[1])
        elif op == 8:
            D[loc] = int(params[0] == params[1])
        else:
            assert False


if __name__ == "__main__":
    L = [int(i) for l in fileinput.input() for j, i in enumerate(l.strip().split(","))]
    m = 0
    for i, perms in enumerate([permutations(range(5)), permutations(range(5, 10))], start=1):
        m = 0
        for a, b, c, d, e in perms:
            # print(f"{a}{b}{c}{d}{e}")
            gens = [
                (run(L[:], "a"), a),
                (run(L[:], "b"), b),
                (run(L[:], "c"), c),
                (run(L[:], "d"), d),
                (run(L[:], "e"), e)
            ]
            for g, v in gens:
                next(g)
                g.send(v)

            finished = False
            first = True
            v = 0
            while not finished:
                for g, _ in gens:
                    try:
                        if not first:
                            next(g)
                        # print(f"\n  val: {v:>10}", end=" -> ")
                        v = g.send(v)
                        # print(f"{v:<10}", end="")
                    except StopIteration:
                        finished = True

                first = False
            m = max(m, v)

        print(f"\nPart {i}: {m}")
