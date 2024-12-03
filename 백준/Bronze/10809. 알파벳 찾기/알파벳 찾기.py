a_list = [-1] * 26
s = list(input())

for i in s :
    n = ord(i) - 97
    s_index = s.index(i)
    a_list[n] = s_index


print(' '.join(map(str, a_list)))