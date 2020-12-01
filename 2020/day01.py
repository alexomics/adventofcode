import sys

with open(sys.argv[1], "r") as f:
    lines = [int(i.strip()) for i in f]

for i in lines:
    for j in lines:
        if 2020 - i - j == 0:
            print(i, j, i * j)

for i in lines:
    for j in lines:
        for k in lines:
            if 2020 - i - j -k == 0:
                print(i, j, k, i * j * k)
