def solution(number, limit, power):
    answer = []
    for n in range(1, number+1) :
        cnt = 0
        for i in range(1, int(n**0.5)+1) :
            if n % i == 0 :
                cnt += 1 
                if i ** 2 != n :
                    cnt+= 1
                    
        if cnt > limit :
            answer.append(power)
        else :
            answer.append(cnt)  
    return sum(answer)