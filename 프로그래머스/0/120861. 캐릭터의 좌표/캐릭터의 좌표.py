def solution(keyinput, board):
    move = {'up' : (0, 1), 'down' : (0, -1), 'left' : (-1, 0), 'right' : (1, 0)}
    x, y = 0, 0
    x_limit = board[0]//2
    y_limit = board[1]//2
    for i in keyinput :
        dx, dy = move[i]
        if abs(x+dx) > x_limit or abs(y+dy) > y_limit :
            continue
        else :
            x = x+dx
            y = y+dy
    return [x, y]