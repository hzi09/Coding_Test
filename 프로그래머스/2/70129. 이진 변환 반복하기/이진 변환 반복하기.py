def solution(s):
    cnt_bin = 0
    cnt_zero = 0
    
    while True :
        if s == '1' :
            break
        cnt_zero += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        
        cnt_bin += 1
    return [cnt_bin, cnt_zero]