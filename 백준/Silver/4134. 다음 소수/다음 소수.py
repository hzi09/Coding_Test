n = int(input())
test_case = [int(input()) for _ in range(n)]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in test_case:
    while True:
        if is_prime(i):
            print(i)
            break
        i += 1