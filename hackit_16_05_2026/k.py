import sys


def solve():
    n, m = map(int, sys.stdin.readline().split())
    k = int(sys.stdin.readline())

    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    a.sort(reverse=True)
    b.sort()

    res = 0
    j = 0

    for x in a:
        while j < m and x + b[j] <= k:
            j += 1

        res += m - j

    print(res)


if __name__ == "__main__":
    solve()
