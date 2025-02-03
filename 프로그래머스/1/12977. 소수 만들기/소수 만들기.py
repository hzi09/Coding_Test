from itertools import combinations

def solution(nums):
    cnt = 0

    for i in list(combinations(nums, 3)) :
        num = sum(i)
        e = 0
        for n in range(2,num):
            if num % n==0:
                e += 1
                break
        if e == 0 :
            cnt += 1

    return cnt