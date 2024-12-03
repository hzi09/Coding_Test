t = int(input())
score_list = []

for _ in range(t) :
    score_list.clear()
    ox = list(input())
    score = 0
    for i in ox :
        if i == 'O' :
            score += 1
            score_list.append(score)
        else :
            score = 0
    print(sum(score_list))
