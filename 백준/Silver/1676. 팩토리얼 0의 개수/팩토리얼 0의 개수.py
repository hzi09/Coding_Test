from math import factorial

n = int(input())
n_f = str(factorial(n))
answer = 0

for i in n_f[::-1] :
    if i != '0' :
        break
    answer += 1

print(answer)