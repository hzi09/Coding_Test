import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)

def bfs(graph, start, distance):
    queue = deque([start])
    distance[start] = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if distance[i] == -1:
                distance[i] = distance[v] + 1
                queue.append(i)

bfs(graph, x, distance)

found = False

for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        found = True

if not found:
    print(-1)
