def solution(num_list):
    cnt = 0
    for i in num_list :
        while i > 1 :
            cnt += 1
            if i % 2 == 0 :
                i //= 2
            else :
                i = (i-1) // 2
    return cnt