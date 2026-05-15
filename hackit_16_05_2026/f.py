import sys


def solve():
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    d = list(map(int, input().split()))
    f = int(input())

    pref_p = [0] * n
    for i in range(n - 1):
        pref_p[i + 1] = pref_p[i] + p[i]

    pref_a = [0] * (n + 1)
    for i in range(n):
        pref_a[i + 1] = pref_a[i] + a[i]

    best = -1
    idx = -1

    dragon_time = f
    q = []
    q_it = 0
    archer_time = 0
    archers_right = 0

    for i in range(n - 1, -1, -1):

        l, r = 0, i
        while l <= r:
            m = (l + r) // 2
            dist = pref_p[i] - pref_p[m]
            if dist > dragon_time:
                l = m + 1
            else:
                r = m - 1

        archers = pref_a[i + 1] - pref_a[l]

        while q_it < len(q):
            ix, at = q[q_it]
            if dragon_time < archer_time - at:
                archers_right -= a[ix]
                q_it += 1
            else:
                break

        archers += archers_right

        if archers > best:
            best, idx = archers, i + 1

        q.append((i, archer_time))
        archer_time += p[i - 1]  # когда i = 0, то i - 1 = -1, но это still safe
        dragon_time += d[i - 1]
        archers_right += a[i]

    print(best, idx)


solve()
