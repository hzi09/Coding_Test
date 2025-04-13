word = input()
n = int(input())
dictionary = [input() for _ in range(n)]

found = False

for shift in range(0, 25):
    new_word = ''
    for char in word:
        new_char = chr(ord(char) - shift)
        if ord(new_char) < 97:
            new_char = chr(ord(new_char) + 26)
        new_word += new_char

    for dic in dictionary:
        if dic in new_word:
            found = True
            break
    if found:
        break

print(new_word)