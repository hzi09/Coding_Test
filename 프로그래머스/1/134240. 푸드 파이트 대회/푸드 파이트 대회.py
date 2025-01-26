def solution(food):
    answer = ''
    for idx, f in enumerate(food) :
        if idx != 0 :
            if f % 2 == 1 :
                answer += str(idx)*((f-1)//2)
            else :
                answer += str(idx)*(f//2)         
    return answer + '0' + answer[::-1]
