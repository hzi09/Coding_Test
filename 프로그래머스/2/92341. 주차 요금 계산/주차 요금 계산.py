def solution(fees, records):
    parking = {}
    in_time = {}
    
    for record in records:
        time, car_n, action = record.split()
        hour, minute = map(int, time.split(":"))
        time_set = hour * 60 + minute
        
        if action == 'IN':
            in_time[car_n] = time_set
        elif action == 'OUT':
            if car_n in parking:
                parking[car_n] += time_set - in_time[car_n]
            else:
                parking[car_n] = time_set - in_time[car_n]
            del in_time[car_n]
    
    for car_n, t in in_time.items():
        if car_n in parking:
            parking[car_n] += (23 * 60 + 59) - t
        else:
            parking[car_n] = (23 * 60 + 59) - t
    
    answer = []
    for car_n in sorted(parking.keys()):
        basic_time, basic_fee, unit_time, unit_fee = fees
        if parking[car_n] <= basic_time:
            total_fee = basic_fee
        else:
            extra_time = parking[car_n] - basic_time
            extra_fee = ((extra_time + unit_time - 1) // unit_time) * unit_fee
            total_fee = basic_fee + extra_fee
        answer.append(total_fee)
    
    return answer