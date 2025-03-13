def solution(n, s):
    quo, rem = divmod(s, n)
    
    if quo == 0 :
        return [-1]
        
    answer = [quo] * n
    for i in range(rem) :
        answer[i] += 1
    return sorted(answer)