str = input()
answer = ''

for i in str :
    if i.islower():
        answer += i.upper()
    elif i.isupper() :
        answer += i.lower()
        
print(answer)