n = int(input())

dot = 2
plus_dot = 1

for i in range(n) :
    dot += plus_dot
    plus_dot *= 2
    
print(dot**2)