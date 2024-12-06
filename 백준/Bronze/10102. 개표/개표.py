# 입력받는 변수와 심사위원들의 투표를 받을 리스트 생성
v = int(input())
choice = input()
choice_list = []

# 입력받은 투표들을 하나씩 요소로 추가
for i in choice :
    choice_list.append(i)

# A와 B가 득표한 수
a_score = 0
b_score = 0

# 득표의 수를 확인합니다
for i in choice_list :
    # A이면 A 득표수를 +1
    if i == 'A' :
        a_score += 1
    # B이면 B 득표수를 +1
    elif i == 'B' :
        b_score += 1

# 각 조건에 맞게 출력하여줍니다.
if a_score > b_score :
    print('A')
elif a_score < b_score :
    print('B')
elif a_score == b_score :
    print('Tie')