n, k = map(int, input().split())

money = sorted([int(input()) for i in range(n)], reverse=True)

cnt = 0

for i in money :
    if i > k :
        continue
    else :
        cnt += k // i
        k = k % i
        
print(cnt)
