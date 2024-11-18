import itertools

nan = []

for _ in range(9) :
    nan.append(int(input()))
for i in itertools.combinations(nan, 7) :
    if sum(i) == 100 :
        for j in sorted(i) :
            print(j)
        break
