def solution(myString, pat):
    answer = []
    for i in range(len(myString)) :
        slice_str = myString[i:i+len(pat)]
        if len(slice_str) != len(pat) :
            break
        else :
            answer.append(myString[i:i+len(pat)])
    return answer.count(pat)