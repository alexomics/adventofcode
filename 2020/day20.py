import sys
from collections import defaultdict, namedtuple


BORDERS = namedtuple("BORDERS", "top right bottom left")


class Grid:
    def __init__(self, tile, grid):
        self.tile = int(tile[5:-1]) if tile.startswith("Tile") else tile
        self.grid = [g for g in grid.split("\n") if g]
        self.grid = [list(g) for g in grid.split("\n") if g]
        self.all_grids = {k: g for k, g in enumerate(self.get_all_grids(self.grid))}
        self.borders = {i: self.get_borders(g) for i, g in self.all_grids.items()}

    def __str__(self):
        return "\n".join(map("".join, self.grid))

    def __repr__(self):
        return f"{self}"

    def __getitem__(self, item):
        return self.all_grids[item]

    @staticmethod
    def get_borders(grid):
        top = "".join(grid[0])
        right = "".join(l[-1] for l in grid)
        bottom = "".join(grid[-1])
        left = "".join(l[0] for l in grid)
        return BORDERS(top, right, bottom, left)

    @staticmethod
    def get_all_grids(grid):
        res = [g for x in Grid.all_flips(grid) for g in Grid.all_rotations(x)]
        ret = []
        for g in res:
            if g not in ret:
                ret.append(g)
        return ret

    @staticmethod
    def rotate(grid):
        return list(map(list, zip(*grid)))

    @staticmethod
    def all_rotations(grid):
        res = [grid]
        for _ in range(3):
            grid = Grid.rotate(grid)
            res.append(grid)
        return res

    @staticmethod
    def all_flips(grid):
        return [
            grid,
            grid[::-1],
            [l[::-1] for l in grid],
            [l[::-1] for l in grid[::-1]],
        ]

    @staticmethod
    def iter_window(grid, dx, dy):
        x, y = len(grid[0]), len(grid)
        for i in range(x - dx):
            for j in range(y - dy):
                yield [k[i : i + dx] for k in grid[j : j + dy]]


class Img:
    def __init__(self, imgs):
        self.imgs = imgs
        self.grids = {p.tile: p for p in [Grid(*g.split("\n", 1)) for g in self.imgs]}
        self.tiles = self.grids.keys()
        self.dims = int(len(self.grids) ** 0.5)
        self.img = [[(None, None)] * self.dims for _ in range(self.dims)]
        self.img = self.assemble_image(self.img, 0, 0, set())
        self.trimmed = self.trim()

    def __str__(self):
        return Img.print_img(self.img)

    @property
    def corners(self):
        return (
            self.img[0][0][0]
            * self.img[0][-1][0]
            * self.img[-1][0][0]
            * self.img[-1][-1][0]
        )

    @staticmethod
    def print_img(img):
        a = ""
        for i, row in enumerate(img):
            s = "  ".join(
                f"{'' if x is None else x:>4} \033[96m{'' if y is None else y:>2}\033[0m"
                for x, y in row
            )
            if i == 0:
                a += f"[{s},"
            else:
                a += f"\n {s},"
        print(f"{a[:-1]}]")

    def trim(self):
        trimmed = [[None] * self.dims for _ in range(self.dims)]
        for i, row in enumerate(self.img):
            for j, (tile, idx) in enumerate(row):
                trimmed[i][j] = ["".join(g[1:-1]) for g in self.grids[tile][idx][1:-1]]
        return trimmed

    def assemble_image(self, image, x, y, seen):
        # self.print_img(image)
        if y == self.dims:
            return image

        next_x = x + 1
        next_y = y
        if next_x == self.dims:
            next_x = 0
            next_y += 1

        for tile, grids in self.grids.items():
            if tile in seen:
                continue
            seen.add(tile)
            for i, curr in grids.borders.items():
                if x > 0:
                    prev_num, prev_idx = image[y][x - 1]
                    prev = self.grids[prev_num].borders[prev_idx]
                    if curr.left != prev.right:
                        continue
                if y > 0:
                    prev_num, prev_idx = image[y - 1][x]
                    prev = self.grids[prev_num].borders[prev_idx]
                    if curr.top != prev.bottom:
                        continue
                image[y][x] = (tile, i)
                answer = self.assemble_image(image, next_x, next_y, seen)
                if answer is not None:
                    return answer
            seen.remove(tile)


lines = open(sys.argv[1]).read().split("\n\n")
img = Img(lines)
print(f"Part 1: {img.corners}")

MONSTER = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
MONSTER = [list(r) for r in MONSTER.split("\n")]
M = set((x, y) for y, l in enumerate(MONSTER) for x, c in enumerate(l) if c == "#")
mx, my = len(MONSTER[0]), len(MONSTER)

comp = []
for row in img.trimmed:
    n = len(row[0])
    for i in range(n):
        comp.append("".join(r[i] for r in row))

image = Grid("Image", "\n".join(comp))
res = []
r = None
for idx, grid in image.all_grids.items():
    c = set((x, y) for y, l in enumerate(grid) for x, c in enumerate(l) if c == "#")
    count = len(c)
    for s in Grid.iter_window(grid, mx, my):
        w = set((x, y) for y, l in enumerate(s) for x, c in enumerate(l) if c == "#")
        if M.issubset(w):
            r = idx
            count -= len(M)
    res.append(count)

if r is not None:
    print(f"Part 2: {res[r]}")
