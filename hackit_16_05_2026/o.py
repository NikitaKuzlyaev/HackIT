F = {}
MOD = 10 ** 9 + 1000 - 7


def f(rem_n, rem_m):
    if (rem_n, rem_m) in F:
        return F[(rem_n, rem_m)]

    if rem_n == 1:
        return int(rem_m > 0 and rem_m != 4)

    res = 0
    for i in range(1, rem_m - (rem_n - 1) + 1):
        if i == 4:
            continue
        res += f(rem_n - 1, rem_m - i)

    res = res % MOD
    F[(rem_n, rem_m)] = res
    return res


def solve():
    n, m = map(int, input().split())
    print(f(n, m))


if __name__ == '__main__':
    solve()
