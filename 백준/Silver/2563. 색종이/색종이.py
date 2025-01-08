# 색종이의 갯수 입력
n = int(input())

# 전체 넓이
dim = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n) :
    x, y = map(int, input().split())

    for row in range(x, x+10) :
        for col in range(y, y+10) :
            dim[row][col] = 1

answer = 0

for i in dim :
    answer += i.count(1)

print(answer)