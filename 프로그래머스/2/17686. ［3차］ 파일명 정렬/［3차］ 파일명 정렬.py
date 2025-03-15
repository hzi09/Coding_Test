import re

def solution(files):
    filename = []
    
    for file in files :
        match = re.match(r"([a-zA-Z\-\.\s]+)(\d+)", file)
        head = match.group(1)
        number = match.group(2)
        tail = file[len(head)+len(number):]
        filename.append([head, number, tail])
        
    sort_file = sorted(filename, key=lambda x: (x[0].lower(), int(x[1])))
    
    return ["".join(i) for i in sort_file]