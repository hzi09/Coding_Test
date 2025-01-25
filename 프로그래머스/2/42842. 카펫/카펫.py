def solution(brown, yellow):
    total = brown + yellow
    
    for y in range(3, int(total ** 0.5) + 1) :
        if total % y == 0 :
            x = total // y
            
            if (x-2)*(y-2) == yellow and x >= y :
                return [x, y]
