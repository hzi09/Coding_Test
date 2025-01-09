def solution(arr, intervals):
    answer = [arr[i[0]:i[1]+1] for i in intervals]
    return answer[0] + answer[1]