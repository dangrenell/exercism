def is_paired(input_string: str):
    input_string = ''.join([l for l in input_string if l in '[](){}'])
    couples = ['[]', '()', '{}']
    flag = True
    while flag:
        old_string = input_string
        for couple in couples:
            input_string = input_string.replace(couple, '')
        new_string = input_string
        if old_string == new_string:
            flag = False
    return input_string == ''
