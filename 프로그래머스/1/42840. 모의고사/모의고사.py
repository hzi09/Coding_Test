def solution(answers):
    st_1 = [1, 2, 3, 4, 5]
    st_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    st_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0, 0, 0]
    
    for i in range(len(answers)) :
        if answers[i] == st_1[i%len(st_1)] :
            score[0] += 1
        if answers[i] == st_2[i%len(st_2)] :
            score[1] += 1
        if answers[i] == st_3[i%len(st_3)] :
            score[2] += 1
    
    answer = []
    for n in range(3):
        if score[n] == max(score):
            answer.append(n + 1)
    return answer