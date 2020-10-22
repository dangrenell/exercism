# def steps(number):
#     if number <= 0:
#         raise ValueError("Nope.")
#     else:
#         fitbit = 0
#         while number != 1:
#             fitbit += 1
#             number = step(number)
#         return fitbit


# def step(n):
#     if n % 2 == 0:
#         return n/2
#     else:
#         return 3*n + 1

# This was an ideal opportunity for a recursive function

def steps(n):
    if n <= 0:
        raise ValueError("Nope.")
    if n == 1:
        return 0
    else:
        n = n/2 if n % 2 == 0 else 3*n+1
        return 1 + steps(n)
