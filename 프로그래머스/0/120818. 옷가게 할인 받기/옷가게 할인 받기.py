def solution(price) :
    m = 0
    if price >= 500000 :
        m = price * 0.8
    elif price >= 300000 :
        m = price * 0.9
    elif price >= 100000 :
        m = price * 0.95
    else :
        m = price
    return int(m)