# def is_prime(p):
#     return p > 1 and all(p % i != 0 for i in range(2, p//2+1))


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True


def factors(value):
    primes = [p for p in range(int(value**0.5)+2) if is_prime(p)]

    factors = []

    for p in primes:
        while value % p == 0:
            factors.append(p)
            if is_prime(value/p):
                factors.append(int(value/p))
                value /= value/p
            value /= p

    return factors
