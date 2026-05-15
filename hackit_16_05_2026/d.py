import sys
from heapq import heappop, heappush


def solve():
    n, k = map(int, sys.stdin.readline().split())

    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    q = []
    for i in range(n):
        heappush(q, (-a[i], b[i]))

    res = 0
    for i in range(k):
        a, b = heappop(q)
        a = -a

        res += a
        heappush(q, (-(a - b), b))

    print(res)


if __name__ == "__main__":
    solve()
