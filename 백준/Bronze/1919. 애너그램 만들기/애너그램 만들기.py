s1 = input()
s2 = input()

alphabet = [0] * 26

for s in s1: 
    alphabet[ord(s) - ord('a')] += 1

for s in s2:
    alphabet[ord(s) - ord('a')] -= 1

res = 0
for i in alphabet:
    res += abs(i)

print(res)