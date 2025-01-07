n = int(input())
users = []


for i in range(n) :
    age, name = input().split()
    users.append([int(age), name])


for i in sorted(users, key=lambda x: x[0]) :
    print(*i)