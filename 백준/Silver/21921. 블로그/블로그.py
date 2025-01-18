import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visit = list(map(int, input().split()))


current_sum = sum(visit[:x])
max_sum = current_sum
max_count = 1

for i in range(x, n):
    current_sum = current_sum - visit[i - x] + visit[i]  
    if current_sum > max_sum:
        max_sum = current_sum
        max_count = 1
    elif current_sum == max_sum:
        max_count += 1

if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(max_count)