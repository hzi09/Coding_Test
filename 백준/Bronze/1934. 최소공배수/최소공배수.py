t = int(input())
nums = [list(map(int, input().split())) for _ in range(t)]

for i in range(t):
    a, b = nums[i]
    while b:
        a, b = b, a % b
    print(nums[i][0] * nums[i][1] // a)