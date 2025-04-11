n = int(input())

student = []
candy = 0

for i in range(n):
    student.append(int(input()))
    candy += student[i] * (-1) ** i
candy = candy // 2
print(candy)

for i in range(n-1):
    candy = student[i] - candy
    print(candy)
