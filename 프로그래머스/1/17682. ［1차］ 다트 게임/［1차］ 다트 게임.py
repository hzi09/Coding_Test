import re

def solution(dartResult):
    pattern = re.findall(r'\d+[SDT][*#]?', dartResult)
    score = []
    
    for idx, p in enumerate(pattern) :
        num = int(re.search(r'\d+', p).group())
        bonus = re.search(r'[SDT]', p).group()
        option = re.search(r'[*#]', p)
        
        num **= {'S': 1, 'D': 2, 'T': 3}[bonus]
        
        if option :
            option = option.group()
            if option == '*' :
                num *= 2
                if score :
                    score[-1] *=2
            elif option == '#' :
                num *= -1
        
        score.append(num)
    return sum(score)