from collections import Counter

def solution(strArr):
    str_len = [len(i) for i in strArr]
    return max(Counter(str_len).values())