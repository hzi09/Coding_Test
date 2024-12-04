while True :
    s_list = list(map(int, input().split()))
    n_list = sorted(s_list)
    
    if n_list[0] == 0 and  n_list[1] == 0 and n_list[2] == 0:
        break
    elif (n_list[0] ** 2) + (n_list[1] ** 2) == (n_list[2] ** 2) :
        print('right')
    else :
        print('wrong')