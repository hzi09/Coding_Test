bowls = input()
hight = 0


for i, bowl in enumerate(bowls) :
    if i == 0 :
        hight += 10
    else :
        if bowls[i] != bowls[i-1]:
            hight += 10
        else:
            hight += 5

print(hight)