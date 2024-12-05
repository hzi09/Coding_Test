def solution(box, n):
    total_dice = 1
    for i in box :
        total_dice *=  i // n
    return total_dice
