def solution(a, b, c, d):
    answer = 0
    dice = [0, 0, 0, 0, 0, 0]
    player = [a, b, c, d]
    for i in player :
         dice[i-1] += 1
    
    if 4 in dice :
        answer = 1111 * (dice.index(4) + 1)
    elif 3 in dice :
        answer = (10 * (dice.index(3) + 1) + (dice.index(1) + 1)) ** 2
    elif 2 in dice :
        if dice.count(2) == 2 :
            player = list(set(player))
            answer = sum(player) * abs(player[0]-player[1])
        else :
            player1 = [idx+1 for idx, v in enumerate(dice) if v == 1]
            answer = player1[0] * player1[1]
    elif dice.count(1) == 4 :
        answer = min(player)
    return answer