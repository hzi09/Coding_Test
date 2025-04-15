from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], 0, i, j))

def bfs(graph, virus, s, x, y):
    n = len(graph)

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    virus.sort()
    queue = deque(virus)

    while queue:
        virus_id, time, vx, vy = queue.popleft()
        if time == s:
            break
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = virus_id
                queue.append((virus_id, time + 1, nx, ny))

    return graph[x - 1][y - 1]

print(bfs(graph, virus, s, x, y))
