from collections import Counter


def part_1(a, b):
    for i in range(a, b + 1):
        x = list(str(i))
        if x != sorted(x) or len(set(x)) == len(x):
            continue
        yield i


def part_2(passwords):
    return len([i for i in passwords if 2 in Counter(str(i)).values()])


def main():
    passwords = list(part_1(152085, 670283))
    print(len(passwords))
    print(part_2(passwords))


if __name__ == "__main__":
    main()