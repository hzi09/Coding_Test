n = int(input())
floor = 1
room = 1
room_list = [1]

while True :
    if sum(room_list) < n :
        if floor == 1 :
            floor += 1
            room += 5
            room_list.append(room)
        else :
            floor += 1
            room += 6
            room_list.append(room)
    else :
        print(floor)
        break