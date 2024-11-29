n = int(input())
s = list(map(int, input().split()))
v = int(input())
num = 0

for i in s :
    if i == v :
        num += 1
print(num)
