import threading


def account_logic(func):
    def wrapper(self, *args):
        if self.opened:
            return func(self, *args)
        else:
            raise ValueError("Account closed")
    return wrapper


class BankAccount:
    def __init__(self):
        self.lock = threading.Lock()
        self.opened = False

    @account_logic
    def get_balance(self):
        return self.balance

    @account_logic
    def deposit(self, amount):
        with self.lock:
            if amount < 0:
                raise ValueError("Try a withdrawl")
            else:
                self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Try a deposit")
        else:
            with self.lock:
                if amount <= self.balance:
                    self.balance -= amount
                else:
                    raise ValueError("Looks like you're in the red")

    def open(self):
        if not self.opened:
            self.opened = True
            self.balance = 0
        else:
            raise ValueError("Account already open")

    @account_logic
    def close(self):
        self.opened = False
