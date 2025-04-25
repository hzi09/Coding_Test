dot = [list(map(int, input().split())) for _ in range(3)]

x = []
y = []

for i in range(3):
    x.append(dot[i][0])
    y.append(dot[i][1])

for i in range(3):
    if x.count(x[i]) == 1:
        a = x[i]
    if y.count(y[i]) == 1:
        b = y[i]

print(a, b)