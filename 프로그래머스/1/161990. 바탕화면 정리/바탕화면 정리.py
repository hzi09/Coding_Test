def solution(wallpaper):
    x_list, y_list = [], []
    
    for x in range(len(wallpaper)) :
        for y in range(len(wallpaper[0])) :
            if wallpaper[x][y] == '#' :
                x_list.append(x)
                y_list.append(y)

    return [min(x_list), min(y_list), max(x_list)+1, max(y_list)+1]