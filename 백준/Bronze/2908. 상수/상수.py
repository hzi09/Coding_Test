n_list = list(input().split())
sangsu = []

for i in n_list :
    sangsu.append(int(''.join(reversed(i))))

print(max(sangsu))