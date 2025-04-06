def find_primes(n):
    if n < 2:
        return []

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for current in range(2, int(n ** 0.5) + 1):
        if sieve[current]:
            sieve[current * current:: current] = [False] * len(sieve[current * current:: current])

    return [i for i, is_prime in enumerate(sieve) if is_prime]


N = int(input())
primes = find_primes(N)

for prime in primes:
    print(prime)