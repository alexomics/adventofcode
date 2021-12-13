import sys


class TransparentPaper(dict):
    def set_folds(self, folds):
        if not hasattr(self, "folds"):
            self.folds = []
        for fold in folds:
            *_, axis = fold.split()
            axis, value = axis.split("=")
            self.folds.append((axis, int(value)))

    def __setitem__(self, key, value):
        if self.folds:
            for axis, fold in self.folds:
                kx, ky = key
                if axis == "x":
                    if kx < fold:
                        key = (kx, ky)
                    else:
                        key = (2 * fold - kx, ky)
                elif axis == "y":
                    if ky < fold:
                        key = (kx, ky)
                    else:
                        key = (kx, 2 * fold - ky)
                else:
                    raise ValueError()
        super().__setitem__(key, value)

    def __repr__(self):
        mx = max(dot[0] for dot in self.keys()) + 1
        my = max(dot[1] for dot in self.keys()) + 1
        out = []
        for y in range(my):
            s = ""
            for x in range(mx):
                s += "X" if (x, y) in self else " "
            out.append(s)
        return "\n".join(out)


dots, folds = sys.stdin.read().split("\n\n")

d = TransparentPaper()
d.set_folds(folds.splitlines()[:1])
for l in dots.splitlines():
    x, y = list(map(int, l.split(",")))
    d[(x, y)] = True
print(f"Part 1: {len(d)}")

d = TransparentPaper()
d.set_folds(folds.splitlines())
for l in dots.splitlines():
    x, y = list(map(int, l.split(",")))
    d[(x, y)] = True
print("Part 2:")
print(d)
