n, m = map(int, input().split())

poketmon = [input() for _ in range(n)]
poketmon_dict = {name: i+1 for i, name in enumerate(poketmon)}
solved = [input() for _ in range(m)]

for i in solved:
    if i.isdigit():
        print(poketmon[int(i)-1])
    else:
        print(poketmon_dict[i])