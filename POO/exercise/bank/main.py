"""
→ Exercise with Abstraction, Inheritance, Encapsulation and Polymorphism

→ Create an (extremely simple) banking system that has clients, accounts and a bank. The idea is that the client has an account (savings or current) and can withdraw/deposit in that account. Checking accounts have an extra limit. Bank has clients and accounts.

→ Tips:

    → Create class client that inherits from class Person (Inheritance)
        * Person has name and age (with getters)
        * client HAS an account (Aggregation of the Current Account or Savings Account class)
    → Create classes SavingAccount and CurrentAccount that inherit from Account
        *CurrentAccount must have an extra limit
        * Accounts have branch, account number and balance
        * Accounts must have deposit method
        * Account (super class) must have abstract draw method (Abstract and polymorphism - the subclasses that implement the draw method)
    → Create Bank class to ADD client and account classes (Aggregation)
    → Bank will be responsible for authenticating the client and accounts as follows:
        * Bank has accounts and clients (Aggregation)
        * Check if the branch is from that bank
        * Check if the client is from that bank
        * Check if the account is from that bank
    → It will only be possible to withdraw if you pass the bank authentication (described above)
"""

from bank import Bank
from client import Client
from account import CurrentAccount, SavingAccount

bank = Bank()

client1 = Client("Luiz", 30)
client2 = Client("Maria", 18)
client3 = Client("João", 50)

account1 = SavingAccount(1111, 254136, 0)
account2 = CurrentAccount(2222, 254137, 0)
account3 = SavingAccount(1212, 254138, 0)

client1.insertAccount(account1)
client2.insertAccount(account2)
client3.insertAccount(account3)

bank.insertClient(client1)
bank.insertAccount(account1)

bank.insertClient(client2)
bank.insertAccount(account2)

if bank.authenticate(client1):
    client1.account.deposit(0)
    client1.account.withdraw(20)
else:
    print("Client not authenticated.")

print("###################")

if bank.authenticate(client2):
    client2.account.deposit(0)
    client2.account.withdraw(20)
else:
    print("Client not authenticated.")
