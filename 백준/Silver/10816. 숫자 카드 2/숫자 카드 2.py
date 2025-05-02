n = int(input())
card = list(map(int, input().split()))
m = int(input())
solved = list(map(int, input().split()))

card.sort()

def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left

for i in solved:
    print(upper_bound(card, i) - lower_bound(card, i), end=' ')