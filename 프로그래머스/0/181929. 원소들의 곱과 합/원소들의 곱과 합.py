from math import prod

def solution(num_list):
    return 1 if (sum(num_list)) ** 2 > prod(num_list) else 0