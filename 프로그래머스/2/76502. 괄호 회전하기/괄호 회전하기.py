def solution(s):
    cnt = 0
    n = len(s)
    
    for _ in range(n):
        ex_s = s
        while any(pair in ex_s for pair in ('()', '[]', '{}')):
            for pair in ('()', '[]', '{}'):
                ex_s = ex_s.replace(pair, '')

        if len(ex_s) == 0:
            cnt += 1

        s = s[1:] + s[0]
    
    return cnt