def solution(prices):
    n_price = len(prices)
    answer = [0] * n_price
    
    for n in range(n_price) :
        for p in range(n+1, n_price) :
            answer[n] += 1
            if prices[n] > prices[p] :
                break
    return answer