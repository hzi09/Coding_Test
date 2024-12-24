def solution(babbling):
    answer = []
    for i in babbling :
        i = i.replace("aya", "-")
        i = i.replace("ye", "-")
        i = i.replace("woo", "-")
        i = i.replace("ma", "-")
        answer.append(set(i))

    return answer.count({'-'})