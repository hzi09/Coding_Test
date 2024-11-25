h, m= map(int, input().split())
oven = int(input())

if m + oven < 60 :
    print(h, m+oven)
else :
    h += (m+oven)//60
    m = (m+oven) % 60
    if h > 23 :
        h -= 24
    print(h, m)