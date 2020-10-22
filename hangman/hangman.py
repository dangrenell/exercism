from getpass import getpass

STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.guessed_letter_in_word = []

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("Out of guesses!")
        elif char.lower() == "quit":
            self.status = STATUS_LOSE
        else:
            if char in self.word and char not in self.guessed_letter_in_word:
                self.guessed_letter_in_word.append(char)
                if set(self.guessed_letter_in_word) == set(self.word):
                    self.status = STATUS_WIN
            else:
                self.remaining_guesses -= 1
                if self.remaining_guesses < 0:
                    self.status = STATUS_LOSE

    def get_masked_word(self):
        ans = [char if char in self.guessed_letter_in_word else "_" for char in self.word]
        return ''.join(ans)

    def get_status(self):
        return self.status


if __name__ == "__main__":
    secret_word = getpass("Enter the secret word: ")
    game = Hangman(secret_word)

    print()
    print()
    print("Hangman game. Type 'quit' to end game.".center(80))
    print()
    print()

    while game.status == STATUS_ONGOING:
        guess = input("Guess a letter: ")
        game.guess(guess)
        if game.get_status() == STATUS_WIN:
            print("Winner winner chicken dinner\n".upper())
            break
        else:
            print(game.get_masked_word())
            print(game.remaining_guesses, "guesses left")
            print()
