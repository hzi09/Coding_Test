n, m = map(int, input().split())
listen = set([input() for _ in range(n)])
see = set([input() for _ in range(m)])

result = sorted(list(listen & see))

print(len(result))

for i in result:
    print(i)