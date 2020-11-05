def primes(limit):
    primes = []
    for num in range(2, limit+1):
        if not any(num % p == 0 for p in primes):
            primes.append(num)
    return primes
