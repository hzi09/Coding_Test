words = ['{0:*<15}'.format(input()) for i in range(5)]

for i in range(15) :
    for w in words :
        if w[i] != '*' :
            print(w[i], end='')
        else :
            pass
