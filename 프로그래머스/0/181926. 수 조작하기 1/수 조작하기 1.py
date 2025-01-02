def solution(n, control):
    answer = n
    answer += control.count('w')
    answer -= control.count('a') * 10
    answer -= control.count('s')
    answer += control.count('d') * 10
    return answer