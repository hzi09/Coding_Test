def solution(left, right):
    answer = 0
    for n in range(left, right+1) :
        cnt = 0
        for i in range(1, int(n**0.5) + 1) :
            if (n % i ==0) :
                cnt += 1
                if i ** 2 != n :
                    cnt += 1
        if cnt % 2 == 0 :
            answer += n
        else :
            answer -= n
    return answer