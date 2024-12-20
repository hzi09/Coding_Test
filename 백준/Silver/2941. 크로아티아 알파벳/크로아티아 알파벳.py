string = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cro_str = 0

for i in croatia :
    if i in string :
        cro_str += string.count(i)

answer = len(string) - (cro_str)
print(answer)