n = int(input())
coordinates = [input().split() for _ in range(n)]

coordinates.sort(key=lambda x: (int(x[1]), int(x[0])))

for coordinate in coordinates:
    print(coordinate[0], coordinate[1])