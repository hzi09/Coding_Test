n = int(input())

words = [input().strip() for _ in range(n)]

weight = {}
first_chars = {word[0] for word in words}

for word in words:
    for i, char in enumerate(word):
        weight[char] = weight.get(char, 0) + 10 ** (len(word) - 1 - i)

sorted_chars = sorted(weight.items(), key=lambda x: -x[1])

char_to_num = {}
num = 9

if len(sorted_chars) >= 10:
    zero_char = None
    for char, _ in reversed(sorted_chars):
        if char not in first_chars:
            zero_char = char
            break
    
    if zero_char is None:
        zero_char = sorted_chars[-1][0]
    
    for char, _ in sorted_chars:
        if char == zero_char:
            char_to_num[char] = 0
        else:
            char_to_num[char] = num
            num -= 1
else:
    for char, _ in sorted_chars:
        char_to_num[char] = num
        num -= 1

result = sum(int(''.join(str(char_to_num[c]) for c in word)) for word in words)
print(result)