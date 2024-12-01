t = int(input())

for i in range(t) :
    p, r = input().split()
    for i in range(len(r)) :
        print(int(p) * r[i], end = '')
    print('')