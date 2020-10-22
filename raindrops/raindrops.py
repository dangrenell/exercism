def convert(number):
    return_string = ''

    factor_dict = {3: "Pling", 5: "Plang", 7: "Plong"}

    try:
        for factor, string in factor_dict.items():
            return_string += string if number % factor == 0 else ''

        return str(number) if return_string == '' else return_string

    except:
        raise Exception("Something went wrong!")
