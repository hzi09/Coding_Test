def solution(numbers, k):
    answer = 1
    for i in range(k-1) :
        answer += 2
        if answer > numbers[-1] :
            answer -= numbers[-1]
    return answer