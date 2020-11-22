from collections import Counter


def count_words(sentence):
    chars = ':,."_\n\t!&@$%^'

    translator = str.maketrans(chars, ' '*len(chars))
    sentence = ' '.join(word.translate(translator)
                        for word in sentence.split())

    sentence = (word.strip("'").lower() for word in sentence.split())

    return Counter(sentence)
