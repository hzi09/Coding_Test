T = int(input())

for _ in range(T) :
    math = list(input().split())
    answer = 0
    for i in math :
        if math.index(i) == 0 :
            answer += float(i)
        elif i == '@' :
            answer *=3
        elif i == '%' :
            answer +=5
        elif i == '#' :
            answer -=7
    print(f"{answer:.2f}")