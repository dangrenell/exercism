def classify(number):
    if number <= 0:
        raise ValueError("Enter a natural number")
    else:
        aloquat_sum = sum(
            [num for num in range(1, number//2+1) if number % num == 0])
        return "abundant" if aloquat_sum > number else "perfect" if aloquat_sum == number else "deficient"
