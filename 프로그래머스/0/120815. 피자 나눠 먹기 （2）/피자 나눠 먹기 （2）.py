def solution(n) :
    answer = 0
    while True:
        answer += 1
        if (6 * answer) % n == 0:
            break
    return answer
