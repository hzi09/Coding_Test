n, l = map(int, input().split())
x = sorted(list(map(int, input().split())))

tape = l
cnt = 1
prev = x[0]

for i in range(1, n):
    dist = x[i] - prev
    if dist < tape:
        tape -= dist
        prev = x[i]
    else:
        cnt += 1
        tape = l
        prev = x[i]

print(cnt)
