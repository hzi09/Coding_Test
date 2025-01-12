def solution(x):
    sum_x = sum([int(i) for i in str(x)])
    if x % sum_x == 0:
        return True
    return False