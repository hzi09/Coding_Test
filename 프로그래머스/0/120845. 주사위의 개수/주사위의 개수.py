def solution(box, n):
    box_volume = 1
    for i in box :
        box_volume *=  i // n
    return box_volume
