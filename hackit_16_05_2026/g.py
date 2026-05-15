s = str(input())

res = 0

for i in s:
    if i.isdigit():
        res += int(i)

print(res)
