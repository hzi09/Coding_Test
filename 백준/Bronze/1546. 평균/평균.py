n = int(input())
score = list(map(int, input().split()))

score.sort()
new_score = []

for i in score :
    new_score.append((i/score[-1])*100)

print(sum(new_score)/n)