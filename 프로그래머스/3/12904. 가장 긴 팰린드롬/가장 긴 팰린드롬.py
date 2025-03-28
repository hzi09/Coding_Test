def solution(s):
    max_length = 0
    
    for i in range(len(s)) :
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right] :
            max_length = max(max_length, right - left +1)
            left -= 1
            right += 1
            
            
        left, right = i, i+1
        while left >= 0 and right < len(s) and s[left] == s[right] :
            max_length = max(max_length, right - left + 1)
            left -= 1
            right += 1

    return max_length