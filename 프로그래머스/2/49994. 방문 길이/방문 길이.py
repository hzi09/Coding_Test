def solution(dirs):
    x, y = 0, 0
    move = set()
    location = {
        'U' : [0, 1],
        'D' : [0, -1],
        'R' : [1, 0],
        'L' : [-1, 0]
    }
    for i in dirs :
        dx = x + location[i][0]
        dy = y + location[i][1]
        if (-5 <= dx <=5) and (-5 <= dy <=5) :
            move.add((x, y, dx, dy))
            move.add((dx, dy, x, y))
            x, y = dx, dy
    return len(move) // 2