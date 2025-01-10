def solution(numLog):
    log = dict(zip([1,-1,10,-10],['w','s','d','a']))
    return ''.join([log[numLog[i]-numLog[i-1]] for i in range(1,len(numLog))])