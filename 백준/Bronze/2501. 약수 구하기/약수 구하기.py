n, k = map(int, input().split())

div = []

for i in range(1, int(n**0.5) + 1) :
    if (n % i ==0 ) :
        div.append(i)
        if i ** 2 != n :
            div.append(n // i)

if k <= len(div) :
    print(sorted(div)[k-1])
else :
    print(0)