def solution(my_string):
    numbers = 0
    for i in my_string :
        if i.isdigit() :
            numbers += int(i)
    return numbers
