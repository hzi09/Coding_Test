n = int(input())
k = int(input())
x = sorted(list(map(int, input().split())))

cnt = 1
dist = []

for i in range(1, n) :
    dist.append(x[i] - x[i-1])

dist.sort()

print(sum(dist[:n-k]))