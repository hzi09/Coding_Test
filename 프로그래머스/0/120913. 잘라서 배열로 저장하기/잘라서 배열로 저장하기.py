def solution(my_str, n):
    answer = []
    i = 0
    j = n
    for _ in range(len(my_str)//n) :
        answer.append(my_str[i:j])
        i += n
        j += n
    if len(my_str)%n != 0 :
        answer.append(my_str[-(len(my_str)%n):])
    return answer