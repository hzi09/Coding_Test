while True :
    n = int(input())

    if n == -1 :
        break

    answer = []
    for i in range(1, n) :
        if n % i == 0 :
            answer.append(i)
    if sum(answer) == n :
        print(n, ' = ', ' + '.join(str(i) for i in answer), sep='')
    else :
        print(n, 'is NOT perfect.')