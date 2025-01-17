def solution(order):
    price = 0
    for i in order :
        if 'cafelatte' in i :
            price += 5000
        else :
            price += 4500
    return price