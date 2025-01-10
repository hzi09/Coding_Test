n, b = map(int, input().split())
x = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while n != 0:
    x += str(arr[n % b])
    n //= b

print(x[::-1])