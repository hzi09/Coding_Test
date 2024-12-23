def solution(score):
    avg_score = []
    for i in score :
        avg_score.append(sum(i)/2)
        
    score_sort = sorted(avg_score, reverse=True)
    
    answer = [score_sort.index(i)+1 for i in avg_score]

    return answer
