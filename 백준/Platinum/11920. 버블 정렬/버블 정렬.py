import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

pq = arr[:k]
heapq.heapify(pq)

for i in range(n - k):
    heapq.heappush(pq, arr[i + k])
    arr[i] = heapq.heappop(pq)

for i in range(n - k, n):
    arr[i] = heapq.heappop(pq)

print(*arr)