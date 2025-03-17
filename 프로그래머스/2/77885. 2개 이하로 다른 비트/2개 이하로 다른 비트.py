def solution(numbers):
    answer = []
    
    for number in numbers :
        if number % 2 == 0 :
            answer.append(number + 1)
        else :
            bit = 1
            while number & bit :
                bit <<= 1
            answer.append(number+bit-(bit>>1))
    return answer