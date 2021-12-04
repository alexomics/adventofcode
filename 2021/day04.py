import sys

sequence, *boards = sys.stdin.read().split("\n\n")
sequence = [int(x) for x in sequence.split(",")]
boards = [[[int(x) for x in l.split()] for l in b.strip().split("\n")] for b in boards]


def wins(board, nums):
    rows_and_cols = board + [list(b) for b in zip(*board)]
    return any(all(x in nums for x in rc) for rc in rows_and_cols)


winner = False
seen_nums = set()
for n in sequence:
    seen_nums.add(n)

    for board in boards:
        if wins(board, seen_nums):
            not_seen = sum([i for r in board for i in r if i not in seen_nums])
            print(f"Part 1: {not_seen * n}")
            winner = True
            break

    if winner:
        break

seen_nums = set()
for n in sequence:
    seen_nums.add(n)

    for board in boards:
        if wins(board, seen_nums):
            boards.remove(board)
    if not boards:
        # None left
        not_called = set(i for r in board for i in r)
        print(f"Part 2: {n * sum(not_called - seen_nums)}")
        break
