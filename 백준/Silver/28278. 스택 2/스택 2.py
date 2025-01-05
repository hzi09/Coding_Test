import sys

n = int(sys.stdin.readline())

stack = []

for _ in range(n) :
    s = list(map(int, sys.stdin.readline().split()))

    if s[0] == 1 :
        stack.append(s[1])
    
    elif s[0] == 2 :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack.pop())

    elif s[0] == 3 :
        print(len(stack))

    elif s[0] == 4 :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)

    elif s[0] == 5 :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])