def solution(s):
    cnt = 0
    i = 0
    
    while i < len(s):
        x = s[i]
        cnt_x = 0
        cnt_o = 0
        
        for j in range(i, len(s)) :
            if s[j] == x :
                cnt_x += 1
            else :
                cnt_o += 1
            
            if cnt_x == cnt_o :
                cnt += 1
                i = j + 1
                break
        else :
            cnt += 1
            break
    
    return cnt