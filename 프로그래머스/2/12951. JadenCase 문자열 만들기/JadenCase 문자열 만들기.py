def solution(s):
    s_list = list(s.split(' '))
    answer = [i.capitalize() for i in s_list]
    return ' '.join(answer)