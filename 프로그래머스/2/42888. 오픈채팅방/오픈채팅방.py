def solution(record):
    user = {}
    answer = []
    
    for i in record :
        parts = i.split()
        action, uid = parts[0], parts[1]
        
        if action in ('Enter', 'Change') :
            nickname = parts[2]
            user[uid] = nickname
    
    for i in record :
        parts = i.split()
        action, uid = parts[0], parts[1]
        
        if action == 'Enter' :
            answer.append(f'{user[uid]}님이 들어왔습니다.')
        elif action == 'Leave' :
            answer.append(f'{user[uid]}님이 나갔습니다.')

    return answer