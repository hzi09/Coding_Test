def solution(board, moves):
    answer = [] 
    cnt = 0
    
    for move in moves :
        col = move - 1
        for b in board :
            if b[col] != 0 :
                doll = b[col]
                b[col] = 0
                
                if answer and answer[-1] == doll :
                    answer.pop()
                    cnt += 2
                else :
                    answer.append(doll)
                break
    return cnt