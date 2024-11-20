a = list(map(int,input().split()))
b = []

for i in a :
    n = i ** 2
    b.append(n)
print(sum(b) % 10)