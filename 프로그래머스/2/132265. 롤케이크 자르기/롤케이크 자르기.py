def solution(topping):
    older = set()
    younger = set()
    
    older_cnt = []
    younger_cnt = []
    
    for t in topping :
        older.add(t)
        older_cnt.append(len(older))
        
    for t in reversed(topping) :
        younger.add(t)
        younger_cnt.append(len(younger))
    
    younger_cnt.reverse()
    
    cnt = 0
    
    for n in range(len(topping)-1) :
        if older_cnt[n] == younger_cnt[n+1] :
            cnt += 1
        
    return cnt