def solution(chicken):
    answer = 0

    while chicken >= 10 :
        service, coupon = divmod(chicken, 10)
        answer += service
        chicken = service + coupon

    return answer
