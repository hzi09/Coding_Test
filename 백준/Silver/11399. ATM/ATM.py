n = int(input())
p = list(map(int, input().split()))

p.sort(reverse=True)

for i in range(n) :
    p[i] = p[i] * (i+1)

print(sum(p))
