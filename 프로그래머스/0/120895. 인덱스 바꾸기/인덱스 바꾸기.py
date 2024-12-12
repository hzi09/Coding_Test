def solution(my_string, num1, num2):
    str_l = list(my_string)
    str_l[num1], str_l[num2] = str_l[num2], str_l[num1]
    return ''.join(str_l)