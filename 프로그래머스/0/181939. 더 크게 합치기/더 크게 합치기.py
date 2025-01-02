def solution(a, b):
    plus_a = str(a) + str(b)
    plus_b = str(b) + str(a)
    return int(plus_a) if plus_a > plus_b else int(plus_b)
