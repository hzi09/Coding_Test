n = int(input())
a = list(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

a.sort()

def binary_search(target, arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for i in x:
    print(binary_search(i, a))
