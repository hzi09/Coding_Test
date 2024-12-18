def solution(polynomial):
    a = 0 # x앞의 상수
    b = 0 # 그냥 상수
    for i in polynomial.split(' + ') :
        if i.isdigit() :
            b += int(i)
        else :
            if i == "x" :
                a += 1
            else :
                a += int(i[:-1])
    if a == 0 :
        return str(b)
    elif a == 1 :
        return f'x + {str(b)}' if b !=0 else 'x'
    else :
        return f'{a}x + {b}' if b != 0 else f'{a}x'
