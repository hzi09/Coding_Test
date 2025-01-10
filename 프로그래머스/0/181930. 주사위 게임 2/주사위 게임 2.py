def solution(a, b, c):
    answer = 0
    total_1 = a + b + c
    total_2 = a**2 + b**2 + c**2
    total_3 = a**3 + b**3 + c**3
    if a != b != c != a :
        answer = total_1
    elif a == b == c :
        answer = total_1 * total_2 * total_3
    else :
        answer = total_1 * total_2
    return answer