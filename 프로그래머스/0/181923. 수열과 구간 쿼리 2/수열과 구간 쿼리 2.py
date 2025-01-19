def solution(arr, queries):
    answer = []
    for s, e, k in queries :
        li = [i for i in arr[s:e+1] if i > k]
        if li :
            answer.append(min(li))
        else :
            answer.append(-1)
    return answer