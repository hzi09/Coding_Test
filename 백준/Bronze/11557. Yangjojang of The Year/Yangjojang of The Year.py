t = int(input())

for _ in range(t):
    n = int(input())
    
    data = {}
    for _ in range(n):
        name, alchol = input().split()
        data[name] = int(alchol)
    print(max(data, key=data.get))