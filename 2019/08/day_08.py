import sys

assert len(sys.argv) == 4, "Usage: day_08.py width height input.txt"

with open(sys.argv[3], "r") as fh:
    image = [list(l.strip()) for l in fh][0]

width = int(sys.argv[1])
height = int(sys.argv[2])
_l = width * height
pixels = {"0": " ", "1": u"\u2588"}

res = []
c = 0
d = {}

while image:
    c += 1
    layer = image[:_l]
    image = image[_l:]

    res.append((layer.count("0"), layer.count("1") * layer.count("2")))
    d[c] = {i: pixels.get(j) for i, j in enumerate(layer, start=1) if j != "2"}


print(min(res, key=lambda x: x[0])[1])
r = {}
while d:
    k, v = d.popitem()
    r.update(v)

for i in range(1, _l + 1):
    print(r.get(i, ""), end="")
    if i % width == 0:
        print()
