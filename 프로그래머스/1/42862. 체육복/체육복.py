def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    answer = n - len(lost_set)
    
    for student in sorted(lost_set) :
        if student - 1 in reserve_set :
            reserve_set.remove(student - 1)
            answer += 1
        elif student + 1 in reserve_set :
            reserve_set.remove(student + 1)
            answer += 1
    return answer