def is_armstrong_number(number):
    str_num = str(number)
    num_sum = sum([int(num)**len(str_num) for num in str_num])
    return num_sum == number
