def solution(n, computers):
    visited = [False] * n
    network_cnt = 0
    
    for i in range(n) :
        if not visited[i] :
            stack = [i]
            while stack :
                computer = stack.pop()
                visited[computer] = True
                
                for j in range(n) :
                    if computers[computer][j] == 1 and not visited[j] :
                        stack.append(j)
            network_cnt += 1
    return network_cnt