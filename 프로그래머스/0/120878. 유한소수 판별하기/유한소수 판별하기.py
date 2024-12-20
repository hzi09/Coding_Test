import math as m

def solution(a, b):
    gcd = m.gcd(a, b)
    b //= gcd

    num = []
    i = 2
    while i <= b: 
        if b % i == 0:
            b //= i
            num.append(i)
        else:
            i += 1
    if all(x in (2, 5) for x in num) :
        return 1
    else:
        return 2