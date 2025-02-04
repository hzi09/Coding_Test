def solution(n, m, section):
    cnt = 1
    start_section = section[0]
    
    for i in section :
        if start_section + (m-1) < i :
            start_section = i
            cnt +=1
    return cnt