def solution(keymap, targets):
    key_n = {}
    
    for i, keys in enumerate(keymap) :
        for j, char in enumerate(keys) :
            if char in key_n :
                key_n[char] = min(key_n[char], j+1)
            else :
                key_n[char] = j+1
    answer = []
    
    for target in targets:
        total_presses = 0
        for char in target:
            if char not in key_n:
                total_presses = -1
                break 
            total_presses += key_n[char]
        
        answer.append(total_presses)
    return answer