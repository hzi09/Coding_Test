def solution(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    n = (rev_base[::-1]).split('0')
    
    n = list(filter(None, n))
    
    cnt = 0
    
    for i in n :
        if int(i) < 2 :
            continue
        e = 0
        j = 2
        while j * j <= int(i):
            if int(i) % j == 0:
                e += 1
                break
            j += 1
        
        if e == 0:
            cnt += 1
    return cnt