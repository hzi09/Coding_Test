def solution(n):
    cnt = 1
    for i in range(1, n):
        sum_n = 0
        for j in range(i, n) :
            sum_n += j
            if sum_n == n :
                cnt += 1
                break
            elif sum_n > n :
                break
    return cnt