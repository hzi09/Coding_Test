def solution(lottos, win_nums):
    score = len(list(set(lottos) & set(win_nums)))
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    zero_cnt = lottos.count(0)
    max_rank = 0
    if zero_cnt + score > 6 :
        max_rank = 1
    else :
        max_rank = rank[zero_cnt+score]
    min_rank = rank[score]
    return [max_rank, min_rank]