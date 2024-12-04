n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
t_n = 0

for i in range(6) :
    if size[i] % t == 0:
        t_n += int(size[i]/t)
    else :
        t_n += (int(size[i]/t)+1)

print(t_n)

p_n = [int(n/p), n%p]
print(*p_n)