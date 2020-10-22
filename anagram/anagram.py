from collections import Counter


def find_anagrams(word, candidates):
    word = word.lower()
    word_dict = Counter(word)
    candidates = [cand for cand in candidates if cand.lower() != word]
    answers = []

    for cand in candidates:
        cand_dict = Counter(cand.lower())
        if set(word_dict.keys()) == set(cand_dict.keys()):
            if all([word_dict[letter] == cand_dict[letter] for letter in word_dict.keys()]):
                answers.append(cand)

    return answers
