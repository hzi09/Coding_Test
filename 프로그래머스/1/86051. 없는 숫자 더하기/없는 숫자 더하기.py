def solution(numbers):
    n_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return sum([i for i in n_list if i not in numbers])