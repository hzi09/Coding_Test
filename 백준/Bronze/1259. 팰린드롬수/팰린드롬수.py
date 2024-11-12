while True:
    n1 = input()
    n_list = list(reversed(n1))
    n2 = int(''.join(n_list))
    
    if int(n1) != n2 :
        print("no")
    elif int(n1) == 0:
        break
    else :
        print("yes")