from collections import Counter
import re


def count_words(sentence):
    chars = ':,."_\n\t!&@$%^'
    for char in chars:
        sentence = sentence.replace(char, ' ')

    pattern = r'[\'"]+(\w+)[\'"]+'
    sentence = re.sub(pattern, r'\1', sentence)

    sentence = sentence.lower()
    sentence = sentence.split()
    return Counter(sentence)
