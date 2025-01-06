t = int(input())

for _ in range(t) :
    str_n = input()
    stack = [] 

    for i in str_n :
        if i == '(' : 
            stack.append(i)
        elif i == ')' :
            if stack :
                stack.pop()
            else :
                print('NO')
                break
    else : 
        if not stack :
            print('YES')
        else : 
            print('NO')