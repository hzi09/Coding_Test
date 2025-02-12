def solution(participant, completion):
    dic = {}
    
    for p in participant :
        if p not in dic :
            dic[p] = 1
        else : 
            dic[p] += 1
            
    for c in completion :
        dic[c] -= 1
    
    return ''.join([k for k, v in dic.items() if v >= 1])