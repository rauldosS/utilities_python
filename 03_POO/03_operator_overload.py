'''
    → Operator overload

    → In python, the behavior of operators is defined by special methods.

    → Let's change the behavior of operators with user-defined classes.

    Operator            Method                      Operation
    ---------------------------------------------------------------------------
    +                   __add__                     addition
    -                   __sub__                     subtraction
    *                   __mul__                     multiplication
    /                   __div__                     division
    //                  __floordiv__                integer division
    %                   __mod__                     Module
    **                  __pow__                     Power
    +                   __pos__                     Positive
    -                   __neg__                     Negative
    <                   __lt__                      Less than
    >                   __gt__                      Greater than
    <=                  __le__                      Less than or equal to
    >=                  __ge__                      Greater than or equal to
    ==                  __eq__                      Equal to
    !=                  __ne__                      Other than
    <<                  __lshift__                  Shift to the left
    >>                  __rshift__                  Shift to the right
    &                   __and__                     And bit-by-bit
    |                   __or__                      OR bit-by-bit
    ^                   __xor__                     OR bit-by-bit exclusive
    ~                   __inv__                     inversion
'''

# Example
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getArea(self):
        return self.x * self.y

    def __repr__(self):
        return f"<class 'Rectangle({ self.x }, { self.y })'>"

    # Teach the python interpreter how to use the + operator with my class
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y

        return Rectangle(new_x, new_y)
        
    def __lt__(self, other):
        a1 = self.getArea()
        a2 = other.getArea()

        return a1 < a2

    def __gt__(self, other):
        a1 = self.getArea()
        a2 = other.getArea()

        return a1 > a2

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)

r3 = r1 + r2

print('r1:',r1)
print('r2:',r2)
print('r3:',r3)

print(f'r3 is greater than r1: { r3 > r1 }')
print(f'r3 is less than r1: { r3 < r1 }')

print(f'r1 its the same as r2: { r1 == r2 }')
print(f'r3 its the same as r1: { r3 == r1 }')