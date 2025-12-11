m = int(input())
n = int(input())

num_list = []

for i in range(m, n + 1):
    temp = i ** 0.5
    if temp == int(temp):
        num_list.append(i)

if len(num_list) == 0:
    print(-1)
else:
    print(sum(num_list))
    print(min(num_list))