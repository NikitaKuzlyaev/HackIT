import sys


def solve():
    s = sys.stdin.readline().strip()

    words = []

    cur_first = s[0].lower()
    cur_last = s[0].lower()
    cur_len = 1

    for i in range(1, len(s)):
        if s[i].isupper():
            words.append((cur_first, cur_last, cur_len))
            cur_first = s[i].lower()
            cur_last = s[i].lower()
            cur_len = 1
        else:
            cur_last = s[i]
            cur_len += 1

    words.append((cur_first, cur_last, cur_len))

    dp = [0] * 26
    dp[ord(words[0][1]) - 97] = words[0][2]

    for wn in range(1, len(words)):

        first, last, length = words[wn]

        mx = dp[ord(last) - 97]
        for i in range(26):
            if i == ord(first) - 97:
                continue
            mx = max(mx, dp[i] + length)

        dp[ord(last) - 97] = mx

    print(max(dp))


if __name__ == "__main__":
    solve()
