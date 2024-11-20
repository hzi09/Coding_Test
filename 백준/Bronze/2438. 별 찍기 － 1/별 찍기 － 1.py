a = input()
b = ''

for i in range(int(a)):
    for j in range(0, i+1) :
        b += '*'
    b += '\n'
print(b)