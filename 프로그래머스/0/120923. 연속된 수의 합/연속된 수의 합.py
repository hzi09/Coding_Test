def solution(num, total):
    answer = []
    median = total // num
    for i in range(median-(num-1)//2, median + (num+2)//2) :
        answer.append(i)
    return answer