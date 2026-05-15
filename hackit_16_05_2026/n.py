p, i, s, k, a = map(int, input().split())  # мышка делает "пи пи пи"

need = a * (p + i)

rest_time = max(0, need - s) / k
answer = 2 * a + rest_time

print(f"{answer:.10f}")
