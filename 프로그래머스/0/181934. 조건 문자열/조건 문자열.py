def solution(ineq, eq, n, m):
    eq = '' if eq == "!" else eq
    if eval(str(n)+ineq+eq+str(m)):
        return 1
    return 0