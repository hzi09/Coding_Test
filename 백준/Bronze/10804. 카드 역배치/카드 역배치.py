cards_idx = [list(map(int, input().split())) for _ in range(10)]
cards = [i for i in range(1, 21)]

for i in cards_idx:
    cards[i[0]-1:i[1]] = cards[i[0]-1:i[1]][::-1]

for i in cards:
    print(i, end=' ')