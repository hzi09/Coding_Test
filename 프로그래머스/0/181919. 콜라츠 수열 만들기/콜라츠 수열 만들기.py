def solution(n):
    answer = [n]
    
    while True :
        if n == 1 :
            break
        elif n % 2 == 0 :
            answer.append(n//2)
            n //= 2
        elif n % 2 != 0 :
            answer.append(3 * n + 1)
            n = 3 * n + 1
    return answer