ball = 1
change = int(input()) # 컵의 위치는 몇번 바꿀건지?

for i in range(change) : # 컵의 위치 바뀌는 동안만 실행
    x, y = map(int, input().split())
    if x == ball :
        ball = y
    elif y == ball :
        ball = x

print(ball)