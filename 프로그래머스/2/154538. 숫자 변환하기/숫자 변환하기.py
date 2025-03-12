from collections import deque

def solution(x, y, n):
    queue = deque([(x, 0)])
    visit = set()
    
    while queue :
        current, cnt = queue.popleft()
        
        if current == y :
            return cnt
        
        if current in visit :
            continue
        visit.add(current)
        
        for new_x in (current + n, current * 2, current * 3) :
            if new_x <= y and new_x not in visit :
                queue.append((new_x, cnt + 1))
                
    return -1