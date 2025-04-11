m, n = map(int, input().split())
table = [[0] * n for _ in range(m)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cnt = -1
x, y = 0, 0
direction = 0

for i in range(m*n):
    table[x][y] = i+1

    nx = x + dx[direction]
    ny = y + dy[direction]

    if (nx < 0 or nx >= m or ny < 0 or ny >= n or table[nx][ny] != 0):
        direction = (direction + 1) % 4
        cnt += 1
        nx = x + dx[direction]
        ny = y + dy[direction]

    x, y = nx, ny

            
print(cnt)