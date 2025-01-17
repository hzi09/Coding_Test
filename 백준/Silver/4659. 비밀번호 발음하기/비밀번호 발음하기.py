vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    password = input()

    if password == 'end' :
        break

    if not any(i in vowel for i in password) :
        print(f'<{password}> is not acceptable.')
        continue


    is_acceptable = True
    for i in range(len(password)-2) :
        sub = password[i:i+3]
        if all(i in vowel for i in sub) or all(i not in vowel for i in sub) :
            print(f'<{password}> is not acceptable.')
            is_acceptable = False
            break
    
    if not is_acceptable :
        continue


    for i in range(len(password)-1) :
        if password[i] == password[i+1] and password[i] not in ['e','o'] :
            print(f'<{password}> is not acceptable.')
            is_acceptable =False
            break

    if not is_acceptable :
        continue
    
    print(f'<{password}> is acceptable.')