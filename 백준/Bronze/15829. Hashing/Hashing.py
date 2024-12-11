n =  int(input())
string = input()
hashing = 0

for i in range(n) :
    hashing += (ord(string[i])-96) * (31**i)

print(hashing % 1234567891)