def solution(clothes):
    dic = {}
    for name, kind in clothes :
        if kind in dic.keys():
            dic[kind] += 1
        else :
            dic[kind] = 1
    
    answer = 1
    for i, v in dic.items() :
        answer *= v + 1

    return answer - 1