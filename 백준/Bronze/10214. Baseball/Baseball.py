t = int(input())
y_score = 0
k_score = 0

for i in range(t) :
    for _ in range(9) :
        y, k = map(int, input().split())
        y_score += y
        k_score += k

    if y_score > k_score :
        print('Yonsei')
    elif y_score < k_score :
        print('Korea')
    elif y_score == k_score :
        print('Draw')