def solution(elements):
    extended = elements * 2 
    answer = set()
    
    for i in range(len(elements)) :
        for j in range(len(elements)) :
            answer.add(sum(extended[j:j+i+1]))
    return len(answer)