def solution(my_string):
    str_list = []
    for s in my_string:
        if s.isdigit() :
            str_list.append(s)
        else :
            str_list.append(' ')
            
    new_str = ''.join(str_list)
    
    return sum(int(i) for i in new_str.split())