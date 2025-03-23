n = int(input())

coordinates = []
for i in range(n) :
    [x, y] = map(int, input().split())
    coordinates.append([x,y])

coordinates.sort()

for coordinate in coordinates :
    print(coordinate[0], coordinate[1])