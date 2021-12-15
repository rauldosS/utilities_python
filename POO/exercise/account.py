from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, agency, account, balance):
        self.agency = agency
        self.account = account
        self.balance = balance

    def deposit(self, value):
        self.balance += value
        self.details()

    def details(self):
        print(
            f"Agency: {self.agency} "
            f"Account: {self.account} "
            f"Balance: {self.balance}"
        )

    @abstractmethod
    def withdraw(self, value):
        pass


class SavingAccount(Account):
    def withdraw(self, value):
        if self.balance < value:
            print("Insufficient balance")
            return

        self.balance -= value
        self.details()


class CurrentAccount(Account):
    def __init__(self, agency, account, balance, limit=100):
        super().__init__(agency, account, balance)
        self.limit = limit

    def withdraw(self, value):
        if (self.balance + self.limit) < value:
            print("Insufficient balance")
            return

        self.balance -= value
        self.details()
