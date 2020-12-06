import sys
import functools
import operator


ops = {
    "AND": operator.and_,
    "OR": operator.or_,
    "LSHIFT": operator.lshift,
    "RSHIFT": operator.rshift,
    "NOT": operator.invert,
}
d = dict(l.strip().split(" -> ")[::-1] for l in open(sys.argv[1]))


@functools.lru_cache
def evaluate(output):
    try:
        return int(output)
    except:
        pass

    command = d[output].split()

    if len(command) == 1:
        return evaluate(command[0])
    elif len(command) == 2:
        op, inp = command
        return ops[op](evaluate(inp))
    elif len(command) == 3:
        inp1, op, inp2 = command
        return ops[op](evaluate(inp1), evaluate(inp2))


ans = evaluate("a")
print(f"Part 1: {ans}")
d["b"] = str(ans)
evaluate.cache_clear()
print(f"Part 2: {evaluate('a')}")
