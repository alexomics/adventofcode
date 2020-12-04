import sys
import re


fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

print("Part 1:", end=" ")
print(
    sum(
        [
            set(re.findall("(\w+):", l)).issuperset(fields)
            for l in open(sys.argv[1]).read().split("\n\n")
        ]
    )
)

colour = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
lines = [re.findall("(\w+):(\S+)", l) for l in open(sys.argv[1]).read().split("\n\n")]

x = 0
for passport in lines:
    if not set([f[0] for f in passport]).issuperset(fields):
        continue

    d = dict(passport)

    x += all(
        [
            1920 <= int(d["byr"]) <= 2002,
            2010 <= int(d["iyr"]) <= 2020,
            2020 <= int(d["eyr"]) <= 2030,
            (
                (d["hgt"].endswith("cm") and 150 <= int(d["hgt"][:-2]) <= 193)
                or (d["hgt"].endswith("in") and 59 <= int(d["hgt"][:-2]) <= 76)
            ),
            re.fullmatch("#[\da-f]{6}", d["hcl"]),
            d["ecl"] in colour,
            re.fullmatch("\d{9}", d["pid"]),
        ]
    )

print(f"Part 2: {x}")
