def solution(msg):
    dictionary = {chr(i + 65): i + 1 for i in range(26)}
    next_index = 27
    answer = []
    
    i = 0
    while len(msg) > i : 
        w = msg[i]
        while i + 1 < len(msg) and w + msg[i + 1] in dictionary :
            w += msg[i+1]
            i += 1
        answer.append(dictionary[w])
        
        if i + 1 < len(msg) :
            dictionary[w + msg[i + 1]] = next_index
            next_index += 1
        
        i += 1
        
    return answer