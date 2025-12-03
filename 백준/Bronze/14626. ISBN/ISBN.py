code = list(input().strip())
numbers = []
sqe = 0

for idx, num in enumerate(code) :
    if num == '*' :
        if idx % 2 == 0:
            sqe = 1
        else:
            sqe = 3
        continue
    if idx % 2 == 0:
        numbers.append(int(num))
    else :
        numbers.append(int(num) * 3)

for x in range(10):
    if (sum(numbers) + sqe * x) % 10 == 0:
        print(x)
        break