def solution(a, b, n):
    cola_cnt = 0
    
    while n >= a :
        bin_cnt = n % a
        n = (n // a) * b
        cola_cnt += n
        n += bin_cnt
    return cola_cnt