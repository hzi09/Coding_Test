import re

def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    cnt = 0
    
    for b in babbling :
        if re.search(r'(aya|ye|woo|ma)\1', b) :
            continue
        
        for word in words :
            b = b.replace(word, ' ')
            
        if b.strip() == '' :
            cnt += 1
    
    return cnt