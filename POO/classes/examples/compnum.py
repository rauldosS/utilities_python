# Imitating the behavior of numbers in a class


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Coordinate x:{0},y:{1}>".format(self.x, self.y)

    # Implement addition
    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    # Implement subtraction
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)

    # Implement in-place addition
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

def main():
    # Declare some Coordinates
    c1 = Coordinate(10, 20)
    c2 = Coordinate(30, 30)
    print(c1, c2)

    # Add two coordinates
    c3 = c1 + c2
    print(c3)

    # Subtract two coordinates
    c4 = c2 - c1
    print(c4)

    # Perform an in-place addition
    c1 += c2
    print(c1)


if __name__ == "__main__":
    main()