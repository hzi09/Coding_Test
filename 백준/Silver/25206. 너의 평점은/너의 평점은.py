# 학점의 총합
sum_score = 0
# 전체 과목의 (학점 × 과목평점) 합
all_score = 0

unit = {'A+' : 4.5, 'A0' : 4.0, 
        'B+' : 3.5, 'B0' : 3.0, 
        'C+' : 2.5, 'C0' : 2.0,
        'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0 }

for _ in range(20) :
    report_card = input().split()
    
    if report_card[2] == 'P' :
        pass
		
    else :
        sum_score += float(report_card[1])
        all_score += float(report_card[1]) * float(unit.get(report_card[2]))

print(f'{all_score / sum_score : 0.6f}')