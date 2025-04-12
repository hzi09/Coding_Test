n, m = map(int, input().split())
r, c, d = map(int, input().split())

robot = [list(map(int, input().split())) for _ in range(n)]

robot_x = [-1, 0, 1, 0]
robot_y = [0, 1, 0, -1]

cnt = 0
x, y = r, c

while True:
    if robot[x][y] == 0:
        robot[x][y] = 2
        cnt += 1

    clean = True
    for i in range(4):
        nx = x + robot_x[i]
        ny = y + robot_y[i]
        if 0 <= nx < n and 0 <= ny < m and robot[nx][ny] == 0:
            clean = False
            break

    if clean:
        back = (d + 2) % 4
        nx = x + robot_x[back]
        ny = y + robot_y[back]
        if 0 <= nx < n and 0 <= ny < m and robot[nx][ny] != 1:
            x, y = nx, ny
        else:
            break
    
    else:
        d = (d + 3) % 4
        nx = x + robot_x[d]
        ny = y + robot_y[d]

        if 0 <= nx < n and 0 <= ny < m and robot[nx][ny] == 0:
            x, y = nx, ny

print(cnt)