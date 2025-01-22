def solution(t, p):
    num_p = int(p)
    cnt = 0
    
    for i in range(len(t)-len(p)+1) :
        sub_str = t[i:i+len(p)]
        if int(sub_str) <= num_p :
            cnt += 1
    return cnt