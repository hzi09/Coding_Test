table = [list(map(int, input().split())) for _ in range(9)]

max_num = 0

max_x, max_y = 0, 0
for x in range(9) :
    for y in range(9) :
        if max_num <= table[x][y] :
            max_x = x + 1
            max_y = y + 1
            max_num = table[x][y]

print(max_num)
print(max_x, max_y)