import random
import string


class Robot:
    def __init__(self):
        self.name = self.namer()

    def namer(self):
        name = ""
        for _ in range(2):
            name += random.choice(string.ascii_uppercase)
        for _ in range(3):
            name += str(random.randint(0, 9))
        self.name = name
        return self.name

    def reset(self):
        old_name = self.name
        new_name = self.namer()
        if old_name == new_name:
            self.reset()
