def solution(a, b):
    day_week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    date_31 = [1, 3, 5, 7, 8, 10, 12]
    date_30 = [4, 6, 9, 11]
    date_29 = [2]
    
    day = 0
    for i in range(1, a) :
        if i in date_31 :
            day += 31
        elif i in date_30 :
            day += 30
        elif i in date_29 :
            day += 29
    day += b
    
    if day % 7 > 7 :
        return day_week[(day-1) % 7 - 7]
    else :
        return day_week[(day-1) % 7]