import sys

t= int(input())
for i in range(t) :
    a, b = map(int, sys.stdin.readline().split())
    print("Case #",end="")
    print(i+1, end="")
    print(':', a+b)