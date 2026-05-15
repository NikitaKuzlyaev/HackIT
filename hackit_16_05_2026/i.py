import sys


def solve():
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))

    k = int(sys.stdin.readline())
    d = list(map(int, sys.stdin.readline().split()))

    res = sum(p)
    used = set()

    for i in d:
        if i in used:
            continue

        used.add(i)
        res -= p[i - 1]

    print(res)


if __name__ == "__main__":
    solve()
