def solution(priorities, location):
    priorities = [[x, i] for i,x in enumerate(priorities)]
    cnt = 0
    
    while priorities :
        process = priorities[0]
        priorities.pop(0)
        
        if any(process[0] < i[0] for i in priorities) :
            priorities.append(process)
        else :
            cnt += 1
            if process[1] == location :
                return cnt