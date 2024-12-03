import math as mt

def solution(balls, share):
    n = mt.factorial(balls)
    m = mt.factorial(share)
    n_m = mt.factorial(balls-share)
    return int(n / (n_m * m))