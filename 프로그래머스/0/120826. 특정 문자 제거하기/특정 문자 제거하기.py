def solution(my_string, letter):
    str_l = list(my_string)
    while letter in str_l :
        str_l.remove(letter)
    answer = ''.join(str_l)
    return answer
