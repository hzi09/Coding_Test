from collections import Counter

def solution(want, number, discount):
    day = 0
    dic = {w:n for w,n in zip(want, number)}

    for i in range(len(discount)):
        if dic == Counter(discount[i:i+10]):
            day += 1
    return day