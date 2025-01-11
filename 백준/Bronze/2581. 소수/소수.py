m = int(input())
n = int(input())
n_list = []

for i in range(m, n+1):
    e = 0
    if i > 1:
        for j in range(2,i):
            if i%j==0:
                e+=1
                break
        if e == 0 :
            n_list.append(i)

if len(n_list) < 1:
    print(-1)
else:
    print(sum(n_list))
    print(min(n_list))