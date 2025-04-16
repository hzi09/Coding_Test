n = int(input())
graph = [list(map(str, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check():
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'T':
                for k in range(4):
                    nx, ny = i, j
                    while True:
                        nx += dx[k]
                        ny += dy[k]
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            break
                        if graph[nx][ny] == 'O':
                            break
                        if graph[nx][ny] == 'S':
                            return False
    return True

def dfs(count):
    if count == 3:
        if check():
            print("YES")
            exit()
        return
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                dfs(count + 1)
                graph[i][j] = 'X'

dfs(0)
print("NO")
