def solve():
    n, m, k = map(int, input().split())
    s = str(input())

    dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n + m + 1)]
    res = 0

    for K in range(1, k + 1):

        for i in range(n + m):
            idx = 0 if s[i] == 'a' else 1

            dp[i + 1][K][idx] = max(
                dp[i + 1][K][idx],
                1 + max(
                    dp[i][K][idx],
                    dp[i][K - 1][1 - idx]
                )
            )

            dp[i + 1][K][1 - idx] = max(
                dp[i + 1][K][1 - idx],
                dp[i][K][1 - idx]
            )

            res = max(
                res,
                dp[i + 1][K][idx],
                dp[i + 1][K][1 - idx]
            )

    print(res)


if __name__ == "__main__":
    solve()
