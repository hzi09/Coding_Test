n, m = map(int, input().split())
a = list(map(int, input().split()))

count = 0
interval_sum = 0
end = 0

for i in range(n):
    while interval_sum < m and end < n:
        interval_sum += a[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= a[i]

print(count)