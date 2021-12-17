"""
Base class for creating enumerated constants

unique and constant values

Use whenever you have a set of choices and cannot get out of that set.
"""

from enum import Enum, auto

class Directions(Enum):
    """ What not to do
        
        if direction != 'right' ... :
    """

    right = auto()
    left = auto()
    up = auto()
    down = auto()

def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError("Cannot move in this direction")

    return f"Moving {direction.name}"

if __name__ == "__main__":
    print(move(Directions.right))
    print(move(Directions.left))
    print(move(Directions.up))
    print(move(Directions.down))

    print()

    for direction in Directions:
        print(direction, direction.value, direction.name)