n = int(input()) # 참가자의 수
moneys = [] # 상금

for _ in range(n) : # 참가자의 수만큼 실행
    dice_n=[0]*6    # [0, 0, 0, 0, 0, 0]
    dice=list(map(int,input().strip().split()))
    money = 0
    for i in dice:
        dice_n[i-1]+=1 # 각 숫자가 나오면 위치에 맞게 +1 해주기
    if max(dice_n) == 4 :
        money = max(money, 50000+(dice_n.index(4)+1)*5000)
    elif max(dice_n) == 3 :
        money = max(money, 10000+(dice_n.index(3)+1)*1000)
    elif max(dice_n) == 2 and dice_n.count(2) ==2 :
        money = max(money, 2000+(dice_n.index(2)+1)*500)+(dice_n.index(2,dice_n.index(2)+1)+1)*500
    elif max(dice_n) == 2 and dice_n.count(2) ==1 :
        money = max(money, 1000 + (dice_n.index(2) + 1) * 100)
    elif max(dice_n) == 1 :
        money = max(money, (max(dice) * 100))
    moneys.append(money)
print(max(moneys))