def solution(name, yearning, photo):
    missing_score = dict(zip(name, yearning))
    answer = []
    for p in photo :
        score = 0
        for i in p :
            if i not in name :
                pass
            else :
                score += missing_score[i]
        answer.append(score)
    return answer