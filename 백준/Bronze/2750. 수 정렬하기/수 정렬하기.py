n = int(input())
numbers = [int(input()) for _ in range(n)]

for number in sorted(numbers):
    print(number)
