n, m = map(int, input().split())
basket_n = [0]*n

for _ in range(m) :
    i, j, k = map(int, input().split())
    for b in list(range(i, j+1)) :
        basket_n[b-1] = k
print(' '.join(map(str, basket_n)))