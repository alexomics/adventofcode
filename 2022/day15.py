import sys
import re

from tqdm import tqdm
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches


def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def get_poly(source, beacon):
    m = manhattan_distance(source, beacon)
    sx, sy = source
    verts = [(sx - m, sy), (sx, sy - m), (sx + m, sy), (sx, sy + m), (sx - m, sy)]
    codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
    return Path(verts, codes)


pat = re.compile(r"(-?\d+)")
s = open(sys.argv[1]).read().splitlines()
s = [list(map(int, pat.findall(l))) for l in s]
y = 2000000
d = {(a, b): (c, d) for a, b, c, d in s}

xmin, xmax = float("inf"), float("-inf")
ymin, ymax = float("inf"), float("-inf")

# fig, ax = plt.subplots()
polys = {}
for s, b in d.items():
    path = get_poly(s, b)
    # patch = patches.PathPatch(path, facecolor="orange", lw=2, alpha=0.2)
    # ax.add_patch(patch)
    exts = path.get_extents()
    xmin = min(xmin, exts.xmin)
    xmax = max(xmax, exts.xmax)
    ymin = min(ymin, exts.ymin)
    ymax = max(ymax, exts.ymax)
    polys[s] = (b, path)

(xmin, xmax, ymin, ymax) = map(int, (xmin, xmax, ymin, ymax))
print(xmin, xmax, ymin, ymax)
# ax.set_xlim(xmin, xmax)
# ax.set_ylim(ymin, ymax)
# ax.grid()
# plt.show()
in_polys = False
c = 0
for x in tqdm(range(xmin, xmax + 1)):
    in_polys = any(
        p.contains_point((x, y)) for s, (b, p) in tqdm(polys.items(), leave=False)
    )
    if not in_polys:
        continue
    if (x, y) not in d.values():
        c += 1
print(c)
