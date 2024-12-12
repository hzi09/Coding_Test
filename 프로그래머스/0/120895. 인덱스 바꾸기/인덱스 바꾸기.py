def solution(my_string, num1, num2):
    my_string = list(my_string)
    change_str = [my_string[num1], my_string[num2]]
    my_string[num1] = change_str[1]
    my_string[num2] = change_str[0]
    return ''.join(my_string)