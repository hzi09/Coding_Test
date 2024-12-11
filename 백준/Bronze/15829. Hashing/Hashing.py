n =  int(input())
string = input()
hashing = 0
cnt = 0

for i in string :
    hashing += (ord(i)-96) * (31**cnt)
    cnt += 1

print(hashing)