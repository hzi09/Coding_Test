def solution(my_string, m, c):
    answer = [my_string[i: m+i] for i in range(0, len(my_string), m)]
    return ''.join([answer[j][c-1] for j in range(len(answer))])