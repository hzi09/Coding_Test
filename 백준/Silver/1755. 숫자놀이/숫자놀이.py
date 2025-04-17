m, n = map(int, input().split())

numbers = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

answer = []

for i in range(m, n+1):
    if i in numbers:
        answer.append(numbers[i])
    else:
        new_num = ''
        for j in str(i):
            new_num += numbers[int(j)] + ' '
        answer.append(new_num.strip())

answer.sort()

count = 0
for word in answer:
    if ' ' in word:
        digits = word.split()
        for digit in digits:
            for k, v in numbers.items():
                if digit == v:
                    print(k, end='')
    else:
        for k, v in numbers.items():
            if word == v:
                print(k, end='')
    count += 1
    if count % 10 == 0:
        print()
    else:
        print(' ', end='')
