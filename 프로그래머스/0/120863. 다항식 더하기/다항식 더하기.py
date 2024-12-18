def solution(polynomial):
    x = 0 # x앞의 상수
    a = 0 # 그냥 상수
    for i in polynomial.split(' + ') :
        if i.isdigit() :
            a += int(i)
        else :
            if i == "x" :
                x += 1
            else :
                x += int(i[:-1])
    if x == 0 :
        return str(a)
    elif x == 1 :
        return f'x + {str(a)}' if a !=0 else 'x'
    else :
        return f'{x}x + {a}' if a != 0 else f'{x}x'