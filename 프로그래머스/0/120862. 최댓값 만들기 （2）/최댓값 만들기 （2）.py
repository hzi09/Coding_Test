from itertools import combinations

def solution(numbers):
    mix = list(combinations(numbers, 2))
    sum_list = []
    for i in mix :
        multiply = i[0] * i[1]
        sum_list.append(multiply)
    return max(sum_list)