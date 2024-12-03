n_list = []

for _ in range(10) :
    n = int(input())
    n_list.append(n % 42)

print(len(set(n_list)))