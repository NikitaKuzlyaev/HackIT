import sys


def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    a.sort()

    last = [a[0]]
    size = [1]
    start_idx = 0
    res = 0

    for i in range(1, n):
        if a[i] != a[i - 1]:
            start_idx = 0
        else:
            start_idx += 1

        if len(last) == start_idx:
            last.append(a[i])
            size.append(1)
        else:
            last[start_idx] = a[i]
            res += size[start_idx]
            size[start_idx] += 1

    print(res)


if __name__ == "__main__":
    solve()
