from itertools import cycle

L = [int(i) for i in open("input.txt")]

print(sum(L))

seen = set()
freq = 0

for i in cycle(L):
    freq += i
    if freq in seen:
        break
    seen.add(freq)

print(freq)
