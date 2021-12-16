"""
What are dataclasses? The Dataclasses module provides a decorator and functions 
to automatically create methods such as __init__(), __repr__(), __eq__ (etc) in 
user-defined classes.

Basically, dataclasses are syntax sugar for creating normal classes.
It was originally described in PEP 557.
Added in version 3.7 of Python.

Read the documentation: https://docs.python.org/en-us/3/library/dataclasses.html
"""
from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple


# 💡 declare

@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class Person:
    name: str
    last_name: str = field(repr=False)

    def __post_init__(self):
        if not isinstance(self.name, str):
            raise TypeError(
                f'Invalid type {type(self.name).__name__} != str in {self}'
            )

    @property
    def fullName(self):
        return f'{self.firstname} {self.lastname}'

p1 = Person('A', '5')
p2 = Person('C', '3')
p3 = Person('D', '4')
p4 = Person('E', '6')

people = [p1, p2, p3, p4]

print(sorted(persons, key=person's lamb: person.lastname, reverse=True))
print(p1)

# print(p1)
# print(p1 == p2)

# print(p1.name)
# print(p1.last name)
# print(p1.full_name)

print()

print(asdict(p1))
print(astuple(p1))