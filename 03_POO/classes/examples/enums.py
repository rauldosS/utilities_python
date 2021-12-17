# Defining Enumerations Using the Base Enum Class

from enum import Enum, auto


# TODO: Define the Fruit class that inherits from Enum
class Fruit(Enum):
    GRAPE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()

def main():
    # Enum objects have easy-to-read values and types
    print(Fruit.GRAPE)
    print(type(Fruit.GRAPE))
    print(repr(Fruit.GRAPE))

    # Enum objects have "name" and "value" properties
    print(Fruit.GRAPE.name, Fruit.GRAPE.value)

    # Show automatically generated value for PEAR
    print(Fruit.PEAR.value)

    # It is possible to use enum objects as keys
    fruits = {}
    fruits[Fruit.BANANA] = "Yellow Fruit"
    print(fruits[Fruit.BANANA])

if __name__ == "__main__":
    main()