def solution(players, callings):
    player_rank = {player : i for i, player in enumerate(players)}
    
    for call in callings :
        idx = player_rank[call]
        if idx > 0 :
            prev_player = players[idx-1]
            players[idx], players[idx-1] = players[idx-1], players[idx]
            
            player_rank[call] -= 1
            player_rank[prev_player] += 1
    return players