n,m = map(int, input().split())
s = [input() for _ in range(n)]
check = [input() for _ in range(m)]

s = set(s)

count = 0

for i in check:
    if i in s:
        count += 1

print(count)
