def solution(n):
    num = 1
    i = 1
    while num <= n  :
        i += 1
        num *= i
    return i-1