from collections import deque


def solution(board):
    n = len(board)

    queue = deque()
    visited = []
    pos = {(0, 0), (0, 1)}
    queue.append((pos, 0))
    visited.append(pos)
    
    while queue:
        pos, cost = queue.popleft()
        if (n-1, n-1) in pos:
            return cost
        
        next_pos = []
        pos = list(pos)
        pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        for i in range(4):
            pos1_next_x, pos1_next_y = pos1_x + dx[i], pos1_y + dy[i]
            pos2_next_x, pos2_next_y = pos2_x + dx[i], pos2_y + dy[i]
            
            if 0 <= pos1_next_x < n and 0 <= pos1_next_y < n and 0 <= pos2_next_x < n and 0 <= pos2_next_y < n:
                if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
                    next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
        
        if pos1_x == pos2_x:
            for i in [-1, 1]:
                if 0 <= pos1_x + i < n and 0 <= pos2_x + i < n:
                    if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                        next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                        next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
        else:
            for i in [-1, 1]:
                if 0 <= pos1_y + i < n and 0 <= pos2_y + i < n:
                    if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                        next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                        next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
        
        for next_pos in next_pos:
            if next_pos not in visited:
                queue.append((next_pos, cost + 1))
                visited.append(next_pos)
    
    return 0


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))