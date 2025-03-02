def solution(data, ext, val_ext, sort_by):
    dataset = {'code': 0, 'date' : 1, 'maximum' : 2,'remain' : 3}
    
    answer = []
    for d in data: 
        if d[dataset[ext]] < val_ext :
            answer.append(d)
    
    return sorted(answer, key=lambda x:x[dataset[sort_by]])