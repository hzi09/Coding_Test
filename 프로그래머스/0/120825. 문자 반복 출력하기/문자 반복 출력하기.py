def solution(my_string, n):
    s_list = list(my_string)
    new_list = []
    for i in my_string :
        a = i * n
        new_list  += a
    return ''.join(new_list)