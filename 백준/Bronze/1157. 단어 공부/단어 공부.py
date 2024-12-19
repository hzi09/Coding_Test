string = input().upper()
str_one = list(set(string))
n_list = []

for i in str_one:
    n = string.count(i)
    n_list.append(n)

dict_str = {strs : ints for strs, ints in zip(str_one, n_list)} 

if n_list.count(max(n_list)) != 1 :
    print("?")
else :
    max_key = max(dict_str, key=dict_str.get)
    print(max_key)