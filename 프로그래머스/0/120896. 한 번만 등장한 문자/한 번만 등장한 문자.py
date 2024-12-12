def solution(s):
    cnt_1 = []
    for i in s :
        if s.count(i) == 1 :
            cnt_1.append(i)
    return ''.join(sorted(cnt_1))