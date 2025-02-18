def solution(n):
    matrix = [[0] * n for _ in range(n)]
    
    directs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    row, col = 0, 0
    direct = 0
    num = 1
    
    while num <= n*n :
        matrix[row][col] = num
        num += 1
        
        next_row = row + directs[direct][0]
        next_col = col + directs[direct][1]
        
        if not (0 <= next_row < n and 0 <= next_col < n and matrix[next_row][next_col] == 0) :
            direct = (direct + 1) % 4
            next_row = row + directs[direct][0]
            next_col = col + directs[direct][1]
        
        row, col = next_row, next_col
        
    return matrix