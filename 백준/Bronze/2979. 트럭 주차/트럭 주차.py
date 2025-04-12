a, b, c = map(int, input().split())
time = [list(map(int, input().split())) for _ in range(3)]

end_time = max(time[i][1] for i in range(3))

parking = [0] * 100

for i in range(3) :
    for j in range(time[i][0], time[i][1]):
        parking[j] += 1

price = 0

for i in range(end_time):
    if parking[i] == 1:
        price += a
    elif parking[i] == 2:
        price += b * 2
    elif parking[i] == 3:
        price += c * 3

print(price)