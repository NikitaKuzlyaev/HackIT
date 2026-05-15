n, m = map(int, input().split())
a, b = map(int, input().split())

res = (n + a - 1) // a + (m + b - 1) // b

print(res)
