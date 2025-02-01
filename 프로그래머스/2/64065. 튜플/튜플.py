def solution(s):
    s = s[2:-2].split('},{')
    
    num_cnt = dict()
    
    for i in s :
        numbers = map(int, i.split(','))
        
        for n in numbers :
            if n in num_cnt :
                num_cnt[n] += 1
            else :
                num_cnt[n] = 1
    
    answer = sorted(num_cnt, key=lambda x: num_cnt[x], reverse=True)
    
    return answer