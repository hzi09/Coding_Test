import sys
import copy
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def virus(graph):
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    queue.append((nx, ny))


def get_score(graph):
    return sum(row.count(0) for row in graph)

def dfs(count, start):
    global result
    if count == 3:
        temp = copy.deepcopy(lab)
        virus(temp)
        result = max(result, get_score(temp))
        return
    
    for i in range(start, n * m):
        x = i // m
        y = i % m
        if lab[x][y] == 0:
            lab[x][y] = 1
            dfs(count + 1, i + 1)
            lab[x][y] = 0

dfs(0,0)
print(result)

