n = int(input())

name = set()

for i in range(n):
    a, b = input().split()
    if b == "enter":
        name.add(a)
    else:
        name.remove(a)


for i in sorted(name, reverse=True):
    print(i)
