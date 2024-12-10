def solution(my_string):
    str_list = list(my_string)
    answer = []
    for i in str_list :
        if i in answer :
            pass
        else :
            answer.append(i)
    return ''.join(answer)
