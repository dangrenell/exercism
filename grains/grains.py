def square(n):
    if 1 <= n <= 64:
        return 2**(n-1)
    else:
        raise ValueError("Number must be between 1 and 64.")


def total():
    return 2**64 - 1
