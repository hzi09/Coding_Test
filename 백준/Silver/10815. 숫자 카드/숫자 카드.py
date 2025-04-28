n = int(input())
card = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

card.sort()

def binary_search(target):
    left, right = 0, n-1
    while left <= right:
        mid = (left + right) // 2
        if card[mid] == target:
            return 1
        elif card[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for i in range(m):
    print(binary_search(check[i]), end=' ')