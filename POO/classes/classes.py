'''
    → Classes
        → First letter capital

'''
from datetime import datetime

# 💡 people
class People:
    current_year = int(datetime.now().year)

    def __init__(self, name, age, eating=False, talking=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.talking = talking

    def __str__(self):
        print(self.name)

    def eat(self, food):
        if self.eating:
            print(f'{ self.name } is eating!')
        else:
            print(f'{ self.name } is eating { food }!')
            self.eating = True

    def stopEating(self):
        print(f'{ self.name } stopped eating!')
        self.eating = False

    def speak(self, phrase):
        if not self.eating and not self.talking:
            self.talking = True
            return print(f'{ self.name } is talking: { phrase }')

    def yearBirth(self):
        print(f'{ self.name } was born in { self.current_year - self.age}')

# 💡 instance - create object through class
raul = People('Raul', 22)

raul.eat('apple')
raul.stopEating()
raul.speak("I'm going to eat!")
raul.yearBirth()