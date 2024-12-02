answer = 1
for i in range(3) :
    n = int(input())
    answer *= n

for i in range(10) :
    num_list = list(map(int, str(answer)))
    print(num_list.count(i))