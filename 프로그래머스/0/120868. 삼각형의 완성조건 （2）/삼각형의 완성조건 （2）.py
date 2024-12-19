def solution(sides):
    answer = 0

    # 가장 긴 변이 sides의 max 값일 경우
    for i in range(1, max(sides)):
        if i + min(sides) > max(sides) :
            answer += 1
    # 나머지 한 변이 가장 긴 변인 경우
    for i in range(max(sides), sum(sides)) :
        answer += 1

    return answer