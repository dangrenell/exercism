import string


def is_pangram(sentence):
    alphabet = string.ascii_lowercase
    try:
        flag = True
        for letter in alphabet:
            if letter not in sentence.lower():
                flag = False
        return flag
    except:
        raise Exception("Error")
