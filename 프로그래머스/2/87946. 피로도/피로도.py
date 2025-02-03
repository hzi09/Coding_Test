from itertools import permutations

def solution(k, dungeons):
    max_cnt = 0
    for dungeon in list(permutations(dungeons, len(dungeons))) :
        fatigue = k
        cnt = 0
        for f_min, f_cost in dungeon :
            if f_min <= fatigue :
                fatigue -= f_cost
                cnt += 1
            else :
                break
        
        max_cnt = max(max_cnt, cnt)
    return max_cnt