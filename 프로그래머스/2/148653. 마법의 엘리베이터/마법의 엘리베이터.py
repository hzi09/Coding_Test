def solution(storey):
    answer = 0

    while storey > 0:
        last_digit = storey % 10
        next_digit = (storey // 10) % 10

        if last_digit > 5 :
            answer += (10 - last_digit)
            storey += 10

        elif last_digit < 5 :
            answer += last_digit

        else :
            if next_digit >= 5 :
                storey += 10
            answer += last_digit

        storey //= 10

    return answer