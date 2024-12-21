t = int(input())
group_n = t

for _ in range(t) :
    word = input()
    for i in range(len(word)-1) :
        if word[i] == word[i+1] :
            continue
        elif word[i] in word[i+1:] :
            group_n -= 1
            break


print(group_n)