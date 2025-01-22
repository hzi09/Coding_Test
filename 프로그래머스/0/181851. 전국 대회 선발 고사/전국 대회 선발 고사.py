def solution(rank, attendance):
    new_rank = []
    for i,j in zip(rank, attendance) :
        if j == True :
            new_rank.append(i)
    new_rank.sort()
    student_idx = [rank.index(new_rank[i]) for i in range(3)]
    return 10000 * student_idx[0] + 100 * student_idx[1] + student_idx[2]