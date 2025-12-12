n = int(input())

for _ in range(n) :
    p = int(input())
    players = {}

    for _ in range(p) :
        price, name = input().split()
        players[name] = int(price)
        
    max_player = max(players, key=players.get)
    print(max_player)
