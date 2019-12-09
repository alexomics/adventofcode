import fileinput
from collections import defaultdict


OPS = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    9: 1,
    99: 0,
}


def run(D, inputs, prev_out):
    rel = 0
    def parse(_idx):
        # Get first OP code
        a, b, c, *de = f"{D[_idx]:05d}"
        modes, de = [int(c), int(b), int(a)], int("".join(de))
        _idx += 1  # Move pointer to first parameter
        # target pointer, parameter array
        update_idx, _params = 0, []

        for mode in modes[: OPS[de]]:
            if mode == 0:
                _params.append(D[D[_idx]])
            elif mode == 1:
                _params.append(D[_idx])
            elif mode == 2:
                _params.append(D[D[_idx] + rel])

            if modes[OPS[de] - 1] == 1:
                update_idx = _idx
            elif modes[OPS[de] - 1] == 2:
                update_idx = D[_idx] + rel
            else:
                update_idx = D[_idx]
            _idx += 1
        return de, update_idx, _params, _idx

    inputs = inputs + prev_out
    idx = 0
    while D[idx] != 99:
        # print(f"{','.join(map(str, D.values()))}", end=": ")
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
        elif op == 9:
            rel += params[0]
        else:
            assert False


if __name__ == "__main__":
    L = {j:int(i) for l in fileinput.input() for j, i in enumerate(l.strip().split(","))}
    # L = {j:int(i) for j, i in enumerate("109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99".split(","))}
    x = defaultdict(int)
    x.update(L)
    m = 0
    r_out = []
    r_out = list(run(x, [2], r_out))
    # m = max(m, *r_out)
    print(r_out)
