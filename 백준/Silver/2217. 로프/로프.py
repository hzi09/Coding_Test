n = int(input())
w = [int(input()) for _ in range(n)]

w.sort()
max_w = 0

for i in range(n):
    max_w = max(max_w, w[i] * (n - i))

print(max_w)
