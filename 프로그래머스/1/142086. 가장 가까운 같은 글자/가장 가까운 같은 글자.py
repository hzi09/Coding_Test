def solution(s):
    answer = []
    for idx, v in enumerate(s) :
        if idx == 0 :
            answer.append(-1)
        elif s[:idx].rfind(v) == -1:
            answer.append(-1)
        else :
            answer.append(idx - s[:idx].rfind(v))
    return answer