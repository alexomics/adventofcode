import sys


def neighbours(col, row):
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            yield col + dc, row + dr


def enhance(inp, default, iterations):
    alg, img = inp.translate(str.maketrans(".#", "01")).split("\n\n")
    img = [list(l) for l in img.splitlines()]
    rows = len(img)
    cols = len(img[0])
    img = {(c, r): v for r, row in enumerate(img) for c, v in enumerate(row)}

    cols = range(cols)
    rows = range(rows)
    for _ in range(iterations):
        cols = range(cols[0] - 1, cols[-1] + 2)
        rows = range(rows[0] - 1, rows[-1] + 2)
        new_img = {
            (col, row): alg[
                int(
                    "".join(img.get((c, r), default) for c, r in neighbours(col, row)),
                    2,
                )
            ]
            for col in cols
            for row in rows
        }

        default = alg[int(default * 9, 2)]
        img = new_img

    return sum(map(int, img.values()))


inp = sys.stdin.read()
print(f"Part 1: {enhance(inp, '0', 2)}")
print(f"Part 2: {enhance(inp, '0', 50)}")
