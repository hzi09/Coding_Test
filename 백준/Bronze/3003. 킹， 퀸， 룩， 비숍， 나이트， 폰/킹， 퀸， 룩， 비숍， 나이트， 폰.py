n = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]

for i in range(6) :
    urine = chess[i] - n[i]
    print(urine, end= ' ')