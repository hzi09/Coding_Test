numbers = [int(input()) for _ in range(5)]
numbers.sort()

print(sum(numbers) // len(numbers))
print(numbers[len(numbers) // 2])