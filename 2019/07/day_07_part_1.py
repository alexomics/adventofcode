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


def run(D, inputs, prev_out):
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

    inputs = inputs + prev_out
    idx = 0
    while D[idx] != 99:
        # print(f"{','.join(map(str, D))}", end=": ")
        op, loc, params, idx = parse(idx)
        # print(f"{op} to {loc} ({params})")
        if op == 1:
            D[loc] = params[0] + params[1]
        elif op == 2:
            D[loc] = params[0] * params[1]
        elif op == 3:
            D[loc] = inputs.pop(0) if inputs else 0
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
    for p in permutations(range(5)):
        r_out = []
        for x, a in enumerate(p):
            r_out = list(run(L[:], [a], r_out))
        m = max(m, *r_out)
    print(m)
