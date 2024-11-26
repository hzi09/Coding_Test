def solution(n) :
    p = 7
    if n / p <= 1:
        answer = 1
    elif n%p == 0 :
        answer = n//p
    else:
        answer = (n // p) + 1
    return answer