from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    union = [(x, y)]
    total = graph[x][y]
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    total += graph[nx][ny]
                    count += 1

    for i, j in union:
        graph[i][j] = total // count

    return count > 1

def solve():
    result = 0
    while True:
        visited = [[False] * n for _ in range(n)]
        moved = False
        
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    if bfs(i, j, visited):
                        moved = True
        
        if not moved:
            break
        
        result += 1
    
    return result

print(solve())
