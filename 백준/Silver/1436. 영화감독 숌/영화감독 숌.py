n = int(input())
answer = 666
cnt = 0

while True :
    if '666' in str(answer) :
        cnt += 1
        if cnt == n :
            break
    answer += 1

print(answer)