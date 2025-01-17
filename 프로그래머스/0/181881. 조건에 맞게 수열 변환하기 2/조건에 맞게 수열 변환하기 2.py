def solution(arr):
    cnt = 0
    
    while True : 
        change = []
        for i in arr :
            if i > 50 and i % 2 == 0 :
                change.append(i//2)
            elif i < 50 and i % 2 == 1 :
                change.append(i*2+1)
            else :
                change.append(i)
        if arr != change :
            cnt += 1
            arr = change
        else :
            return cnt