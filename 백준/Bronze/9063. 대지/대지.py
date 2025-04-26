n = int(input())
dot = [list(map(int, input().split())) for _ in range(n)]

x_list = []
y_list = []

for i in range(n):
    x_list.append(dot[i][0])
    y_list.append(dot[i][1])

print((max(x_list) - min(x_list)) * (max(y_list) - min(y_list)))