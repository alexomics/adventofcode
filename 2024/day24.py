# {('z13', 'pqc'), ('bgs', 'z31'), ('wsv', 'rjm'), ('swt', 'z07')}
# bgs,pqc,rjm,swt,wsv,z07,z13,z31
import sys
from collections import deque


def decode(vals, pre):
    vals_ = {k: str(v) for k, v in vals.items() if k.startswith(pre)}
    r, k = "", 0
    while (key := f"{pre}{k:>02}") in vals_:
        r += vals_[key]
        k += 1
    return int(r[::-1], 2)


# inputs, data = sys.stdin.read().strip().split("\n\n")
inputs, data = open("input").read().strip().split("\n\n")
inputs = dict(l.split(": ") for l in inputs.splitlines())
inputs = {k: int(v) for k, v in inputs.items()}
x, y = decode(inputs, "x"), decode(inputs, "y")
data_ = deque(data.splitlines())
while data_:
    line = data_.popleft()
    a, op, b, _, res = line.split()
    if not (a in inputs and b in inputs):
        data_.append(line)
        continue
    match op:
        case "AND":
            inputs[res] = inputs[a] & inputs[b]
        case "OR":
            inputs[res] = inputs[a] | inputs[b]
        case "XOR":
            inputs[res] = inputs[a] ^ inputs[b]
        case _:
            raise TabError

print(f"{x=} {y=} {x+y=}")
zz = decode(inputs, "z")
print(zz)


def ripple_carry_adder(A: str, B: str):
    """This impl is so I know what this is/does

    Steps are:
    1. Start from LSB: Add the least significant bit of A and B along with an initial carry of 0.
    2. For each bit:
        - Sum = A[i] XOR B[i] XOR Carry
        - Carry = (A[i] AND B[i]) OR (Carry AND (A[i] XOR B[i]))
    3. Propagate the carry: The carry from each bit is sent as the carry to the next higher bit.
    4. Repeat: This process continues bit by bit until all bits have been processed.
    """
    # padding with 0s if needed
    n = max(len(A), len(B))
    a = A.zfill(n)
    b = B.zfill(n)

    sum_bits, carry = [], 0
    for bit_a, bit_b in zip(a[::-1], b[::-1]):
        bit_a, bit_b = int(bit_a), int(bit_b)
        sum_bit = bit_a ^ bit_b ^ carry
        carry = (bit_a & bit_b) | (carry & (bit_a ^ bit_b))
        sum_bits.append(sum_bit)
    if carry:
        sum_bits.append(1)
    res = "".join(map(str, sum_bits[::-1]))
    return res, int(res, 2)


# done manually with _a lot_ of help from the megathread/reading
