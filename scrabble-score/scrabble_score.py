letter_dict = {
    'd': 1,
    'g': 1,
    'b': 2,
    'c': 2,
    'm': 2,
    'p': 2,
    'f': 3,
    'h': 3,
    'v': 3,
    'w': 3,
    'y': 3,
    'k': 4,
    'j': 7,
    'x': 7,
    'q': 9,
    'z': 9,
}


def score(word):
    word = word.lower()
    score = len(word)

    for letter in word:
        score += letter_dict.get(letter, 0)

    return score
