a = int(input())
b = int(input())

c1 = a*(b % 10)
c10 = a*(b % 100 // 10)
c100 = a*(b // 100)

print(c1)
print(c10)
print(c100)
print(c1+c10*10+c100*100)