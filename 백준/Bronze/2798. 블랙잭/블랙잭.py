from itertools import permutations

n, m = map(int, input().split())
card_list = list(map(int, input().split()))
card_group = []

for i in list(permutations(card_list, 3)) :
    card_group.append(i)

sum_card = []
for i in range(len(card_group)) :
    sum_num = sum(card_group[i])
    if m >= sum_num : 
        sum_card.append(sum_num)

print(max(sum_card))