def solution(friends, gifts):
    give_gift = dict.fromkeys(friends, 0)
    receive_gift = dict.fromkeys(friends, 0)
    
    gift_map = {friend: dict.fromkeys(friends, 0) for friend in friends}

    for gift in gifts:
        giver, receiver = gift.split()
        give_gift[giver] += 1
        receive_gift[receiver] += 1
        gift_map[giver][receiver] += 1

    gift_score = {}
    for key in friends:
        gift_score[key] = give_gift[key] - receive_gift[key]

    next_month_gifts = dict.fromkeys(friends, 0)

    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            f1, f2 = friends[i], friends[j]

            if gift_map[f1][f2] > gift_map[f2][f1]:
                next_month_gifts[f1] += 1
            elif gift_map[f1][f2] < gift_map[f2][f1]:
                next_month_gifts[f2] += 1
            else:
                if gift_score[f1] > gift_score[f2]:
                    next_month_gifts[f1] += 1
                elif gift_score[f1] < gift_score[f2]:
                    next_month_gifts[f2] += 1
    return max(next_month_gifts.values())
