def sieve_of_eratosthenes(start, end):
    is_prime = [True] * (end + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(end ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, end + 1, i):
                is_prime[j] = False
    
    return sum(1 for i in range(start, end + 1) if is_prime[i])

while True:
    n = int(input())
    
    if n == 0:
        break

    count = sieve_of_eratosthenes(n + 1, 2 * n)
    print(count)