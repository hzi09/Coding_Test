def solution(ingredient):
    hamburger = [1, 2, 3, 1]
    item = []
    answer = 0
    
    for i in ingredient :
        item.append(i)
        
        if item[-4:] == [1, 2, 3, 1] :
            answer += 1
            
            for _ in range(4) :
                item.pop()
    return answer