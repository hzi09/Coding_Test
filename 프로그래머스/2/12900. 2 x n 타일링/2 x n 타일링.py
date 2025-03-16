def solution(n):
    MOD = 1000000007
    a, b = 1, 2

    for _ in range(3, n + 1):
        a, b = b, (a + b) % MOD 

    return b 