def solution(citations):
    citations.sort(reverse = True)
    h_index = 0
    
    for i, v in enumerate(citations, start=1):
        if i <= v :
            h_index = i
        else :
            break
    return h_index