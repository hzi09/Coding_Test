def solution(progresses, speeds):
    days = [(100 - progress + speed - 1) // speed for progress, speed in zip(progresses, speeds)]
    
    answer = []
    max_day = days[0]
    cnt = 0
    
    for day in days :
        if day <= max_day :
            cnt += 1
        else :
            answer.append(cnt)
            cnt = 1
            max_day = day
            
    answer. append(cnt)
    return answer