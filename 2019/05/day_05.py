import fileinput


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


def run(D):
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
        # print(f"{idx:>3}:", end="")
        op, loc, params, idx = parse(idx)
        # print(f"{idx:>3}: code {op} acts on {loc} using values {params}")
        if op == 1:
            D[loc] = params[0] + params[1]
        elif op == 2:
            D[loc] = params[0] * params[1]
        elif op == 3:
            D[loc] = int(input(f"Change index {loc}: "))
        elif op == 4:
            print(f"Out: {params[0]}")
        elif op == 5:
            if params[0]:
                # print(f"pointer changed: {idx} -> {params[1]}")
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

    return D[0]


run({j: int(i) for l in fileinput.input() for j, i in enumerate(l.strip().split(","))})
