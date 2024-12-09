import sys
from collections import deque
from copy import deepcopy
from dataclasses import dataclass
from itertools import zip_longest as zipl


@dataclass
class Block:
    id: int | None
    size: int


def checksum(fs):
    t, i = 0, 0
    for b in fs:
        if b.id is not None:
            for _ in range(b.size):
                t += i * b.id
                i += 1
        else:
            i += b.size
    return t


data = sys.stdin.read().strip()
fs = [
    [Block(i, int(x[0])), Block(None, int(x[1]))]
    for i, x in enumerate(zipl(data[::2], data[1::2], fillvalue=0))
]


def frag(fs):
    blocks, spaces = map(deque, zip(*fs))
    new = deque([blocks.popleft()])
    while blocks:
        curr = blocks.pop()
        if curr.size == spaces[0].size:
            spaces.append(spaces.popleft())
            new.append(curr)
            new.append(blocks.popleft())
        elif curr.size < spaces[0].size:
            spaces.append(Block(None, spaces[0].size - curr.size))
            spaces[0].size -= curr.size
            new.append(curr)
        else:
            new.append(Block(curr.id, spaces[0].size))
            blocks.append(Block(curr.id, curr.size - spaces[0].size))
            new.append(blocks.popleft())
            spaces.append(spaces.popleft())
    return new


def better_frag(fs):
    blocks = [b_ for b in fs for b_ in b]
    for id_ in range((len(blocks) // 2) - 1, -1, -1):
        for i, b in enumerate(blocks):
            if b.id == id_:
                break
        for j, nb in enumerate(blocks):
            if j >= i:
                break
            if nb.id is None and nb.size >= b.size:
                blocks[j] = deepcopy(b)
                if nb.size > b.size:
                    blocks.insert(j + 1, Block(None, nb.size - b.size))
                    i += 1
                if i > 0 and blocks[i - 1].id is None:
                    blocks[i - 1].size += b.size
                    blocks.pop(i)
                    i -= 1
                else:
                    blocks[i].id = None
                if i < len(blocks) - 1 and blocks[i + 1].id is None:
                    blocks[i].size += blocks[i + 1].size
                    blocks.pop(i + 1)
                break
    return blocks


p1 = checksum(frag(deepcopy(fs)))
p2 = checksum(better_frag(deepcopy(fs)))
print(p1, p2, sep="\n")
