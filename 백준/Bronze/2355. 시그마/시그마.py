x, y = map(int, input().split())

max_n = max(x,y)
min_n = min(x,y)

sum = ((max_n-min_n+1)*(x+y))/2

print(int(sum))