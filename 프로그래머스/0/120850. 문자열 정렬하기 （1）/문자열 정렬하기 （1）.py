def solution(my_string):
    numbers = []
    for i in my_string :
        if i.isdigit() :
            numbers.append(int(i))
    return sorted(numbers)