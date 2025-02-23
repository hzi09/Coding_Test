from collections import Counter

def solution(X, Y):
    cnt_x = Counter(X)
    cnt_y = Counter(Y)
    
    answer = []
    for digit in range(9, -1, -1) :
        min_cnt = min(cnt_x[str(digit)], cnt_y[str(digit)])
        answer.extend([str(digit)] * min_cnt)
    
    if not answer:
        return "-1"
    if answer[0] == "0":
        return "0"
    return ''.join(answer)