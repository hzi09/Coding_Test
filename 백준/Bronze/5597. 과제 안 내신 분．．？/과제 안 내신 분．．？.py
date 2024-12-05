n_list = [i for i in range(1, 31)]

for i in range(28):
    n = int(input())
    n_list.remove(n)
print(f'{n_list[0]}\n{n_list[1]}')