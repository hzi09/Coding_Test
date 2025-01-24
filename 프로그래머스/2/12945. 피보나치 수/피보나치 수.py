def solution(n):
    f_x = [0, 1]
    for i in range(n-2) :
        f_x.append(sum(f_x))
        del f_x[0]
    return sum(f_x) % 1234567