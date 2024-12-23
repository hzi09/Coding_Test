def solution(score):
    avg_score = [sum(i)/2 for i in score]
    score_sort = sorted(avg_score, reverse=True)
    return [score_sort.index(i)+1 for i in avg_score]
