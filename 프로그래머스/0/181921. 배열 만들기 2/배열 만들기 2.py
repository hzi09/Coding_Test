def solution(l, r):
    answer = []
    for i in range(l, r+1) :
        arr = True
        for j in str(i) :
            if j not in ['0', '5'] :
                arr = False
                break
        if arr == True :
            answer.append(i)
    if len(answer) == 0 :
        return [-1]
    return answer