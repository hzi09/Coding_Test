while True:
    n1 = input()
    n2 = n1[::-1]

    if int(n1) == 0:
        break
    else :
        if n1 != n2:
            print("no")
        else:
            print("yes")
