def solution(s):
    s_list = ''.join(list(s)).split()
    num_list = []
    for i in s_list :
        if i == 'Z' :
            del num_list[-1]
        else :
            num_list.append(int(i))
    return sum(num_list)
