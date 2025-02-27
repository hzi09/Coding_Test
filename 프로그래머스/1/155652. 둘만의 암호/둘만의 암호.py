def solution(s, skip, index):
    alp = [chr(i) for i in range(97, 123)]
    for i in skip:
        alp.remove(i)
    
    answer = ''
    for char in s:
        idx = alp.index(char)
        new_idx = (idx + index) % len(alp)
        answer += alp[new_idx]
        
    return answer
