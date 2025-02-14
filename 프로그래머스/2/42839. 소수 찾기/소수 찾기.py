from itertools import permutations

def solution(numbers):
    numbers = list(numbers)
    answer = []
    for n in range(1, len(numbers)+1) :
        answer.extend(int(''.join(p)) for p in permutations(numbers, n))
    cnt = 0
    for i in set(answer) :
        if i < 2 :
            continue
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1) :
            if i % j == 0:
                is_prime = False
                break
        if is_prime :
            cnt += 1
            
    return cnt