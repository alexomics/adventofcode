import sys
import re
import collections

w = re.compile(r"\w+")
lines = [list(map(w.findall, l.split("contains"))) for l in open(sys.argv[1])]

possibles = collections.defaultdict(list)
all_ings = []
for ingredients, allergens in lines:
    all_ings.extend(ingredients)
    for a in allergens:
        possibles[a].append(set(ingredients))

possibles = {k: set.intersection(*v) for k, v in possibles.items()}
p = set.union(*possibles.values())
print("Part 1:", sum(ing not in p for ing in all_ings))

alg_ings = {}
while possibles:
    for allergen, ings in possibles.items():
        if len(ings) == 1:
            break
    ing = ings.pop()
    alg_ings[allergen] = ing
    del possibles[allergen]
    for allergen in possibles:
        possibles[allergen].difference_update({ing})
print("Part 2:", ",".join(ing for _, ing in sorted(alg_ings.items())))
