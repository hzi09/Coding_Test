def solution(N, stages):
    n_stage = {}
    
    users = len(stages)
    
    for i in range(1, N+1) :
        if users != 0 :
            n_stage[i] = stages.count(i)/users
            users -= stages.count(i)
        else :
            n_stage[i] = 0
        
    return sorted(n_stage, key=lambda x:n_stage[x], reverse=True)