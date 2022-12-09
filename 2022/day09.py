import sys


def adjacent_8(x, y):
    for y_d in (-1, 0, 1):
        for x_d in (-1, 0, 1):
            if y_d == x_d == 0:
                continue
            yield x + x_d, y + y_d


s = [(l.split()[0], int(l.split()[1])) for l in sys.stdin.read().splitlines()]
H_pos = (0, 0)
T_pos = (0, 0)
H_been = [H_pos]
T_been = [T_pos]
dirs = {"R": (1, 0), "U": (0, 1), "D": (0, -1), "L": (-1, 0)}

rope = [(0, 0) for _ in range(10)]
T2_been = [rope[-1]]

for d, v in s:
    # print(f" >> {d} {v}")
    dx, dy = dirs.get(d)
    for _ in range(v):
        # print(f"   >H {H_pos} => ", end="")
        H_pos = (H_pos[0] + dx, H_pos[1] + dy)
        rope[0] = (rope[0][0] + dx, rope[0][1] + dy)
        # print(f"{H_pos}")
        # print(f"   >T {T_pos} => ", end="")
        H_been.append(H_pos)
        if T_pos != H_pos and T_pos not in set((c for c in adjacent_8(*H_pos))):
            # print("=> ", end="")
            if T_pos[0] == H_pos[0]:
                # Same row
                if H_pos[1] > T_pos[1]:
                    T_pos = (T_pos[0], T_pos[1] + 1)
                else:
                    T_pos = (T_pos[0], T_pos[1] - 1)
            elif T_pos[1] == H_pos[1]:
                # Same col
                if H_pos[0] > T_pos[0]:
                    T_pos = (T_pos[0] + 1, T_pos[1])
                else:
                    T_pos = (T_pos[0] - 1, T_pos[1])
                pass
            else:
                # Going diagonally
                if H_pos[0] > T_pos[0] and H_pos[1] > T_pos[1]:
                    # Going right + up
                    T_pos = (T_pos[0] + 1, T_pos[1] + 1)
                elif H_pos[0] < T_pos[0] and H_pos[1] > T_pos[1]:
                    # Going left + up
                    T_pos = (T_pos[0] - 1, T_pos[1] + 1)
                elif H_pos[0] < T_pos[0] and H_pos[1] < T_pos[1]:
                    # Going left + down
                    T_pos = (T_pos[0] - 1, T_pos[1] - 1)
                elif H_pos[0] > T_pos[0] and H_pos[1] < T_pos[1]:
                    # Going right + down
                    T_pos = (T_pos[0] + 1, T_pos[1] - 1)

        for i in range(1, 10):
            head = rope[i - 1]
            tail = rope[i]
            # head = (head[0] + dx, head[1] + dy)
            if tail != head and tail not in set((c for c in adjacent_8(*head))):
                if tail[0] == head[0]:
                    # Same row
                    if head[1] > tail[1]:
                        tail = (tail[0], tail[1] + 1)
                    else:
                        tail = (tail[0], tail[1] - 1)
                elif tail[1] == head[1]:
                    # Same col
                    if head[0] > tail[0]:
                        tail = (tail[0] + 1, tail[1])
                    else:
                        tail = (tail[0] - 1, tail[1])
                    pass
                else:
                    # Going diagonally
                    if head[0] > tail[0] and head[1] > tail[1]:
                        # Going right + up
                        tail = (tail[0] + 1, tail[1] + 1)
                    elif head[0] < tail[0] and head[1] > tail[1]:
                        # Going left + up
                        tail = (tail[0] - 1, tail[1] + 1)
                    elif head[0] < tail[0] and head[1] < tail[1]:
                        # Going left + down
                        tail = (tail[0] - 1, tail[1] - 1)
                    elif head[0] > tail[0] and head[1] < tail[1]:
                        # Going right + down
                        tail = (tail[0] + 1, tail[1] - 1)
            rope[i - 1] = head
            rope[i] = tail
        # print(f"{T_pos}")
        T_been.append(T_pos)
        # print(rope)
        T2_been.append(rope[-1])

print("Part 1:", len(set(T_been)))
print("Part 2:", len(set(T2_been)))
