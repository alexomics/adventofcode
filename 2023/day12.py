import sys
import functools
import re


def parse(stream):
    stream_ = map(str.split, stream)
    yield from ((s, tuple(map(int, b.split(",")))) for s, b in stream_)


@functools.cache
def f(dots, blocks):
    return (
        not blocks
        if not dots
        else (dots[0] != "#" and f(dots[1:], blocks))
        + (
            blocks
            and re.match(rf"[#?]{{{blocks[0]}}}([.?]|$)", dots)
            and f(dots[blocks[0] + 1 :], blocks[1:])
            or 0
        )
    )


p1, p2 = 0, 0
for spec, blocks in parse(sys.stdin):
    spec2 = "?".join([spec, spec, spec, spec, spec])
    blocks2 = blocks * 5
    p1 += f(spec, blocks)
    p2 += f(spec2, blocks2)
print(p1, p2, sep="\n")
