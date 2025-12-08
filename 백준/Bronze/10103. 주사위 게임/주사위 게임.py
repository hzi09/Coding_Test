n = int(input())

user1, user2 = 100, 100

for _ in range(n):
    num1, num2 = map(int, input().split())

    if num1 > num2 :
        user2 -= num1
    elif num1 < num2 :
        user1 -= num2
    else :
        pass

print(user1)
print(user2)