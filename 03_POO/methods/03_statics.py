'''
    → Static methods
        → Normal function, but cls or self cannot be used in it.
'''
from random import randint

# people
class People:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print(self.name)

    # Is a static methods
    @staticmethod
    def generateId():
        rand = randint(0, 10000)

        return rand

# instance by classmethod
raul = People('Raul')

raul.generateId()

# 
# 