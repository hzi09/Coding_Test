vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True :
    cnt = 0
    st = input()
    if st == '#' :
        break
    for i in st :
        if i in vowel :
            cnt += 1
    print(cnt)