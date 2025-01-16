def solution(arr):
    cnt = 1
    while cnt < len(arr) :
        cnt *= 2    
    return arr + [0]  * (cnt - len(arr))