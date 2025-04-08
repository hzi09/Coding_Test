math = input().split('-')

result = 0

first = math[0].split('+')
for num in first:
    result += int(num)

for i in range(1, len(math)):
    nums = math[i].split('+')
    for num in nums:
        result -= int(num)

print(result)