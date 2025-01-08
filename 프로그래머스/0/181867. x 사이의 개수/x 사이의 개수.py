def solution(myString):
    str_list = myString.split('x')
    return [len(i) for i in str_list]