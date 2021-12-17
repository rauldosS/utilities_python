'''
    → Abstract classes

    → Concrete methods
        It works correctly according to your inheritance chain.

    → Abstract method
        → Creates a method and does not write its body, mentions that the method 
        is abstract so that the classes that inherit are obliged to create these 
        methods within themselves.

'''

# create class abstract (concept)
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def speak(self):
        pass

class B(A):
    def speak(self):
        print('Talking B')
        
# abstract classes cannot be instantiated
#  a = A() => TypeError: Can't instantiate abstract class A with abstract method speak
a = B()
a.speak()

# Bank account system
class Account(ABC):
    def __init__(self, agency, account, balance):
        self._agency = agency
        self._account = account
        self._balance = balance

    @property
    def agency(self):
        return self._agency

    @property
    def account(self):
        return self._account

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Balance must be a numeric value.')
            
        self._balance = value

    def deposit(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Deposit value must be a numeric value.')
            
        self._balance += value
        self.details()

    def details(self):
        print(f'Agency: { self.agency }', end=' ')
        print(f'Account: { self.account }', end=' ')
        print(f'Balance: { self.balance }')

    @abstractmethod
    def withdraw(self, value):
        pass

# Accounts
class SavingsAccount(Account):
    def withdraw(self, value):
        if self.balance < value:
            print(f'{ self.account } Insufficient funds')
            return
        
        self.balance -= value
        self.details()

class CheckingAccount(Account):
    def __init__(self, agency, account, balance, limit=100):
        super().__init__(agency, account, balance)
        self._limit = limit

    @property
    def limit(self):
        return self._limit

    def withdraw(self, value):
        if (self.balance + self.limit) < value:
            print(f'{ self.account } Insufficient funds')
            return
        
        self.balance -= value
        self.details()

account1 = SavingsAccount(1000, 2222, 0)
account2 = CheckingAccount(2222, 3333, 0)
account3 = CheckingAccount(2222, 4444, 0, 500)

account1.deposit(10)
account1.deposit(99)
account1.withdraw(10)

account2.deposit(100)
account2.withdraw(150)
account2.withdraw(150)

account2.deposit(100)
account2.withdraw(150)