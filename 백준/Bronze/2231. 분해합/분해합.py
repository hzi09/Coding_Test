n = int(input())

for i in range(n//2, n+1) :
    num = [int(i) for i in str(i)]

    if i + sum(num) == n :
        print(i)
        break
    elif i == n :
        print(0)