num_set = [i for i in range(10)]
n = list(map(int, input().strip()))

cnt = 1

for i in n :
    if i in num_set :
        num_set.remove(i)
    else :
        if i == 6 and 9 in num_set:
            num_set.remove(9)
        elif i == 9 and 6 in num_set:
            num_set.remove(6)
        else :
            cnt += 1
            num_set += [j for j in range(10)]
            num_set.remove(i)

print(cnt)