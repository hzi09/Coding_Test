t = int(input())

for _ in range(t) :
    c = int(input())

    quarter = c // 25
    dime = (c - (25*quarter)) // 10
    nikel = (c - (25*quarter) - (10*dime)) // 5
    penny = (c - (25*quarter) - (10*dime) - (5*nikel)) 
    
    print(quarter, dime, nikel, penny)