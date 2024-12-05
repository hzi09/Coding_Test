def solution(n):
    count = 0
    for x in range(4, n+1):
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                count += 1
                break
    return count