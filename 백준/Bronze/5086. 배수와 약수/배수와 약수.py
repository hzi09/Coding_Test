while True :
    n1, n2 = map(int, input().split())
    if n1 == 0 and n2 == 0 :
        break
    elif n1 < n2 :
        if n2 % n1 == 0 :
            print('factor')
    elif n1 >= n2 :
        if n1 % n2 == 0:
            print('multiple')
        elif n1 % n2 != 0 :
            print('neither')