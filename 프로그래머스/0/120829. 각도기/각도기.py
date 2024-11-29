def solution(angle):
    answer = 0
    if angle == 180 :
        answer = 4
    elif angle in range(91, 180):
        answer = 3
    elif angle == 90 :
        answer = 2
    elif angle in range(1, 90) :
        answer = 1
    return answer