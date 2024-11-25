x, y, z = map(int, input().split())
money = 0

if x == y == z :
    money = 10000 + x * 1000
elif x == y or x == z:
    money = 1000 + x * 100
elif y == z :
    money = 1000 + y * 100
else :
    dice = [x, y, z]
    money = max(dice) * 100
print(money)