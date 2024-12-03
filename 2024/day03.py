import sys
import re


pat = re.compile("mul\((\d+),(\d+)\)")
pat2 = re.compile("(do\(\)(.*?)don't\(\))", re.DOTALL)
inp = f"do(){sys.stdin.read()}don't()"
p1 = sum(int(m.group(1)) * int(m.group(2)) for m in pat.finditer(inp))
p2 = sum(
    int(m.group(1)) * int(m.group(2))
    for m_ in pat2.findall(inp)
    for m in pat.finditer(m_[0])
)

print(p1, p2, sep="\n")
