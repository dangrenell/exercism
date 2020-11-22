from collections import Counter


def count_words(sentence):
    chars = ':,."_\n\t!&@$%^'
    translator = str.maketrans(chars, ' '*len(chars))
    sentence = sentence.translate(translator).lower()
    sentence = (word.strip("'") for word in sentence.split())

    return Counter(sentence)
