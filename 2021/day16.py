import sys
from functools import reduce
from operator import mul, gt, lt, eq


CHAR_MAP = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


class Buffer:
    def __init__(self, bits):
        self.arr = bits
        self.ptr = 0
        self.it = iter(self.arr)

    def read_int(self, n):
        return int(self.read_str(n), 2)

    def read_str(self, n):
        self.ptr += n
        return "".join(next(self.it) for _ in range(n))


def parse(r):
    version = r.read_int(3)
    op = r.read_int(3)

    if op == 4:
        value = ""
        while r.read_int(1) != 0:
            value += r.read_str(4)
        value += r.read_str(4)
        return version, op, int(value, 2)

    length_type = r.read_int(1)
    if length_type == 0:
        target = r.read_int(15) + r.ptr  # order matters!
        subs = []
        while r.ptr < target:
            subs.append(parse(r))
        return version, op, subs
    elif length_type == 1:
        subpackets = r.read_int(11)
        subs = []
        for _ in range(subpackets):
            subs.append(parse(r))
        return version, op, subs


def version_sum(packet):
    version, op, subpackets = packet
    if op == 4:
        return version
    else:
        return version + sum([version_sum(p) for p in subpackets])


operators = [
    sum,
    lambda s: reduce(mul, s),
    min,
    max,
    lambda s: s,
    lambda s: int(gt(*s)),
    lambda s: int(lt(*s)),
    lambda s: int(eq(*s)),
]


def eval_packet(packet):
    version, op, subpackets = packet
    if isinstance(subpackets, list):
        subpackets = list(map(eval_packet, subpackets))
    return operators[op](subpackets)


bits = sys.stdin.read().strip()
bits = "".join(map(CHAR_MAP.get, bits))
packets = parse(Buffer(bits))
print("Part 1:", version_sum(packets))
print("Part 2:", eval_packet(packets))
