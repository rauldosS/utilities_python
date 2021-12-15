'''
    → Class methods
        →  Use decorator and refer to class
'''
from datetime import datetime

# 💡 people
class People:
    current_year = int(datetime.now().year)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        print(self.name)

    # Is a instance method
    def yearBirth(self):
        print(f'{ self.name } was born in { self.current_year - self.age}')

    # Is a class method
    @classmethod
    def byYearBirth(cls, name, year_birth):
        age = cls.current_year - year_birth

        return cls(name, age)

# 💡 instance by classmethod
raul = People.byYearBirth('Raul', 1999)

print(raul.name, raul.age)