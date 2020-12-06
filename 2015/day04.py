import sys
import hashlib

key = "ckczppom"
ans = ""
num = 0
six = 0
while not ans.startswith("00000"):
    num += 1
    ans = hashlib.md5(bytes(f"{key}{num}", "ascii")).hexdigest()
    if ans.startswith("000000"):
        six = num

print(f"Part 1: {num}")
if six:
    print(f"Part 2: {six}")
    sys.exit()
ans = ""
while not ans.startswith("000000"):
    num += 1
    ans = hashlib.md5(bytes(f"{key}{num}", "ascii")).hexdigest()

print(f"Part 2: {num}")
