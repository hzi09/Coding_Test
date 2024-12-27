def solution(my_string):
    numbers = [int(i) for i in my_string if i.isdigit()]
    return sum(numbers)
