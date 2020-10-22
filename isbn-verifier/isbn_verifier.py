def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    if isbn[-1] not in list(map(str, range(10))) + ['X']:
        print(type(isbn[-1]))
        return False
    try:
        int(isbn[:-1])
    except:
        return False
    else:
        isbn = [int(char) if char != 'X' else 10 for char in isbn]
        check_sum = sum(
            [x*rev_int for x, rev_int in zip(isbn, range(10, 0, -1))])
        return check_sum % 11 == 0
