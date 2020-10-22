import string
import random


class Cipher:
    alphabet = string.ascii_lowercase

    rand_key = ''.join([random.choice(string.ascii_lowercase)
                        for _ in range(100)])

    def __init__(self, key=rand_key):
        self.key = key

    def encode(self, text):
        encoded_text = []
        key = self.key*(len(text)//len(self.key) + 1)
        for t, k in zip(text, key):
            k_index = self.alphabet.index(k)
            t_index = self.alphabet.index(t)
            encoded_text.append(self.alphabet[(t_index + k_index) % 26])
        return ''.join(encoded_text)

    def decode(self, text):
        decoded_text = []
        key = self.key*(len(text)//len(self.key) + 1)
        for t, k in zip(text, key):
            k_index = self.alphabet.index(k)
            t_index = self.alphabet.index(t)
            decoded_text.append(self.alphabet[(t_index - k_index) % 26])
        return ''.join(decoded_text)
