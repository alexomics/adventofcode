import sys

sequence, *boards = sys.stdin.read().split("\n\n")

sequence = [int(x) for x in sequence.split(",")]
boards = [[[int(x) for x in l.split()] for l in b.strip().split("\n")] for b in boards]


def wins(board, nums):
    rows_and_cols = board + [list(b) for b in zip(*board)]
    return any(all(x in nums for x in rc) for rc in rows_and_cols)


winning_board = None
last_number = None
seen_nums = set()
for n in sequence:
    seen_nums.add(n)

    for board in boards:
        if wins(board, seen_nums):
            winning_board = board
            last_number = n
            break
    if winning_board is not None:
        break

ns = [x for r in winning_board for x in r if x not in seen_nums]
print(f"Part 1: {sum(ns) * last_number}")

winning_board = None
last_number = None
seen_nums = set()
for n in sequence:
    seen_nums.add(n)

    for board in boards:
        if wins(board, seen_nums):
            boards.remove(board)
    if not boards:
        # None left
        not_called = set(x for r in board for x in r)
        x = sum(not_called - seen_nums)
        print(f"Part 2: {n * x}")
        break
